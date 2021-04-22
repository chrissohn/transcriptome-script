# transcriptome-scripts
Obtain unique genes from gene transcripts 

Information regarding each script is commented at the top of their respective files
Pipeline using all the scripts in this repo: 

python minus_xs.py #gives you filename_minus_xs.tmap 

python sort.py > sort_filename_minus_xs.tmap

python loci_unique_genes.py > sorted_genes.out

sorted_genes.out will contain the total number of types of genes found and underneath that will be the unique genes and their associated loci.
