import requests
from bs4 import BeautifulSoup
import sys

# Supported Languages
languages = ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese', 'Dutch', 'Polish', 'Portuguese',
             'Romanian', 'Russian', 'Turkish']


def translate(input_language, output_language, word, f):
    direction = input_language.lower() + '-' + output_language.lower()
    # Get Translation
    url = f'https://context.reverso.net/translation/{direction}/{word}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers)
    except:
        return 'network_issue'
    if response.status_code == 200:
        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            translations = [a.text.strip() for a in soup.find('div', {'id': 'translations-content'}).find_all('a')]
            examples = [ele.text.strip() for ele in
                        soup.find('section', {'id': 'examples-content'}).find_all('span', {'class': 'text'})]
        except:
            return 'translation_issue'
        # Write to File
        f.write(f"{output_language.title()} Translations:\n")
        f.write("\n".join(translations[:5]))
        f.write(f"\n\n{output_language.title()} Examples:\n")
        for i in range(0, 10, 2):
            f.write((examples[i]+'\n'))
            f.write((examples[i + 1]+'\n'))
            f.write('\n')
        # Write to console
        print(f"{output_language.title()} Translations:")
        print("\n".join(translations[:5]))
        print(f"\n{output_language.title()} Examples:")
        for i in range(0, 10, 2):
            print(examples[i])
            print(examples[i + 1])
            print()
    else:
        return 'translation_issue'
    return 'Success'

# Get Translation Direction and word
args = sys.argv
input_language, output_language, word = args[-3:]
with open(f'{word}.txt', 'w', encoding="utf-8") as f:
    if output_language == 'all':
        for output_language in languages:
            if output_language.lower() == input_language.lower():
                continue
            response = translate(input_language, output_language, word, f)
            if response == 'network_issue':
                print('Something wrong with your internet connection')
                break
            elif response == 'translation_issue':
                print(f'Sorry, unable to find {word}')
                break
    else:
        if output_language.title() in languages:
            response = translate(input_language, output_language, word, f)
            if response == 'network_issue':
                print('Something wrong with your internet connection')
            elif response == 'translation_issue':
                print(f'Sorry, unable to find {word}')
        else:
            print(f"Sorry, the program doesn't support {output_language}")
