"""
Napisać skrypt, który na stronie http://seleniumdemo.com/?page_id=7 uworzy wiele kont na raz
odczytujac dane z pliku dane.csv

wykorzystaj selenium, pandas, odczytywanie z pliku
"""

import pandas as pd

df = pd.read_csv("dane.csv")

# print(df.head())
# print(df.info())

# dobranie się do elementów pierwszego wiersza
print(df.iloc[0, 0])  # >> e-mail
print(df.iloc[0, 1])  # >> haslo