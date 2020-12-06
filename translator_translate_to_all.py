import requests
from bs4 import BeautifulSoup

# Supported Languages
languages = ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese', 'Dutch', 'Polish', 'Portuguese',
             'Romanian', 'Russian', 'Turkish']


def translate(input_language, output_language, word):
    direction = input_language.lower() + '-' + output_language.lower()
    # Get Translation
    url = f'https://context.reverso.net/translation/{direction}/{word}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        translations = [a.text.strip() for a in soup.find('div', {'id': 'translations-content'}).find_all('a')]
        examples = [ele.text.strip() for ele in
                    soup.find('section', {'id': 'examples-content'}).find_all('span', {'class': 'text'})]
        with open(f'{word}.txt', 'a', encoding="utf-8") as f:
            f.write(f"{output_language.title()} Translations:\n")
            f.write("\n".join(translations[:5]))
            f.write(f"\n\n{output_language.title()} Examples:\n")
            for i in range(0, 10, 2):
                f.write((examples[i]+'\n'))
                f.write((examples[i + 1]+'\n'))
                f.write('\n')
        print(f"{output_language.title()} Translations:")
        print("\n".join(translations[:5]))
        print(f"\n{output_language.title()} Examples:")
        for i in range(0, 10, 2):
            print(examples[i])
            print(examples[i + 1])
            print()
# Get Translation Direction and word
print("Hello, you're welcome to the translator. Translator supports: ")
for index, language in enumerate(languages):
    print(f"{index+1}. {language}")
input_language = languages[int(input("Type the number of your language:\n")) - 1]
output_language = int(input("Type the number of a language you want to translate to or '0' to translate to all languages:\n"))
word = input('Type the word you want to translate:\n')
if output_language == 0:
    for output_language in languages:
        if output_language == input_language:
            continue
        translate(input_language, output_language, word)
else:
    output_language = languages[output_language - 1]
    translate(input_language, output_language, word)


