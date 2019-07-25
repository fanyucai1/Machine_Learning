import requests
from bs4 import BeautifulSoup
import os
from multiprocessing import Pool
import re
clinvar="/data/Database/clinvar/2019.7.20/clinvar.vcf"
gene={}
dict={}
if os.path.exists("knownCanonical.tsv"):
    file=open("knownCanonical.tsv","r")
    for line in file:
        line =line.strip()
        array=line.split("\t")
        dict[array[0]]=1
    file.close()
###########################################
infile=open(clinvar,"r")
id=[]
for line in infile:
    line = line.strip()
    if not line.startswith("#"):
        array = line.split("\t")
        if array[2] not in dict:
            id.append(array[2])
infile.close()


def dict2d(dict, key_a, key_b, val):
    if key_a in dict:
        dict[key_a].update({key_b: val})
    else:
        dict.update({key_a: {key_b: val}})
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
        print(ID)

if __name__=="__main__":
    pool = Pool(processes=50)
    pool.map(run, id)
    print("done")
    infile = open("knownCanonical.tsv", 'r')
    trans=[]
    dict={}
    gene=[]
    counts={}
    gene2trans={}
    for line in infile:
        if re.search(r'NM_',line):
            line=line.strip()
            array=line.split("\t")
            p=re.compile(r'[(](\S+)[)]')
            a=p.findall(array[1])
            if a==[]:
                continue
            if not a[0] in gene:
                gene.append(a[0])
            b=array[1].split(".")
            trans.append(b[0])
            if b[0] in counts:
                counts[b[0]]+=1
            else:
                counts[b[0]]=1
            if a[0] in gene2trans:
                if b[0] not in gene2trans[a[0]]:
                    gene2trans[a[0]].append(b[0])
            else:
                gene2trans[a[0]]=[]
                gene2trans[a[0]].append(b[0])
            dict2d(dict,a[0],b[0],counts[b[0]])
    infile.close()
    print("gene counts %s"%(len(gene)))
    outfile=open("knownCanonical.final.tsv", 'w')
    for a in gene:
        outfile.write("%s"%(a))
        tmp=[]
        for b in gene2trans[a]:
            tmp.append(dict[a]["%s"%(b)])
        set1=sorted(list(set(tmp)),reverse=True)#去重复并转化为list
        for key in set1:
            for b in gene2trans[a]:
                if dict[a][b]==key:
                    outfile.write("\t%s(%s)" % (b,dict[a][b]))
        outfile.write("\n")
    outfile.close()