import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

scores = []
scores_total = {}

file = open("mega-hand-scores-temp.txt", 'r')
for line in file:
    scores.append(int(line[:2]))
file.close()

for score in scores:
    if score in scores_total:
        scores_total[score] += 1
    else:
        scores_total[score] = 1

print("Max:" + str(max(scores)))
sorted_dict = dict(sorted(scores_total.items()))
for i in sorted_dict:
    print(i, sorted_dict[i])

n_bins = max(scores)
fig, axs = plt.subplots(1, sharey=True, tight_layout=True)
N, bins, patches = axs.hist(scores, bins=n_bins, density=True)
fracs = N / N.max()
norm = colors.Normalize(fracs.min(), fracs.max())
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)
axs.yaxis.set_major_formatter(PercentFormatter(xmax=1))
plt.show(block=True)
