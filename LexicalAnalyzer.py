from pprint import pprint 

class LexicalAnalyzer:
    
    # Char classes
    LETTER = 0
    DIGIT = 1
    BLANK_SPACE = 2
    UNKNOWN = 99
    
    # Identifiers
    NUMERIC = 10
    IDENTIFIER = 11
    
    # Tokens
    ASSIGN_OP = 20
    ADD_OP = 21
    SUB_OP = 22
    MULT_OP = 23
    DIV_OP = 24
    LEFT_PAREN = 25
    RIGHT_PAREN = 26
    LEFT_KEY = 27
    RIGHT_KEY = 28
    SEMICOLON = 29
    COLON = 30
    AND = 31
    OR = 32
    AND_OP = 33
    OR_OP = 34
    EQUAL = 35
    GREATER = 36
    GREATER_EQ = 37
    LESS = 38
    LESS_EQ = 39
    DIFF_VALUE = 40
    COMMA = 41
    
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
        'void': TYPE_VOID,
        'main': MAIN_FUNCTION,
        'if': IF_STMT,
        'else': ELSE_STMT,
        'while': WHILE_STMT,
        'for': FOR_STMT,
        'int': TYPE_INT,
        'float': TYPE_FLOAT,
        'double': TYPE_DOUBLE,
        'char': TYPE_CHAR,
    }
    
    LOOKUP = {
        '=' : ASSIGN_OP,
        '+' : ADD_OP,
        '-' : SUB_OP,
        '*' : MULT_OP,
        '/' : DIV_OP,
        '(' : LEFT_PAREN,
        ')' : RIGHT_PAREN,
        '{' : LEFT_KEY,
        '}' : RIGHT_KEY,
        ';' : SEMICOLON,
        ':' : COLON,
        '&' : AND,
        '|' : OR,
        '&&' : AND_OP,
        '||' : OR_OP,
        '=' : EQUAL,
        '>' : GREATER,
        '>=' : GREATER_EQ,
        '<' : LESS,
        '<=' : LESS_EQ,
        '!=' : DIFF_VALUE,
        ',' : COMMA
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
        self.currentLine = 1

    def parse(self):
        self.open_file()
        
        while self.currentToken != 'EOF':
            self.lexical()
    
        self.close_file()
        
    def lexical(self):
        self.validateChar()
        self.validateNextChar()
        
        if self.currentCharClass == LexicalAnalyzer.LETTER:
            self.lexeme.append(self.currentChar)
            
            lexemeString = ''.join(self.lexeme)
            
            if self.nextCharClass == LexicalAnalyzer.DIGIT:
                self.gelAllIdentifierFromMixedString()
                return
            
            if lexemeString in self.RESERVED_WORDS_AND_TOKENS:
                if self.nextCharClass != 'EOF':
                    if self.nextChar.isspace() or self.nextCharClass == LexicalAnalyzer.UNKNOWN:
                        self.parseTokenFromReservedWord(lexemeString)
                        return
                else:
                    self.parseTokenFromReservedWord(lexemeString)
                    self.currentToken = 'EOF'
                    return
            
            if self.nextCharClass != 'EOF':
               if self.nextChar.isspace() or self.nextCharClass == LexicalAnalyzer.UNKNOWN:
                   self.parseIdentifier(lexemeString)
                   return
            else:
                self.parseIdentifier(lexemeString)
                self.currentToken = 'EOF'
                return
            
        elif self.currentCharClass == LexicalAnalyzer.DIGIT:
            self.lexeme.append(self.currentChar)
            
            lexemeString = ''.join(self.lexeme)
            
            if self.nextCharClass == LexicalAnalyzer.LETTER:
                raise ValueError("Invalid identifier write: digits before alpha chars")
            
            if self.nextCharClass != 'EOF':
                if self.nextChar.isspace() or self.nextCharClass == LexicalAnalyzer.UNKNOWN:
                    self.parseInteger(lexemeString)
                    return
            else:
                self.parseInteger(lexemeString)
                self.currentToken = 'EOF'
                return
            
        elif self.currentCharClass == LexicalAnalyzer.UNKNOWN:
            self.lookup()
            return
        elif self.currentCharClass == LexicalAnalyzer.BLANK_SPACE:
            return
        else:
            raise ValueError("Some error occured")
        
    def validateChar(self):        
        char = self.file.read(1)
        
        if not char:
            self.currentToken = 'EOF'
        else:
            self.currentChar = char
            
            if char == '\n':
                self.currentLine += 1
            
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
            self.nextCharClass = 'EOF'
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
        self.tokens[len(self.tokens)] = {lexemeString : LexicalAnalyzer.RESERVED_WORDS_AND_TOKENS[lexemeString]}
        self.lexeme = []
        
    def parseIdentifier(self, lexemeString):
        self.tokens[len(self.tokens)] = {lexemeString : LexicalAnalyzer.IDENTIFIER}
        self.lexeme = []
        
    def gelAllIdentifierFromMixedString(self):
        while self.nextCharClass != 'EOF' and self.nextChar != ' ' and self.nextCharClass != LexicalAnalyzer.UNKNOWN:
            self.validateChar()
            self.validateNextChar()
            self.lexeme.append(self.currentChar)
        
        if self.nextCharClass == 'EOF':
            self.currentToken = 'EOF'
            
        lexemeString = ''.join(self.lexeme)
        self.parseIdentifier(lexemeString)
    
    def parseInteger(self, lexemeString):
        self.tokens[len(self.tokens)] = {lexemeString : LexicalAnalyzer.NUMERIC}
        self.lexeme = []
                    
    def lookup(self):
        if self.currentChar in LexicalAnalyzer.LOOKUP:
            if self.nextCharClass == LexicalAnalyzer.UNKNOWN:
                possibleToken = self.currentChar + self.nextChar
                if possibleToken in LexicalAnalyzer.LOOKUP: 
                    self.tokens[len(self.tokens)] = {possibleToken : LexicalAnalyzer.LOOKUP[possibleToken]}
                    self.lexeme = []
                    self.validateChar()
                    self.validateChar()
                    self.validateNextChar()
                else:
                    self.tokens[len(self.tokens)] = {self.currentChar : LexicalAnalyzer.LOOKUP[self.currentChar]}
                    self.lexeme = []
            else:
                self.tokens[len(self.tokens)] = {self.currentChar : LexicalAnalyzer.LOOKUP[self.currentChar]}
                self.lexeme = []
                if (self.nextCharClass == 'EOF'): 
                    self.currentToken = 'EOF'
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