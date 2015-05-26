"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2


# use nsfg method to translate the raw data into pandas df
#fem_resp_df = nsfg.ReadFemPreg(dct_file='2002FemResp.dct',
#                                dat_file='2002FemResp.dat.gz')

# can almost use the existing ReadFemPreg() method, but the 
#   built-in CleanFemPreg() refers to columns that won't match.
#   ideally, we'd separate out these concerns. instead, we'll 
#   just replicate the code (and feel icky). 
def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz'):
    """Reads the NSFG pregnancy data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    return df


def main(script):
    """Exercise 1-2:
    Create a file named chap01ex.py and write code that reads the respondent file, 2002FemResp.dat.gz. You might want to start with a copy of nsfg.py and modify it.
    The variable pregnum is a recode that indicates how many times each respondent has been pregnant. Print the value counts for this variable and compare them to the published results in the NSFG codebook.
    script: string script name
    """
    #print('%s: All tests passed.' % script)
    # read the data file
    fp_df = ReadFemResp()
    # print the value counts
    print("'pregnum' value counts from data:")
    print(fp_df['pregnum'].value_counts().sort_index())

if __name__ == '__main__':
    main(*sys.argv)
