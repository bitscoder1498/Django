from django import forms 

class StudentForm(forms.Form):  
    username = forms.CharField(label="Enter user name",max_length=20)  
    password  = forms.CharField(widget=forms.PasswordInput,label="Password",min_length=6) 

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)    
    