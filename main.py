from LexicalAnalyzer import LexicalAnalyzer
from Parser import Parser

def start():
    filename = "entrada.txt"
    
    lexicalAnalyzer = LexicalAnalyzer(filename)
    lexicalAnalyzer.parse()
    
    parser = Parser(lexicalAnalyzer.tokens)
    parser.ignite()

start()