#!/usr/bin/env python3

# Write a program that does the following
# 1. generates N random sequences
# 2. each sequence has GC composition S and length L
# 3. calculate GC in a sliding window of size W
# 4. calculate entropy in a sliding window of size W
#
# Parameters N, S, L, and W are command line parameters
# Hint: write functions

import math
import random
import sys




"""
python3 randomfun.py 1 0.5 15 7
AATTACAGATCGTGT
gc
0.1429
0.2857
0.2857
0.2857
0.4286
0.5714
0.4286
0.5714
0.4286
entropy
1.3788
1.8424
1.8424
1.8424
1.8424
1.9502
1.9502
1.8424
1.8424
"""
