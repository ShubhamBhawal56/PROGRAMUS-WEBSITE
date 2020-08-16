from django.shortcuts import render
from app.forms import UserForm
# Create your views here.
def index(request):
    return render(request,'app/thankyou.html')

def register(request):
    registered=False
    user_form=UserForm()
    if request.method=="POST":
        user_form=UserForm(data=request.POST)

        if user_form.is_valid():
            user_form.save(commit=True)
            return index(request)

            registered=True

    else:
        user_form=UserForm()
    return render(request,'app/registration.html',{
    'user_form':user_form,'registered':registered
    })
