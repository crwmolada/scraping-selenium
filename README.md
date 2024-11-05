## scraping-selenium-puppeter

# Web Scraper de Noticias We-Fi

Este proyecto contiene dos implementaciones de un web scraper para el sitio de noticias [We-Fi](https://we-fi.org/news/), utilizando **Selenium** y **Puppeteer**. Ambos scripts extraen títulos, fechas y enlaces de las noticias y los guardan en una base de datos o en un archivo Excel.

## Tecnologías

- **Selenium**: Script en Python que utiliza Chrome WebDriver para el scraping y guarda los datos en un archivo Excel.
- **Puppeteer**: Script en JavaScript/Node.js que utiliza Brave Browser para el scraping y guarda los datos en una base de datos.

---

## Selenium Script en Python

### Descripción

Este script automatiza la extracción de noticias desde el sitio de We-Fi utilizando **Selenium** con el controlador de Chrome. Se desplaza hasta el final de la página para cargar más contenido, luego extrae los títulos, fechas y enlaces de noticias, y finalmente guarda los datos en un archivo Excel (`noticias_wefi.xlsx`).

### Requisitos

- **Python 3.x**
- **Selenium**: Instalar con:
  ```bash
  pip install selenium pandas
- **Chrome WebDriver**: Debe estar en el PATH del sistema. Descárgalo de ChromeDriver.

### Ejecución
- Ejecuta el script:
  ```bash
  python selenium_scraper.py

- El archivo noticias_wefi.xlsx se generará en el mismo directorio.

## Puppeteer Script en JavaScript

### Descripción
Este script en Node.js utiliza Puppeteer para extraer datos de noticias desde We-Fi. Usa Brave Browser y realiza un desplazamiento automático para cargar más contenido. Los datos extraídos se guardan en una base de datos mediante la función saveEvent.

### Archivos
- **puppeteer_scraper.js**: Contiene el código de scraping en JavaScript.
- **fintechScraping.js**: Contiene la función saveEvent que almacena los datos en la base de datos y la conexión a la base de datos.

### Requisitos
- **Node.js**
- **Puppeteer**: Instalar con:
  ```bash
  npm install puppeteer
- **Función saveEvent**: Crea la siguiente función en `fintechScraping.js`
  ```bash
  export async function saveEvent(event){
    const {titulo, fecha, fuente} = event
    const sql = 'INSERT INTO newswefi (titulo, fecha, fuente) VALUES(?, ?, ?)';
    const [result] = await fintechDB.query(sql, [titulo, fecha, fuente])
    return result;}
- **Brave Browser**: Asegúrate de que Brave esté instalado y la ruta esté correctamente configurada en executablePath.

### Ejecución
- Ejecuta el script:
  ```bash
  node scrapingController.js
