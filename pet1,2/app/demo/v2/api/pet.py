# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas

import csv

class Pet(Resource):

    def get(self):
        with open('pets.csv', mode='r') as csvFile:
            csv_reader = csv.DictReader(csvFile)
            r = [l for l in csv_reader]
            print(r)
        return r, 200, None

    def post(self):
        row = list(g.json.values())
        with open('pets.csv', 'a+') as csvFile:
            pet_writer = csv.writer(csvFile)
            pet_writer.writerow(row)
        return row,201,None