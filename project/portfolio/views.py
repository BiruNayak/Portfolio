from django.shortcuts import render, redirect
from django.contrib import messages
from portfolio.models import Contact,Blogs


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def handleblog(request):
    posts = Blogs.objects.all()
    context = {"posts":posts}
    return render(request, "handleblog.html",context)


def contact(request):
    if request.method == "POST":
        get_name = request.POST.get("name")
        get_email = request.POST.get("email")
        get_phonenumber = request.POST.get("phonenumber")
        get_desc = request.POST.get("description")
        print(get_name, get_email, get_phonenumber, get_desc)
        query = Contact(name=get_name,email=get_email,phonenumber=get_phonenumber,description=get_desc)
        query.save()
        messages.info(request,"Thank you for contacting us. we will get you soon!" )
        return redirect("/contact")
    return render(request, "contact.html")

