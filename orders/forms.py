from django import forms
from orders.models import Order, Comment


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

