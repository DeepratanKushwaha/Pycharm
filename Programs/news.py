from GoogleNews import GoogleNews
googleNews = GoogleNews()
googleNews = GoogleNews(period='7d')
googleNews.search('Pakistan')
result = googleNews.result()

for x in result:
    print("="*50)
    print("Title--", x['title'])
    print("Date/Time--", x['date'])
    print("Description--", x['desc'])
    print("Link", x['link'])
