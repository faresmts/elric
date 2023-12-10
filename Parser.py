from LexicalAnalyzer import LexicalAnalyzer

class Parser:
    
    TYPES = [
        LexicalAnalyzer.TYPE_INT,
        LexicalAnalyzer.TYPE_FLOAT,
        LexicalAnalyzer.TYPE_DOUBLE,
        LexicalAnalyzer.TYPE_CHAR
    ]
    
    def __init__(self, tokens):
        self.tokens = tokens
        self.currentTokensPosition = -1       
        self.currentLexeme = None
        self.currentLexemeCode = None
        self.nextLexeme = None
        self.nextLexemeCode = None
    
    def iterate(self):
        self.currentTokensPosition += 1
        currentTokenAssoc = self.tokens[self.currentTokensPosition]
        
        lexemeValue, lexemeCode = list(currentTokenAssoc.items())[0]
        self.currentLexeme = lexemeValue
        self.currentLexemeCode = lexemeCode
        
        print(f"Next token is: {self.currentLexemeCode} Next lexeme is {self.currentLexeme}")
        
        if self.currentTokensPosition == len(self.tokens) - 1:
            self.nextLexeme = 'EOF'
            self.nextLexemeCode = -1
        else:
            nextTokenAssoc = self.tokens[self.currentTokensPosition + 1]
            
            nextLexemeValue, nextLexemeCode = list(nextTokenAssoc.items())[0]
            self.nextLexeme = nextLexemeValue
            self.nextLexemeCode = nextLexemeCode
                
    def ignite(self):
        self.program()
    
    def program(self):
        print("Enter <program>")
        self.iterate()
        if self.currentLexemeCode == LexicalAnalyzer.TYPE_VOID:
            self.iterate()
            if self.currentLexemeCode == LexicalAnalyzer.MAIN_FUNCTION:
                self.iterate()
                if self.currentLexemeCode == LexicalAnalyzer.LEFT_PAREN:
                    self.iterate()
                    if self.currentLexemeCode == LexicalAnalyzer.RIGHT_PAREN:
                        self.iterate()
                        if self.currentLexemeCode == LexicalAnalyzer.LEFT_KEY:
                            self.stmt_list()
                            if self.currentLexemeCode == LexicalAnalyzer.RIGHT_KEY:
                                print("Exit <program>")
                            else: raise ValueError("Function main without right key")
                        else: raise ValueError("Function main without left key")
                    else: raise ValueError("Function main without rigth parentesis")
                else: raise ValueError("Function main without left parentesis")
            else: raise ValueError("Function main without main declaration")
        else: raise ValueError("Function main without main type void declaration")

    def stmt_list(self):
        print("Enter <stmt_list>")
        self.iterate()
        
        self.stmt()
        
        print("Exit <stmt_list>")
        
    def stmt(self):
        print("Enter <stmt>")
        
        self.delcr()
        
        print("Exit <stmt>")
        
    def delcr(self):
        print("Enter <delcr>")

        if self.currentLexemeCode in Parser.TYPES:
            self.iterate()
            if self.currentLexemeCode == LexicalAnalyzer.IDENTIFIER:
                self.iterate()
                if self.currentLexemeCode == LexicalAnalyzer.SEMICOLON:
                    self.iterate()
                else: raise ValueError("Declaring without semicolon")
            else: raise ValueError("Declaring without identifier")
        else: raise ValueError("Declaring with invalid type")
            
        print("Exit <delcr>")
        
            
    def expr(self):
        print("Enter <expr>")
        
        self.term()
        
        print("Exit <expr>")
        
        
    def term(self):
        print("Enter <term>")
        
        self.factor()
        
        print("Exit <term>")
        
    def factor(self):
        print("Enter <factor>")
        if self.currentLexemeCode == LexicalAnalyzer.IDENTIFIER or self.currentLexemeCode == LexicalAnalyzer.NUMERIC:
            self.iterate()
            return
        else:
            if self.currentLexemeCode == LexicalAnalyzer.LEFT_PAREN:
                self.iterate()
                self.expr()
                if self.currentLexemeCode == LexicalAnalyzer.RIGHT_PAREN:
                    self.iterate()
                else:
                    raise ValueError("Is not right parentesis")
            else:
                raise ValueError("Is not right parentesis, identifier or numeric")
            
        print("Exit <factor>")
        
        