import re

# definição das Classes de caracteres
LETTER = 0
DIGIT = 1
UNKNOWN = 99

# definição dos Códigos de tokens
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26

# Definindo a lista de palavras-chave
expressoes_regulares = [
    (r'\(', LEFT_PAREN),
    (r'\)', RIGHT_PAREN),
    (r'\+', ADD_OP),
    (r'\*', MULT_OP),
    (r'\=', ASSIGN_OP),
    (r'[0-9]+', INT_LIT),  # Números inteiros
    (r'[a-zA-Z_][a-zA-Z0-9_]*', IDENT),  # Identificadores
]

# classe principal do analisador lexico
class Analisador_Lexico:
    
    #primeira coisa a ser feita é ler o arquivo
    def __init__(self):
        print("Começou \n")

    def pegaTokens (self):
        with open('entrada.txt', 'r', encoding='utf-8') as arquivo:
            tokens = []
            for linha in arquivo:
                linha = self.ignorando_comentarios(linha)
                tokens = tokens + self.analisador_lexico(linha)
           # print(tokens)
           # print("\n Tokens pegos dentro de lexico")
        return tokens

    #função para ignorar comentários
    def ignorando_comentarios(self, text):
        return re.sub(r'//.*', '', text).rstrip()

    #função princiapl do analisador. retorna os tokens com lexemas em uma array associativa 
    def analisador_lexico(self, expressao):
        tokens = []
        while expressao:
            expressao = expressao.lstrip()
            for pattern, codigo_do_token in expressoes_regulares:
                match = re.match(pattern, expressao)
                if match:
                    lexema = match.group(0)
                    tokens.append((codigo_do_token, lexema))
                    expressao = expressao[len(lexema):]
                    break
               # else:
                #    raise ValueError(f"Caractere inválido na expressão: {expressao[0]}")
        return tokens
