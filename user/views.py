from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login as authLogin
from django.contrib.auth import logout as authLogout
from django.contrib.auth import authenticate
from contact.models import Contact
from pets.models import Pet

# Create your views here.


def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")  

        # create new user
        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()

        # login with new user
        authLogin(request,newUser)

        # login flash messages
        messages.success(request,"Başarıyla kayıt oldunuz..")

        # redirecting to index.html
        return redirect("index")

    context = {
        "form":form
    }
    return render(request,"register.html",context)


def login(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    # if form is not empty
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username, password = password)

        # if user box is empty, return login.html
        if user is None:
            messages.info(request,"Wrong username or password!")
            return render(request,"login.html",context=context)
        
        # if login
        messages.success(request,"You have successfully logged in!")
        authLogin(request,user)
        return redirect("index")

    return render(request,"login.html",context=context)

def logout(request):
    authLogout(request) # user logout
    messages.success(request,"You have successfully logged out!")
    return redirect("index")

def allUsers(request):

    contacts = Contact.objects.all()
    pets = Pet.objects.all()
    noPetUsers: list = []

    # Does user have "Pet"? 
    for contact in contacts:
        isThere = False
        for pet in pets:
            if contact.author == pet.author:
                isThere = True
        if isThere == False:
            noPetUsers.append(contact.author)

    # Search request 
    keyword = request.GET.get("keyword")

    # Return search results
    if keyword:
        contacts = Contact.objects.filter(author__username__icontains = keyword)
        context = {
            "contacts":contacts,
            "pets":pets,
            "noPetUsers":noPetUsers,
        }
        return render(request,"users.html",context=context)
    
    # For default page display
    context = {
        "contacts":contacts,
        "pets":pets,
        "noPetUsers":noPetUsers,
        }

    return render(request,"users.html",context=context)


