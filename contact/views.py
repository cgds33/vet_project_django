from .models import Contact
from .forms import ContactForm
from django.shortcuts import render,redirect
from django.contrib import messages
from contact.models import Contact
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def contact(request):
    form = ContactForm(request.POST or None)

    # Updating contact page by user
    if form.is_valid():

        # If new form comes, delete old one 
        Contact.objects.filter(author = request.user).delete()

        contact = form.save(commit=False)
        contact.author = request.user # add logged user
        contact.save()
        messages.success(request,"Successfully saved!")
        return redirect("index")

    if Contact.objects.filter(author = request.user).exists():
        # Receiving the filled form data
        pet = Contact.objects.filter(author = request.user).first()
        form = ContactForm(request.POST or None,instance=pet)
        # Send old form data
        return render(request,"contact.html",context={"form":form})

    context = {
        "form":form
    }
    return render(request,"contact.html",context=context)

@login_required
def profile(request):
    # Call to profile detail
    info = Contact.objects.filter(author = request.user).first()

    exist = False
    # Is there detailed profile information? 
    if Contact.objects.filter(author = request.user).exists():
        exist = True

    # Send info to html page 
    context = {
        "info":info,
        "exist":exist,
        }
    return render(request,"profile.html",context=context)

def sProfile(request,id):
    info = Contact.objects.filter(id=id).first()

    context = {
        "info":info,
        }
    return render(request,"sprofile.html",context=context)


