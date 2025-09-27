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


# BUAT SPREADSHEET / EXCEL

# =ARRAYFORMULA(
#   LET(
#     nim; TEXT(SEQUENCE(23; 1; 1); "000");
#     usnPlayer; FILTER(Sheet1!B3:B; Sheet1!B3:B <> "");
#     dataJawaban; FILTER(Sheet1!D3:D; Sheet1!B3:B <> "");
#     reNIM; IFERROR(REGEXEXTRACT(usnPlayer; "\d{3}"));
#     hLookup; VLOOKUP(nim; {reNIM\ dataJawaban}; 2; FALSE);
#     {"NIM"\ "Correct Answers";
#      nim\ IFERROR(hLookup; "Data tidak tersedia")}
#   )
# )