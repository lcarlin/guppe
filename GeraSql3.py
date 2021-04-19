# -*- coding: cp1252 -*-
print ("-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=")
## AM-tb14516.txt.ok
# nomeArq = input('Entre com o nome do arquivo a ser tratado :-> ' )

nomeArq = "dois.csv"

conta_erros=20001
contador = 0 
try:
    with open(nomeArq,'r+') as entrada:
        saida = open(nomeArq + ".sql", 'w')
        for linha in entrada:          
            if linha.find('MENOR_CEP') != 0 :
                # cep	logradouro	tipo_logradouro	complemento	local	id_cidade	id_bairro
               registro =  linha.replace('"', '').split(";")
                  
               CIDADE = registro[2]
                  
               COD_IBGE = registro[4]
               ESTADO_ID = registro[5]
               VERSAO = registro[6]
               CODIGOTOM = registro[7]
               MENOR_CEP = registro[8]
               MAIOR_CEP = registro[9]
               conta_erros += 1 

               string_sql =   "BEGIN\n"
               string_sql +=  "   BEGIN\n"
               string_sql +=  "      UPDATE CSF_OWN.CIDADE N\n "
               string_sql += f"         SET N.CEP_INICIAL = '{MENOR_CEP}' \n"
               string_sql += f"           , N.CEP_FINAL   = '{MAIOR_CEP}' \n"
               string_sql += f"           , N.VERSION     = {VERSAO} \n"
               string_sql += f"       WHERE N.IBGE_CIDADE = {COD_IBGE}  ; \n"
               string_sql +=  "       VN_LINHAS := SQL%rowcount ; \n "
               string_sql +=  "   EXCEPTION\n"
               string_sql +=  "       WHEN OTHERS THEN\n"
               string_sql += f"          RAISE_APPLICATION_ERROR(-{conta_erros}, 'Erro no script 77784.  Erro: ' || sqlerrm);\n"
               string_sql +=  "   END;\n"
               conta_erros += 1 
               string_sql +=  "   IF VN_LINHAS = 0 THEN\n  "
               string_sql +=  "       BEGIN\n"
               string_sql +=  "           INSERT INTO  CSF_OWN.CIDADE (ID, ESTADO_ID, DESCR, IBGE_CIDADE, CODIGOTOM, VERSION, CEP_INICIAL, CEP_FINAL, DM_FATO_GERADOR_RET_ISS) \n"
               string_sql += f"                VALUES (CIDADE_SEQ.nextval , {ESTADO_ID}, '{CIDADE}' , {COD_IBGE} , {CODIGOTOM} , 1, '{MENOR_CEP}', '{MAIOR_CEP}', 0 ); \n"
               string_sql +=  "       EXCEPTION\n"
               string_sql +=  "           WHEN OTHERS THEN\n"
               string_sql += f"               RAISE_APPLICATION_ERROR(-{conta_erros}, 'Erro no script 77784.  Erro: ' || sqlerrm);\n"
               string_sql +=  "       END;  \n"
               string_sql +=  "   END IF ;\n"
            #   string_sql +=  "   \n"
            #    string_sql +=  "   \n"
            #    string_sql +=  "   \n"
            #    string_sql +=  "   \n"
            #    string_sql +=  "   \n"
            #    string_sql +=  " \n"
               
              
               string_sql += "END;\n/\n\n"
               if contador > 1000:
                   string_sql += "commit;\n/\n\n"
                   contador = 0

               print(string_sql)
               saida.writelines(string_sql)

        saida.close()
                    
except FileNotFoundError:
    print('Arquivo não achado')
