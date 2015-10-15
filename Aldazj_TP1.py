import os
import re

__author__ = 'aldazj'


def interactiveinterpreter():
    """
    On différencie les mots qui commencent par "wh" en ajoutant un *
    au début de chaque mot contrairement aux autres mots où on ajoute un -
    Le resultat est affiché dans un fichier text
    :return:
    """
    mylist = ["how", "why", "however", "where", "never"]
    for element in mylist:
        print("* "+element[:2]+" "+element)
    print("")
    f = open('interactiveInterpreter.txt', 'w')
    for element in mylist:
        if element.startswith('wh'):
            print("* "+element[:2]+" "+element)
            f.write("* "+element[:2]+" "+element+"\n")
        else:
            print("- "+element[:2]+" "+element)
            f.write("- "+element[:2]+" "+element+"\n")
    f.close()


def listcomprehension():
    """
    Grâce aux "list comprehesions pour afficher nous affichons les mots plus grand que 4 qui
    commencent par "sh"
    :return:
    """
    text1 = ["how", "why", "however", "where", "never"]
    mylist = ["she", "sells", "sea", "shells", "by", "the", "sea", "shore"]
    print("Question a)")
    # la commande "sum([len(w) for w in text1])" additionne tous les lettres de chaque élement
    # existants dans la list "text1"
    print("Moyenne: ", float(sum([len(w) for w in text1])/len(text1)))
    print("Question b)")
    print([w for w in mylist if w.startswith('sh')])
    print([w for w in mylist if len(w) > 4])


def wordfrequenties():
    mydict = dict()
    mytext = "Le poids politique de Lorient s’affirme à partir de la Révolution française et la ville gagne un rôle " \
             "administratif à partir du premier Empire Les activités commerciales restent alors en retrait dans la " \
             "première moitié du 19e siècle en raison des conflits fréquents mais les activités militaires gagnent en" \
             "importance"
    for w in mytext.lower().split(' '):
        if w not in mydict.keys():
            mydict[w] = 1
        else:
            mydict[w] += 1

    for key in sorted(mydict):
        print(key, mydict[key])


def patterns(n):
    """
    Affiche le pattern de dimension nxn demandé
    :param n: taille du pattern
    :return:
    """
    print("n: ", n)
    for i in reversed(range(1, n+1)):
        print((n-i)*'-'+i*'+')


def index(filename):
    """
    Pour chaque mot présent dans le fichier envoyé en paramètre,
    Nous affichons les numéros des lines où ce mot est présent
    :param filename: fichier à analyser
    :return:
    """
    mydict = dict()
    scriptdir = os.path.dirname(os.path.abspath(__file__))
    sp_file = os.path.join(scriptdir, filename)
    f = open(sp_file, 'r')
    for num, line in enumerate(f, 1):
        #Grâce à "\s+" nous capturons tous les \t, \n, espace, double espace
        for w in re.sub('\s+', ' ', line.lower().strip()).split(' '):
            if w:
                if w not in mydict.keys():
                    mydict[w] = [num]
                else:
                    if num not in mydict[w]:
                        mydict[w].append(num)
    f.close()
    for key in sorted(mydict):
        print("{0:20} {1}".format(key, str(mydict[key]).strip('[]').replace(',', '')))


print("----------------   Exo1   ----------------")
interactiveinterpreter()

print("----------------   Exo2   ----------------")
listcomprehension()

print("----------------   Exo3   ----------------")
wordfrequenties()

print("----------------   Exo4   ----------------")
n = [3, 4, 5]
for w in n:
    patterns(w)
    print("")

print("----------------   Exo5   ----------------")
filename = 'austen.txt'
index(filename)