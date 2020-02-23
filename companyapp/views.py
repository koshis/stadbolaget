from django.shortcuts import render,redirect
from .contact_us import ContactForm
from companyapp import models as m
from django.utils import timezone
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives



# Create your views here.
def home(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        # A POST request: Handle Form Upload
        # Bind data from request.POST into a PostForm
        form = ContactForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            _send_email(model_instance.Name, model_instance.Email, model_instance.PhoneNumber, model_instance.Location, model_instance.Message)
            return redirect('/')

    return render(request, 'home_page.html', {
        'form': form,
    })

def quality(request):
    return render(request, 'quality.html')

def cleaning(request):
     if request.method == 'GET':
        form = ContactForm()
     else:
        # A POST request: Handle Form Upload
        # Bind data from request.POST into a PostForm
        form = ContactForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            _send_email(model_instance.Name, model_instance.Email, model_instance.PhoneNumber, model_instance.Location, model_instance.Message)
            return redirect('/')

     return render(request, 'cleaning.html', {
        'form': form,
    })
def propertyservice(request):
     if request.method == 'GET':
        form = ContactForm()
     else:
        # A POST request: Handle Form Upload
        # Bind data from request.POST into a PostForm
        form = ContactForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            _send_email(model_instance.Name, model_instance.Email, model_instance.PhoneNumber, model_instance.Location, model_instance.Message)
            return redirect('victory')

     return render(request, 'propertyservice.html', {
        'form': form,
    })
def pages(request, title):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            _send_email(model_instance.Name, model_instance.Email, model_instance.PhoneNumber, model_instance.Location, model_instance.Message)
            return redirect('/')
    pagedetail=m.Pages.objects.filter(Title__icontains=title,published=True)
    if pagedetail:
        return render(request,'detailpage.html',{'pagedetail':pagedetail, 'form': form,})
    else:
        return render(request,'404.html')
def _send_email( Name, Email, Phonenumber, Location, Message):
    html_email='Name: '+  Name +'<br/>'+'Email: '+Email+'<br/>'+'Phone Number: '+Phonenumber+'<br/>'+'Location: '+Location+'<br/>'+'Message: '+Message
    msg = EmailMultiAlternatives(subject='Customer Enquery', body=html_email, from_email='customer@stadbolagetmarsta.se', to=['info@stadbolagetmarsta.se'])
    msg.attach_alternative(html_email, "text/html")

   # msg.content_subtype = "html"  # Main content is now text/html
    return msg.send(fail_silently=False)