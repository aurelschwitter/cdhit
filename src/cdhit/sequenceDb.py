import numpy as np
import gzip
import os
from sequence import Sequence
from options import Options


class SequenceDB:

    NAAN = 0

    sequences = []

    rep_seqs = []

    total_letter = 0
    total_desc = 0
    max_len = 0
    min_len = 0
    len_n50 = 0

    def __del__(self):
        self.clear()

    def clear(self):
        del self.sequences
        self.sequences = []
        self.rep_seqs = []

    def read(self, path, options: Options):

        # read from file directly or use gzip when necessary
        file_extension = os.path.splitext(path)[1]
        if (file_extension == ".gz"):
            file_in = gzip.open(path, "r")
        else:
            file_in = open(path, "r")

        seq_one = Sequence(options)
        seq_des = Sequence(options)  # sequence for description

        line = '>'

        while line:
            line = file_in.readline()

            if (line[0] == "+"):
                parse_quality_score(seq_one, line, file_in)
            elif (line[0] == '>' or line[0] == '@' or (line == None and seq_one.size)):
                parse_sequence_description(
                    self, path, line, file_in.tell(), seq_one, seq_des, options.opt)
            else:
                seq_one.tot_length += len(line)
                seq_one += line

        seq_one.identifier = ""
        del line
        file_in.close()

    def read_seqs(self, paths: list, options: Options):
        pass

    def write_clusters(self, db_path, new_db_path, options: Options):
        pass

    def write_clusters_pe(self, db_path, db_pe_path, new_db_path, new_db_path_pe, options: Options):
        pass

    def write_extra_1d(self, options: Options):
        pass

    def write_extra_2d(self, other_seq, options: Options):
        pass

    def divide_save(self, db_path: str, new_db_path: str, n: int, options: Options):
        pass

    def swap_in(self, seg: int, reponly: bool = False):
        pass

    def swap_out(self, seg: int):
        pass

    def sort_divide(self, options: Options, sort: bool = True):
        pass

    def compute_minimal_memory(self, frag_no: int, bsize: int, threads_num: int, options: Options, extra: int = 0):
        pass

    # missing methods:
    """
        void ClusterOne( Sequence *seq, int id, WordTable & table, WorkingParam & param, WorkingBuffer & buf, const Options & options );
        void ComputeDistance( const Options & options );
		void DoClustering( const Options & options );
		void DoClustering( int T, const Options & options );
		void ClusterTo( SequenceDB & other, const Options & optioins );
		int  CheckOne( Sequence *seq, WordTable & tab, WorkingParam & par, WorkingBuffer & buf, const Options & opt );
		int  CheckOneEST( Sequence *seq, WordTable & tab, WorkingParam & par, WorkingBuffer & buf, const Options & opt );
		int  CheckOneAA( Sequence *seq, WordTable & tab, WorkingParam & par, WorkingBuffer & buf, const Options & opt );
    """


def parse_sequence_description(seq_db: SequenceDB, path: str, line: str, curr_file_offset: int, seq_one: Sequence, seq_des: Sequence, opt: dict):
    if (seq_one.size):
        # previous record was written
        if (seq_one.identifier == "" or seq_one.format()):
            print(f"WARNING: From File '{path}':\n")
            print(
                f"Discarding invalid sequence or sequence without identifier and description!\n")
            if (seq_one.identifier):
                print(seq_one.identifier)
            print(seq_one.data)
            seq_one.size = 0

        seq_one.index = len(seq_db.sequences)

        if (seq_one.size > opt["min_length"]):
            if (opt["trim_len"] > 0):
                seq_one.trim(opt["trim_len"])
            seq_db.sequences += Sequence(seq_one)

    seq_one.size = 0
    seq_one.tot_length = 0

    seq_des.size = 0
    seq_des += line

    line_len = len(line)
    seq_one.des_begin = curr_file_offset - line_len
    seq_one.tot_length += line_len

    # count first line
    i = 0
    if (seq_des.data[i] in ('>', '@', '+')):
        i += 1

    if(seq_des.data[i] in (' ', '\t')):
        i += 1

    if (opt["des_len"] and opt["des_len"] < seq_des.size):
        seq_des.size = opt["des_len"]

    while(i < seq_des.size and not seq_des.data[i].isspace()):
        i += 1

    seq_des.data = seq_des.data[:i] + '\0' + seq_des.data[i + 1:]
    seq_one.identifier = seq_des.data


def parse_quality_score(seq_one: Sequence, line: str, file):
    seq_one.tot_length += len(line)

    # read next line quality score
    line = file.readline()
    seq_one.tot_length += len(line)
