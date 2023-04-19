import json
import requests

#1
with open('./arquivos/base_tdspy.json') as file:
    text = json.load(file)

insertRm = int(input('Digite o rm:'))

#2
response = requests.get("http://www.fiap.com.br")
file_html = response.content2


#3
with open('fiap.html', 'w') as file_site:
    file_site.write("<html>henrique</html>")