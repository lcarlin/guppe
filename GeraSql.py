# -*- coding: cp1252 -*-
print ("-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=")
## AM-tb14516.txt.ok
# nomeArq = input('Entre com o nome do arquivo a ser tratado :-> ' )
# estado = int(input('Entre com o estado que sera tratado nesse arquivo :-> '))
nomeArq = "AM-tb14516.txt.ok"
estado = 2

versao = 0 
conta_erros=20001
try:
    with open(nomeArq,'r+') as entrada:
        saida = open(nomeArq + ".sql", 'w')
        for linha in entrada:          
            if linha.find('versão=') == 0 :
                versao = int(linha.split("=")[1].split(" ")[0])
            else:
                registro = linha.split("|")
                ESTADO_ID = estado
                COD_REC = str(registro[0])
                DESC_COD = registro[1]
                DT_INI = " '"+registro[2][0:2]+"/"+registro[2][2:4]+"/"+registro[2][4:8]+"', "
                if len(registro[3]) == 1 :
                    DT_FIM = " NULL "
                else:
                     DT_FIM = "'"+registro[3][0:2]+'/'+registro[3][2:4]+"/"+registro[3][4:8]+"'"
                string_sql = "BEGIN\n"
                string_sql += "  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) \n "
                string_sql += "    VALUES (CODRECUF_SEQ.NEXTVAL, "
                string_sql += str(ESTADO_ID) +" , "
                string_sql += " '"+COD_REC+"' ,"
                string_sql += " '"+DESC_COD+"' ,"
                string_sql += DT_INI
                string_sql += DT_FIM +" , "
                string_sql += str(versao)+ " ); \n"
                string_sql += "EXCEPTION\n"
                string_sql += "    WHEN DUP_VAL_ON_INDEX THEN\n"
                string_sql += "       BEGIN\n"
                string_sql += "            UPDATE COD_REC_UF\n"
                string_sql += f"               SET DESC_COD  = '{DESC_COD}'\n"
                string_sql += f"                 , DT_FIM    = {DT_FIM}\n"
                string_sql += f"                 , VERSAO    = {versao}\n"
                string_sql += f"             WHERE ESTADO_ID = {ESTADO_ID}\n"
                string_sql += f"               AND COD_REC   = {COD_REC}\n"
                string_sql += f"                AND DT_INI   = {DT_INI}\n"
                string_sql += "       EXCEPTION\n"
                string_sql += "          WHEN OTHERS THEN\n"
                string_sql += f"            RAISE_APPLICATION_ERROR(-{conta_erros}, 'Erro no script 77784.  Erro: ' || sqlerrm) ;\n"
                string_sql += "        END;\n"
                string_sql += "   WHEN OTHERS THEN\n"
                conta_erros += 1 
                string_sql += f"       RAISE_APPLICATION_ERROR(-{conta_erros}, 'Erro no script 77784.  Erro: ' || sqlerrm);\n"
                string_sql += "END;\n/\n\n"
                conta_erros += 1 
                print(string_sql)
                saida.write(string_sql + "\n")
        saida.close()
except FileNotFoundError:
    print('Arquivo não achado')
