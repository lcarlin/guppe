dicionario_sites = {"Diego": "diegomariano.com"}
print(dicionario_sites['Diego'])

dicionario_sites = {"Diego": "diegomariano.com", "Google": "google.com", "Udemy": "udemy.com", "Luiz Carlin" : "luizcarlin.com.br"}

print ("-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=")
for chave in dicionario_sites:
    print (chave + " -:- " +dicionario_sites[chave]) 
    print(dicionario_sites[chave])

print ("-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=")
for i in dicionario_sites.items():
    print(i)

print ("-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=")
for i in dicionario_sites.values():
    print(i)

print ("-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=")
for i in dicionario_sites.keys():
    print(i)