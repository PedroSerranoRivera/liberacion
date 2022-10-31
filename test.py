import pytesseract
from importlib.metadata import files
from logging import lastResort
import glob, os, shutil, sys, fitz
from PIL import Image
from PyPDF2 import PdfReader

os.system('clear')

folder = os.getcwd()

#funcion crear carpeta con nombre del archivo 
def creador_nombre_carpeta():
    # for para sacar el archivo reciente 
    for file_path in glob.glob(os.path.join(folder, '*.pdf*')):
     # crea variable con el nombre quitando el tipo de archivo
     new_dir = file_path.rsplit('.', 1)[0]
    try:
        # Crea el directorio uniendo ruta y nombre del archivo
        os.mkdir(os.path.join(folder, new_dir))
    except WindowsError:
        # Ventana de error si el directorio existe
        # Handle the case where the target dir already exist.
        pass
    #Mueve el archivo al directorio creado
    shutil.move(file_path, os.path.join(new_dir, os.path.basename(file_path)))

#funcion buscar carpeta y meterse en el directorio
def buscador_carpeta_reciente():
 # Buscador de carpeta reciente
  all_subdirs = [d for d in os.listdir('.')
                 if os.path.isdir(d)]
  Directorio = max(all_subdirs, key=os.path.getmtime)                 
 #Junta las rutas de directorios
  QE = os.getcwd ()
  path = QE+'/'+Directorio 
  #cambia al directorio
  os.chdir(path)
  dirctory = os.getcwd()
  print(f'Current working directory: After= {dirctory}')
  
def pdf_extractor():
    folder = os.getcwd()
    for file_path in glob.glob(os.path.join(folder, '*.pdf*')):
     # crea variable con el nombre quitando el tipo de archivo
     new_file_pdf = file_path.rsplit('.', 0)[0]
    try:
        # Crea ruta completa
        ruta_c = os.path.join(folder, new_file_pdf)
    except WindowsError:
        # Ventana de error si el directorio existe
        # Handle the case where the target dir already exist.
        pass
    # print(ruta_c)
    # Usa modulo PyPDF
    reader = PdfReader(ruta_c)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(text)
    #Escribir archivo en txt
    salida = open(f"{ruta_c}_.csv", "w")
    salida.write( str(text) )
    salida.close()



# Jaladores
creador_nombre_carpeta()
buscador_carpeta_reciente()
pdf_extractor()


