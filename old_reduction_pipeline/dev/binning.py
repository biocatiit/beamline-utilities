from scipy import *
from numpy import *

def get_bin_mean(a, b_start, b_end):
    ind_upper = nonzero(a >= b_start)[0]
    a_upper = a[ind_upper]
    a_range = a_upper[nonzero(a_upper < b_end)[0]]
    mean_val = mean(a_range)
    return mean_val


q, I, error = genfromtxt('AgB_0002.dat', skip_header=3, skip_footer=4, unpack=True)
#data = rand(100)
#bins = linspace(0, 1, 10)
bins = range(0, q.size, 4)
binned_data = []

n = 0
for n in range(0, len(bins)-1):
    q_start = bins[n]
    q_end = bins[n+1]
    binned_data.append(get_bin_mean(q, q_start, q_end))

print binned_data