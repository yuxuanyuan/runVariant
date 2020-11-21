#!/usr/bin/env python

# Written by: Yuxuan (Andy) Yuan
# Email: yuxuan.yuan@outlook.com

import pandas as pd
import sys

#Two cols in the list file seprated by tab.
#The first col is the sample name
#The second col is the generated sorted bam file

myfile=pd.read_csv(sys.argv[1], sep=" ", names=['sample', 'bam'])
runGATK_path=sys.argv[2]
outDir=sys.argv[3]

B=''

for i in myfile['sample'].unique():
    sub=myfile[myfile['sample']==i].reset_index(drop=True)
    if len (sub) == 1:
        name = sub['sample'][0].rsplit('.', 1)[0]
        cmd = 'cd %s && java -jar %s/../tools/picard.jar MarkDuplicates I=%s O=%s.dedup.bam M=%s.dedup.txt && samtools index %s.dedup.bam' % (outDir, runGATK_path, sub['bam'][0], name, name, name)
        print (cmd)
    else:
        for j in range(len(sub)):
            B+='%s '%(sub['bam'][j])
        name = sub['sample'][j]
        B=B.rsplit(' ',1)[0]
        cmd = 'cd %s && samtools merge %s.merged.bam %s && samtools index %s.merged.bam && java -jar %s/../tools/picard.jar MarkDuplicates I=%s.merged.bam O=%s.dedup.bam M=%s.dedup.txt && samtools index %s.dedup.bam' % (outDir, name, B, name, runGATK_path, name, name, name, name)
        print (cmd)
        B=''
