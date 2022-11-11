# By  
# https://github.com/carlosmyr23   
# https://github.com/PedroSerranoRivera

#Liberias
import pandas as pd
import os
import shutil
from datetime import datetime
import xlwings as xw

#Constantes
nombres = {'SDESC':'MERCADO', 'SDESC.1':'PERIODO', 'SDESC.2':'FABRICANTE', 'VTAS. EN VALOR':'VENTAS EN VALOR (in 000 PESOS)',
           'VTAS. EN UNIDADES EQ (in LTS)':'VENTAS EN UNIDADES EQ (in 000 KILOS)', 'DIST. NUM. MANEJANTES':'DISTRIBUCION NUMERICA MANEJANTES',
           'VTAS. EN UNIDADES EQ (in LTS).1':'VENTAS EN UNIDADES (in 000)','INVENTARIO TOTAL EN UNID. EQ. (in LTS)':'INVENTARIO TOTAL EN UNIDADES (in 000)',
           'COMPRAS EN UNIDADES EQ. (in LTS)':'COMPRAS EN UNIDADES (in 000)','SHARE VENTAS UNIDADES EQ. (in LTS)':'SHARE VENTAS EN VALOR',
           'VTAS. EN UNIDADES':'VENTAS EN UNIDADES EQUIVALENTES 3 (in 00'}
base_csv = str()

fecha = datetime.today().strftime('%Y_%m_%d_%H_%M')

for i in os.listdir():
    if '.csv' in i:
        base_csv = i

#Cargamos la base
base = pd.read_csv(base_csv)
#Renombramos las columnas
base.rename(columns = nombres, inplace = True)

#Insertamos el dataframe decil_fugados en la hoja Decil Fugados
app = xw.App(visible=False)
book = xw.Book('LIBERACION_ORIGINAL.xlsx')
INFORMACION = book.sheets['INFORMACION']


INFORMACION.range('A1').options(index=False).value = base
nombre_liberacion = 'LIBERACION_ORIGINAL_' + fecha + '_MOD.xlsx'
book.save(nombre_liberacion)
book.close()
app.quit()

#Creamos carpeta
os.mkdir(base_csv[:-4] + '_' + fecha )
nombre_carpeta = base_csv[:-4] + '_' + fecha

os.getcwd() + '\\' + base_csv[:-4] + '_' + fecha

shutil.move(os.getcwd() + '\\' + nombre_liberacion, os.getcwd() + '\\' + nombre_carpeta)
shutil.move(os.getcwd() + '\\' + base_csv, os.getcwd() + '\\' + nombre_carpeta)
