#!/usr/bin/env python3

debug = True

import sys
import os


sys.path.append(os.curdir + "/src/cdhit/")

from cdhit import cdhit_div

cdhit_div.main()
