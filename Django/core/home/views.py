from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("Hey I am a robot")
    peoples = [
        {'name' : 'Onkar', 'age':20},
        {'name':'ijare', 'age':18}
    ]

    for people in peoples:
        print(people)

    vegetables = ["tomato", "chilli", "potato"]
    return render(request, "home/index.html", context={'peoples' : peoples, 'vegetables':vegetables})

def about(request):
    return render(request, "home/about.html")

def contact(request):
    return render(request, "home/contact.html")

def success_page(request):
    return HttpResponse("<h1>Be Successful.</h1>")


