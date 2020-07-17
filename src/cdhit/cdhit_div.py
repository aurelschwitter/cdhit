#!/usr/bin/env python3

"""
=============================================================================
// CD-HIT
// http://cd-hit.org/
// http://bioinformatics.burnham-inst.org/cd-hi
//
// program written by
//                                      Weizhong Li
//                                      UCSD, San Diego Supercomputer Center
//                                      La Jolla, CA, 92093
//                                      Email liwz@sdsc.edu
//                 at
//                                      Adam Godzik's lab
//                                      The Burnham Institute
//                                      La Jolla, CA, 92037
//                                      Email adam@burnham-inst.org
//
// Modified by:
//                                      Limin Fu
//                                      Center for Research in Biological Systems (CRBS), UCSD
//                                      La Jolla, CA, 92093
//                                      Email: l2fu@ucsd.edu, fu@daovm.net
//
// =============================================================================
"""

from options import Options
from sequenceDb import SequenceDB
from sequence import Sequence
import argparse
import os
import sys
import datetime as dt


def main():
    parser = parse_args()

    start_time = dt.datetime.now()

    opt = Options()
    opt.store_disk = 1
    seqDb = SequenceDB()

    seqDb.read(parser.db_in, opt)
    print(f"total seq: {len(seqDb.sequences)}\n")

    for s in seqDb.sequences:
        print(f"identifier: {s.identifier}\t tot_len={s.tot_length}\n")

    return

    seqDb.sort_divide(opt)

    print("Writing new databases\n")

    seqDb.divide_save(parser.db_in, parser.db_out, parser.div, opt)

    end_time = dt.datetime.now()

    seconds_elapsed = (end_time - start_time).total_seconds()
    print(f"Total CPU Time {seconds_elapsed:.4}\n")
    print("Program completed!\n")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', dest='db_in',
                        type=str, help="input db-path", required=True)
    parser.add_argument('-o', '--output', dest='db_out',
                        type=str, help="output db-path", required=True)
    parser.add_argument('-d', '--div', dest='div', type=int,
                        help="number of divides", required=True)
    args = parser.parse_args()

    if (args.div <= 1):
        raise UserWarning(
            "nr of divides must be greater than 1! No database is written, exiting")

    return args


if __name__ == "__main__":
    main()
