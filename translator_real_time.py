import requests
from bs4 import BeautifulSoup

# Get Translation Direction and word
direction = input('Type "en" if you want to translate from French into English, '
                  'or "fr" if you want to translate from English into French:\n')
word = input('Type the word you want to translate:\n')
print(f'You chose "{direction}" as a language to translate "{word}".')
directions = {
    'fr': 'english-french',
    'en': 'french-english'
}
direction = directions[direction]

# Get Translation
url = f'https://context.reverso.net/translation/{direction}/{word}'
headers={'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    print(response.status_code, 'OK')
    soup = BeautifulSoup(response.content, 'html.parser')
    translations = [a.text.strip() for a in soup.find('div', {'id': 'translations-content'}).find_all('a')]
    examples = [ele.text.strip() for ele in soup.find('section', {'id': 'examples-content'}).find_all('span', {'class': 'text'})]
    print('Translations')
    print(translations)
    print(examples)
