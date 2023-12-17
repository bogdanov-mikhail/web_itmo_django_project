from django.shortcuts import render
from app.models import Feedback

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect


def redirect(request):
    return HttpResponseRedirect("/main")


def main(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def feedback(request):
    if request.method == 'POST':
        process_feedback(request.POST)

    return render(request, "feedback.html")


def process_feedback(body):
    name = body.get("name")
    surname = body.get("surname")
    email = body.get("email")
    message = body.get("message")

    feedback_entity = Feedback()
    feedback_entity.name = name
    feedback_entity.surname = surname
    feedback_entity.email = email
    feedback_entity.message = message

    feedback_entity.save()
