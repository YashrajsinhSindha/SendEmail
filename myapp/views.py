from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail,EmailMultiAlternatives
from sendEmailDemo.settings import EMAIL_HOST_USER
# Create your views here.
def index(request):

    if request.method=="POST":
        #fetch data from form
        sub=request.POST.get("subject")
        msg=request.POST.get("message")

        #approach1 
        #send_mail('Subject here', 'Here is the message.',  'from@example.com',  ['to@example.com'], fail_silently=False,)
        #send_mail(sub,msg,EMAIL_HOST_USER,['Enter the mail details where you want to send'])

        #approach 2
        email=EmailMultiAlternatives(sub,msg,EMAIL_HOST_USER,['Enter the mail details where you want to send'])
        email.attach('django.png','static/images')
        email.send()

        return HttpResponse("Email sent successfully")
    else:
        return render(request,'mail.html')    


