import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Fetch the web page
url = 'https://www.diw.go.th/datahawk/factype.php'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
response.raise_for_status()  # Check for request errors

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Locate the table
table = soup.find('table')  # Adjust the selector based on the table's attributes

# Step 4: Extract headers
headers = []
for th in table.find_all('th'):
    headers.append(th.get_text(strip=True))

# Step 5: Extract rows
rows = []
for tr in table.find_all('tr'):
    cells = tr.find_all(['td', 'th'])
    row = [cell.get_text(strip=True) for cell in cells]
    if row:  # Ensure the row is not empty
        rows.append(row)

print(rows)
# Step 6: Save to CSV
#with open('factory_types.csv', 'w', newline='', encoding='utf-8') as f:
#    writer = csv.writer(f)
#    if headers:
#        writer.writerow(headers)
#    writer.writerows(rows)

#"Data has been successfully scraped and saved to 'factory_types.csv'.")