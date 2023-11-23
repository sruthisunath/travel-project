from django.shortcuts import render
from.models import Place
from.models import Team
# Create your views here.
def home(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'res':obj,'result':obj1})
    


# def addition(request):
    # a=int(request.GET['num1'])
    # b=int(request.GET['num2'])
    # res=(a+b)
    # return render(request,"result.html",{"result": res})
    # res1=(a-b)
    # return render(request,"result.html",{"result": res1})
    #
    # res2=(a*b)
    # return render(request,"result.html",{"result": res2})
    #
    # res3=(a/b)
    # return render(request,"result.html",{"result":res3})
