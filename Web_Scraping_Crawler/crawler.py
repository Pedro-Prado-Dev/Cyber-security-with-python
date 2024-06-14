import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter
import re

def start(url):
    wordlist = []
    source_code = requests.get(url).text
    
    soup = BeautifulSoup(source_code, 'html.parser')

    # Imprimindo toda a estrutura HTML para verificação
    with open("page_content.html", "w", encoding='utf-8') as file:
        file.write(soup.prettify())
    
    # Analisando uma seção mais geral, como um artigo
    content_section = soup.findAll('article')
    if not content_section:
        print("A tag 'article' não foi encontrada na página.")
        return
    
    for each_text in content_section:
        content = each_text.text
        print("Conteúdo encontrado:", content)
        words = re.findall(r'\b\w+\b', content.lower())  # Usa regex para separar palavras
    
        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)

def clean_wordlist(wordlist):
    clean_list = []
    symbols = '!@#$%^¨&*()-_={[]}.|;?/<>,'
    
    for word in wordlist:
        for symbol in symbols:
            word = word.replace(symbol, '')
        
        if len(word) > 0:
            clean_list.append(word)
    
    remove_stop_words(clean_list)
    
def remove_stop_words(wordlist):
    stop_words = set(['the', 'is', 'in', 'it', 'and', 'to', 'a', 'of'])  # Adicione mais palavras conforme necessário
    clean_list = [word for word in wordlist if word not in stop_words]
    
    create_dictionary(clean_list)
    
def create_dictionary(clean_list):
    word_count = {}
    
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(), key=operator.itemgetter(1), reverse=True):
        print(f'{key} - {value}')
    
    c = Counter(word_count)
    top = c.most_common(10)
    print(top)        

if __name__ == '__main__':
    start('https://www.geeksforgeeks.org/how-to-get-list-of-git-branches-ordered-by-most-recent-commit/')
