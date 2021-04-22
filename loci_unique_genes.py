#!/usr/bin/python
#Identifies all loci which transcribe only one gene and the type of gene it is  
#filename should correspond to the sorted tmap file from the sort script
#filename1 should correspond to the gff reference genome file

import re
import json
import timeit
from datetime import datetime

startTime = datetime.now()
filename = 'f300k_sorted_filtered.tmap'
filename1 = 'gencode33.gff3'

def unique(list1):
    list_set = set(list1)
    unique_list = (list(list_set))
    return unique_list
count = 0
gene_id = []
locus = []
bad_loci = set()#bad loci are loci whose transcripts code for more than one gene
line1=[]
prev_line=''
fh = open(filename, 'r')

for line in fh:#first read to get bad loci
    line1 = str(line).split()
    if count > 0:
        prev_locus = (str(prev_line).split()[2])
        prev_gene_id = (str(prev_line).split()[0])
        if line1[0] != prev_gene_id and line1[2] == prev_locus and gene_id != "-":
            bad_loci.add(line1[2])
    prev_line=line
    count+=1

fh1 = open(filename, 'r')
count1 =0
dict={}
prev_line=''
good_genes=[]
bad_loci=unique(bad_loci)
bad_loci.sort()
inside_count=0

for line in fh1:#second read which takes the main bulk of the time
    line1 = str(line).split()
    if count1 > 0:
        prev_locus = (str(prev_line).split()[2])
        prev_gene_id = (str(prev_line).split()[0])
        if not any(bad_word in line for bad_word in bad_loci):
            good_genes.append(line1[0])
            dict[line1[0]] = [line1[2]]#dictionary with gene id as key and locus as value 
    prev_line=line
    count1+=1

good_genes = filter (lambda good: len (good) > 2, good_genes)#to filter out the single character genes (which are -'s)
count=0
good_genes=unique(good_genes)
fh2 = open(filename1, 'r')

for line in fh2:#third read to extract gene name and type
    if any(gene in line for gene in good_genes):
        inside = 0
        m = re.search("gene_name\=((.*?))\;", line)
        if m:
            if m.group(1) in good_genes:
                gene1 = m.group(1)
                inside = 1
        m1 = re.search("gene_type\=((\w+))", line)
        if m1 and inside == 1:
            if len(dict[gene1]) <= 1:
                dict[gene1].append(m1.group(1))
    count+=1

count_list=list(dict.values())
count3 = 0
type_count=[]

for item in sorted(count_list):#
    if len(count_list[count3]) == 2:#so as to not include ones with no gene_type
        type_count.append(count_list[count3][1])
    count3+=1
count_dict={}
unique_type_list = unique(type_count)

for type in unique_type_list:
    count_dict[type] = 0
for item in type_count:
    count_dict[item] = count_dict[item] + 1
for gene_type in count_dict:
    print (gene_type +": "+ str(count_dict[gene_type]))
print("")
print("Runtime: " +  str(datetime.now() - startTime))
for key,value in sorted(dict.items()):
    if len(dict[key]) == 2:#only printing those whose genes are found in the gencode file  
        print("{}: {}".format(key, dict[key]))
