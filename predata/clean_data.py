#!/usr/bin/env python

# -*-coding=utf-8-*-

path = "location.txt"
import json

EX = ['省直辖县级行政区划',
      '自治区直辖县级行政区划']


data_path = "../data/top_address.json"
shot_name_path  = "../data/short_address.json"
whole_name_path = '../data/whole_address.json'

def clean_data():
    f = open(path)
    all_data = {}
    province = []
    city = []
    sub_city = []

    for line in f.readlines():
        line = line.strip()
        data = line.split()
        code = int(data[0])
        name = data[1]
        if code % 10000 == 0:
            province.append((name, code))
        elif code % 100 ==0:
            if name in EX :
                continue

            city.append((name, code))
        else:
            sub_city.append((name, code))

    all_data["province"] = province
    all_data['city'] = city
    all_data['sub_city'] = sub_city
    json.dump(all_data, open(data_path, 'w', encoding="utf-8"), ensure_ascii=False , indent=4)


class ShortName(object):
    def __init__(self):
        self.suffix = [
            "自治州",
            "自治区",
            "自治县",
            "地区",
            "省",
            "市",
            "区",
            "县",
            "镇",
            "旗",
        ]

    def gen_shotname(self, name):
        for suffix in self.suffix:
            if suffix in name:
                shot_name = name.replace(suffix, "")
                if len(shot_name) > 1:
                    return shot_name
        return ""

SHORT_NAME = ShortName()
def gen_name_dict():
    shot_names = {}
    whole_names = {}
    data = json.load(open(data_path))
    province = data.get("province")
    city = data.get("city")
    sub_city = data.get("sub_city")

    province_names = [item[0] for item in province]
    city_names = [item[0] for item in city]
    sub_city_names = [item[0] for item in sub_city]

    whole_names["province"] = province_names
    whole_names['city'] = city_names
    whole_names["sub_city"] = sub_city_names
    json.dump(whole_names, open(whole_name_path, "w"), ensure_ascii=False, indent=4)
    shot_names['province'] = list(set([SHORT_NAME.gen_shotname(name) for name in province_names if SHORT_NAME.gen_shotname(name)]))
    shot_names["city"] = list(set([SHORT_NAME.gen_shotname(name) for name in city_names if SHORT_NAME.gen_shotname(name)]))
    shot_names['sub_city']  = list(set([SHORT_NAME.gen_shotname(name) for name in sub_city_names if SHORT_NAME.gen_shotname(name)]))
    json.dump(shot_names, open(shot_name_path, 'w') , ensure_ascii=False, indent=4)


clean_data()
gen_name_dict()

