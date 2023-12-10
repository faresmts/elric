from LexicalAnalyzer import LexicalAnalyzer

def start():
    #filename = input("enter the name of the file with relative path to this script: ")
    filename = "entrada.txt"
    
    lexicalAnalyzer = LexicalAnalyzer(filename)
    lexicalAnalyzer.parse()

start()

