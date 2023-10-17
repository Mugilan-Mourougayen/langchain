from bs4 import BeautifulSoup
import csv

# Load the HTML file
with open('output.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract and organize the data
data = []
for row in soup.find_all('tr'):
    columns = row.find_all('td')
    if len(columns) == 3:
        product_name = columns[0].text.strip()
        manufacturer = columns[1].text.strip()
        link = columns[0].find('a')['href']
        data.append([product_name, manufacturer, link])

# Write the data to a CSV file
with open('product_details.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Product Name', 'Manufacturer', 'Link'])
    csv_writer.writerows(data)

print('Data has been extracted and saved to product_details.csv')
