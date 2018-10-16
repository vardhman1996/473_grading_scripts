# plot a histogram of scores for cse 473 project 1
# author: nicholas ruhland
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
import sys
import os
import seaborn as sns
sns.set()

if len(sys.argv) != 2:
    print 'Usage: python plot_scores.py <student code output directory>'
    exit()

_, d = sys.argv
if d[-1] != '/':
    d += '/'

# Read in scores from student output files
all_txt = sorted(i for i in os.listdir(d) if i.endswith('.txt'))
scores = {}
for txt in all_txt:
    with open(d + txt, 'r') as f:
        data = f.read()

	if 'expanded nodes:' in data:
	    remainder=data[data.index('expanded nodes:')+len('expanded nodes:'):]
	    output_val = remainder.split()[0]
	    if output_val.isdigit():
		    scores[txt[:-4]] = int(output_val)

best_score = min(scores.values())
best_names = [i for i in scores.iteritems() if i[1] == best_score]
print 'Best score students:', best_names

# Create histogram plot of scores
x = scores.values()
n_bins=20
N, bins, patches = plt.hist(x, bins=n_bins)
fracs = N.astype(float) / N.max()
norm = colors.Normalize(fracs.min(), fracs.max())
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.Reds(norm(thisfrac))
    thispatch.set_facecolor(color)
plt.title('Project 1 - Question 7 expanded nodes')
plt.show()
