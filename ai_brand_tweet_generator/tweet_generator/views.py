from django.shortcuts import render
from .helper import generate_tweet
import json
import os
import psutil

def home_page_view(request):

    return render(request,'home.html')


def form_page_view(request):

    if request.method == 'POST':
        arguments = request.POST.dict()
        del arguments['csrfmiddlewaretoken']

        answer = generate_tweet(arguments)

        answer = json.loads(answer)

        brand_summery = answer.get('brand_summary')
        tweets = answer.get('tweets')

        context = {
            'brand_summery':brand_summery,
            'tweets':tweets
        }

        return render(request,'generated_tweet.html',context=context)

    return render(request,'form.html')



def get_django_ram_usage(request):
    process = psutil.Process(os.getpid())
    ram_mb = process.memory_info().rss / (1024 ** 2)
    print(f"Current Django Process RAM Usage: {ram_mb:.2f} MB")
