from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from django.contrib import messages
from contact.models import Contact
from pets.models import Pet
from .forms import PetForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

@login_required # Shown only logged in users 
def dashboard(request):
    # Calls the user's pet objects
    pets = Pet.objects.filter(author = request.user)
    context = {
        "pets":pets,
        }
    return render(request,"dashboard.html",context=context)

def objectives(request):
    return render(request,"objectives.html")

@login_required # Shown only logged in users 
def addpet(request):
    # Receives what is sent (form and pictures)
    form = PetForm(request.POST or None,request.FILES or None)

    # add new pet
    if form.is_valid():
        pet = form.save(commit=False)
        pet.author = request.user # add logged user
        pet.save()
        messages.success(request,"Successfully saved!") # Flash messages
        return redirect("dashboard")

    return render(request,"addpet.html",{"form":form})

def detail(request,id):
    pet = get_object_or_404(Pet,id=id) # Send 404 if not found 
    return render(request,"detail.html",{"pet":pet})

# For the page that lists all the pets 
def allPets(request):
    # Call all Contact objects for allpets page
    contacts = Contact.objects.all()

    # Search request 
    keyword = request.GET.get("keyword")

    # Return search results
    if keyword:
        pets = Pet.objects.filter(petName__contains = keyword) 
        form = {
            "pets":pets,
            "contacts":contacts,
        }
        return render(request,"allpets.html",context=form)

    # For default page display
    pets = Pet.objects.all()
    form = {
        "pets":pets,
        "contacts":contacts,
    }
    return render(request,"allpets.html",context=form)

@login_required # Shown only logged in users 
def updatePet(request,id):
    pet = get_object_or_404(Pet,id=id) # Send 404 if not found 

    # Receives what is sent (form and pictures)
    form = PetForm(request.POST or None,request.FILES or None,instance=pet)

    if form.is_valid():
        pet = form.save(commit=False)
        pet.author = request.user
        pet.save()
        messages.success(request,"Successfully updated")
        return redirect("index")

    return render(request,"update.html",{"form":form})

@login_required # Shown only logged in users 
def deletePet(request,id):
    pet = get_object_or_404(Pet,id=id) # Send 404 if not found 
    pet.delete()
    messages.success(request,"Successfully deleted")
    return redirect("dashboard")


