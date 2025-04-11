from django import forms
from app1.models import *



#ModelForms:

class SchoolInfoUII(forms.ModelForm): #forms creation
    class Meta: #datatypes or input fields creation
        model=SchoolInfo #partivular model name
        fields='__all__' #HE automatically creating fields for the particular models 
        #hint:- how many columns are created in that particular menctioned table in the  models.py ,... that many input fields are created,... 'it is also an advantage for model forms'
        


        #ERROR Hints:
        #don't create spelling mistakes,follow class standards(Title case) and give the exact same names which is menctioned bellow
        '''Meta (title case)
        '''
        '''models,
        fields'''




#ModelForms:
class StudentInfoUII(forms.ModelForm):
    class Meta:
        model=StudentInfo
        fields='__all__'


