from groq import Groq
import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

client_search = TavilyClient(os.getenv('Tavily_API_KEY'))
client = Groq(api_key=os.getenv('GROQ_API_KEY') )


def research_brand(brand):
    goal = f"""
    Research the brand {brand} using its official website
    and publicly accessible, relevant campaign pages.


    Find:
    1. Main products and services.
    2. Target audience.
    3. Brand voice and messaging.
    4. Recent campaigns or product announcements, if available.
    5. Relevant public social media posts, if accessible.

    Return a concise research report in String.
    Include source URLs and dates when available.
    Distinguish verified findings from assumptions.
    Do not invent posts, engagement numbers, or dates.
    """

    response = client_search.search(
        query=goal,
        search_depth="advanced"
    )


    return response['results'][0].get('content')

def generate_tweet(kwargs):
    brand = kwargs.get('brand_name',None)
    industry = kwargs.get('industry',None)
    objective = kwargs.get('objective',None)
    audience = kwargs.get('audience',None)
    products = kwargs.get('products',None)
    additional_info = kwargs.get('additional_info',None)


    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role":"system",
                "content":" Donot add any link and any foul language "
            },
            {
                "role": "user",
                "content":f"""
                        
                        Information about the brand is
                        Brand: {brand}
                        Industry / Category: {industry}
                        Campaign Objective: {objective}
                        Traget Audience: {audience}
                        Products / Services: {products}
                        any if present additional_info:{additional_info} 

                        Brand Research
                        {research_brand(brand)}

                        Analysing recent social media posts (Twitter/X, Instagram, LinkedIn, etc.) and Brand Reasearch
                        and 
                        First Brand Summery in  100-150 words then
                        Generate 10 Brand Tweet with mixed tone like  engaging / conversational, promotional, witty / meme-style, informative / value-driven
                        The tweet should be below 100 words

                        """,
            }
        ],
        model="openai/gpt-oss-120b",
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "brand_tweets",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "brand_summary": {
                            "type": "string",
                        },
                        "tweets": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "minItems": 10,
                            "maxItems": 10
                        }
                    },
                    "required": [
                        "brand_summary",
                        "tweets"
                    ],
                    "additionalProperties": False
                }
            }
        }
    )

    return chat_completion.choices[0].message.content


