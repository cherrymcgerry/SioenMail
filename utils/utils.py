from __future__ import absolute_import, division, print_function

import csv
import logging
import os
import sys
from io import open

from numpy import unicode
from scipy.stats import pearsonr, spearmanr
from sklearn.metrics import matthews_corrcoef, f1_score

from multiprocessing import Pool, cpu_count
from tqdm import tqdm

class Input(object):

    def __init__(self,guid,text_a,text_b=None,label=None):

        self.guid = guid
        self.text_a = text_a
        self.text_b = text_b
        self.label = label


class InputFeatures(object):
    def __init__(self,input_ids,input_mask,segment_ids,label_id):
        self.input_ids = input_ids
        self.input_mask = input_mask
        self.segment_ids = segment_ids
        self.label_id = label_id


class DataProcessor(object):

    def get_train_set(self,data_dir):
        raise NotImplementedError()


    def get_dev_examples(self,data_dir):
        raise NotImplementedError()

    def get_labels(self):
        raise NotImplementedError()

    @classmethod
    def _read_tsv(cls,input_file,quotechar=None):
        with open(input_file, 'r', encoding="utf-8-sig") as f:
            reader = csv.reader(f,delimiter="\t",quotechar=quotechar)
            lines = []
            for line in reader:
                if sys.version_info[0] ==2:
                    line = list(unicode(cell, 'utf-8') for cell in line)
                lines.append(line)
            return lines



#TODO implement data to inputexamples
class BinaryProcessor(DataProcessor):

    def get_train_set(self,data_dir):
        raise NotImplementedError()

    def get_dev_examples(self,data_dir):
        raise NotImplementedError()

    def get_labels(self):
        raise NotImplementedError



