import os
import re

__author__ = 'aldazj'


class Concordancer:
    """
    Cherche un mot désiré dans un fichier text et affiche les "deltaword" précédents et suivantes
    "deltaword" est un nombre entier
    """

    def foundindexword(self, word, line):
        """
        Trouve tous les indices du mot à chercher "word" dans une line
        :param word: mot à chercher
        :param line: une line du texte
        :return: les indices
        """
        all_index = []
        index_word = 0
        copyline = list(line)
        first = True
        while word in copyline:
            if first:
                index_word += copyline.index(word)
                first = False
            else:
                index_word += copyline.index(word)+1
            all_index.extend([index_word])
            copyline = line[index_word+1:len(line)]
        return all_index

    def displays(self, word):
        """
        Par rapport au fichier texte à analyse, on affiche le mot cherché "word"
        avec ses mots précédents ou suivantes
        :param word:
        :return:
        """
        # Pour chaque mot trouvé, nous affichos
        # les "deltawords" précédents et suivants
        deltawords = 6
        word = word.lower()
        for text in self.mytext:
            for line in text:
                if self.foundindexword(word, line):
                    for indexword in self.foundindexword(word, line):
                        if indexword == 0:
                            # Quand les mots commencent une ligne
                            avant = " "
                            apres = " ".join(line[indexword+1:(indexword+1+deltawords)])
                        elif indexword == len(line):
                            # Quand les mots terminent une ligne
                            avant = " ".join(line[indexword-deltawords:indexword])
                            apres = " "
                        elif indexword-deltawords < 0 and indexword+deltawords > len(line):
                            # Quand les mots ne respectent leur "deltaword" précédents et suivants
                            # car la ligne est tres petite.
                            avant = " ".join(line[0:indexword])
                            apres = " ".join(line[indexword+1:len(line)])
                        elif indexword-deltawords < 0 and indexword+deltawords < len(line):
                            # Quand les mots possèdent que leurs "deltaword" suivants
                            avant = " ".join(line[0:indexword])
                            apres = " ".join(line[indexword+1:(indexword+1+deltawords)])
                        elif indexword-deltawords > 0 and indexword+deltawords < len(line):
                            # Quand les mots possèdent leurs "deltaword" précédents et suivants
                            avant = " ".join(line[(indexword-deltawords):indexword])
                            apres = " ".join(line[indexword+1:indexword+1+deltawords])
                        elif indexword-deltawords > 0 and indexword+deltawords > len(line):
                            avant = " ".join(line[(indexword-deltawords):indexword])
                            apres = " ".join(line[indexword+1:len(line)])
                        print("{0:50} {1:20} {2:20}".format(avant, word, apres))

    def __init__(self, file):
        """
        Initialisation de notre classe
        :param file: fichier à analyser
        :return:
        """
        scriptdir = os.path.dirname(os.path.abspath(__file__))
        sp_file = os.path.join(scriptdir, file)
        self.mytext = []
        with open(sp_file) as file:
            self.mytext.append([re.sub('\s+', ' ', line.lower().strip()).split(' ') for line in file])


print("----------------   Exo6   ----------------")
file = 'austen.txt'
word = 'and'
c = Concordancer(file)
c.displays(word)