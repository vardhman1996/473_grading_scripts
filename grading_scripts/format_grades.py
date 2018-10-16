# grade formatting for cse 473
# author: nicholas ruhland
import os
import sys
import zipfile

if len(sys.argv) != 3:
    print 'Usage: python format_grades.py <project number> <output directory>'
    exit()

_, project_num, d = sys.argv
if project_num not in ['0','1','2','3','4','5']:
    print 'Invalid project number. Must be one of [0,1,2,3,4,5].'
    exit()

if d[-1] != '/':
    d += '/'

all_txt = sorted(i for i in os.listdir(d) if i.endswith('.txt'))
len_longest = len(max(all_txt, key=len))

for cur_file in all_txt:
    name = cur_file[:-4]
    with open(d+cur_file, 'r') as f:
        txt = f.read()

    output_val='?'
    if len(txt.split('\n')) > 10:
        if project_num == '0':
            # Project 0 output
            print name.ljust(len_longest) + '- ' + txt.split('\n')[-6] + ' (' + str(output_val) + ' nodes)'

        if project_num == '1':
            # Project 1 output
            if 'expanded nodes:' in txt:
                remainder=txt[txt.index('expanded nodes:')+len('expanded nodes:'):]
                output_val = remainder.split()[0]
            print name.ljust(len_longest) + '- ' + txt.split('\n')[-6]

        elif project_num == '2':
            # Project 2 output
            if 'Question q5\n===========' in txt:
                remainder=txt[txt.rfind('Average Score: ')+len('Average Score: '):]
                output_val = remainder.split()[0]
            print name.ljust(len_longest) + '- ' + txt.split('\n')[-6] + ' (' + str(output_val) + ' average)'

        elif project_num == '3':
            # Project 3 output
            if 'Question q7\n===========' in txt:
                remainder=txt[txt.rfind('Average Score: ')+len('Average Score: '):]
                output_val = remainder.split()[0]
            print name.ljust(len_longest) + '- ' + txt.split('\n')[-6] + ' (' + str(output_val) + ' points)'

        elif project_num == '4':
            # Project 4 output
            if 'Question q7\n===========' in txt:
                remainder=txt[txt.rfind('Average Score: ')+len('Average Score: '):]
                output_val = remainder.split()[0]
            total=txt[txt.rfind('Total: '):].split('\n')[0]
            print name.ljust(len_longest) + '- ' + total + ' (' + str(output_val) + ' points)'

        elif project_num == '5':
            # Project 5 output
            if 'Question q4\n===========' in txt:
                remainder=txt[txt.rfind('correct out of 100 (')+len('correct out of 100 ('):]
                output_val = remainder.split()[0][:-2]
            total=txt[txt.rfind('Total: '):].split('\n')[0]
            print name.ljust(len_longest) + '- ' + total + ' (' + str(output_val) + ' points)'

    else:
        print name.ljust(len_longest) + '- ' + 'error'
