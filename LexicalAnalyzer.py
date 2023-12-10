from pprint import pprint 

class LexicalAnalyzer:
    
    # Char classes
    LETTER = 0
    DIGIT = 1
    BLANK_SPACE = 2
    UNKNOWN = 99
    
    INT_LIT = 10
    IDENT = 11
    ASSIGN_OP = 20
    ADD_OP = 21
    SUB_OP = 22
    MULT_OP = 23
    DIV_OP = 24
    LEFT_PAREN = 25
    RIGHT_PAREN = 26
    LEFT_KEY = 27
    RIGHT_KEY = 28
    PONTO_VIRGULA = 29
    DOIS_PONTOS = 30
    SETA_ESQUERDA = 31
    SETA_DIREITA = 42
    TIPO_INTEIRO = 32
    TIPO_BOOLEAN = 33
    COND_IF = 34
    COND_ELSE = 35
    LOOP_WHILE = 36
    LOOP_FOR = 37
    PR_STD = 38
    PR_COUT = 39
    PR_ENDL = 40
    AND_OP = 41
    
    DOUBLE_AND = 70
    DOUBLE_OR = 71
    MAIN_FUNCTION = 80
    IF_STMT = 81
    ELSE_STMT = 82
    WHILE_STMT = 83
    FOR_STMT = 84
    TYPE_VOID = 91
    TYPE_INT = 92
    TYPE_FLOAT = 93
    TYPE_DOUBLE = 94
    TYPE_CHAR = 95
    
    RESERVED_WORDS_AND_TOKENS = {
        'void' : 91,
        'main' : 80,
        '&&' : 70,
        '||' : 71,
        'if' : 81,
        'else' : 82,
        'while' : 83,
        'for' : 84,
        'int' : 92,
        'float' : 93,
        'double' : 94,
        'char' : 95,
    }
    
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.currentCharClass = None
        self.currentChar = None
        self.nextChar = None
        self.nextCharClass = None
        self.lexemeLenght = None
        self.currentToken = None
        self.lexeme = []
        self.tokens = {}
        

    def parse(self):
        self.open_file()
        
        while self.currentToken != 'EOF':
            self.lexical()
            
        pprint(self.tokens)
    
            
        self.close_file()
        
        
    def lexical(self):
        self.validateChar()
        self.validateNextChar()
        
        if self.currentCharClass == LexicalAnalyzer.LETTER:
            self.lexeme.append(self.currentChar)
            
            lexemeString = ''.join(self.lexeme)
            
            if self.nextChar.isspace():
                if lexemeString in self.RESERVED_WORDS_AND_TOKENS:
                    self.parseTokenFromReservedWord(lexemeString)
            
            
            #validar se a string do lexema não é uma palavra reservada
            #se for e o próximo caractere for vazio, chamar o lookup 
            # vai adicionar digitos até proximo não ser um dígito ou não ser uma letra
        elif self.currentCharClass == LexicalAnalyzer.DIGIT:
            print(f"Digito: {self.currentChar}")
            # self.lexeme.append(self.currentChar)
            # vai adicionar digitos até proximo não ser um digito
        elif self.currentCharClass == LexicalAnalyzer.UNKNOWN:
            print(f"Desconhecido: {self.currentChar}")
            # self.lookup()
        else:
            raise ValueError("Some error occured")

        
    def validateChar(self):        
        char = self.file.read(1)
        
        if not char:
            self.currentToken = 'EOF'
        else:
            self.currentChar = char
            
            if char.isalpha():
                self.currentCharClass = LexicalAnalyzer.LETTER
            elif char.isdigit():
                self.currentCharClass = LexicalAnalyzer.DIGIT
            elif char.isspace():
                self.currentCharClass = LexicalAnalyzer.BLANK_SPACE
            else: 
                self.currentCharClass = LexicalAnalyzer.UNKNOWN
                
    def validateNextChar(self):
        position = self.file.tell()
        next_char = self.file.read(1)

        if not next_char:
            self.nextChar = None
            self.nextCharClass = None
        else:
            self.nextChar = next_char

            if next_char.isalpha():
                self.nextCharClass = LexicalAnalyzer.LETTER
            elif next_char.isdigit():
                self.nextCharClass = LexicalAnalyzer.DIGIT
            elif next_char.isspace():
                self.nextCharClass = LexicalAnalyzer.BLANK_SPACE
            else:
                self.nextCharClass = LexicalAnalyzer.UNKNOWN
        
        self.file.seek(position)
    
    def parseTokenFromReservedWord(self, lexemeString):
        self.tokens[lexemeString] = LexicalAnalyzer.RESERVED_WORDS_AND_TOKENS[lexemeString]
        

    def lookup(self):
        return
            
        
    def open_file(self):
        try:
            self.file = open(self.filename, 'r')
        except FileNotFoundError:
            print(f"File {self.filename} not found.")
        except Exception as e:
            print(f"Some error occurred in file {self.filename}: {e}")
            
    def close_file(self):
        self.file.close()