from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from first_app.models import User
from first_app.forms import MyForm

def index(request):
    return HttpResponse("<em> hello! Go to /user to see user list</em>")

def help(request):
    dict = {'help_insert': " hello! Go to /user to see user list "}
    return render(request, 'first_app/help.html', dict)

def user(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'first_app/user.html', user_dict)

def signup(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<em> Saved! Thanks!</em>")
    else:
        form = MyForm()
    return render(request, 'first_app/signup.html', {'form': form})
