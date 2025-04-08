from serpapi import GoogleSearch
import os


def search_with_serpapi(query):
    search = GoogleSearch({
        "q": query,
        "api_key": os.getenv("SERPAPI_KEY"),
        "num": 3
    })
    results = search.get_dict()
    return [result['title'] + ": " + result['link'] for result in results.get('organic_results', [])]
