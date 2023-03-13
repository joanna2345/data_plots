#Wykresy rozrzutu na podstawie danych ics uci datasets

import pandas as pd
import matplotlib.pyplot as plt

#Wczytuję dane z pliku IRIS
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",
                 names = ["Długość kielicha", "Szerokość kielicha", "Długość płatka", "Szerokość płatka", "Klasa"])
# df.head()
# print(df)

#Stworzenie list na podstawie danych z pliku IRIS
df_dl_kielicha = df['Długość kielicha']
dl_kielicha_lista = df_dl_kielicha.tolist()

df_szer_kielicha = df['Szerokość kielicha']
szer_kielicha_lista = df_szer_kielicha.tolist()

df_dl_platka = df['Długość płatka']
dl_platka_lista = df_dl_platka.tolist()

df_szer_platka = df['Szerokość płatka']
szer_platka_lista = df_szer_platka.tolist()

#Stworzenie 4wykresów na rysunku i nadanie kolorów każdemu
figure, ((axes1, axes2), (axes3, axes4)) = plt.subplots(2,2)
figure.suptitle('Wykresy rozrzutu IRIS')
axes1.scatter(dl_kielicha_lista,szer_kielicha_lista, color='blue')
axes2.scatter(dl_platka_lista,szer_platka_lista, color='orange')
axes3.scatter(dl_kielicha_lista,szer_platka_lista, color='red')
axes4.scatter(dl_platka_lista,szer_kielicha_lista, color='green')
plt.savefig('Rysunek_wykres_rozrzutu.png', dpi=(200))
plt.show()