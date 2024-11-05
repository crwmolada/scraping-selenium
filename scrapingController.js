import puppeteer from "puppeteer";
import { saveEvent } from "../model/fintechScraping.js";

export async function scrapeAndSave(req, res) {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe', 
    headless: false,
    slowMo: 500,
    defaultViewport: null,
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
    timeout: 60000 
  });

  const page = await browser.newPage();
  await page.setDefaultNavigationTimeout(60000);
  await page.goto('https://we-fi.org/news/', { waitUntil: 'domcontentloaded', timeout: 60000 });

  // Desplazarse para cargar más contenido
  let previousHeight = await page.evaluate('document.body.scrollHeight');
  while (true) {
    await page.evaluate('window.scrollTo(0, document.body.scrollHeight)');
    await page.evaluate(() => new Promise(resolve => setTimeout(resolve, 2000))); // Pausa de desplazamiento
    const newHeight = await page.evaluate('document.body.scrollHeight');
    if (newHeight === previousHeight) break;
    previousHeight = newHeight;
  }

  // Extraer los datos
  const data = await page.evaluate(() => {
    const titulos = Array.from(document.querySelectorAll('h3.title a')).map(el => el.innerText);
    const fechas = Array.from(document.querySelectorAll('div.post-header span')).map(el => el.innerText);
    const fuentes = Array.from(document.querySelectorAll('h3.title a')).map(el => el.href);
    return titulos.map((titulo, index) => ({
      titulo,
      fecha: fechas[index],
      fuente: fuentes[index]
    }));
  });

  console.log(data);
  await browser.close();

  for (const event of data) {
    await saveEvent(event);
  }

  res.send('Datos scrapeados y guardados en la base de datos.');
}


// Función para obtener los eventos
export async function getEvents(req, res) {
  try {
    const [events] = await fintechDB.query("SELECT * FROM events");
    res.status(200).json(events);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: "An error occurred retrieving events" });
  }
}