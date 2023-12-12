from formatter import NullFormatter
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse

# Create your views here.

numbers={
    "first":"Thanks for visiting this my first code",
    "second":"Thanks for visiting this my second code",
    "third":"Thanks for visiting this my third code",
    "four":"Thanks for visiting this my foruht code",
    "five":"Thanks for visiting this my fivth code"
}

def index(request):
    got_list= list(numbers.keys())
    cont="Python with Django framework project"
    items=""
    
    for i in got_list:
        items+= f"<li><a href=\"/firstpage/{i}\">{i}</a></li>"
    
    result=f"<h1>{cont}</h1><ul><h1>{items}</h1></ul><footer><h3>Thanks for visiting<h3/></footer>"
    return HttpResponse(result)
    
'''''def firstpage_by_number(request, number):
    numb= list(numbers.keys())
    redirect_number= numb[number-1]
    redirect_path= reverse("numbergot", kwargs=[redirect_number])
    return HttpResponseRedirect(redirect_path) '''''

def firstpage(request, mon):    
    try:
        num=numbers[mon]
        return render(request, "firstpage/color.html", {"text":num})
        #result= render_to_string("color.html")
        #return HttpResponse(result)
    except:
        return HttpResponseNotFound("This is invalid code")
                
