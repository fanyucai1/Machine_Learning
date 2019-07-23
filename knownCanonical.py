import requests
from bs4 import BeautifulSoup
import os
import re
from multiprocessing import Pool
clinvar="/data/Database/clinvar/clinvar.vcf"
genelist="/data/Panel275/gene_list/gene_275.list"
gene={}
dict={}
if os.path.exists("knownCanonical.tsv"):
    file=open("knownCanonical.tsv","r")
    for line in file:
        line =line.strip()
        array=line.split("\t")
        dict[array[0]]=1
    file.close()
infile=open(genelist,"r")
for line in infile:
    line=line.strip()
    gene[line]=1
infile.close()
###########################################
infile=open(clinvar,"r")
id=[]
for line in infile:
    line = line.strip()
    if not line.startswith("#"):
        array = line.split("\t")
        p=re.compile(r'GENEINFO=(\S+)')
        geneinfo=p.findall(line)
        if geneinfo !=[]:
            if geneinfo[0].split(":")[0] in gene and array[2] not in dict:
                id.append(array[2])
infile.close()

def run(ID):
    html="https://www.ncbi.nlm.nih.gov/clinvar/variation/%s"%(ID)
    try:
        res = requests.get(html)
        ret = res.text
        soup = BeautifulSoup(ret, 'html.parser')
        result=soup.find('h2',class_='usa-color-text usa-color-text-white blue-box').text.strip()
        outfile=open("knownCanonical.tsv",'a+')
        outfile.write("%s\t%s\n"%(ID,result))
        outfile.close()
    except:
        pass
if __name__=="__main__":
    pool = Pool(processes=200)
    pool.map(run, id)
    print("done")