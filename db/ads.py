from db.db import connect
from bson.objectid import ObjectId


class Ads():
    def __init__(self):
        self._ad = connect('ads')

    def getAdsByGreaterThreshold(self, threshhold_men_women_ratio, threshhold_crowd):
        try:
            query = {'$and': [{'threshold_men_women_ratio': {
                '$gte': threshhold_men_women_ratio}},
                {'threshhold_crowd_count': {'$gte': threshhold_crowd}},
                {'duration': {'$gt': 0}}]}
            ads = self._ad.find(query)
            allAds = []
            for ad in ads:
                allAds.append(ad)
            return allAds
        except Exception as e:
            print(e)
            return []

    def getMaxDurationAd(self):
        try:
            ad = self._ad.find().sort('duration', -1).limit(1)
            for ads in ad:
                ad = ads
            return ad
        except Exception as e:
            print(e)
            return {}

    def cutDurationOfads(self, id, duration, full_duration):
        try:
            self._ad.find_one_and_update(
                {'_id': ObjectId(id)}, {'$set': {'duration': full_duration-duration}})
            return True
        except Exception as e:
            print(e)
            return False

    def updatePrice(self, id, price):
        try:
            obj = self._ad.find_one_and_update({'_id': ObjectId(id)}, {
                '$inc': {'price': int(price)}})
            if bool(obj):
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False
