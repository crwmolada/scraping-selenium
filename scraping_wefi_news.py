import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# inicializa el controlador S
navegador = webdriver.Chrome()

navegador.get('https://we-fi.org/news/')

# espera antes de continuar
espera = WebDriverWait(navegador, 10)

# Desplazarse para cargar más contenido si es necesario
tiempo_pausa_desplazamiento = 2  # scrollea cada 2 segundos
contador_titulos_previos = 0

for i in range(10):  # veces que se desplaza
    navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);") # desplaza hasta el final de la página
    time.sleep(tiempo_pausa_desplazamiento)
    
    # busca los titulos
    titulos = navegador.find_elements(By.XPATH, '//h3[@class="title"]/a')
    contador_titulos_actual = len(titulos)

    # si no hay cambios, se detiene
    if contador_titulos_actual == contador_titulos_previos:
        break
    
    #  actualiza el contador de titulos si encuentran más
    contador_titulos_previos = contador_titulos_actual

# se usa el xpath para apuntar a los títulos y fechas
titulos = navegador.find_elements(By.XPATH, '//h3[@class="title"]/a')
fechas = navegador.find_elements(By.XPATH, '//div[@class="post-header"]/span')

# listas de almacenamiento
lista_titulos = []
lista_fuentes = []
lista_fechas = []

# se agrupan datos
for titulo, fecha in zip(titulos, fechas):
    lista_titulos.append(titulo.text)
    lista_fuentes.append(titulo.get_attribute('href'))
    lista_fechas.append(fecha.text)

# se crea un DataFrame de pandas
df = pd.DataFrame({
    'Título': lista_titulos,
    'Fecha': lista_fechas,
    'Fuente': lista_fuentes
})

# se eliminan duplicados en el DataFrame
df = df.drop_duplicates(subset=['Título', 'Fecha', 'Fuente'])

# crear excel
df.to_excel('noticias_wefi.xlsx', index=False)

# cerrar el navegador
navegador.quit()
