import numpy as np
from os import listdir
import matplotlib.pyplot as plt


class ECG:
    def __init__(self, path, id):
        self.id = id
        self.data_1 = []
        self.data_2 = []

        with open(path, 'r') as fp:
            all_lines = fp.readlines()
            self.data_1 = [int(i.replace('\n', ''))
                           for i in all_lines if i != '']
        
        path2 = path.replace('HealthCare', 'HealthCare2')[:-34] + listdir(path.replace('HealthCare', 'HealthCare2')[:-34])[0]
        try:
            with open(path2, 'r') as fp:
                all_lines = fp.readlines()
                self.data_2 = [int(i.replace('\n', ''))
                               for i in all_lines if i != '']
        except:
            print(f'{path2}not found')
