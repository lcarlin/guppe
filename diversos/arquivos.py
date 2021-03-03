# -*- coding: utf-8 -*-
Arquivo = open("C:\TEMP\python\Meu Filé2.txt")
print(Arquivo)

print ("-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=")
linhas = Arquivo.readlines() 
# for linha_atual in linhas:
    #print (linha_atual)

print ("-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=")
textoCompleto = Arquivo.read() 
print (textoCompleto)

Saida = open("File3.txt","a")
Saida.write("Esse é o 3 file\n\n ")

Saida.close()
Arquivo.close()