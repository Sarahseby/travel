from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#def demo(request):
 #   name="sara"
  #  return render(request,"form1.html")
def tem(request):
    return render(request,'index.html')
#def addition(request):
 #   x=int(request.GET['num1'])
  #  y=int(request.GET['num2'])
   # res=x+y
    #return render(request,'result.html',{'result':res})

