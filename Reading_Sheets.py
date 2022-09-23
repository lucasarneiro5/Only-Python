import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

arquivo_excel_1 = 'nome_do_arquivo.xlsx' # Tem q estar nesta pasta ou dar o diretorio

df_dia_1 = pd.read_excel(arquivo_excel_1, sheet_name='nome_da_aba_1')
df_dia_2 = pd.read_excel(arquivo_excel_1, sheet_name='nome_da_aba_2')

# Juntar as planilhas
df_todas_planilhas = pd.concat([df_dia_1, df_dia_2])