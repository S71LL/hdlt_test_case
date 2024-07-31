import requests
import xml.etree.ElementTree as ET


RSS_URL = 'http://static.feed.rbc.ru/rbc/logical/footer/news.rss'


def loadRSS():
    resp = requests.get(RSS_URL)
    with open('newsfeed.xml', 'wb') as f:
        f.write(resp.content)


def make_newsfeed():
    loadRSS()
    tree = ET.parse('newsfeed.xml')
    root = tree.getroot()

    title_list = root.findall('.//item/title')
    news_line = ''
    for title in title_list:
        news_line = news_line + '       ' + title.text
    return news_line
