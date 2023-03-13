#Wykresy kolowe na podstawie danych ics uci datasets

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Wczytuję dane z pliku IRIS
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/zoo//zoo.data",
                 names = ["animal name", "hair", "feathers", "eggs", "milk", "airborne", "aquatic", "predator", "toothed", "backbone", "breathes", "venomous", "fins", "legs", "tail", "domestic", "catsize", "type"])
#df.head()
#Stworzenie list na podstawie danych z pliku zoo
#pióra
df_feathers = df['feathers']
feathers_lista = df_feathers.tolist()
#znosza jaja
df_eggs = df['eggs']
eggs_lista = df_eggs.tolist()
#latają
df_airborne = df['airborne']
airborne_lista = df_airborne.tolist()
#są drapieżnikami
df_predator = df['predator']
predator_lista = df_predator.tolist()
#są jadowite
df_venomous = df['venomous']
venomous_lista = df_venomous.tolist()
#mają ogon
df_tail = df['tail']
tail_lista = df_tail.tolist()

#Przygotowanie danych do wykresów kołowych
#pióra
ile_pior = feathers_lista.count(1) #ile jedynek w liście
ile_niepior = feathers_lista.count(0) #ile zer
#jaja
ile_jaj = eggs_lista.count(1)#ile jedynek w liście
ile_niejaj = eggs_lista.count(0) #ile zer
#lot
ile_lata = airborne_lista.count(1)#ile jedynek w liście
ile_nielata = airborne_lista.count(0) #ile zer
#drap
ile_drap = predator_lista.count(1)#ile jedynek w liście
ile_niedrap = predator_lista.count(0) #ile zer
#jad
ile_jad = venomous_lista.count(1)#ile jedynek w liście
ile_niejad = venomous_lista.count(0) #ile zer
#ogon
ile_ogon = tail_lista.count(1)#ile jedynek w liście
ile_nieogon = tail_lista.count(0) #ile zer

#Stworzenie wykresów i nadanie etykiet
figure, ((axes1, axes2), (axes3, axes4), (axes5, axes6)) = plt.subplots(3,2)
labels_a1 = ['z piórami', 'bez piór']
labels_a2 = ['znoszące jaja', 'nieznoszące jaj']
labels_a3 = ['latające', 'nielatające']
labels_a4 = ['są drapieżnikami', 'nie są drapieżnikami']
labels_a5 = ['są jadowite', 'nie są jadowite']
labels_a6 = ['mają ogony', 'nie mają ogonów']
figure.suptitle('Liczba zwierząt z poszczególnymi cechami')
sizes = [ile_pior,ile_niepior]
cuts=(0,0)
axes1.pie(sizes, explode=cuts, labels=labels_a1,
         autopct='%1.1f%%', textprops={'fontsize': 5})
axes2.pie(sizes, explode=cuts, labels=labels_a2,
         autopct='%1.1f%%', textprops={'fontsize': 5})
axes3.pie(sizes, explode=cuts, labels=labels_a3,
         autopct='%1.1f%%', textprops={'fontsize': 5})
axes4.pie(sizes, explode=cuts, labels=labels_a4,
         autopct='%1.1f%%', textprops={'fontsize': 5})
axes5.pie(sizes, explode=cuts, labels=labels_a5,
         autopct='%1.1f%%', textprops={'fontsize': 5})
axes6.pie(sizes, explode=cuts, labels=labels_a6,
         autopct='%1.1f%%', textprops={'fontsize': 5})

plt.savefig('Rysunek_wykres_kolowy.png', dpi=(200))
plt.show()