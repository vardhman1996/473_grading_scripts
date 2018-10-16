# uncanvas student submissions for cse 473
# author: nicholas ruhland
import os
import sys
import zipfile

if len(sys.argv) != 2:
    print 'Usage: python uncanvas.py <submissions path>'
    exit()

d = sys.argv[1]
if d[-4:] == '.zip':
    output_dir = d[:-4]
    print 'Unzipping files to {}...'.format(output_dir)
    with zipfile.ZipFile(d,'r') as z:
        z.extractall(output_dir)
    d = output_dir

if d[-1] != '/':
    d += '/'

print 'Moving student files into directories...'
all_txt = sorted(os.listdir(d))

for txt in all_txt:
    splits = txt.split('_')
    if len(splits) < 4:
        print 'Filename not understood, not touching file: ' + txt
        continue
    if splits[1] == 'late':
        # example: studentname_late_3434243_12343423_file_name_here-1.py
        user     = splits[0]
        filename = '_'.join(splits[4:])
    else:
        # example: studentname_3434243_12343423_file_name_here-1.py
        user     = splits[0]
        filename = '_'.join(splits[3:])

    # Canvas adds '-1' to the end of some filenames
    split_filename = filename.split('-')
    number_and_extension = split_filename[-1].split('.')
    if len(number_and_extension) == 2:
        number, ext = number_and_extension
        if number.isdigit():
            filename = '-'.join(split_filename[:-1]) + '.' + ext

    result_directory = d + user + '/'
    if not os.path.exists(result_directory):
        os.mkdir(result_directory)
    if os.path.exists(result_directory + filename):
        print 'Err - path already exists:' + result_directory + filename
    os.rename(d + txt, result_directory + filename)

print 'Done.'
