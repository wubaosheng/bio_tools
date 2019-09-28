#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_essemble_index(input_filename):
    """
    from the input_file get the essemble number and make them be a list
    :param input_filename: 
    :return: 
    """
    data_0 = open(input_filename,"r")
    list_0 = []
    for i in data_0:
        list_0.append(i.strip())
    return list_0

table = open(r"/home/clad/clad/wubaosheng/genome/Stickleback/essemble_download/hypoxia.txt","r")
table2 = open(r"/home/clad/clad/wubaosheng/genome/hadalsnail/transcriptome_hadal/hypoxia.txt.txt","w")
table_new = table.readlines()
sequence = {}
ac = ""
seq = ""
for i in table_new:
    if i.startswith(">") and seq != "":
        sequence[ac] = seq
        seq = ""
    if i.startswith(">"):
        ac = i.strip()
    else:
        seq =  i.strip()
sequence[ac] = seq
target_list = get_essemble_index()
for m in target_list:
    finder = sequence[m]
    table2.writelines(str(m) + "\n")
    table2.writelines(str(finder) + "\n")
table.close()
table2.close()




