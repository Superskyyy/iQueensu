import datetime

import pymongo
from pyspider.result import ResultWorker

# This is deprecated change to postgresql

TIME = str(datetime.datetime.now())  # timestamp results in db


# OVERRIDE DEFAULT - OUTPUT TO MONGODB
class MyResultWorker(ResultWorker):
    def on_result(self, task, result):

        if not result:
            return
        client = pymongo.MongoClient(host='35.183.130.225',
                                     port=27017, username="root",
                                     password="iqueensu", authSource="admin")

        db = client['qhousing_result_dev']
        coll = db['sky_test_scrape']
        if result['address'][0] == ',':
            result['address'] = result['address'][1:]
        ##################################################
        #   translate address to geocode - to do list    #
        ##################################################
        # dummy geocode
        dummy_geo = '123321,456789'
        data = {
            'time_stamp': TIME,
            'house_url': result['url'],
            'house_title': result['title'],
            'house_price': result['price'],
            'house_address': result['address'],
            # 'house_geocode': result['geocode'],
            'house_geocode': dummy_geo,
            'house_properties': result['properties'],
            'house_dirty_description': result['description_dirty_info'],

        }
        coll.insert(data)
        # print (data_id)
