#!/usr/bin/env python

import sys

def makeLdVcf(pruneIN, orgVCF, prefix):
    d={}
    L=[]
    with open('%s.vcf' % sys.argv[3], 'w') as fh:
        with open (orgVCF, 'r') as LL:
            for i in LL:
                i = i.strip()
                if i[0] == "#":
                    fh.write("%s\n" % i)
                else:
                    items = i.split('\t')
                    d[items[2]] = i
    with open (pruneIN, 'r') as fd:
        for line in fd:
            line=line.strip()
            L.append(line)
    with open('%s.vcf' % sys.argv[3], 'a') as fh:
        with open (pruneIN, 'r') as fd:
            for line in fd:
                line=line.strip()
                fh.write('%s\n' % d[line])
makeLdVcf(sys.argv[1], sys.argv[2], sys.argv[3])
