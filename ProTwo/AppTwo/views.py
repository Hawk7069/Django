from django.shortcuts import render
# from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import NewUserForm
# Create your views here.

def indexA(request):
    return render(request,'main/index.html')

def index(request):
    users = User.objects.order_by('first_name')
    user_dict = {"user_data": users}
    return render(request,'app_two/index.html',context = user_dict)

def users(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return indexA(request)
        else:
            print("ERROR FORM INVALID")
    return render(request,'form/form.html',{'form':form})
