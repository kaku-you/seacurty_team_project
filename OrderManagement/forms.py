from django import forms

from .models import PersonnelList

#class PersonnelListForm(forms.ModelForm):
#
#    class Meta:
#        model = PersonnelList
#        fields = ('title', 'text',)


class KakikomiForm(forms.Form):
     name = forms.CharField()
     email = forms.EmailField()
     body = forms.CharField() 

class EBIT_Calculator(forms.Form):
     作番 = forms.CharField()
     案件名 = forms.CharField()
     売上金額 = forms.FloatField()
     所員費用 = forms.FloatField()
     外注費用 = forms.FloatField()

CHOICE = {'あり','なし'}
class temperatureform(forms.Form):
     temperature = forms.ChoiceField(
          label='朝の体温',
          choices = (
            ('jp', '35.5'),
            ('jp', '35.6'),
            ('jp', '35.7'),
            ('jp', '35.8'),
            ('jp', '35.9'),
            ('jp', '36.0'),
            ('jp', '36.1'),
            ('jp', '36.2'),
            ('jp', '36.3'),
            ('jp', '36.4'),
            ('jp', '36.5'),
            ('jp', '36.6'),
            ('jp', '36.7'),
            ('jp', '36.8'),
            ('jp', '36.9'),
            ('jp', '37.0'),
            ('jp', '37.1'),
            ('jp', '37.2'),
            ('jp', '37.3'),
            ('jp', '37.4'),
            ('jp', '37.5'),
            ('jp', '37.5度以上'),

          ),
          widget=forms.widgets.Select
     )
     symptoms = forms.ChoiceField(
          label='風邪の症状',
          choices = (
            ('jp', 'あり'),
            ('jp', 'なし'),
          ),
          widget=forms.widgets.Select
     )
     notes = forms.CharField(label='連絡事項',max_length=200)
