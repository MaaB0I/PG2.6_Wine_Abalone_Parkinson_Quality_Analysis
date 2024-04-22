import pandas as pd
import matplotlib.pyplot as plt

# Daten laden
data = pd.read_csv('CSV/parkinsons+telemonitoring/parkinsons_updrs.data')

# Erkunden des DataFrames
print("Erste 5 Zeilen:")
print(data.head())
print("\nLetzte 5 Zeilen:")
print(data.tail())
print("\nDimensionen des DataFrames:")
print(f"Anzahl der Zeilen: {data.shape[0]}, Anzahl der Spalten: {data.shape[1]}")
print("\nDatentypen der Spalten:")
print(data.dtypes)

# Datenbereinigung
print("\nFehlende Werte pro Spalte vor der Bereinigung:")
print(data.isnull().sum())
data.dropna(inplace=True)  # Fehlende Werte entfernen
data.drop_duplicates(inplace=True)  # Duplikate entfernen

# Datenanalyse
print("\nDeskriptive Statistiken für jede numerische Spalte:")
print(data.describe())
correlation = data.corr()
print("\nKorrelationen in den Daten:")
print(correlation)

# Datenvisualisierung
# Histogramme für einige ausgewählte numerische Eigenschaften
data['total_UPDRS'].hist()
plt.title('Verteilung von total_UPDRS')
plt.show()

# Scatter Plot für eine exemplarische Beziehung
plt.scatter(data['motor_UPDRS'], data['total_UPDRS'])
plt.title('Motor UPDRS vs. Total UPDRS')
plt.show()

# Boxplot für Total UPDRS basierend auf einem relevanten Merkmal
data.boxplot(column='total_UPDRS', by='age')
plt.title('Total UPDRS nach Alter')
plt.show()
