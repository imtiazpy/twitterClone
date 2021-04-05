import random
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.utils.http import is_safe_url

from .models import Tweet
from .forms import TweetForm

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.

def home(request, *args, **kwargs):
    return render(request, 'pages/home.html', context={}, status=200)

def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
        
    return render(request, 'components/form.html', context={'form': form})

def tweet_list_view(request, *args, **kwargs):
    """
    API View

    """

    qs = Tweet.objects.all().order_by('-id')
    tweet_list = [{'id': i.id, 'content': i.content, 'likes': random.randint(0, 123)} for i in qs]
    # print('testing..............',tweet_list)
    # print('testing...............', qs)
    data = {
        'isUser': False,
        'response': tweet_list
    }
    return JsonResponse(data)
    


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    API View
    consume by JS
    """
    data = {
        'id': tweet_id,
        # 'content': obj.content,
        # 'img': obj.image.url
    }
    status = 200

    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = 'Not found'
        status = 404
    
    return JsonResponse(data, status=status)



        

