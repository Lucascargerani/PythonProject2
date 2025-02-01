#import platform
import getpass
#from datetime import datetime

#print("Nome maquina:.......", platform.node())
#print("Arquitetura:.......", platform.architecture())
#print("Sistema Operacional:.......", platform.system())
#print("Versão do SO:.......", platform.release())
#print("Processador:.......", platform.processor())
#print("Versão do Python;.......", platform.python_version())

#print(datetime.now().month)

usuario = getpass.getuser()
senha = getpass.getpass("Digite sua senha:....")

if usuario == 'userlucas' and senha == 'Hello':
    print('Bem vindo, Lucas')
    print('Voce nao tem acesso')