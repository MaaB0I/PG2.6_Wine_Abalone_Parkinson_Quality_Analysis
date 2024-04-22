import pandas as pd
import matplotlib.pyplot as plt

# Datensatz laden
data = pd.read_csv('CSV/Wine Quality/winequality-red.csv', delimiter=';')

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
print("\nKorrelation der 'quality' mit anderen chemischen Eigenschaften:")
print(correlation['quality'].sort_values())

# Datenvisualisierung
# Histogramm für Alkoholgehalt
data['alcohol'].hist()
plt.title('Verteilung des Alkoholgehalts')
plt.show()

# Scatter Plot für Alkoholgehalt vs. Qualität
plt.scatter(data['alcohol'], data['quality'])
plt.title('Alkoholgehalt vs. Qualität des Weins')
plt.show()

# Boxplot für die Qualität basierend auf Alkoholgehalt
data.boxplot(column='alcohol', by='quality')
plt.title('Alkoholgehalt nach Weinqualität')
plt.show()
