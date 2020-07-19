from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        current_user = authenticate(username = username, password = password)
        if current_user is not None :
            login(request,current_user)
            return redirect('gallery')
        else:
            return redirect('login')
    else:
        return render(request,'login/index.html')