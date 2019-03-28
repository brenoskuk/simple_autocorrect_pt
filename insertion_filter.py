#important https://docs.python.org/3/library/stdtypes.html#string-methods
import string
from unicodedata import normalize
import os

#cria versões sem acentos das palavras
def delete_acentos(text_input, codif='utf-8'):
    return normalize('NFKD', text_input).encode('ASCII', 'ignore').decode('ASCII')

#cria versões com todas as letras minúsculas
def all_lower(text_input):
    return text_input.lower()

#percorre todos os templates e adiciona frases modificadas
if __name__ == '__main__':
    more = []
    dir = './data/nlu_data'
    for file in os.listdir(dir):
        if file != 'synonyms.md' and file != 'lookups.md' and file != 'base.md' and 'describe_' not in file and file !='compare_scores.md':
            f = open(dir + "/" + file, 'r')
            line = f.readline()
            line = f.readline()
            while (line):
                if line[-1] != '\n':
                    line = line + '\n'
                new1 = delete_acentos(line)
                if line != new1:
                    more.append(new1)
                    new2 = all_lower(new1)
                    if new2 != new1:
                        more.append(new2)
                new = all_lower(line)
                if line != new:
                    more.append(new)
                line = f.readline()
            f.close()
            f = open(dir + "/" + file, 'a')
            f.write('\n' + ''.join(more))
            f.close()
            more = []

