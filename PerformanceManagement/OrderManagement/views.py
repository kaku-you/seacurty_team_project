from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import PersonnelList
from .forms import KakikomiForm
from .forms import EBIT_Calculator
from .forms import temperatureform
#from .logic import EBIT_Calculation

def index(request):
    #return HttpResponse("Hello World!")
    pl = PersonnelList.objects.order_by('-PersonnelNameID')
    return render(request, 'OrderManagement/index.html',{'pl': pl})

def tmperatureform(request):
    t = temperatureform()
    return render(request,'OrderManagement/tmperatureform.html',{'form':t})

def kakikomi(request):
    if request.method == 'POST':
        f = EBIT_Calculator(request.POST)
        earning = request.POST['売上金額']
        emplyeefee = request.POST['所員費用']
        outsourcingfee = request.POST['外注費用']
        grossprofit = float(earning) - float(emplyeefee) - float(outsourcingfee)
        processingcost = float(emplyeefee) + float(outsourcingfee)
        generalexpenses = processingcost*0.21
        EBIT = grossprofit - generalexpenses
        U = '{:.2%}'.format(EBIT / float(earning))
        context = {
            'earning' : earning,
            'emplyeefee' : emplyeefee,
            'outsourcingfee' : outsourcingfee,
            'grossprofit': grossprofit,
            'processingcost' : processingcost,
            'generalexpenses' : generalexpenses,
            'EBIT' : EBIT,
            'U' : U,
        }
        #e = EBIT_Calculation(f)
        #return render(request, 'OrderManagement/sakuban.html',{'form1': f})
        return render(request, 'OrderManagement/sakuban.html',context)
    else:
        f = EBIT_Calculator()
        return render(request,'OrderManagement/kakikomiform.html',{'form1': f} )


# Create your views here.
