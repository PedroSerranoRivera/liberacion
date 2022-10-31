from ctypes.wintypes import tagRECT
from sys import float_repr_style
from openpyxl import Workbook
#from openpyxl.utils import get_column_letterfrom
from openpyxl import load_workbook

# Cargar el archivo y imprime hojas
wb = load_workbook(filename = "Muebles_dico_pa_Abril_22.xlsx")
print(wb.sheetnames)
# elegir hoja
wb.active = wb['Soporte Técnico Avanzado']
#
hoja = wb.active
#print(hoja)
celda = hoja['C37']
celda1 = hoja['C38']

# 

"""
if celda.value == celda1.value:
  print("Value of the Cell 1:",celda.value)
  print("ahuevirri")
else: 
  print("seas mamon") 
"""

valor = 2700

if celda.value == valor:
  print("Value of the Cell 1:",celda.value)
  print("ahuevirri")
else: 
  print("seas mamon") 
