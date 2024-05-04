from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from main.models import Person

# def index(request):
#     person=Person.objects.all()
#     next_page_url=reverse("main:next_page")
#     context={
#         'Login': 'Таблица',
#         'description': 'Список пользователей',
#         'person': person,
#         'next_page_url' : next_page_url,
#     }
#     return render(request, "main/main.html", context)

def index(request):
    people = Person.objects.all()
    return render(request, "main/main.html", {"people": people})

def create(request):
    if request.method=="POST":
        person=Person()
        person.name=request.POST.get("name")
        person.surname=request.POST.get("surname")
        person.save()
    #return render(request, "main/main.html")
    return HttpResponseRedirect('/')

def edit(request, id):
    try:
        person=Person.objects.get(id=id)
        if request.method=="POST":
            person.name=request.POST.get("name")
            person.surname=request.POST.get("surname")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "main/next.html", {"person" : person})
                                             
    except person.DoesNotExist:
        return HttpResponseRedirect("<h2>Not found page :(</h2>")
    
def delete(request, id):
    try:
        person=Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except person.DoesNotExist:
        return HttpResponseRedirect("<h2>Not found page :( </h2>")

# def next_page(request):
#     index_url=reverse("main:index")
#     context={
#         'index_url' : index_url,
#     }
#     return render(request, "main/next.html", context)
    
