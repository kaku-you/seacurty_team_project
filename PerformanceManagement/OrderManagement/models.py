from django.db import models
 

#from OrderManagement.forms import PersonnelList
#from OrderManagement.forms import temperatureform

# Create your models here.
class PersonnelList(models.Model):
    PersonnelNameID = models.CharField(max_length=20)
    PersonnelName = models.CharField(max_length=20) 
    Affiliation = models.CharField(max_length=40)
    values = models.IntegerField()

    def __str__(self):
        rs = self.PersonnelNameID + '_' + self.PersonnelName + '_' + self.Affiliation + '_' + str(self.values/1000000)
        return rs

    def strlist(self):
        rs = self.PersonnelNameID + '_' + self.PersonnelName + '_' + self.Affiliation + '_' + str(self.values/1000000)
        return rs

class StudentList(models.Model):
    ElementarySchoolID = models.CharField(max_length=20)
    Grage = models.IntegerField()
    ClaseNo = models.IntegerField()
    StudentID = models.IntegerField()
    StudentName = models.CharField(max_length=30)
    LoginEmail = models.EmailField()

    def __str__(self):
        return self.StudentName
    
class DailyTemperature(models.Model):

    studentUID = models.CharField(max_length=200)
    TemperatureMeasurdDate = models.DateField()
    TemperatureMeasurd = models.FloatField()
    SymptomsOfCold = models.CharField(max_length=5)
    NoteInfo = models.CharField(max_length=20000)

