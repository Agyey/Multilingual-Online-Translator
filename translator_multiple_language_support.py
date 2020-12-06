import requests
from bs4 import BeautifulSoup

# Supported Languages
languages = ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese', 'Dutch', 'Polish', 'Portuguese',
             'Romanian', 'Russian', 'Turkish']

# Get Translation Direction and word
print("Hello, you're welcome to the translator. Translator supports: ")
for index, language in enumerate(languages):
    print(f"{index+1}. {language}")
input_language = languages[int(input("Type the number of your language:\n"))-1]
output_language = languages[int(input("Type the number of language you want to translate to:\n"))-1]
word = input('Type the word you want to translate:\n')
direction = input_language.lower() + '-' + output_language.lower()

# Get Translation
url = f'https://context.reverso.net/translation/{direction}/{word}'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    translations = [a.text.strip() for a in soup.find('div', {'id': 'translations-content'}).find_all('a')]
    examples = [ele.text.strip() for ele in soup.find('section', {'id': 'examples-content'}).find_all('span', {'class': 'text'})]
    print('\nContext examples:\n')
    print(f"{output_language.title()} Translations:")
    print("\n".join(translations[:5]))
    print(f"\n{output_language.title()} Examples:")
    for i in range(0,10,2):
        print(examples[i])
        print(examples[i+1])
        print()
