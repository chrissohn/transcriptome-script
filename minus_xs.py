#!/usr/bin/python
#removes x and s class codes 
#filename should correspond to Gffcompare union file ending in .combined.gtf
import re

filename = 'gencode.gffcmp.combined.gtf'

x_s = ['x', 's']

with open(filename+'.tmap') as oldfile, open(filename+'_minus_xs.tmap', 'w') as newfile:
    header = next(oldfile)
    newfile.write(header)
    for line in oldfile:
        if not any(bad_word in line for bad_word in x_s):
            newfile.write(line)
