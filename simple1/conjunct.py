from nltk import CFG
import nltk

grammar = CFG.fromstring("""
S -> N L
N -> Num N | Num
Num -> '1' | '2' | '3'
L -> Let L | Let 
Let -> 'A' | 'B' | 'C'
""")

from nltk.parse import BottomUpChartParser
parser = nltk.ChartParser(grammar)

sentence = '1 2 1 3 A C B C'.split()

for t in parser.parse(sentence):
    print(t)