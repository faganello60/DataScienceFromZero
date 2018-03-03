# -*- coding: utf-8 -*-
from matplotlib import  pyplot as plt

years = [1950,1960,1970,1980,1990,2000,2010]
amount = [300.2, 600.3, 450.5,900.0,600.0,100.0,200.0]

#Create a line Chart, years in X and amount in Y
# plt.plot(years,amount,color='green', linestyle='solid', marker='H',
#      markerfacecolor='blue', markersize=12)
# plt.title('Tax')
# plt.ylabel('R$ Bilhao')
# plt.xlabel('Anos')
# plt.show()
#Documentation about Plot -> https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html


#Create Bar Chart
# movie   = ['Frozen', 'Moana', 'Bela e a Fera']
# oscars  = [10, 5, 15]
# xs = [i + 0.1 for i, _  in enumerate(movie)]
# plt.bar(xs, oscars)
# plt.ylabel("# de Premiacao")
# plt.title("Filmes")
# plt.xticks([i + 0.5 for i, _ in enumerate(movie)],movie)
# plt.show()


# Create Line Chart
variance = [1,2,4,8,16,32,64,128,256]
bias_squared = [256,128,64,32,16,8,4,2,1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

plt.plot(xs,variance, 'g-', label='variance') # Linha verde solida
plt.plot(xs, bias_squared, 'r-.',label='bias') #Linha com linhas de pontos tracejadas vermelho
plt.plot(xs,total_error, 'b:',label='Error') # Linha com pontilhado azul

plt.legend(loc=9)
plt.xlabel('Complexidade do Modelo')
plt.title('Compromisso')
plt.show()