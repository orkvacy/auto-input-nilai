import pandas as pd
import re

df = pd.read_csv('review3.csv', skiprows=2)
df['NIM'] = df['Player'].str.extract(r'(\d{3})') #cari 3 digit ankga

hasilDF = df[['NIM', 'Correct Answers']].dropna(subset=['NIM'])
cariNim = [f'{i:03}' for i in range(1, 24)] #sesuaikan aja sama nim kelas kalian
cariNimDF = pd.DataFrame(cariNim, columns=['NIM'])


fixDF = pd.merge(cariNimDF, hasilDF, on='NIM', how='left')

fixDF['Correct Answers'] = fixDF['Correct Answers'].fillna('Data tidak tersedia')

fixDF = fixDF.sort_values(by='NIM')


fixDF.to_csv('Nilai Review.csv', index=False)

print("selesai")