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

table_3 = open(r"F:\博士\深海鱼适应性进化\候选基因\三刺鱼\Gasterosteus_aculeatus.longest.cds.txt","r")
table_2 = open(r"/home/clad/clad/wubaosheng/genome/Stickleback/essemble_download/Gasterosteus_aculeatus_2.cds","w")
table_new = table_3.readlines()
for i in table_new:
    if i.startswith(">"):
        table_2.writelines("\n" + str(i.strip()[0:21]) + "\n")
    else:
        table_2.writelines(i.strip())

table = open(r"/home/clad/clad/wubaosheng/genome/Stickleback/essemble_download/Gasterosteus_aculeatus_2.cds","r")
table2 = open(r"/home/clad/clad/wubaosheng/genome/Stickleback/essemble_download/Gasterosteus_aculeatus.hapoxia_result.txt","w")
table_new = table.readlines()
sequence = {}
ac = ""
seq = ""
for i in table_new:
    if i.startswith(">") and seq != "":
        sequence[ac] = seq
        seq = ""
    if i.startswith(">"):
        ac = i.strip()[1:21]
    else:
        seq = i.strip()
sequence[ac] = seq
for i in sequence:
    print()
target_list = get_essemble_index(r"/home/clad/clad/wubaosheng/genome/Stickleback/essemble_download/Gasterosteus_aculeatus.id.txt")
for m in target_list:
    print(m)
    finder = sequence[m]
    table2.writelines(">" + str(m) + "\n")
    table2.writelines(str(finder) + "\n")
table.close()
table2.close()