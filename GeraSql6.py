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
        HEADER += 'Prompt INI - Redmine #77329 Atualiza��o Base CEP - LIBERADO Release_2.9.8 , Patch_2.9.6.4 e Patch_2.9.7.1\n'
        HEADER += '-------------------------------------------------------------------------------------------------------------------------------------------\n'
        saida.writelines(HEADER)
        for linha in entrada:          
            if linha.find('COD_IBGE') != 7 :
                # cep	logradouro	tipo_logradouro	complemento	local	id_cidade	id_bairro
               registro =  linha.replace('"', '').split(";")
               COD_IBGE = registro[1]
               VERSAO = registro[2]
               MENOR_CEP = registro[3]
               MAIOR_CEP = registro[4]
               
               string_sql =   "-----------------------------------------------------------------------\n"
               string_sql += f"-- Realizando a atualizacao N� {conta_geral}\n"
               string_sql +=  "BEGIN\n"
               string_sql +=  "     UPDATE CSF_OWN.CIDADE N\n "
               string_sql += f"       SET N.CEP_INICIAL = '{MENOR_CEP}'\n"
               string_sql += f"          , N.CEP_FINAL   = '{MAIOR_CEP}'\n"
               string_sql += f"          , N.VERSION     = {VERSAO}\n"
               string_sql += f"      WHERE N.IBGE_CIDADE = {COD_IBGE} ;\n"
               string_sql +=  "EXCEPTION\n"
               string_sql +=  "    WHEN OTHERS THEN\n"
               string_sql += f"       RAISE_APPLICATION_ERROR(-{conta_erros}, 'Erro no script 77329.  Erro: ' || sqlerrm);\n"
               string_sql += "END;\n/\n"
     
               if conta_geral%100 == 0 :
                   string_sql += f"prompt  Commit point Reached at {conta_geral}\n"
                   string_sql +=  "commit;\n"
                   
               conta_geral += 1
               conta_erros += 1 
               
               print(string_sql)
               saida.writelines(string_sql)
        
        TRAILLER =  "commit;\n/\n"
        TRAILLER += '-------------------------------------------------------------------------------------------------------------------------------------------\n'
        TRAILLER += 'Prompt FIM - Redmine #77329 Atualiza��o Base CEP - LIBERADO Release_2.9.8 , Patch_2.9.6.4 e Patch_2.9.7.1\n'
        TRAILLER += '-------------------------------------------------------------------------------------------------------------------------------------------\n'
        saida.writelines(TRAILLER)
        saida.close()
                    
except FileNotFoundError:
    print('Arquivo n�o achado')
