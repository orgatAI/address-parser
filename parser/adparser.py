#!/usr/bin/env python
# -*-coding=utf-8-*-


from parser.prefix_query import PrefixQuery
from parser.utils import  load_all_data

class Address(object):
    def __init__(self):
        self.province = ""
        self.city = ""
        self.sub_city = ""

    def to_dict(self):
        return self.__dict__


class AddressParser(object):
    def __init__(self):
        self._init()


    def _init(self):
        province, city, sub_city = load_all_data()
        self.province_search = PrefixQuery(province)
        self.city_search = PrefixQuery(city)
        self.sub_city_search = PrefixQuery(sub_city)


    def parse(self, text):
        address = Address()
        province, index = self.province_search.query(text)

        if province:
            address.province = province
            text = text[index:]
        city , index = self.city_search.query(text)

        if city:
            address.province = city
            text =text[index:]
        sub_city, index = self.sub_city_search.query(text)
        if sub_city:
            address.sub_city = sub_city
        return address.to_dict()