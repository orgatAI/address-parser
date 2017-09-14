#!/usr/bin/env python
# -*-coding=utf-8-*-


import json
import os
CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
DATA_PATH = os.path.join("/".join(CURRENT_PATH.split("/")[:-1]) , "data")

SHORT_NAME_PATH = os.path.join(DATA_PATH, "short_address.json")
WHOLE_NAME_PATH = os.path.join(DATA_PATH, "whole_address.json")

def load_data(path):
    data = json.load(open(path))
    return data

def load_all_data():
    shot_names = load_data(SHORT_NAME_PATH)
    whole_names = load_data(WHOLE_NAME_PATH)

    provinces = shot_names.get("province") + whole_names.get("province")
    citys = shot_names.get("city") + whole_names.get("city")
    sub_city = shot_names.get("sub_city") + whole_names.get("sub_city")
    return provinces, citys, sub_city


