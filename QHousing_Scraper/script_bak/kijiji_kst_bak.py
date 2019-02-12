#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-11-06 14:11:56
# Project: QHousing_Kijiji_KST_DEV

'''
https://github.com/googlemaps/google-maps-services-python
'''
import datetime

import googlemaps
from pyspider.libs.base_handler import *

'''
DATA IS STILL DIRTY> NEEDS FURTHER CLEANUPS _ SOME POSTINGS ARE "LOOKING FOR" but SNEAKED IN
'''

# GEOCODER - COCO's Account api
GEO_APIKEY = "AIzaSyApYnvaIs_OrTPauFoYfNpX149PhTJ_u44"
gmaps = googlemaps.Client(key=GEO_APIKEY)
TIME = str(datetime.datetime.now())  # timestamp results in db

KIJIJI_BASE = ['https://www.kijiji.ca/', '/kingston-on/',
               'r40.0?ad=offering&address=Kingston&ll=44.231172,-76.485954', ]
TARGET_CATA = ['b-apartments-condos', 'b-room-rental-roommate', 'b-house-rental', 'b-short-term-rental']
TARGET_HASH = ['c37l1700183', 'c36l1700183', 'c43l1700183', 'c42l1700183']


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):

        for idx in range(len(TARGET_CATA)):
            self.crawl(
                KIJIJI_BASE[0] + TARGET_CATA[idx] + KIJIJI_BASE[1] \
                + TARGET_HASH[idx] + KIJIJI_BASE[2],
                callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        housing_names = []  # store all the posting titles
        housing_details = []

        # these are Regular postings but there are some ads needs consider too
        # NOT IMPLEMENTED YET
        # [.urgent a] is likely a paid urgent posting == needs extra attention
        # [.top-feature .title > a] is likely a company posting
        # [.showcase.top-feature .title > a] a top featured posting, highly paid

        for each in response.doc('.regular-ad .title > a').items():
            housing_names.append(each.html().strip())
            self.crawl(each.attr.href, callback=self.detail_page)

        # Clearly this is for going NEXT PAGE
        print("debug section")

        next_page = response.doc('.bottom-bar a[title~="Next"]').attr.href

        self.crawl(next_page, callback=self.index_page)

    def detail_page(self, response):

        address = response.doc('[itemprop="address"]').text()

        # Housing properties
        attr_list = response.doc('.attributeLabel-240934283').contents()
        attr_content = response.doc('.attributeValue-2574930263').contents()
        attr_mapped = '**' + '**'.join([(pair[0] + ' ' + pair[1]) \
                                        for pair in zip(attr_list, attr_content)])

        # Descriptions - some descriptions have strong tags.
        try:
            dirty_info = (response.doc('.showMoreChild-3420331552 p') \
                          .contents())
            dirty_info_merged = '**' + '**'.join([i.text() \
                                                  for i in dirty_info.items() \
                                                  if i.text() != ''])
        except:
            # extremely rare bullshit extreme cases, html structure changed
            dirty_info_strong = (response.doc('strong') \
                                 .contents())

            dirty_info_merged = '**' + '**'.join([i.text() \
                                                  for i in dirty_info.items() \
                                                  if i.text() != ''])

        return {
            "url": response.url,
            "title": response.doc('.title-2323565163').text(),
            "price": response.doc('span > span').text(),
            "address": address,
            "properties": attr_mapped,
            # This description will need further clean up.
            "description_dirty_info": dirty_info_merged,
            # "geocode": gmaps.geocode(address)
        }


# OVERRIDE DEFAULT - OUTPUT TO MONGODB
'''
def on_result(self, result):

    if not result:
        return
    client = pymongo.MongoClient(host='35.183.130.225', port=27017)
    db = client['qhousing_project_dev']
    coll = db['sky_test_scrape']

    ##################################################
    #   translate address to geocode - to do list    #
    ##################################################
    data = {
        'time_stamp': TIME
        'house_url': result['url'],
        'house_title': result['title'],
        'house_price': result['price'],
        'house_address': result['address'],
        'house_geocode': result['geocode'],
        'house_properties': result['properties'],
        'house_dirty_description': result['description_dirty_info'],

    }

    data_id = coll.insert(data)
    print (data_id)

'''
