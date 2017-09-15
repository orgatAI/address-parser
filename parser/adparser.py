#!/usr/bin/env python
# -*-coding=utf-8-*-


from prefix_query import PrefixQuery
from utils import  load_all_data

class Address(object):
    def __init__(self):
        self.province = ""
        self.city = ""
        self.sub_city = ""
        self.aera = ""
        self.road = ""
        self.poi = ""
        self.num = ""
        self.rom = ""

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
        province, province_index = self.province_search.query(text)
        print(province)
        print(province_index)
        if province:
            address.province = province
            text = text[province_index:]

        city , city_index = self.city_search.query(text)
        print(text)
        if city and city_index == len(city):
            address.city= city
            text =text[city_index:]

        sub_city, sub_index = self.sub_city_search.query(text)
        print(self.sub_city_search.prefix_dict.get('朝阳区'))
        print(sub_city)
        print("sub_city")
        print(text)
        if sub_city:
            if city_index>0 and sub_index == len(sub_city):
                address.sub_city = sub_city
                text = text[sub_index:]
        return address.to_dict()


parser = AddressParser()

text = "北京市朝阳区建外SOHO西区11号楼2605室"
res = parser.parse(text)
print(res)
exit(0)
def test():
    path = "../data/all_location.csv"
    f = open(path)
    for line in f.readlines():
        data_info = line.split()
        print (line)
        res = parser.parse(data_info[0])
        print(res)
        input()
test()
