from django.shortcuts import redirect, render
from django.http import HttpResponse
from .utils import send_email_to_client

def send_email(request):
    send_email_to_client()

    return redirect('/')


def home(request):
    # return HttpResponse("Hey I am a robot")
    peoples = [
        {'name' : 'Onkar', 'age':20},
        {'name':'ijare', 'age':18}
    ]

    for people in peoples:
        print(people)

    vegetables = ["tomato", "chilli", "potato"]
    # return render(request, "home/index.html", context={'peoples' : peoples, 'vegetables':vegetables})
    return render(request, "home/index.html", context={'page':'Django', 'peoples':peoples})

def about(request):
    context={'page':'About'}
    return render(request, "home/about.html", context)

def contact(request):
    context={'page':'Contact'}
    return render(request, "home/contact.html", context)

def success_page(request):
    return HttpResponse("<h1>Be Successful.</h1>")


