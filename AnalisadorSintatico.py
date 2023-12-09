from AnalisadorLexico import Analisador_Lexico

class Analisador_Sintatico:
  def __init__(self):
    self.analisadorLexico = Analisador_Lexico()
    self.tokens = (self.analisadorLexico.pegaTokens())
    self.posicaoAtual = 0
  
  def analise(self):
    if self.verificaGramatica():
      print("Analise feita")
    else:
      print("ERRROOOOOOO")

  def verificaGramatica(self):
    if not self.verificaToken(11):
      return False
      
    self.proximoToken()

    if not self.verificaToken(21):
      return False
      
    self.proximoToken()

    if not self.verificaToken(11):
      return False
      
    return True

  def verificaToken(self, tipoEsperado):
    if self.posicaoAtual < len(self.tokens) and self.tokens[self.posicaoAtual][0] == tipoEsperado:
      return True
    return False

  def proximoToken(self):
    if self.posicaoAtual < len(self.tokens) - 1:
      self.posicaoAtual += 1



'''
  def expr(self):
    analisadorLexico = Analisador_Lexico()
    tokensPrincipal = (analisadorLexico.pegaTokens())
    tokens = tokensPrincipal
    print(tokens)
    print(tokensPrincipal)
    print("entrou no expr")
    for par in tokens:
      if par[0] == 11:
        print("Eba")
        print(tokens)
        tokens.pop(0)
        break
      else:
        print("não achou")
        break
    for par in tokens:
      if par[0] == 21:
        print("Eba")
        print(tokens)
        tokens.pop(0)
        break
      else:
        print("não achou")
        break
    for par in tokens:
      if par[0] == 11:
        print("Eba")
        print(tokens)
        tokens.pop(0)
        break
      else:
        print("não achou")
        break
    print("Temos uma expressao")
    print(tokens)
    print(tokensPrincipal)
'''

analise = Analisador_Sintatico()
analise.analise()







'''
A * B
factor 
 expr()
 verifica se tem um +
 expr()

Expr 
 id()
 verifico se tem *
 assing()

ASSIGN
 id()

id
 verifica de tem IDENT
 

Expr > id + id
'''
