from django.shortcuts import render
from .helper import generate_tweet
import json

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

