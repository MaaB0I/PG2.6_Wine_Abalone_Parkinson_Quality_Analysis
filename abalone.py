import pandas as pd
import matplotlib.pyplot as plt

# Laden der Daten
column_names = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']
data = pd.read_csv('CSV/abalone/abalone.data', header=None, names=column_names)

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
print("\nKorrelation der 'Rings' mit anderen Eigenschaften:")
print(correlation['Rings'].sort_values())

# Datenvisualisierung
# Histogramm für die Länge
data['Length'].hist()
plt.title('Verteilung der Länge')
plt.show()

# Scatter Plot für Länge vs. Ringe
plt.scatter(data['Length'], data['Rings'])
plt.title('Länge vs. Ringe')
plt.show()

# Boxplot für die Ringe basierend auf dem Geschlecht
data.boxplot(column='Rings', by='Sex')
plt.title('Ringe nach Geschlecht')
plt.show()
