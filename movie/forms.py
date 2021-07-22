from django import forms

class WatchForm(forms.Form):
    pass

class UserForm(forms.Form):
    username = forms.CharField(label='username', max_length=30)
    firstname = forms.CharField(label='firstname',max_length=30)
    lastname = forms.CharField(label='lastname',max_length=30)
    email = forms.EmailField(label='email',max_length=50)
    phonenumber = forms.CharField(label='phonenumber',max_length=11)
    password = forms.CharField(label='password',max_length=20)
    nationalID = forms.CharField(label='nationalID', max_length=10)
    


class LogInForm(forms.Form):
    username = forms.CharField(label='username', max_length=30)
    password = forms.CharField(label='password',max_length=20)


class IntroducerForm(forms.Form):
    introducer_username = forms.CharField(label='introducer username', max_length=30)


class WalletForm(forms.Form):
    amount = forms.IntegerField(label='amount', min_value=0)


class CommentForm(forms.Form):
    rate = forms.IntegerField(label='rate',min_value=1,max_value=5)
    comment = forms.CharField(label='comment', widget=forms.Textarea, required=False)



class CreateListForm(forms.Form):
    name = forms.CharField(label='list name')
    description = forms.CharField(label='description', widget=forms.Textarea)


class AddToListForm(forms.Form):
    movie = forms.CharField(label='movie name')