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

mean(num_friends) # 53.2352941176

