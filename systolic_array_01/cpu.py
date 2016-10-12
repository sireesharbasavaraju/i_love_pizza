from functionalunit import FU
import json
from pprint import pprint

class CPU(object):

    def __init__(self):
        self.A0 = FU()
        self.A1 = FU()
        self.B0 = FU()
        self.B1 = FU()

        self.a0 = []
        self.a1 = []
        self.b0 = []
        self.b1 = []

    def init(self, filename):
        with open(filename) as json_data:
            json_read = json.load(json_data)
        for k,v in json_read.items():
            print k
            print v
            print type(v)
    def run(self):
        pass

