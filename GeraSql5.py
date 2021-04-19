# -*- coding: cp1252 -*-
print ("-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=")
# nomeArq = input('Entre com o nome do arquivo a ser tratado :-> ' )

nomeArq = "dois.csv"

conta_erros=20001
conta_geral = 1
try:
    with open(nomeArq,'r+') as entrada:
        saida = open(nomeArq + ".sql", 'w')
        HEADER =  '-------------------------------------------------------------------------------------------------------------------------------------------\n'
        HEADER += 'Prompt INI - Redmine #77329 Atualização Base CEP - LIBERADO Release_2.9.8 , Patch_2.9.6.4 e Patch_2.9.7.1\n'
        HEADER += '-------------------------------------------------------------------------------------------------------------------------------------------\n'
        saida.writelines(HEADER)
        for linha in entrada:          
            if linha.find('ID_CIDADE') != 7 :
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
               string_sql =   "-----------------------------------------------------------------------\n"
               string_sql += f"-- Realizando a atualizacao Nº {conta_geral}\n"
               string_sql +=  "BEGIN\n"
               string_sql +=  "   BEGIN\n"
               string_sql +=  "       INSERT INTO  CSF_OWN.CIDADE (ID, ESTADO_ID, DESCR, IBGE_CIDADE, CODIGOTOM, VERSION, CEP_INICIAL, CEP_FINAL, DM_FATO_GERADOR_RET_ISS) \n"
               string_sql += f"         VALUES (CIDADE_SEQ.nextval , {ESTADO_ID}, '{CIDADE}' , {COD_IBGE} , {CODIGOTOM} , 1, '{MENOR_CEP}', '{MAIOR_CEP}', 0 ); \n"
               string_sql +=  "   EXCEPTION\n"
               string_sql +=  "      WHEN DUP_VAL_ON_INDEX THEN\n"
               string_sql +=  "         BEGIN\n"
               string_sql +=  "            UPDATE CSF_OWN.CIDADE N\n "
               string_sql += f"               SET N.CEP_INICIAL = '{MENOR_CEP}' \n"
               string_sql += f"                 , N.CEP_FINAL   = '{MAIOR_CEP}' \n"
               string_sql += f"                 , N.VERSION     = {VERSAO} \n"
               string_sql += f"             WHERE N.IBGE_CIDADE = {COD_IBGE}  ; \n"
               string_sql +=  "         EXCEPTION\n"
               string_sql +=  "            WHEN OTHERS THEN\n"
               string_sql += f"               RAISE_APPLICATION_ERROR(-{conta_erros}, 'Erro no script 77329.  Erro: ' || sqlerrm);\n"
               string_sql +=  "         END;\n"
               conta_erros += 1 
               string_sql +=  "      WHEN OTHERS THEN\n"
               string_sql += f"         RAISE_APPLICATION_ERROR(-{conta_erros}, 'Erro no script 77329.  Erro: ' || sqlerrm);\n"
               string_sql +=  "   END;\n"
               string_sql += "END;\n/\n\n"
               
               if conta_geral%100 == 0 :
                   string_sql += f"-- Commit point Reached at {conta_geral}\n"
                   string_sql +=  "commit;\n/\n\n"
                   
               conta_geral += 1 
               
               print(string_sql)
               saida.writelines(string_sql)
        
        TRAILLER =  "commit;\n/\n\n"
        TRAILLER += '-------------------------------------------------------------------------------------------------------------------------------------------\n'
        TRAILLER += 'Prompt TRAILLER - Redmine #77329 Atualização Base CEP - LIBERADO Release_2.9.8 , Patch_2.9.6.4 e Patch_2.9.7.1\n'
        TRAILLER += '-------------------------------------------------------------------------------------------------------------------------------------------\n'
        saida.writelines(TRAILLER)
        saida.close()
                    
except FileNotFoundError:
    print('Arquivo não achado')
