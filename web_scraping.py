import requests
# parsear texto html y acceder a el como si fuera un arbol
from bs4 import BeautifulSoup 
# perimite guardar las imagenes
import urllib

FAO = 'http://www.fao.org/economic/ess/ess-home/es'
INDEXMUNDI = 'https://www.indexmundi.com/agriculture/?commodity=corn&graph=production' 

def run():
  for i in range(1, 6):
    # hacemos una solicitud get a la pagina
    response = requests.get('https://xkcd.com/{}'.format(i))

    # parseamos el documento, recibe el contenido del request y el tipo de parseador
    soup = BeautifulSoup(response.content, 'html.parser')

    # accedemos al contendot de la imagen 
    image_container = soup.find(id='comic')

    # obtenemos la url de la imagen
    image_url = image_container.find('img')['src']

    # obtenemos el nombre del archivo 
    image_name = image_url.split('/')[-1]

    # lo mostramos en consola
    print('Descargando la imagen {}'.format(image_name))
    
    # guardamos las imagenes en el directorio actual
    urllib.request.urlretrieve('https:{}'.format(image_url), image_name)

if __name__  == '__main__':
  run()