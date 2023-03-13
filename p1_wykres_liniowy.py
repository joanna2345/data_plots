#Wykres liniowy prezentujący miesięczne temperatury w Warszawie i Miami

import matplotlib.pyplot as plt
from matplotlib import axes
from matplotlib import figure
from matplotlib.pyplot import legend
import pandas as pd

#Wczytanie pliku csv oraz stworzenie list na podstawie temperatur z pliku
temperatury_dt = pd.DataFrame((pd.read_csv('C:\\Users\\joann\\Downloads\\data_plots_file\\temp.csv')))
# print(temperatury_dt)
miami_dt = temperatury_dt['Miami']
miami_lista = miami_dt.tolist()
print(miami_lista)

warszawa_dt = temperatury_dt['Warszawa']
warszawa_lista = warszawa_dt.tolist()
print(warszawa_lista)

#Stworzenie obu wykresów i ustawienie podstawowych wartości na osiach
figure, axes = plt.subplots(1,2)
miesiace = [1,2,3,4,5,6,7,8,9,10,11,12]
axes[0].plot(miesiace, miami_lista, color='darkblue', linewidth=2.0)
axes[0].set(xlim=(1, 12), xticks=(1,2,3,4,5,6,7,8,9,10,11,12), ylim=(-5,35), yticks=(-5, 0, 5, 10, 15, 20, 25, 30, 35))
axes[0].set_title('Temperatury w Miami')
axes[0].set_xlabel('Miesiące')
axes[0].set_ylabel('Średnie temperatury')

#Odstęp między wykresami
figure.tight_layout()

axes[1].plot(miesiace, warszawa_lista,color='green', linewidth=2.0)
axes[1].set(xlim=(1, 12), xticks=(1,2,3,4,5,6,7,8,9,10,11,12), ylim=(-5,35), yticks=(-5, 0, 5, 10, 15, 20, 25, 30, 35))
axes[1].set_title('Temperatury w Warszawie')
axes[1].set_xlabel('''Miesiące
                   
                   
                   
                   ''')
axes[1].set_ylabel('Średnie temperatury')

#Stworzenie tytułu rysunku
plt.suptitle('Średnie temperatury w Miami i Warszawie')
#Odstęp po tytule
figure.tight_layout()

#Stworzenie legendy
figure.legend(['Miami', 'Warszawa'], loc='lower center', shadow=True, fontsize='small', title='Legenda')

#Zapis rysunku wykresów
plt.savefig('Rysunek_wykres_liniowy.png', dpi=(200))
plt.show()
print('Done')