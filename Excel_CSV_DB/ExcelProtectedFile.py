"""
https://stackoverflow.com/questions/15285068/from-password-protected-excel-file-to-pandas-dataframe
"""
import io
import pandas as pd
import msoffcrypto

passwd = 'Senha@01'

decrypted_workbook = io.BytesIO()
with open("G:\\PDW\\LANCAMENTOS_GERAIS.FULL.v2.xlsx", 'rb') as file:
    office_file = msoffcrypto.OfficeFile(file)
    office_file.load_key(password=passwd)
    office_file.decrypt(decrypted_workbook)

df = pd.read_excel(decrypted_workbook, sheet_name='LANCAMENTOS_GERAIS.FULL.v2')
print(f'total de linhas -> {df.count()}')
