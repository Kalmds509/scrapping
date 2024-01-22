import requests
from bs4 import BeautifulSoup
import csv
import logging

logging.basicConfig(level=logging.INFO)

def scraper(url):
    try:
        # reket
        response = requests.get(url)
        # leve eksepsyon
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser') #analize paj la

     
        title = soup.find('h1').text
        link = url
        image = soup.find('img')['src']
        description = soup.find('meta', {'name': 'description'})['content']

        return {'Title': title, 'Link': link, 'Image': image, 'Description': description}
    except requests.RequestException as e:
        #Jere ere 
        logging.error(f"Ere reket http: {e}")
        return None
    except Exception as e:
        # ere san atann
        logging.error(f"Ere nou pa atann : {e}")
        return None

def save_to_csv(data_list, csv_filename):
    header = ['Title', 'Link', 'Image', 'Description']

    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()

        for data in data_list:
            writer.writerow(data)
article_urls = [
  'https://lenouvelliste.com/article/246443/sanctions-onusiennes-le-panel-des-experts-en-mission-a-port-au-prince',
  'https://lenouvelliste.com/article/246436/augmentation-des-plaies-par-balle-dans-les-hopitaux',
  #Ajoute siw vle
 
]
data_list = []
for url in article_urls:
    data = scraper(url)
    if data:
        data_list.append(data)
        
save_to_csv(data_list, 'lenouvelliste_data.csv')
