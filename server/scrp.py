import requests
import time
from bs4 import BeautifulSoup

url = 'https://www.ni.com/site-search/api/results?sn=catnav%3Asup.dwl.idr&locale=fr-FR&ps=500&pg=15&firstLoad=true'
time.sleep(5)
response = requests.get(url)
if response.status_code == 200:


    output_file_path = 'output15.txt'

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(response.text)


    print(f"Response saved to {output_file_path}")

# soup = BeautifulSoup(response.text, 'html.parser')

# rows_of_interest = [0]

# product_names = []
# manufacturers = []

# table = soup.find('tbody')
# rows = table.find_all('tr')

# for row_index in rows_of_interest:
#     row = rows[row_index]
#     columns = row.find_all('td')
#     if len(columns) >= 2:
#         product_name = columns[0].text.strip()
#         manufacturer = columns[1].text.strip()
#         product_names.append(product_name)
#         manufacturers.append(manufacturer)

# for product_name, manufacturer in zip(product_names, manufacturers):
#     print(f"Product Name: {product_name}")
#     print(f"Manufacturer: {manufacturer}")
#     print(len(product_name))

