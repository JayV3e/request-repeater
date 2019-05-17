import os
# portion de l'adresse avant le /
BASE_URL = ''

# Inclure le fichier de logs après avoir supprimé les entrées avant et après celles que l'ont souhaite reproduire
LOG_FILE = ''


urls = []
with open (LOG_FILE) as file:
    data = file.readlines()
    for line in data:
        url = line.split('GET ')[1].split(' HTTP')[0]
        if url not in urls:
            urls.append(url)

for url in urls:
    os.system(f'curl {BASE_URL}{url}')