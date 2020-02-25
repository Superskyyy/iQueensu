# from pyspider.libs.base_handler import *
#
# HUNTER = "http://www.qubirdhunter.com/?page_id=283#"
# class Handler(BaseHandler):
#
#     #@every(minutes=24 * 60)
#     def on_start(self):
#         self.crawl(HUNTER, callback=self.index_page)
#
#     #@config(age=10 * 24 * 60 * 60)
#     def index_page(self, response):
#         res = response.doc('#post-283 > div > table > tbody').items()
#
#     #@config(priority=2)
#     def detail_page(self, response):
#         return {
#             "url": response.url,
#             "title": response.doc('title').text(),
#         }

import requests
from bs4 import BeautifulSoup
import time


def get_web(currenturl):
    try:
        res = requests.get(currenturl)
        res.raise_for_status()
        print(res.content)
        return res.content
    except requests.RequestException as e:
        print(e)
        return


def get_para(url):
    article = []
    #time.sleep(1)
    text = get_web(url)
    soup = BeautifulSoup(text, 'html.parser')
    para_list = soup.find_all("table")


    return para_list


def main():
    # input = "url-md.txt"
    # output = "amd_articles.txt"
    # dom = 'H'
    # domain = 'Health'
    # website = "medical daily"
    # num = 1  # starting ID
    # text_start, text_end = 0, -1

    # no duplicate url(articles)
    q = []
    url = "https://www.qubirdhunter.com"
    print(get_para(url))
    # with open(input) as f:
    #     for line in f:
    #         currenturl = line.strip('\n')
    #         if currenturl not in q:
    #             q.append(currenturl)
    #             self.get_para(output, currenturl, num, dom, domain, website, text_start, text_end)
    #             print('finished URL' + str(num))
    #             num += 1
    return

main()