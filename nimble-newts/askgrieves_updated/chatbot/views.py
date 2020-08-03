from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Chatbot


# Create your views here.
def test(request):
    return HttpResponse("You are on the test page")


def edit(request, bot_id):
    bot = get_object_or_404(Chatbot, pk=bot_id)
    return render(request, 'chatbot/edit.html', {'bot': bot})


def lookat(request, bot_id):
    bot = get_object_or_404(Chatbot, pk=bot_id)
    return render(request, 'chatbot/looking.html', {'bot': bot})