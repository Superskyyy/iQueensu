#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-11-06 14:11:56
# Project: QHousing_Kijiji_KST

# EXMAMPLE CODE DO NOT MODIFY
from pyspider.libs.base_handler import *
import re

'''

DATA IS STILL DIRTY> NEEDS FURTHER CLEANUPS _ SOME POSTINGS ARE "LOOKING FOR" but SNEAKED IN

'''

"""
class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://www.kijiji.ca/b-apartments-condos/kingston-on/c37l1700183r40.0?ad=offering&address=Kingston&ll=44.231172,-76.485954', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }
"""

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl(
            'https://www.kijiji.ca/b-apartments-condos/kingston-on/c37l1700183r40.0?ad=offering&address=Kingston&ll=44.231172,-76.485954',
            callback=self.index_page)
        self.crawl(
            'https://www.kijiji.ca/b-room-rental-roommate/kingston-on/c36l1700183r40.0?ad=offering&address=Kingston&ll=44.231172,-76.485954',
            callback=self.index_page)
        self.crawl(
            'https://www.kijiji.ca/b-house-rental/kingston-on/c43l1700183r40.0?ad=offering&address=Kingston&ll=44.231172,-76.485954',
            callback=self.index_page)

        # This is short term
        self.crawl(
            'https://www.kijiji.ca/b-short-term-rental/kingston-on/c42l1700183r40.0?ad=offering&address=Kingston&ll=44.231172,-76.485954',
            callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        housing_names = []  # store all the posting titles
        housing_details = []
        # these are Regular postings but there are some ads needs consider too

        # [.urgent a] is likely a paid urgent posting == needs extra attention
        # [.top-feature .title > a] is likely a company posting
        # [.showcase.top-feature .title > a] a top featured posting, highly paid

        for each in response.doc('.regular-ad .title > a').items():
            print(each.attr.href)

            housing_names.append(each.html().strip())

            # go in each detail page
            self.crawl(each.attr.href, callback=self.detail_page)

        # Clearly this is for going NEXT PAGE
        print("debug section")

        next_page = response.doc('.bottom-bar a[title~="Next"]').attr.href
        # page_urls = [x.attr.href for x in response.doc('.bottom-bar a').items()]
        self.crawl(next_page, callback=self.index_page)

        return {"names": housing_names}

    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
            "price": response.doc('span > span').text(),
            "address": response.doc('[itemprop="address"]').text(),

            # Here tells what the place has or allows
            "attribute_content_list": response.doc('.attributeValue-2574930263').contents(),
            "attribute_list": response.doc('.attributeLabel-240934283').contents(),

            # This description will need further clean up.
            # Maybe phone nums emails avalibility
            "Description_dirtyInfo": response.doc('.showMoreChild-3420331552 p').contents(),
        }














