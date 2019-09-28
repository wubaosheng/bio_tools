#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" from the CDS.file get the longest sequence as the gen_coding sequence"""
import math,re
def clearBlankLine(inputfile,outputfile):
    file1 = open(inputfile, 'r') 
    file2 = open(outputfile, 'w') 
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            file2.write(line)
    finally:
        file1.close()
        file2.close()
    return outputfile


"""获取只有基因号和序列的文件，并将序列文件中的多行合并成一行"""
table_3 = open(r"/home/clad/clad/wubaosheng/genome/lates_calcarifer/essemble_downloading/Lates_calcarifer.cds","r")
table_2 = open(r"/home/clad/clad/wubaosheng/genome/lates_calcarifer/essemble_downloading/Lates_calcarifer.cds2","w")
table_new = table_3.readlines()
list_key = []
for i in table_new:
    if i.startswith(">"):
        m = i.strip().split()
        m2 = m[3][5: ]
        table_2.writelines("\n" + ">" + str(m2) + "\n")
        list_key.append(m2)
    else:

        table_2.writelines(i.strip())
table_2.close()

"""给每条序列加上长度标签，这样我们就可以根据标签把序列和序列号一一对应起来，并且根据已有的标签筛选出最长的转录本"""
clearBlankLine_line = clearBlankLine(r"/home/clad/clad/wubaosheng/genome/lates_calcarifer/essemble_downloading/Lates_calcarifer.cds2",r"/home/clad/clad/wubaosheng/genome/lates_calcarifer/essemble_downloading/Lates_calcarifer.cds3")
table4 = open(clearBlankLine_line,"r")
table5 = open(r"/home/clad/clad/wubaosheng/genome/lates_calcarifer/essemble_downloading/Lates_calcarifer.cds.marker","w")
marker1 = ""
marker2 = ""
marker3 = ""
table4_new = table4.readlines()
for j in table4_new:
    if j.startswith(">") and marker1 !="":
        n = marker2 + "\t" + marker1
        table5.writelines("\n" + str(n) + "\n")
        table5.writelines(str(marker3))
        marker1 = ""
    if j.startswith(">"):
        marker2 = j.strip()
    else:
        marker1 = str(len(j.strip()))
        marker3 = j.strip()
table5.writelines(str(marker2))
table5.writelines("\n" + str(marker3) + "\n")
table4.close()
table5.close()
"""提取具有重复序列的序列号,将具有不同转录本和唯一转录本的序列分开"""
table6 = open(r"/home/clad/clad/wubaosheng/genome/lates_calcarifer/essemble_downloading/Lates_calcarifer.cds.marker","r")
length_list1 = []
length_list2 = []
list_key2 = []
list_key3 = []
table6_new = table6.readlines()
for h in table6_new:
    if h.startswith(">"):
        h1 = h.strip().split("\t")[0]
        number = list_key.count(h1[1: ])
        if number >= 2:
            list_key2.append(h)
        else:
            list_key3.append(h)

list_longest = []
for g in list_key2:
    h2 = g.strip().split("\t")[0]
    list_key4 = [x for x in list_key2 if x[1:21] == h2[1:]]
    list_key5 = sorted(list_key4, reverse=True)[0]
    list_longest.append(list_key5)
list_longest2 = list(set(list_longest))
"""获得具有不同转录本的最长序列"""
print(len(list_longest))
print(len(list_longest2))

data = list_longest2 + list_key3
print(len(data))

"""构建序列与序列号的一一对应关系"""
table6 = open(r"/home/clad/clad/wubaosheng/genome/lates_calcarifer/essemble_downloading/Lates_calcarifer.cds.marker","r")
table7 = open(r"/home/clad/clad/wubaosheng/genome/lates_calcarifer/essemble_downloading/Lates_calcarifer.cds.marker.longest.txt","w")
table_new = table6.readlines()
sequence = {}
ac = ""
seq = ""
for i in table_new:
    if i.startswith(">") and seq != "":
        sequence[ac] = seq
        seq = ""
    if i.startswith(">"):
        ac = i.strip().split()[0]
    else:
        seq = i.strip()
sequence[ac] = seq
print(len(sequence))

"""提取具有唯一转录本的基因编号和对应的序列"""
for r in data:
    r1 = r.strip().split()[0]
    table7.writelines("\n" + str(r1) + "\n")
    r2 = sequence[r1]
    table7.writelines(str(r2))
table6.close()
table7.close()