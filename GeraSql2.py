# -*- coding: cp1252 -*-
print ("-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=")
## AM-tb14516.txt.ok
# nomeArq = input('Entre com o nome do arquivo a ser tratado :-> ' )

nomeArq = "qualocep_endereco_2.csv.0002"

conta_erros=20001
contador = 0 
try:
    with open(nomeArq,'r+') as entrada:
        saida = open(nomeArq + ".sql", 'w')
        for linha in entrada:          
            if linha.find('cep') != 0 :
                # cep	logradouro	tipo_logradouro	complemento	local	id_cidade	id_bairro
                registro = linha.split(";")
                CEP = str(registro[0])
                LOGRADOURO = registro[1]
                TIPO_LOGRADOURO = registro[2]
                COMPLEMENTO = registro[3]
                LOCAL = registro[4]
                ID_CIDADE = registro[5]
                ID_BAIRRO = registro[5]
               
                string_sql = "BEGIN\n"
                string_sql += "  INSERT INTO LAC_77329_CEP_END (cep, logradouro, tipo_logradouro, complemento, localidade, id_cidade, id_bairro) \n "
                string_sql += f"    VALUES ('{CEP}', '{LOGRADOURO}', '{TIPO_LOGRADOURO}', '{COMPLEMENTO}' , '{LOCAL}', {ID_CIDADE} , {ID_BAIRRO} ); \n"
                string_sql += "EXCEPTION\n"
                string_sql += "   WHEN OTHERS THEN\n"
                conta_erros += 1 
                string_sql += f"       RAISE_APPLICATION_ERROR(-{conta_erros}, 'Erro no script 77784.  Erro: ' || sqlerrm);\n"
                string_sql += "END;\n/\n\n"
                if contador > 1000:
                    string_sql += "commit;\n/\n\n"
                    contador = 0

                print(string_sql)
                
        saida.close()
except FileNotFoundError:
    print('Arquivo não achado')
