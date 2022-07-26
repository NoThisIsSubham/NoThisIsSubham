from re import findall
from VA_voice import say
from requests import get

def news(base_url):


    def content_fetch(url, search_pattern):
        return findall(search_pattern, get(url).text)
        
    
    news_urls = content_fetch(base_url, r"https://www.wsj.com/articles/[\w-]+\d{11}\?")
    for count, contents in enumerate(news_urls):
        news = content_fetch(contents, r"\w+ .")
        say("Today's Headlines..", voice_present=False)
        for i in news:
            print(i)
            say(i, voice_present=False)

        if count == 2:
            break


news("https://www.wsj.com/news/markets?")

