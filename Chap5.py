# -*- coding: utf-8 -*-
from __future__ import division
from collections import Counter
from matplotlib import  pyplot as plt

#Estatística
# Gereador de Array: https://www.random.org/integer-sets/


num_friends = [9, 23, 25, 28, 31, 37, 38, 39, 40,
               42, 49, 55, 57, 60, 65, 77, 79, 88, 90, 93,
               9, 23, 25, 28, 31, 37, 38, 39, 40,
               60, 65, 77, 79, 88,88, 90, 93,55, 57, 60, 65, 77, 79, 88, 90, 93,
               9, 23, 25, 28, 31]

# Histograma
friend_counts = Counter(num_friends)
xs = range(max(num_friends))
ys = [friend_counts[x] for x in xs]
plt.bar(xs,ys)
plt.axis([0,102,0,25])
plt.title('Contagem de Amigos')
plt.xlabel('# de amigos')
plt.ylabel('# de pessoas')
# plt.show()


num_points = len(num_friends)
largest_value = max(num_friends)
smallest_value = min(num_friends)

print("""=======================
O tamanho do array é de {}
O maior valor é de {}
O menor valor é de {}
=======================""".format(num_points,largest_value,smallest_value))

def mean(x):
    return  sum(x) / len(x)

def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    if n % 2 == 1:
        return  sorted_v[midpoint]
    else:
        lo = midpoint -1
        hi = midpoint
        return  (sorted_v[lo] + sorted_v[hi]) / 2



print(mean(num_friends)) # 53.2352941176
print(median(num_friends)) # 55

def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]

print(quantile(num_friends,0.9))


def data_range(x):
    return  max(x) - min(x)

print(data_range(num_friends))