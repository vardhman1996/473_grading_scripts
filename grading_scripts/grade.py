# grade student submissions for cse 473
# author: nicholas ruhland
# note: starter code is copied into student directories
#       to prevent caching giving incorrect results
import os
import sys
import subprocess
import stat
from distutils.dir_util import copy_tree

if len(sys.argv) != 3:
    print 'Usage: python grade.py <source dir> <student code dir>'
    exit()

source_dir = sys.argv[1]
student_code_dir = sys.argv[2]
if source_dir[-1] != '/':
    source_dir += '/'
if student_code_dir[-1] != '/':
    student_code_dir += '/'

original_directory = os.getcwd()

all_source = sorted(os.listdir(source_dir))

files_to_delete = [
    'addition.py', 'buyLotsOfFruit.py', 'shopSmart.py',             # p0
    'search.py', 'searchAgents.py',                                 # p1
    'multiAgents.py',                                               # p2
    'valueIterationAgents.py', 'qlearningAgents.py', 'analysis.py', # p3
    'bustersAgents.py', 'inference.py',                             # p4
    'answers.py','dataClassifier.py','perceptron.py'                # p5
    ]

# Delete files from source that students will write
for file in all_source:
    if file.endswith('.pyc') or file in files_to_delete:
        os.remove(source_dir+file)

all_students = sorted(os.listdir(student_code_dir))
for item in all_students:
    os.chdir(original_directory)
    if not os.path.isdir(student_code_dir+item):
        continue
    student_name = item
    student_dir = student_code_dir+student_name

    # Copy source files into student directory
    copy_tree(source_dir, student_dir)

    # Run the autograder
    print 'Running {}...'.format(student_name)
    os.chdir(student_dir)
    os.system('python autograder.py > ../{}.txt'.format(student_name))
    os.chdir(original_directory)

print 'Done.'
