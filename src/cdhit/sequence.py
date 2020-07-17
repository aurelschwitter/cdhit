import os
import sys
import gzip
import numpy as np


class Sequence:

    # real sequence, if not stored in swapfile
    data = ""

    # length of sequence
    size = 0

    # size of buffer
    bufsize = 0

    # size = size_r1 + size_r2 for back-to-back merged seq
    size_r2 = 0

    # swap file
    swap_file = None

    # current offset in swapfile
    offset = 0

    # stream offset of the description string in the database
    des_begin = 0
    des_begin2 = 0

    # total record lengths
    tot_length = 0
    tot_length2 = 0

    # identifier of the sequence
    identifier = ""

    # index of the sequence in the original database:
    index = 0
    state = 0
    cluster_id = 0
    identity = 0.0
    distance = 0.0
    coverage = np.array({0, 0, 0, 0})

    def __init__(self, options):
        self.distance = 2.0
        self.options = options

    def from_seq(self, other_seq):
        self = other_seq

        if (len(other_seq.data) != 0):
            self.size = self.bufsize = other_seq.size
            self.size_r2 = 0
            str.join(self.data, '\0')

        if (len(other_seq.identifier) != 0):
            self.identifier += '\0'

    def from_2seq(self, other_seq, other_seq2, mode):

        if (mode != 1):
            raise "unknown mode"

    def __del__(self):
        del self.data
        del self.identifier

    def __add__(self, additional_data):
        self.data = ''.join([self.data, additional_data])
        return self

    def clear(self):
        del self.data
        self.bufsize = 0
        self.data = ""

    # replace Sequence = Sequence operation from c++
    def assign(self):
        pass

    def resize(self, n):
        pass

    def reserve(self, n):
        pass

    def swap(self, other):
        pass

    def format(self):
        pass

    def convert_bases(self):
        pass

    def trim(self, trim_len):
        pass

    def swap_in(self):
        pass

    def swap_out(self):
        pass

    def print_info(self, id, out_path, options):
        pass
