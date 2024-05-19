from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

course_dic = {
    "python" : "Python Course Page",
    "java" : "Java Course Page",
    "kotlin" : "Kotlin Course Page",
    "swift" : "Swift Course Page"
}

def index(request):
    return HttpResponse("This is first Django project, first index")

def course(request, item):
    try:
        course1 = course_dic[item]
        return HttpResponse(course1)
    except:
        return HttpResponseNotFound("Not Found! Please look for another course!")
        #raise Http404("Not Found! Please look for another course!")
    #return HttpResponse(course_dic.get(item,"Not Found!"))

def multiply_view(request, num1, num2):
    result = num1 * num2
    return HttpResponse(f"{num1} * {num2} = {result}")

def course_number_view(request,number1):
    course_list = list(course_dic.keys())
    try:
        course_name = course_list[number1]

        page_to_go = reverse("course",args=[course_name])
        return HttpResponseRedirect(page_to_go)
    except:
        return HttpResponseNotFound("Not Found! Please look for another course!")