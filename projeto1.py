# importando bibliotecas
import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter


# funcao start wordlist(obtendo o conteudo da pagina)
def start(url):
    wordlist = []
    word_count = {}
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'html.parser')

    # Procurar por tags com a classe 'entry-content'
    # essa parte do código percorre todos os elementos <div> com a classe 'entry-content', extrai o texto desses elementos, transforma o texto em minúsculas e divide-o em uma lista de palavras.
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text
        words = content.lower().split()
        
        for each_word in words:
            wordlist.append(each_word)

    clean_wordlist(wordlist, word_count)


def clean_wordlist(wordlist, word_count):
    clean_list = []
    symbols = '[email protected]'  # $%^&*()_-+={[}]|;:"<>?/.,'
    
    for word in wordlist:
        for symbol in symbols:
            word = word.replace(symbol, '')

        if word:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    sorted_word_count = sorted(word_count.items(), key=operator.itemgetter(1))
    for key, value in sorted_word_count:
        print("%s: %s" % (key, value))

    c = Counter(word_count)
    top = c.most_common(10)
    print(top)


if __name__ == '__main__':
    start("http://tutorialspoint.dev/slugresolver/programming-language-choose?")
