from django.shortcuts import render,redirect
from .forms import Msg
# Create your views here.
from django.core.mail import send_mail

def send_to_rep_email(name,email,text):
    subject = 'Your Message Reached To Sivakumar'
    message = f"Hey {name} I Got Your Message,\n\n\n\nI will reply As Soon As Posible \n\n\n\nYour Message \n\n{text}"
    from_email = 'sivakumarpersonal.7@gmail.com'
    recipient_list = [f"{email}"]
    send_mail(subject, message, from_email, recipient_list ,fail_silently=False,)
def send_to_sk_email(name,email,text):
    subject = f"Message Reached From {name}"
    message = f"{text} \n\n\n\nFrom:{email}"
    from_email = 'sivakumarpersonal.7@gmail.com'
    recipient_list = ["sivakumar120956@gmail.com"]
    send_mail(subject, message, from_email, recipient_list,fail_silently=False,)
def home(request):
    #here the value should given with dict
    mydict={"hi":"hello"}
    return render(request,"home.html",context=mydict)
def about(request):
    mydict2={"hello" : "hi"}
    return render(request,"about.html",context=mydict2)
def skills(request):
    web={"skilllist":
        [{"Web Development":{"Html" : "html.png","CSS" : "css.png","Javascript" : "javascript.png","Bootstrap":"bootstrap.png","Django" : "django.png",
                           "Flask" : "flask.png","DOM":"javascript.png","jQuery":"jquery.png","Jinja":"jinja.png",
                           }},
       {"Programming Language":{"Python":"python.png","Java":"java.png","C":"c.png","Javascript":"javascript.png",}},
       {"Data Science" : {"Pandas":"pandas.png","NumPy":"numpy.png","Matplotlib":"matplotlib.png","Scikit-Learn":"scikitlearn.png"}},
       {"Machine Learning":{"Tensorflow":"tensorflow.png","Keras":"keras.png","Scikit-Learn":"scikitlearn.png"}},
       {"Data Base":{"SQLite":"sqlite.png","SQLAlchemy":"sqlalchemy.png", "JSON":"json.png",}}, 
       {"Web Scrapping": {"Selenium":"selenium.png","Beautiful Soup":"beautifulsoup.png"}},
       {"Others":{"NLTK":"nltk.png","OpenCV":"opencv.png",}}

       ] 
        }
    return render(request,"skills.html" , context=web)
def projects(request):
    mydict2={"hello" : "hi"}
    return render(request,"projects.html",context=mydict2)
def contact(request):
    mydict2={"hello" : "hi"}

    form= Msg()

    if request.method=="POST":

        form=Msg(request.POST)
        name=request.POST.get("name")
        email=request.POST.get("email")
        text=request.POST.get("text")

        if form.is_valid():
            form=Msg()
            send_to_rep_email(name,email,text)
            send_to_sk_email(name,email,text)        
        else:
            form=Msg()



    return render(request,"contact.html",{'form':form})







