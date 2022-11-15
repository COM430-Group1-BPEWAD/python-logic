from django import forms

# Form for username and password. On the home page
class login(forms.Form):
    uname = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", max_length=30)

# Form for entering initial patient information. Intended for signup.html
class signupform(forms.Form):
    uname = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", max_length=30)
    email = forms.EmailField(label="Email Address")
    fname = forms.CharField(label="First Name", max_length=30)
    lname = forms.CharField(label="Last Name", max_length=30)
    dob = forms.DateField(label="Date of Birth")
    # height = forms.IntegerField(label="Height (ft.)", min_value=1, max_value=7, initial=4)
    # height2 = forms.IntegerField(label="", min_value=0, max_value=11, initial=0)