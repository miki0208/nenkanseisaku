from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Tweet
# Create your views here.
def index(request):
    tweet_list = Tweet.objects.all()
    return render(request,"index.html",{"tweet_list":tweet_list})


def post(request):
    message = request.POST["message"]
    name = request.POST["name"]
    tweet = Tweet(message=message, name=name)
    tweet.save()
    return HttpResponseRedirect(reverse("a:index"))
    # return HttpResponse("Message is:" + message)
# def index(request):
#     template = loader.get_template("polls/index.html")
#     return HttpResponse(template.render({}, request))

def page(request, tweet_id): # ここ変えた
    page = Tweet.objects.get(id=tweet_id) # ここも変えた
    tweet_list = Tweet.objects.all()
    context = {
        "page":page,
        "tweet_list":tweet_list,
        # "name": name,
        # 'message': message,
    }
    template = loader.get_template("page.html")
    return HttpResponse(template.render(context, request))


def vote(request, tweet_id, choice_id):
    choice = page.objects.get(id=choice_id)
    choice.votes = choice.votes + 1
    choice.save()
    return HttpResponse('いいねを押しました。')

def toukou(request):
    return render(request,"toukou.html")