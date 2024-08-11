from django.shortcuts import render,redirect
from .forms import Msg
# Create your views here.
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
                           "Flask" : "flask.png","DOM":"dom.png","jQuery":"jquery.png","Jinja":"jinja.png",
                           "WTForms":"wtforms.png"}},
       {"Programming Language":{"Python":"python.png","Java":"java.png","C":"c.png","Javascript":"javascript.png",}},
       {"Data Science" : {"Pandas":"pandas.png","NumPy":"numpy.png","Matplotlib":"matplotlib.png","Scikit-Learn":"scikitlearn.png"}},
       {"Machine Learning":{"Tensorflow":"tensorflow.png","Keras":"keras.png","Scikit-Learn":"scikitlearn.png"}},
       {"Data Base":{"SQLite":"sqlite.png","SQLAlchemy":"sqlalchemy.png", "JSON":"json.png",}}, 
       {"Web Scrapping": {"Selenium":"selinium.png","Beautiful Soup":"beautifulsoup.png"}},
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

        if form.is_valid():   
            
            form.save(commit=True)

            form=Msg()
            
        else:
            form=Msg()



    return render(request,"contact.html",{'form':form})






