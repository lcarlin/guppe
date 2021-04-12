BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1303' , '1303 ICMS - INSUMO IND. ESTRANG. C/ REDUCAO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1303 ICMS - INSUMO IND. ESTRANG. C/ REDUCAO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1303
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20001, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20002, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1304' , '1304 ICMS - CORREDOR DE IMPORTACAO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1304 ICMS - CORREDOR DE IMPORTACAO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1304
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20003, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20004, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1305' , '1305 ICMS - ANTECIPADO DECLARADO - COMERCIO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1305 ICMS - ANTECIPADO DECLARADO - COMERCIO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1305
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20005, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20006, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1306' , '1306 ICMS - ANTECIPADO DECLARADO - INDUSTRIA' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1306 ICMS - ANTECIPADO DECLARADO - INDUSTRIA'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1306
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20007, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20008, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1307' , '1307 ICMS - ANTECIPADO DECLARADO - DIFERENCA' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1307 ICMS - ANTECIPADO DECLARADO - DIFERENCA'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1307
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20009, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20010, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1308' , '1308 ICMS - INSUMO INDUSTRIAL ESTRANGEIRO C/ RED. 55%' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1308 ICMS - INSUMO INDUSTRIAL ESTRANGEIRO C/ RED. 55%'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1308
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20011, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20012, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1309' , '1309 ICMS - DECLARADO - SUBSTITUICAO TRIBUTARIA' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1309 ICMS - DECLARADO - SUBSTITUICAO TRIBUTARIA'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1309
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20013, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20014, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1310' , '1310 ICMS - INDUSTRIA INCENTIVADA - COMPLEMENTO MEDIA MOVEL' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1310 ICMS - INDUSTRIA INCENTIVADA - COMPLEMENTO MEDIA MOVEL'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1310
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20015, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20016, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1311' , '1311 ICMS - INSUMO IND. ESTRANGEIRO-BEM FINAL-CE 100%' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1311 ICMS - INSUMO IND. ESTRANGEIRO-BEM FINAL-CE 100%'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1311
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20017, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20018, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1312' , '1312 ICMS - PNEUMATICOS, CAMARAS DE AR E PROTETORES DE BORRACHAS IMPORTADAS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1312 ICMS - PNEUMATICOS, CAMARAS DE AR E PROTETORES DE BORRACHAS IMPORTADAS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1312
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20019, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20020, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1313' , '1313 ICMS - REFRIGERANTE E EXTRATO CONCENTRADO PRE-MIX E POST-MIX' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1313 ICMS - REFRIGERANTE E EXTRATO CONCENTRADO PRE-MIX E POST-MIX'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1313
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20021, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20022, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1314' , '1314 ICMS - IMPORTACAO CORREDOR / USO PROPRIO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1314 ICMS - IMPORTACAO CORREDOR / USO PROPRIO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1314
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20023, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20024, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1315' , '1315 ICMS - AUTOMOVEIS DE LUXO E MOTOS ACIMA DE 180 CC' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1315 ICMS - AUTOMOVEIS DE LUXO E MOTOS ACIMA DE 180 CC'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1315
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20025, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20026, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1316' , '1316 ICMS - MERCADORIA NACIONAL' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1316 ICMS - MERCADORIA NACIONAL'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1316
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20027, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20028, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1317' , '1317 ICMS - NORMAL COMERCIO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1317 ICMS - NORMAL COMERCIO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1317
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20029, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20030, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1318' , '1318 ICMS - INSUMO INDUSTRIAL ESTRANGEIRO MI & EPPI' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1318 ICMS - INSUMO INDUSTRIAL ESTRANGEIRO MI & EPPI'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1318
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20031, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20032, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1319' , '1319 ICMS - MALHA FISCAL' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1319 ICMS - MALHA FISCAL'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1319
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20033, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20034, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1320' , '1320 ICMS - INSUMO INDUSTRIAL NACIONAL, INDUSTRIA NAO INCENTIVADA' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1320 ICMS - INSUMO INDUSTRIAL NACIONAL, INDUSTRIA NAO INCENTIVADA'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1320
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20035, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20036, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1321' , '1321 ICMS - VENDAS A PRAZO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1321 ICMS - VENDAS A PRAZO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1321
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20037, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20038, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1322' , '1322 ICMS - ATIVO FIXO NAC.- INDUSTRIA' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1322 ICMS - ATIVO FIXO NAC.- INDUSTRIA'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1322
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20039, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20040, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1323' , '1323 ICMS - INSUMO INDUSTRIAL ESTRANGEIRO C/ RED. 60%' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1323 ICMS - INSUMO INDUSTRIAL ESTRANGEIRO C/ RED. 60%'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1323
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20041, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20042, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1324' , '1324 ICMS - DIFERIDO ALIMENTACAO (IND. INCENTIVADA)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1324 ICMS - DIFERIDO ALIMENTACAO (IND. INCENTIVADA)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1324
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20043, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20044, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1325' , '1325 ICMS - DIFERENCA CESTA BASICA' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1325 ICMS - DIFERENCA CESTA BASICA'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1325
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20045, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20046, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1326' , '1326 ICMS - MERCADORIA ESTRANGEIRA COMERCIALIZACAO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1326 ICMS - MERCADORIA ESTRANGEIRA COMERCIALIZACAO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1326
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20047, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20048, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1327' , '1327 ICMS - SUBSTITUICAO TRIBUTARIA TRANSPORTES' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1327 ICMS - SUBSTITUICAO TRIBUTARIA TRANSPORTES'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1327
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20049, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20050, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1328' , '1328 ICMS - IMPLEMENTOS AGRICOLAS E EQPTOS. INDUSTRIAIS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1328 ICMS - IMPLEMENTOS AGRICOLAS E EQPTOS. INDUSTRIAIS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1328
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20051, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20052, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1329' , '1329 ICMS - FARINHA DE TRIGO E SEMOLINA - IMPORTADO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1329 ICMS - FARINHA DE TRIGO E SEMOLINA - IMPORTADO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1329
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20053, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20054, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1330' , '1330 ICMS - DIFERENCA DE ALIQUOTA NAO NOTIFICADA' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1330 ICMS - DIFERENCA DE ALIQUOTA NAO NOTIFICADA'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1330
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20055, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20056, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1331' , '1331 ICMS - CONHEC.TRANSP.ST TINTAS VERNIZES' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1331 ICMS - CONHEC.TRANSP.ST TINTAS VERNIZES'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1331
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20057, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20058, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1332' , '1332 ICMS - INSUMO INDUSTRIAL ESTRANGEIRO, INDUSTRIA NAO INCENTIVADA' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1332 ICMS - INSUMO INDUSTRIAL ESTRANGEIRO, INDUSTRIA NAO INCENTIVADA'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1332
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20059, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20060, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1333' , '1333 ICMS - ESTIMATIVA FIXA' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1333 ICMS - ESTIMATIVA FIXA'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1333
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20061, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20062, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1334' , '1334 ICMS - NAO RESTITUIVEL' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1334 ICMS - NAO RESTITUIVEL'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1334
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20063, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20064, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1335' , '1335 ICMS - INDUSTRIA NAO INCENTIVADA' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1335 ICMS - INDUSTRIA NAO INCENTIVADA'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1335
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20065, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20066, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1336' , '1336 ICMS - ESTIMATIVA FIXA EPPC' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1336 ICMS - ESTIMATIVA FIXA EPPC'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1336
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20067, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20068, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1337' , '1337 ICMS - FORNECEDORES PREFEITURA DE MANAUS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1337 ICMS - FORNECEDORES PREFEITURA DE MANAUS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1337
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20069, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20070, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1338' , '1338 ICMS - DIFERENCA DE ICMS TRANSPORTE' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1338 ICMS - DIFERENCA DE ICMS TRANSPORTE'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1338
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20071, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20072, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1339' , '1339 ICMS - DIFERENCA DE APURACAO-RECOLHIMENTO ESPONTANEO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1339 ICMS - DIFERENCA DE APURACAO-RECOLHIMENTO ESPONTANEO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1339
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20073, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20074, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1340' , '1340 ICMS - MEDICAMENTOS-NACIONAL' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1340 ICMS - MEDICAMENTOS-NACIONAL'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1340
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20075, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20076, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1341' , '1341 ICMS - DIFERIDO A RECOLHER (PRODUTOS AGRICOLAS)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1341 ICMS - DIFERIDO A RECOLHER (PRODUTOS AGRICOLAS)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1341
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20077, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20078, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1342' , '1342 ICMS - JOIAS, ARMAS E MUNIC.TRANSF/CERV E CHOPP' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1342 ICMS - JOIAS, ARMAS E MUNIC.TRANSF/CERV E CHOPP'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1342
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20079, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20080, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1343' , '1343 ICMS - DIFERENCA ESTIMATIVA FIXA' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1343 ICMS - DIFERENCA ESTIMATIVA FIXA'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1343
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20081, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20082, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1344' , '1344 ICMS - COMPONENTES e BENS DE INFORMATICA' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1344 ICMS - COMPONENTES e BENS DE INFORMATICA'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1344
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20083, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20084, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1345' , '1345 ICMS - BEBIDAS ALCOOLICAS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1345 ICMS - BEBIDAS ALCOOLICAS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1345
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20085, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20086, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1346' , '1346 ICMS - DIFERENCA DE DIESIL TRANSPORTE COLETIVO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1346 ICMS - DIFERENCA DE DIESIL TRANSPORTE COLETIVO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1346
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20087, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20088, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1347' , '1347 ICMS - CESTA BASICA 1%' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1347 ICMS - CESTA BASICA 1%'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1347
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20089, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20090, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1348' , '1348 ICMS - DIFERENCA ICMS S/ VEICULOS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1348 ICMS - DIFERENCA ICMS S/ VEICULOS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1348
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20091, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20092, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1349' , '1349 ICMS - PRODUTOS FARMACEUTICOS E MEDICAMENTOS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1349 ICMS - PRODUTOS FARMACEUTICOS E MEDICAMENTOS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1349
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20093, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20094, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1350' , '1350 ICMS - SUBSTITUICAO - RETIDO NA FONTE' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1350 ICMS - SUBSTITUICAO - RETIDO NA FONTE'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1350
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20095, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20096, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1351' , '1351 ICMS - ESTORNO DE CREDITO APROPRIADO EM ENTRADA INCENTIVADA' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1351 ICMS - ESTORNO DE CREDITO APROPRIADO EM ENTRADA INCENTIVADA'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1351
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20097, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20098, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1352' , '1352 ICMS - SUBSTITUICAO TRIBUTARIA - IMPORTADOS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1352 ICMS - SUBSTITUICAO TRIBUTARIA - IMPORTADOS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1352
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20099, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20100, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1353' , '1353 ICMS - CIMENTO ESTRANGEIRO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1353 ICMS - CIMENTO ESTRANGEIRO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1353
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20101, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20102, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1354' , '1354 ICMS - DIFERENCA DE ALIQUOTA' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1354 ICMS - DIFERENCA DE ALIQUOTA'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1354
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20103, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20104, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1355' , '1355 ICMS - ALIQUOTA 5%' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1355 ICMS - ALIQUOTA 5%'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1355
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20105, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20106, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1356' , '1356 ICMS - CONHEC. NF-PNEUS P/ AUTOMOVEIS DE PASSAGEIROS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1356 ICMS - CONHEC. NF-PNEUS P/ AUTOMOVEIS DE PASSAGEIROS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1356
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20107, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20108, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1357' , '1357 ICMS - CONHEC. NF-PNEUS DE CAMINHOES' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1357 ICMS - CONHEC. NF-PNEUS DE CAMINHOES'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1357
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20109, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20110, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1358' , '1358 ICMS - CONHEC. NF-PNEUS DE MOTOCICLETAS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1358 ICMS - CONHEC. NF-PNEUS DE MOTOCICLETAS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1358
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20111, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20112, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1359' , '1359 ICMS - CONHEC. NF-PROTETORES, CAMARAS E OUTROS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1359 ICMS - CONHEC. NF-PROTETORES, CAMARAS E OUTROS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1359
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20113, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20114, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1360' , '1360 ICMS - ESTORNO DE CREDITO ALCOOL ANIDRO E BIODIESEL' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1360 ICMS - ESTORNO DE CREDITO ALCOOL ANIDRO E BIODIESEL'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1360
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20115, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20116, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1361' , '1361 ICMS - SUBSTITUICAO TRIBUTARIA TRANSPORTES (IND. INCENTIVADA)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1361 ICMS - SUBSTITUICAO TRIBUTARIA TRANSPORTES (IND. INCENTIVADA)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1361
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20117, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20118, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1362' , '1362 ICMS - OUTRAS MERCADORIAS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1362 ICMS - OUTRAS MERCADORIAS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1362
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20119, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20120, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1363' , '1363 ICMS - CARNES E VISCERAS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1363 ICMS - CARNES E VISCERAS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1363
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20121, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20122, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1364' , '1364 ICMS - CONSTRUCAO CIVIL (EXCETO CIMENTO)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1364 ICMS - CONSTRUCAO CIVIL (EXCETO CIMENTO)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1364
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20123, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20124, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1365' , '1365 ICMS - INSUMO INDUSTRIAL DE COMPONENTES SEM REDUCAO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1365 ICMS - INSUMO INDUSTRIAL DE COMPONENTES SEM REDUCAO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1365
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20125, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20126, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1366' , '1366 ICMS - MERCADORIAS ESTRANGEIRAS INTERNADAS-CORREDOR' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1366 ICMS - MERCADORIAS ESTRANGEIRAS INTERNADAS-CORREDOR'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1366
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20127, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20128, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1367' , '1367 ICMS - FORNECEDORES DO ESTADO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1367 ICMS - FORNECEDORES DO ESTADO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1367
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20129, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20130, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1368' , '1368 ICMS - PRODUTOS IN NATURA' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1368 ICMS - PRODUTOS IN NATURA'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1368
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20131, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20132, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1369' , '1369 ICMS - DIFERENCA DE ICMS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1369 ICMS - DIFERENCA DE ICMS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1369
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20133, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20134, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1370' , '1370 ICMS - SUBSTITUICAO TRIBUTARIA LEI 2390/96 E 2826/04' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1370 ICMS - SUBSTITUICAO TRIBUTARIA LEI 2390/96 E 2826/04'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1370
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20135, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20136, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1371' , '1371 ICMS - EXCESSO QUOTA LCD' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1371 ICMS - EXCESSO QUOTA LCD'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1371
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20137, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20138, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1372' , '1372 ICMS - SIMPLES NACIONAL' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1372 ICMS - SIMPLES NACIONAL'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1372
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20139, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20140, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1373' , '1373 ICMS - COMUNICACAO  CREDITO ON LINE' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1373 ICMS - COMUNICACAO  CREDITO ON LINE'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1373
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20141, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20142, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1374' , '1374 ICMS - DESPESAS ADUANEIRAS MERCADORIA ESTRANGEIRA P/ COMERCIALIZACAO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1374 ICMS - DESPESAS ADUANEIRAS MERCADORIA ESTRANGEIRA P/ COMERCIALIZACAO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1374
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20143, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20144, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1375' , '1375 ICMS - DESPESAS ADUANEIRAS MERCADORIA ESTRANGEIRA INSUMO INDUSTRIAL' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1375 ICMS - DESPESAS ADUANEIRAS MERCADORIA ESTRANGEIRA INSUMO INDUSTRIAL'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1375
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20145, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20146, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1376' , '1376 ICMS - PNEUS IMPORTADOS P / AUTOMOVEIS DE PASSAGEIROS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1376 ICMS - PNEUS IMPORTADOS P / AUTOMOVEIS DE PASSAGEIROS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1376
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20147, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20148, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1377' , '1377 ICMS - PNEUS IMPORTADOS P / CAMINHOES, ONIBUS, AVIOES, ETC' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1377 ICMS - PNEUS IMPORTADOS P / CAMINHOES, ONIBUS, AVIOES, ETC'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1377
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20149, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20150, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1378' , '1378 ICMS - PNEUS IMPORTADOS P/ MOTOCICLETA' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1378 ICMS - PNEUS IMPORTADOS P/ MOTOCICLETA'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1378
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20151, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20152, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1379' , '1379 ICMS - PROTETORES, CAMARAS DE AR IMPORTADAS E OUTROS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1379 ICMS - PROTETORES, CAMARAS DE AR IMPORTADAS E OUTROS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1379
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20153, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20154, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1380' , '1380 ICMS - SUBSTITUICAO TRIBUTARIA NOTIFICADOS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1380 ICMS - SUBSTITUICAO TRIBUTARIA NOTIFICADOS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1380
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20155, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20156, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1381' , '1381 ICMS - CONHECIMENTO DE TRANSPORTE - PRECO FOB' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1381 ICMS - CONHECIMENTO DE TRANSPORTE - PRECO FOB'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1381
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20157, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20158, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1382' , '1382 ICMS - NORMAL TRANSPORTE' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1382 ICMS - NORMAL TRANSPORTE'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1382
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20159, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20160, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1383' , '1383 ICMS - NORMAL MINERAIS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1383 ICMS - NORMAL MINERAIS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1383
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20161, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20162, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1384' , '1384 ICMS - PARCELADO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1384 ICMS - PARCELADO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1384
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20163, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20164, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1385' , '1385 ICMS - NORMAL ENERGIA ELETRICA' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1385 ICMS - NORMAL ENERGIA ELETRICA'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1385
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20165, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20166, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1386' , '1386 ICMS - NORMAL COMUNICACAO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1386 ICMS - NORMAL COMUNICACAO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1386
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20167, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20168, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1387' , '1387 ICMS - NORMAL COMBUSTIVEIS E LUBRIFICANTES' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1387 ICMS - NORMAL COMBUSTIVEIS E LUBRIFICANTES'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1387
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20169, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20170, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1388' , '1388 ICMS - PRODUTOS ESTRANGEIROS - ATIVO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1388 ICMS - PRODUTOS ESTRANGEIROS - ATIVO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1388
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20171, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20172, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1389' , '1389 ICMS - MERCADORIA ESTRANGEIRA P/ CONSUMO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1389 ICMS - MERCADORIA ESTRANGEIRA P/ CONSUMO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1389
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20173, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20174, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1390' , '1390 ICMS - INSUMO INDUSTRIAL ESTRANGEIRO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1390 ICMS - INSUMO INDUSTRIAL ESTRANGEIRO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1390
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20175, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20176, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1391' , '1391 ICMS - RETENCAO EM OUTROS ESTADOS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1391 ICMS - RETENCAO EM OUTROS ESTADOS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1391
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20177, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20178, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1392' , '1392 ICMS - OUTROS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1392 ICMS - OUTROS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1392
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20179, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20180, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1393' , '1393 ICMS - CONHEC. NF-RACAO ANIMAL PET' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1393 ICMS - CONHEC. NF-RACAO ANIMAL PET'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1393
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20181, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20182, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1394' , '1394 ICMS - ESTORNO DE CREDITO APROPRIADO EM SAIDA INCENTIVADA' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1394 ICMS - ESTORNO DE CREDITO APROPRIADO EM SAIDA INCENTIVADA'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1394
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20183, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20184, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1395' , '1395 ICMS - NAO INSCRITOS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1395 ICMS - NAO INSCRITOS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1395
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20185, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20186, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1396' , '1396 ICMS - COMUNICACAO (TRIBUTACAO DEFINITIVA)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1396 ICMS - COMUNICACAO (TRIBUTACAO DEFINITIVA)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1396
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20187, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20188, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1397' , '1397 ICMS - ARMAS, EMBARCACOES DE LAZER E OUTROS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1397 ICMS - ARMAS, EMBARCACOES DE LAZER E OUTROS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1397
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20189, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20190, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1398' , '1398 ICMS - MERCADORIA ESTRANGEIRA - LEI HANNAN 7%' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1398 ICMS - MERCADORIA ESTRANGEIRA - LEI HANNAN 7%'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1398
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20191, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20192, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1399' , '1399 ICMS - AUTO DE APREENSAO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1399 ICMS - AUTO DE APREENSAO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1399
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20193, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20194, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1400' , '1400 ICMS - AUTO DE INFRACAO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1400 ICMS - AUTO DE INFRACAO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1400
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20195, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20196, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1401' , '1401 ICMS - PARCELADO - AUTOS DE INFRACAO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1401 ICMS - PARCELADO - AUTOS DE INFRACAO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1401
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20197, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20198, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1402' , '1402 AIR (AUTO DE INFRACAO)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1402 AIR (AUTO DE INFRACAO)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1402
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20199, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20200, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1403' , '1403 AIR (AUTO DE INFRACAO - PARCELAMENTO)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1403 AIR (AUTO DE INFRACAO - PARCELAMENTO)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1403
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20201, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20202, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1499' , '1499 OUTRAS INFRACOES' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1499 OUTRAS INFRACOES'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1499
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20203, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20204, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5121' , '5121 COTA-PARTE ESTADO CORRECAO MONET DIV ATIVA ICMS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5121 COTA-PARTE ESTADO CORRECAO MONET DIV ATIVA ICMS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5121
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20205, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20206, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5122' , '5122 CORRECAO MONETARIA - AUTO DE INFRACAO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5122 CORRECAO MONETARIA - AUTO DE INFRACAO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5122
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20207, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20208, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5123' , '5123 COTA-PARTE DO ESTADO - CORRECAO MONETARIA DO ICMS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5123 COTA-PARTE DO ESTADO - CORRECAO MONETARIA DO ICMS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5123
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20209, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20210, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5125' , '5125 CORRECAO MONETARIA SOBRE AIR' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5125 CORRECAO MONETARIA SOBRE AIR'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5125
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20211, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20212, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5126' , '5126 CORRECAO MONETARIA - AUTO DE APREENSAO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5126 CORRECAO MONETARIA - AUTO DE APREENSAO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5126
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20213, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20214, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5128' , '5128 COTA-PARTE ESTADO CORRECAO MONET DIV ATIVA AINF' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5128 COTA-PARTE ESTADO CORRECAO MONET DIV ATIVA AINF'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5128
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20215, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20216, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5130' , '5130 CORRECAO MONETARIA SOBRE O FMPES' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5130 CORRECAO MONETARIA SOBRE O FMPES'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5130
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20217, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20218, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5131' , '5131 CORRECAO MONET DA CONTRIB PARCELAMENTO-FMPES' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5131 CORRECAO MONET DA CONTRIB PARCELAMENTO-FMPES'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5131
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20219, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20220, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5132' , '5132 CORRECAO MONET DA CONTRIB FTI S / IMPORT E COMERCIALIZACAO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5132 CORRECAO MONET DA CONTRIB FTI S / IMPORT E COMERCIALIZACAO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5132
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20221, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20222, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5133' , '5133 CORRECAO MONET DA CONTRIB FTI S / FAT BRUTO INDUSTRIA LEI 2390/96' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5133 CORRECAO MONET DA CONTRIB FTI S / FAT BRUTO INDUSTRIA LEI 2390/96'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5133
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20223, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20224, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5134' , '5134 CORRECAO MONET DA CONTRIB FTI S / FAT BRUTO INDUSTRIA (EXP. E DIVERSIF.).' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5134 CORRECAO MONET DA CONTRIB FTI S / FAT BRUTO INDUSTRIA (EXP. E DIVERSIF.).'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5134
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20225, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20226, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5135' , '5135 CORRECAO MONET DA CONTRIB FTI S / ACORDO COM GOVERNO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5135 CORRECAO MONET DA CONTRIB FTI S / ACORDO COM GOVERNO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5135
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20227, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20228, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5136' , '5136 CORRECAO MONET DA CONTRIB FTI / IMPORT INSUMOS INDUSTRIAIS BEM FINAIS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5136 CORRECAO MONET DA CONTRIB FTI / IMPORT INSUMOS INDUSTRIAIS BEM FINAIS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5136
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20229, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20230, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5137' , '5137 CORRECAO MONETARIA DA CONTRIBUICAO - FMPES - 50%' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5137 CORRECAO MONETARIA DA CONTRIBUICAO - FMPES - 50%'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5137
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20231, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20232, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5231' , '5231 COTA-PARTE DO ESTADO - MULTAS DO ICMS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5231 COTA-PARTE DO ESTADO - MULTAS DO ICMS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5231
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20233, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20234, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5232' , '5232 COTA-PARTE DO ESTADO - MULTAS DA DIVIDA ATIVA DO ICMS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5232 COTA-PARTE DO ESTADO - MULTAS DA DIVIDA ATIVA DO ICMS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5232
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20235, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20236, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5246' , '5246 MULTAS SOBRE FMPES - 50%' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5246 MULTAS SOBRE FMPES - 50%'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5246
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20237, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20238, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5248' , '5248 MULTAS SOBRE O FMPES' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5248 MULTAS SOBRE O FMPES'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5248
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20239, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20240, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5249' , '5249 MULTAS SOBRE O PARCELAMENTO - FMPES' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5249 MULTAS SOBRE O PARCELAMENTO - FMPES'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5249
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20241, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20242, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5251' , '5251 MULTAS DO FTI S/ IMPORTACAO E COMERCIALIZACAO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5251 MULTAS DO FTI S/ IMPORTACAO E COMERCIALIZACAO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5251
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20243, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20244, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5252' , '5252 MULTAS DO FTI S/ FATURAMENTO BRUTO INDUSTRIA LEI 2390/96' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5252 MULTAS DO FTI S/ FATURAMENTO BRUTO INDUSTRIA LEI 2390/96'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5252
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20245, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20246, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5253' , '5253 MULTAS DO FTI S/ FAT. BRUTO INDUSTRIA EXPANSAO E DIVERSIFICACAO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5253 MULTAS DO FTI S/ FAT. BRUTO INDUSTRIA EXPANSAO E DIVERSIFICACAO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5253
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20247, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20248, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5254' , '5254 MULTAS DO FTI S/ ACORDO C/ GOVERNO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5254 MULTAS DO FTI S/ ACORDO C/ GOVERNO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5254
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20249, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20250, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5255' , '5255 MULTAS DO FTI S/ IMPORTACAO INSUMOS INDUSTRIAIS BEM FINAL (2%)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5255 MULTAS DO FTI S/ IMPORTACAO INSUMOS INDUSTRIAIS BEM FINAL (2%)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5255
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20251, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20252, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5256' , '5256 MULTA DA CONTRIBUICAO P/ U.E. A - P&D' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5256 MULTA DA CONTRIBUICAO P/ U.E. A - P&D'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5256
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20253, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20254, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5257' , '5257 MULTA DA CONTRIBUICAO P/ U.E. A - LEI 1939/89' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5257 MULTA DA CONTRIBUICAO P/ U.E. A - LEI 1939/89'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5257
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20255, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20256, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5258' , '5258 MULTA DA CONTRIBUICAO P/ U.E. A - LEI 2390/96' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5258 MULTA DA CONTRIBUICAO P/ U.E. A - LEI 2390/96'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5258
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20257, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20258, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5511' , '5511 MULTA POR DESCUMPRIMENTO DE OBRIGACAO ACESSORIA' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5511 MULTA POR DESCUMPRIMENTO DE OBRIGACAO ACESSORIA'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5511
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20259, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20260, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5513' , '5513 MULTAS - AUTO DE APREENSAO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5513 MULTAS - AUTO DE APREENSAO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5513
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20261, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20262, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5514' , '5514 MULTAS - AUTO DE INFRACAO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5514 MULTAS - AUTO DE INFRACAO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5514
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20263, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20264, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5515' , '5515 MULTAS - AINF (DIV. ATIVA - INSCRITO)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5515 MULTAS - AINF (DIV. ATIVA - INSCRITO)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5515
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20265, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20266, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5516' , '5516 MULTAS - AINF PARCELADO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5516 MULTAS - AINF PARCELADO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5516
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20267, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20268, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5517' , '5517 MULTAS - AINF (DIV. ATIVA - AJUIZADO)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5517 MULTAS - AINF (DIV. ATIVA - AJUIZADO)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5517
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20269, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20270, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5518' , '5518 MULTAS - PARC. AINF (DIV. ATIVA - INSCRITO)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5518 MULTAS - PARC. AINF (DIV. ATIVA - INSCRITO)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5518
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20271, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20272, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5519' , '5519 MULTAS - PARC. AINF (DIV. ATIVA - AJUIZADA)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5519 MULTAS - PARC. AINF (DIV. ATIVA - AJUIZADA)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5519
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20273, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20274, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5520' , '5520 MULTAS - PARCELAMENTO DA DIV. ATIVA (AINF - INSCRITO)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5520 MULTAS - PARCELAMENTO DA DIV. ATIVA (AINF - INSCRITO)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5520
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20275, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20276, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5521' , '5521 MULTAS - PARCELAMENTO DA DIV. ATIVA (AINF - AJUIZADO)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5521 MULTAS - PARCELAMENTO DA DIV. ATIVA (AINF - AJUIZADO)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5521
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20277, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20278, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5555' , '5555 COTA-PARTE DO ESTADO - JUROS DE MORA DO ICMS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5555 COTA-PARTE DO ESTADO - JUROS DE MORA DO ICMS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5555
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20279, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20280, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5556' , '5556 COTA-PARTE DO ESTADO - JUROS DE MORA DO IPVA' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5556 COTA-PARTE DO ESTADO - JUROS DE MORA DO IPVA'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5556
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20281, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20282, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5557' , '5557 JUROS DO AIR' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5557 JUROS DO AIR'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5557
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20283, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20284, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5558' , '5558 JUROS - AUTO DE INFRACAO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5558 JUROS - AUTO DE INFRACAO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5558
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20285, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20286, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5559' , '5559 JUROS - AUTO DE APREENSAO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5559 JUROS - AUTO DE APREENSAO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5559
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20287, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20288, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5560' , '5560 JUROS DA DIVIDA ATIVA - AUTOS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5560 JUROS DA DIVIDA ATIVA - AUTOS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5560
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20289, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20290, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5571' , '5571 JUROS SOBRE O FMPES' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5571 JUROS SOBRE O FMPES'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5571
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20291, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20292, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5572' , '5572 JUROS SOBRE PARCELAMENTO DO FMPES' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5572 JUROS SOBRE PARCELAMENTO DO FMPES'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5572
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20293, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20294, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5573' , '5573 JUROS DO FTI S/ IMPORTACAO E COMERCIALIZACAO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5573 JUROS DO FTI S/ IMPORTACAO E COMERCIALIZACAO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5573
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20295, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20296, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5574' , '5574 JUROS DO FTI S/ FATURAMENTO BRUTO INDUSTRIA LEI 2390/96' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5574 JUROS DO FTI S/ FATURAMENTO BRUTO INDUSTRIA LEI 2390/96'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5574
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20297, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20298, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5575' , '5575 JUROS DO FTI S/ FATURAMENTO BRUTO INDUSTRIA EXPANSAO E DIVERSIFICACAO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5575 JUROS DO FTI S/ FATURAMENTO BRUTO INDUSTRIA EXPANSAO E DIVERSIFICACAO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5575
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20299, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20300, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5576' , '5576 JUROS DO FTI S/ ACORDO C/ GOVERNO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5576 JUROS DO FTI S/ ACORDO C/ GOVERNO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5576
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20301, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20302, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5577' , '5577 JUROS DO FTI S/ IMPORTACAO INSUMOS INDUSTRIAIS BEM FINAL(2%)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5577 JUROS DO FTI S/ IMPORTACAO INSUMOS INDUSTRIAIS BEM FINAL(2%)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5577
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20303, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20304, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5578' , '5578 JUROS SOBRE O FMPES - 50%' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5578 JUROS SOBRE O FMPES - 50%'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5578
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20305, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20306, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5579' , '5579 JUROS DIVERSOS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5579 JUROS DIVERSOS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5579
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20307, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20308, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5580' , '5580 JUROS DA CONTRIBUICAO P/ U.E.A P&D' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5580 JUROS DA CONTRIBUICAO P/ U.E.A P&D'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5580
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20309, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20310, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5581' , '5581 JUROS DA CONTRIBUICAO P/ U.E.A - LEI 1939/89' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5581 JUROS DA CONTRIBUICAO P/ U.E.A - LEI 1939/89'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5581
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20311, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20312, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5582' , '5582 JUROS DA CONTRIBUICAO P/ U.E.A - LEI 2390/96' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5582 JUROS DA CONTRIBUICAO P/ U.E.A - LEI 2390/96'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5582
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20313, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20314, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5771' , '5771 DIVIDA ATIVA - ICMS NORMAL (INCRITO)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5771 DIVIDA ATIVA - ICMS NORMAL (INCRITO)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5771
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20315, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20316, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5772' , '5772 DIVIDA ATIVA - ICMS ANTECIPADO (INSCRITO)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5772 DIVIDA ATIVA - ICMS ANTECIPADO (INSCRITO)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5772
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20317, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20318, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5773' , '5773 DIVIDA ATIVA - AINF LAVRADO ATE 30.11.89 (INSCRITO)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5773 DIVIDA ATIVA - AINF LAVRADO ATE 30.11.89 (INSCRITO)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5773
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20319, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20320, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5774' , '5774 DIVIDA ATIVA - AINF LAVRADO APOS 30.11.89 (INSCRITO)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5774 DIVIDA ATIVA - AINF LAVRADO APOS 30.11.89 (INSCRITO)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5774
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20321, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20322, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5775' , '5775 DIVIDA ATIVA - PARC. AINF LAVRADO ATE 30.11.89 (INSCRITO)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5775 DIVIDA ATIVA - PARC. AINF LAVRADO ATE 30.11.89 (INSCRITO)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5775
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20323, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20324, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5776' , '5776 DIVIDA ATIVA - PARC. AINF LAVRADO APOS 30.11.89 (INSCRITO)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5776 DIVIDA ATIVA - PARC. AINF LAVRADO APOS 30.11.89 (INSCRITO)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5776
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20325, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20326, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5777' , '5777 DIVIDA ATIVA - PARC. CONFISSAO (INSCRITO)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5777 DIVIDA ATIVA - PARC. CONFISSAO (INSCRITO)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5777
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20327, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20328, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5781' , '5781 DIVIDA ATIVA - ICMS NORMAL (AJUIZADO)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5781 DIVIDA ATIVA - ICMS NORMAL (AJUIZADO)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5781
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20329, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20330, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5782' , '5782 DIVIDA ATIVA - ICMS ANTECIPADO (AJUIZADO)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5782 DIVIDA ATIVA - ICMS ANTECIPADO (AJUIZADO)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5782
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20331, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20332, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5783' , '5783 DIVIDA ATIVA - AINF LAVRADO ATE' 30.11.89 (AJUIZADO)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5783 DIVIDA ATIVA - AINF LAVRADO ATE' 30.11.89 (AJUIZADO)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5783
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20333, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20334, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5784' , '5784 DIVIDA ATIVA - AINF LAVRADO APOS 30.11.89 (AJUIZADO)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5784 DIVIDA ATIVA - AINF LAVRADO APOS 30.11.89 (AJUIZADO)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5784
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20335, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20336, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5785' , '5785 DIVIDA ATIVA - PARC. AINF LAVRADO ATE' 30.11.89 (AJUIZADO)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5785 DIVIDA ATIVA - PARC. AINF LAVRADO ATE' 30.11.89 (AJUIZADO)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5785
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20337, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20338, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5786' , '5786 DIVIDA ATIVA - PARC. AINF LAVRADO APOS 30.11.89 (AJUIZADO)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5786 DIVIDA ATIVA - PARC. AINF LAVRADO APOS 30.11.89 (AJUIZADO)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5786
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20339, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20340, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '5787' , '5787 DIVIDA ATIVA - PARC. CONFISSAO (AJUIZADO)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '5787 DIVIDA ATIVA - PARC. CONFISSAO (AJUIZADO)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 5787
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20341, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20342, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '6401' , '6401 CONTRIBUICAO P/ U.E.A. - P&D' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '6401 CONTRIBUICAO P/ U.E.A. - P&D'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 6401
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20343, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20344, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '6402' , '6402 CONTRIBUICAO P/ U.E.A. - LEI 1939/89 (1,5% S/ ICMS RESTITUIVEL)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '6402 CONTRIBUICAO P/ U.E.A. - LEI 1939/89 (1,5% S/ ICMS RESTITUIVEL)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 6402
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20345, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20346, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '6403' , '6403 CONTRIBUICAO P/ U.E.A. - LEI 2390/96(10%S/ CRED. PRESUMIDO)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '6403 CONTRIBUICAO P/ U.E.A. - LEI 2390/96(10%S/ CRED. PRESUMIDO)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 6403
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20347, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20348, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '6404' , '6404 CONTRIBUICAO P/ U.E.A - LEI 2826/03 (10% S/CRED. ESTIMULO DE 100%)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '6404 CONTRIBUICAO P/ U.E.A - LEI 2826/03 (10% S/CRED. ESTIMULO DE 100%)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 6404
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20349, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20350, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '6405' , '6405 CONTRIBUICAO P/ U.E.A - LEI 2826/03 (1,3% S/ FAT. BRUTO - BEM INT)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '6405 CONTRIBUICAO P/ U.E.A - LEI 2826/03 (1,3% S/ FAT. BRUTO - BEM INT)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 6405
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20351, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20352, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '6406' , '6406 CONTRIBUICAO P/ U.E.A - LEI 2826/03 (1,5% S/ CREDITO ESTIMULO INF)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '6406 CONTRIBUICAO P/ U.E.A - LEI 2826/03 (1,5% S/ CREDITO ESTIMULO INF)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 6406
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20353, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20354, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '6407' , '6407 CONTRIBUICAO P/ U.E.A - LEI 2826/03 PARCELAMENTO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '6407 CONTRIBUICAO P/ U.E.A - LEI 2826/03 PARCELAMENTO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 6407
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20355, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20356, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '6408' , '6408 CONTRIBUICAO P/ INFRA-ESTRUTURA BASICA, ECONOMICA E SOCIAL' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '6408 CONTRIBUICAO P/ INFRA-ESTRUTURA BASICA, ECONOMICA E SOCIAL'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 6408
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20357, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20358, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9830' , '9830 ICMS - RESTITUIVEL' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9830 ICMS - RESTITUIVEL'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9830
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20359, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20360, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9850' , '9850 FTI - SOBRE IMPORTACAO E COMERCIALIZACAO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9850 FTI - SOBRE IMPORTACAO E COMERCIALIZACAO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9850
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20361, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20362, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9851' , '9851 FTI - FATURAMENTO BRUTO INDUSTRIAL 1%' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9851 FTI - FATURAMENTO BRUTO INDUSTRIAL 1%'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9851
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20363, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20364, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9852' , '9852 FTI - FATURAMENTO BRUTO INDUSTRIAL EXPANSAO E DIVERSIFICACAO - 1%' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9852 FTI - FATURAMENTO BRUTO INDUSTRIAL EXPANSAO E DIVERSIFICACAO - 1%'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9852
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20365, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20366, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9853' , '9853 FTI - SOBRE ACORDO C/ GOVERNO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9853 FTI - SOBRE ACORDO C/ GOVERNO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9853
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20367, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20368, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9854' , '9854 FTI - SOBRE IMPORTACAO INSUMOS INDUSTRIAIS BEM FINAL (2%) DO VALOR FOB' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9854 FTI - SOBRE IMPORTACAO INSUMOS INDUSTRIAIS BEM FINAL (2%) DO VALOR FOB'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9854
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20369, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20370, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9855' , '9855 FTI - FATURAMENTO BRUTO BEM INTERMEDIARIO DIFERIMENTO (1%)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9855 FTI - FATURAMENTO BRUTO BEM INTERMEDIARIO DIFERIMENTO (1%)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9855
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20371, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20372, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9856' , '9856 FTI - AQUISICAO DE INSUMOS NACIONAIS BEM FINAL (1%)' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9856 FTI - AQUISICAO DE INSUMOS NACIONAIS BEM FINAL (1%)'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9856
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20373, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20374, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9857' , '9857 FTI - PROJETOS AGROPECUARIOS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9857 FTI - PROJETOS AGROPECUARIOS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9857
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20375, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20376, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9858' , '9858 FTI - CONCENTRADOS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9858 FTI - CONCENTRADOS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9858
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20377, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20378, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9859' , '9859 FTI - LCD' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9859 FTI - LCD'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9859
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20379, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20380, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9860' , '9860 FTI - IMPORTACAO INSUMO INDUSTRIAL - DUAS RODAS - 3,5% DO VALOR FOB' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9860 FTI - IMPORTACAO INSUMO INDUSTRIAL - DUAS RODAS - 3,5% DO VALOR FOB'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9860
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20381, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20382, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9861' , '9861 FTI - FATURAMENTO BRUTO INDUSTRIAL - DUAS RODAS - 0,25%' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9861 FTI - FATURAMENTO BRUTO INDUSTRIAL - DUAS RODAS - 0,25%'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9861
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20383, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20384, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9862' , '9862 FTI - IMPORTACAO INSUMO INDUSTRIAL - ADICIONAL DUAS RODAS' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9862 FTI - IMPORTACAO INSUMO INDUSTRIAL - ADICIONAL DUAS RODAS'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9862
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20385, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20386, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9880' , '9880 FMPES - CONTRIBUICAO EXTRA-ORCAMENTARIA-AFEAM' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9880 FMPES - CONTRIBUICAO EXTRA-ORCAMENTARIA-AFEAM'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9880
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20387, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20388, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9881' , '9881 FMPES - PARCELAMENTO' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9881 FMPES - PARCELAMENTO'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9881
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20389, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20390, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9882' , '9882 FMPES - CONTRIBUICAO ORCAMENTARIA' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9882 FMPES - CONTRIBUICAO ORCAMENTARIA'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9882
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20391, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20392, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9883' , '9883 FMPES - EXERCICIOS ANTERIORES' , '01/01/2013', '31/05/2017' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9883 FMPES - EXERCICIOS ANTERIORES'
                 , DT_FIM    = '31/05/2017'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9883
                AND DT_INI   =  '01/01/2013', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20393, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20394, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1303' , '1303 ICMS – INSUMO IND. ESTRANG. C/ REDUCAO' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1303 ICMS – INSUMO IND. ESTRANG. C/ REDUCAO'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1303
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20395, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20396, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1304' , '1304 ICMS – CORREDOR DE IMPORTACAO' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1304 ICMS – CORREDOR DE IMPORTACAO'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1304
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20397, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20398, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1305' , '1305 ICMS – ANTECIPADO DECLARADO – COMERCIO' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1305 ICMS – ANTECIPADO DECLARADO – COMERCIO'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1305
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20399, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20400, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1306' , '1306 ICMS – ANTECIPADO DECLARADO – INDUSTRIA' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1306 ICMS – ANTECIPADO DECLARADO – INDUSTRIA'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1306
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20401, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20402, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1307' , '1307 ICMS – ANTECIPADO DECLARADO – DIFERENCA' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1307 ICMS – ANTECIPADO DECLARADO – DIFERENCA'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1307
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20403, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20404, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1308' , '1308 ICMS – INSUMO INDUSTRIAL ESTRANGEIRO C/ RED. 55%' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1308 ICMS – INSUMO INDUSTRIAL ESTRANGEIRO C/ RED. 55%'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1308
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20405, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20406, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1309' , '1309 ICMS – DECLARADO – SUBSTITUICAO TRIBUTARIA' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1309 ICMS – DECLARADO – SUBSTITUICAO TRIBUTARIA'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1309
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20407, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20408, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1310' , '1310 ICMS – INDUSTRIA INCENTIVADA – Complemento MEdia MOvel' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1310 ICMS – INDUSTRIA INCENTIVADA – Complemento MEdia MOvel'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1310
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20409, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20410, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1311' , '1311 ICMS – INSUMO INDUSTRIAL ESTRANGEIRO – BEM FINAL COM DIFERIMENTO' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1311 ICMS – INSUMO INDUSTRIAL ESTRANGEIRO – BEM FINAL COM DIFERIMENTO'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1311
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20411, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20412, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1312' , '1312 ICMS – DIFAL – OPERACAO – OUTRAS UFs P/ AMAZONAS' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1312 ICMS – DIFAL – OPERACAO – OUTRAS UFs P/ AMAZONAS'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1312
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20413, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20414, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1313' , '1313 ICMS – SUBSTITUICAO TRIBUTARIA NOTIFICADOS – B' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1313 ICMS – SUBSTITUICAO TRIBUTARIA NOTIFICADOS – B'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1313
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20415, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20416, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1314' , '1314 ICMS – IMPORTACAO CORREDOR / USO PROPRIO' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1314 ICMS – IMPORTACAO CORREDOR / USO PROPRIO'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1314
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20417, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20418, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1315' , '1315 ICMS – AERONAVES, PARTES E PECAS' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1315 ICMS – AERONAVES, PARTES E PECAS'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1315
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20419, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20420, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1316' , '1316 ICMS – MERCADORIA NACIONAL' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1316 ICMS – MERCADORIA NACIONAL'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1316
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20421, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20422, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1317' , '1317 ICMS – NORMAL COMERCIO' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1317 ICMS – NORMAL COMERCIO'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1317
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20423, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20424, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1318' , '1318 ICMS – INSUMO INDUSTRIAL ESTRANGEIRO MI & EPPI' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1318 ICMS – INSUMO INDUSTRIAL ESTRANGEIRO MI & EPPI'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1318
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20425, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20426, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1319' , '1319 ICMS – MALHA FISCAL' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1319 ICMS – MALHA FISCAL'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1319
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20427, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20428, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1320' , '1320 ICMS – INSUMO INDUSTRIAL NACIONAL, INDUSTRIA NAO INCENTIVADA' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1320 ICMS – INSUMO INDUSTRIAL NACIONAL, INDUSTRIA NAO INCENTIVADA'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1320
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20429, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20430, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1321' , '1321 ICMS – VENDAS A PRAZO' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1321 ICMS – VENDAS A PRAZO'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1321
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20431, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20432, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1322' , '1322 ICMS – ATIVO FIXO NAC.– INDUSTRIA' , '01/06/2017', '31/01/2019' , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1322 ICMS – ATIVO FIXO NAC.– INDUSTRIA'
                 , DT_FIM    = '31/01/2019'
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1322
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20433, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20434, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1323' , '1323 ICMS – INSUMO INDUSTRIAL ESTRANGEIRO C/ RED. 60%' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1323 ICMS – INSUMO INDUSTRIAL ESTRANGEIRO C/ RED. 60%'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1323
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20435, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20436, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1324' , '1324 ICMS – DIFERIDO ALIMENTACAO (IND. INCENTIVADA)' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1324 ICMS – DIFERIDO ALIMENTACAO (IND. INCENTIVADA)'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1324
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20437, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20438, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1325' , '1325 ICMS – DIFERENCA – SIMPLES NACIONAL' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1325 ICMS – DIFERENCA – SIMPLES NACIONAL'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1325
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20439, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20440, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1326' , '1326 ICMS – MERCADORIA ESTRANGEIRA COMERCIALIZACAO' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1326 ICMS – MERCADORIA ESTRANGEIRA COMERCIALIZACAO'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1326
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20441, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20442, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1327' , '1327 ICMS – SUBSTITUICAO TRIBUTARIA TRANSPORTES' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1327 ICMS – SUBSTITUICAO TRIBUTARIA TRANSPORTES'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1327
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20443, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20444, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1328' , '1328 ICMS – IMPLEMENTOS AGRICOLAS E EQPTOS. INDUSTRIAIS' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1328 ICMS – IMPLEMENTOS AGRICOLAS E EQPTOS. INDUSTRIAIS'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1328
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20445, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20446, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1329' , '1329 ICMS – GADO EM PE' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1329 ICMS – GADO EM PE'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1329
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20447, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20448, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1330' , '1330 ICMS – DIFERENCA DE ALIQUOTA NAO NOTIFICADA' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1330 ICMS – DIFERENCA DE ALIQUOTA NAO NOTIFICADA'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1330
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20449, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20450, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1331' , '1331 ICMS – FRETE FOB – DIFAL' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1331 ICMS – FRETE FOB – DIFAL'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1331
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20451, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20452, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1332' , '1332 ICMS – INSUMO INDUSTRIAL ESTRANGEIRO, INDUSTRIA NAO INCENTIVADA' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1332 ICMS – INSUMO INDUSTRIAL ESTRANGEIRO, INDUSTRIA NAO INCENTIVADA'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1332
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20453, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20454, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1333' , '1333 ICMS – ESTIMATIVA FIXA' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1333 ICMS – ESTIMATIVA FIXA'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1333
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20455, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20456, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1334' , '1334 ICMS – NAO RESTITUIVEL' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1334 ICMS – NAO RESTITUIVEL'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1334
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20457, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20458, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1335' , '1335 ICMS – INDUSTRIA NAO INCENTIVADA' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1335 ICMS – INDUSTRIA NAO INCENTIVADA'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1335
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20459, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20460, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1336' , '1336 ICMS – DIFAL – APURACAO – OUTRAS UFs P/ AMAZONAS' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1336 ICMS – DIFAL – APURACAO – OUTRAS UFs P/ AMAZONAS'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1336
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20461, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20462, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1337' , '1337 ICMS – FORNECEDORES PREFEITURA DE MANAUS' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1337 ICMS – FORNECEDORES PREFEITURA DE MANAUS'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1337
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20463, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20464, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1338' , '1338 ICMS – DIFERENCA DE ICMS TRANSPORTE' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1338 ICMS – DIFERENCA DE ICMS TRANSPORTE'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1338
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20465, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20466, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1339' , '1339 ICMS – DIFAL – SIMPLES NACIONAL' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1339 ICMS – DIFAL – SIMPLES NACIONAL'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1339
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20467, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20468, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1340' , '1340 ICMS – DOCUMENTOS AVULSOS' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1340 ICMS – DOCUMENTOS AVULSOS'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1340
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20469, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20470, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1341' , '1341 ICMS – DIFERIDO A RECOLHER (PRODUTOS AGRICOLAS)' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1341 ICMS – DIFERIDO A RECOLHER (PRODUTOS AGRICOLAS)'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1341
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20471, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20472, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1342' , '1342 ICMS – ANTECIPADO ALIQUOTAS DIFERENCIADAS' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1342 ICMS – ANTECIPADO ALIQUOTAS DIFERENCIADAS'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1342
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20473, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20474, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1343' , '1343 ICMS – DIFERENCA ESTIMATIVA FIXA' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1343 ICMS – DIFERENCA ESTIMATIVA FIXA'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1343
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20475, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20476, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1344' , '1344 ICMS – DESPESAS ADUANEIRAS – INDUSTRIA – OUTRAS AQUISICOES' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1344 ICMS – DESPESAS ADUANEIRAS – INDUSTRIA – OUTRAS AQUISICOES'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1344
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20477, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20478, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1345' , '1345 ICMS – ICMS – ANTECIPADO COM ACRESCIMO–INADIMPLENCIA–DE. 32.477/12' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1345 ICMS – ICMS – ANTECIPADO COM ACRESCIMO–INADIMPLENCIA–DE. 32.477/12'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1345
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20479, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20480, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1346' , '1346 ICMS – DIFERENCA DE DIESIL TRANSPORTE COLETIVO' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1346 ICMS – DIFERENCA DE DIESIL TRANSPORTE COLETIVO'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1346
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20481, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20482, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1347' , '1347 ICMS – CESTA BASICA 1%' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1347 ICMS – CESTA BASICA 1%'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1347
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20483, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20484, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1348' , '1348 ICMS – DIFERENCA ICMS S/ VEICULOS' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1348 ICMS – DIFERENCA ICMS S/ VEICULOS'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1348
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20485, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20486, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1349' , '1349 ICMS – CONHECIMENTO DE TRANSPORTE – PRECO FOB – B' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1349 ICMS – CONHECIMENTO DE TRANSPORTE – PRECO FOB – B'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1349
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20487, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20488, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1350' , '1350 ICMS – SUBSTITUICAO – RETIDO NA FONTE' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1350 ICMS – SUBSTITUICAO – RETIDO NA FONTE'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1350
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20489, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20490, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1351' , '1351 ICMS – ESTORNO DE CREDITO APROPRIADO EM ENTRADA INCENTIVADA' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1351 ICMS – ESTORNO DE CREDITO APROPRIADO EM ENTRADA INCENTIVADA'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1351
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20491, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20492, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1352' , '1352 ICMS – SUBSTITUICAO TRIBUTARIA – IMPORTADOS – A' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1352 ICMS – SUBSTITUICAO TRIBUTARIA – IMPORTADOS – A'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1352
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20493, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20494, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1353' , '1353 ICMS – SUBSTITUICAO TRIBUTARIA – IMPORTADOS – B' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1353 ICMS – SUBSTITUICAO TRIBUTARIA – IMPORTADOS – B'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1353
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20495, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20496, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1354' , '1354 ICMS – DIFERENCA DE ALIQUOTA' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1354 ICMS – DIFERENCA DE ALIQUOTA'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1354
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20497, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20498, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1355' , '1355 ICMS – ALIQUOTA 5%' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1355 ICMS – ALIQUOTA 5%'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1355
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20499, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20500, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1356' , '1356 ICMS – IMPORTACAO DE INSUMO INDUSTRIAL' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1356 ICMS – IMPORTACAO DE INSUMO INDUSTRIAL'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1356
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20501, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20502, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1357' , '1357 ICMS – GASOLINA IMPORTADO – PMPF' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1357 ICMS – GASOLINA IMPORTADO – PMPF'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1357
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20503, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20504, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1358' , '1358 ICMS – ST MERCADORIA NACIONALIZADA (4%) – B' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1358 ICMS – ST MERCADORIA NACIONALIZADA (4%) – B'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1358
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20505, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20506, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1359' , '1359 ICMS – ANTECIPADO TRANSFERENCIA DA CARNE, FRANGO E SUAS VISCERAS' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1359 ICMS – ANTECIPADO TRANSFERENCIA DA CARNE, FRANGO E SUAS VISCERAS'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1359
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20507, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20508, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1360' , '1360 ICMS – ESTORNO DE CREDITO ALCOOL ANIDRO E BIODIESEL' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1360 ICMS – ESTORNO DE CREDITO ALCOOL ANIDRO E BIODIESEL'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1360
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20509, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20510, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1361' , '1361 ICMS – SUBSTITUICAO TRIBUTARIA TRANSPORTES (IND. INCENTIVADA)' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1361 ICMS – SUBSTITUICAO TRIBUTARIA TRANSPORTES (IND. INCENTIVADA)'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1361
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20511, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20512, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1362' , '1362 ICMS – ENERGIA ELETRICA – PRODUCAO PROPRIA' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1362 ICMS – ENERGIA ELETRICA – PRODUCAO PROPRIA'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1362
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20513, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20514, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1363' , '1363 ICMS – CARNES E VISCERAS' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1363 ICMS – CARNES E VISCERAS'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1363
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20515, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20516, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1364' , '1364 ICMS – CARGA TRIBUTARIA 5%' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1364 ICMS – CARGA TRIBUTARIA 5%'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1364
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20517, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20518, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1365' , '1365 ICMS – INSUMO INDUSTRIAL DE COMPONENTES SEM REDUCAO' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1365 ICMS – INSUMO INDUSTRIAL DE COMPONENTES SEM REDUCAO'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1365
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20519, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20520, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1366' , '1366 ICMS – MERCADORIAS ESTRANGEIRAS INTERNADAS–CORREDOR' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1366 ICMS – MERCADORIAS ESTRANGEIRAS INTERNADAS–CORREDOR'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1366
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20521, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20522, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1367' , '1367 ICMS – FORNECEDORES DO ESTADO' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1367 ICMS – FORNECEDORES DO ESTADO'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1367
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20523, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20524, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1368' , '1368 ICMS – PRODUTOS IN NATURA' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1368 ICMS – PRODUTOS IN NATURA'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1368
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20525, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20526, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1369' , '1369 ICMS – DIFERENCA DE ICMS' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1369 ICMS – DIFERENCA DE ICMS'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1369
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20527, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20528, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1370' , '1370 ICMS – FRETE FOB – DIFAL NAO CONTRIBUINTE' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1370 ICMS – FRETE FOB – DIFAL NAO CONTRIBUINTE'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1370
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20529, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20530, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1371' , '1371 ICMS – EXCESSO QUOTA LCD' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1371 ICMS – EXCESSO QUOTA LCD'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1371
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20531, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20532, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1372' , '1372 ICMS – SIMPLES NACIONAL' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1372 ICMS – SIMPLES NACIONAL'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1372
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20533, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20534, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1373' , '1373 ICMS – COMUNICACAO – TRIBUTACAO DEFINITIVA' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1373 ICMS – COMUNICACAO – TRIBUTACAO DEFINITIVA'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1373
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20535, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20536, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1374' , '1374 ICMS – DESPESAS ADUANEIRAS MERCADORIA ESTRANGEIRA P/ COMERCIALIZACAO' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1374 ICMS – DESPESAS ADUANEIRAS MERCADORIA ESTRANGEIRA P/ COMERCIALIZACAO'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1374
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20537, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20538, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1375' , '1375 ICMS – DESPESAS ADUANEIRAS MERCADORIA ESTRANGEIRA INSUMO INDUSTRIAL' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1375 ICMS – DESPESAS ADUANEIRAS MERCADORIA ESTRANGEIRA INSUMO INDUSTRIAL'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1375
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20539, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20540, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1376' , '1376 ICMS – ST MERCADORIA NACIONALIZADA (4%) – A' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1376 ICMS – ST MERCADORIA NACIONALIZADA (4%) – A'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1376
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20541, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20542, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1377' , '1377 ICMS –COMBUSTIVEL IMPORTADO – PMPF' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1377 ICMS –COMBUSTIVEL IMPORTADO – PMPF'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1377
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20543, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20544, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1378' , '1378 ICMS – MERCADORIA NACIONALIZADA (4%)' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1378 ICMS – MERCADORIA NACIONALIZADA (4%)'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1378
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20545, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20546, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1379' , '1379 ICMS – IMPORTACAO PARA COMERCIALIZACAO S/ ST' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1379 ICMS – IMPORTACAO PARA COMERCIALIZACAO S/ ST'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1379
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20547, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20548, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1380' , '1380 ICMS – SUBSTITUICAO TRIBUTARIA NOTIFICADOS – A' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1380 ICMS – SUBSTITUICAO TRIBUTARIA NOTIFICADOS – A'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1380
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20549, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20550, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1381' , '1381 ICMS – CONHECIMENTO DE TRANSPORTE – PRECO FOB – A' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1381 ICMS – CONHECIMENTO DE TRANSPORTE – PRECO FOB – A'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1381
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20551, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20552, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1382' , '1382 ICMS – NORMAL TRANSPORTE' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1382 ICMS – NORMAL TRANSPORTE'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1382
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20553, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20554, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1383' , '1383 ICMS – NORMAL MINERAIS' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1383 ICMS – NORMAL MINERAIS'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1383
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20555, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20556, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1384' , '1384 ICMS – PARCELADO' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1384 ICMS – PARCELADO'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1384
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20557, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20558, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1385' , '1385 ICMS – NORMAL ENERGIA ELETRICA' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1385 ICMS – NORMAL ENERGIA ELETRICA'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1385
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20559, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20560, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1386' , '1386 ICMS – NORMAL COMUNICACAO' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1386 ICMS – NORMAL COMUNICACAO'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1386
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20561, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20562, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1387' , '1387 ICMS – NORMAL COMBUSTIVEIS E LUBRIFICANTES' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1387 ICMS – NORMAL COMBUSTIVEIS E LUBRIFICANTES'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1387
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20563, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20564, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1388' , '1388 ICMS – PRODUTOS ESTRANGEIROS – ATIVO' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1388 ICMS – PRODUTOS ESTRANGEIROS – ATIVO'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1388
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20565, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20566, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1389' , '1389 ICMS – MERCADORIA ESTRANGEIRA P/ CONSUMO' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1389 ICMS – MERCADORIA ESTRANGEIRA P/ CONSUMO'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1389
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20567, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20568, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1390' , '1390 ICMS – INSUMO INDUSTRIAL ESTRANGEIRO, INDUSTRIA INCENTIVADA' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1390 ICMS – INSUMO INDUSTRIAL ESTRANGEIRO, INDUSTRIA INCENTIVADA'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1390
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20569, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20570, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1391' , '1391 ICMS – RETENCAO EM OUTROS ESTADOS' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1391 ICMS – RETENCAO EM OUTROS ESTADOS'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1391
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20571, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20572, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1392' , '1392 ICMS – OUTROS' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1392 ICMS – OUTROS'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1392
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20573, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20574, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1393' , '1393 ICMS–ST DA MERCADORIA SOBRE PARCELA DO FRETE FOB' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1393 ICMS–ST DA MERCADORIA SOBRE PARCELA DO FRETE FOB'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1393
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20575, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20576, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1394' , '1394 ICMS – ESTORNO DE CREDITO APROPRIADO EM SAIDA INCENTIVADA' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1394 ICMS – ESTORNO DE CREDITO APROPRIADO EM SAIDA INCENTIVADA'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1394
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20577, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20578, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1395' , '1395 ICMS – NAO INSCRITOS' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1395 ICMS – NAO INSCRITOS'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1395
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20579, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20580, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1396' , '1396 ICMS – SUBSTITUICAO TRIBUTARIA NOTIFICADOS/TRANSFERENCIAS' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1396 ICMS – SUBSTITUICAO TRIBUTARIA NOTIFICADOS/TRANSFERENCIAS'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1396
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20581, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20582, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1397' , '1397 ICMS – PRODUTOS COM TRIBUTACAO DIFERENCIADA' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1397 ICMS – PRODUTOS COM TRIBUTACAO DIFERENCIADA'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1397
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20583, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20584, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1398' , '1398 ICMS – Mercadoria Estrangeira – Lei Hannan 7%' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1398 ICMS – Mercadoria Estrangeira – Lei Hannan 7%'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1398
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20585, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20586, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1399' , '1399 ICMS – AUTO DE APREENSAO' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1399 ICMS – AUTO DE APREENSAO'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1399
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20587, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20588, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1400' , '1400 ICMS – AUTO DE INFRACAO' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1400 ICMS – AUTO DE INFRACAO'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1400
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20589, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20590, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1401' , '1401 ICMS – PARCELADO – AUTOS DE INFRACAO' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1401 ICMS – PARCELADO – AUTOS DE INFRACAO'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1401
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20591, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20592, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1499' , '1499 OUTRAS INFRACÕES' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '1499 OUTRAS INFRACÕES'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1499
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20593, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20594, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '3849' , '3849 CONTRIBUICAO AO FUNDO DE PROMOCAO SOCIAL' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '3849 CONTRIBUICAO AO FUNDO DE PROMOCAO SOCIAL'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 3849
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20595, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20596, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '6401' , '6401 CONTRIBUICAO P/ U.E.A. – P&D' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '6401 CONTRIBUICAO P/ U.E.A. – P&D'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 6401
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20597, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20598, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '6402' , '6402 CONTRIBUICAO P/ U.E.A. – LEI 1939/89 (1,5% s/ ICMS RESTITUIVEL)' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '6402 CONTRIBUICAO P/ U.E.A. – LEI 1939/89 (1,5% s/ ICMS RESTITUIVEL)'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 6402
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20599, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20600, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '6403' , '6403 CONTRIBUICAO P/ U.E.A. – LEI 2390/96(10%s/ CRED. PRESUMIDO)' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '6403 CONTRIBUICAO P/ U.E.A. – LEI 2390/96(10%s/ CRED. PRESUMIDO)'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 6403
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20601, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20602, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '6404' , '6404 CONTRIBUICAO P/ U.E.A – Lei 2826/03 (10% s/CRED. ESTIMULO de 100%)' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '6404 CONTRIBUICAO P/ U.E.A – Lei 2826/03 (10% s/CRED. ESTIMULO de 100%)'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 6404
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20603, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20604, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '6405' , '6405 CONTRIBUICAO p/ U.E.A – Lei 2826/03 (1,3% s/ FAT. BRUTO – BEM INT)' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '6405 CONTRIBUICAO p/ U.E.A – Lei 2826/03 (1,3% s/ FAT. BRUTO – BEM INT)'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 6405
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20605, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20606, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '6406' , '6406 CONTRIBUICAO p/ U.E.A – Lei 2826/03 (1,5% s/ CREDITO ESTIMULO INF)' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '6406 CONTRIBUICAO p/ U.E.A – Lei 2826/03 (1,5% s/ CREDITO ESTIMULO INF)'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 6406
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20607, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20608, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '6407' , '6407 CONTRIBUICAO p/ U.E.A – Lei 2826/03 PARCELAMENTO' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '6407 CONTRIBUICAO p/ U.E.A – Lei 2826/03 PARCELAMENTO'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 6407
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20609, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20610, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '6408' , '6408 CONTRIBUICAO p/ INFRA–ESTRUTURA BASICA, ECONÔMICA e SOCIAL' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '6408 CONTRIBUICAO p/ INFRA–ESTRUTURA BASICA, ECONÔMICA e SOCIAL'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 6408
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20611, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20612, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9850' , '9850 FTI – SOBRE IMPORTACAO E COMERCIALIZACAO' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9850 FTI – SOBRE IMPORTACAO E COMERCIALIZACAO'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9850
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20613, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20614, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9851' , '9851 FTI – FATURAMENTO BRUTO INDUSTRIAL 1%' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9851 FTI – FATURAMENTO BRUTO INDUSTRIAL 1%'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9851
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20615, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20616, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9852' , '9852 FTI – FATURAMENTO BRUTO INDUSTRIAL EXPANSAO E DIVERSIFICACAO – 1%' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9852 FTI – FATURAMENTO BRUTO INDUSTRIAL EXPANSAO E DIVERSIFICACAO – 1%'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9852
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20617, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20618, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9853' , '9853 FTI – PARCELAMENTO' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9853 FTI – PARCELAMENTO'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9853
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20619, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20620, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9854' , '9854 FTI – SOBRE IMPORTACAO INSUMOS INDUSTRIAIS BEM FINAL (2%) DO VALOR FOB' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9854 FTI – SOBRE IMPORTACAO INSUMOS INDUSTRIAIS BEM FINAL (2%) DO VALOR FOB'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9854
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20621, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20622, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9855' , '9855 FTI – FATURAMENTO BRUTO BEM INTERMEDIARIO DIFERIMENTO (1%)' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9855 FTI – FATURAMENTO BRUTO BEM INTERMEDIARIO DIFERIMENTO (1%)'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9855
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20623, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20624, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9856' , '9856 FTI – AQUISICAO DE INSUMOS NACIONAIS BEM FINAL (1%)' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9856 FTI – AQUISICAO DE INSUMOS NACIONAIS BEM FINAL (1%)'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9856
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20625, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20626, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9857' , '9857 FTI – PROJETOS AGROPECUARIOS' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9857 FTI – PROJETOS AGROPECUARIOS'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9857
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20627, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20628, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9858' , '9858 FTI – CONCENTRADOS' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9858 FTI – CONCENTRADOS'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9858
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20629, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20630, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9859' , '9859 FTI – LCD' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9859 FTI – LCD'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9859
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20631, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20632, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9860' , '9860 FTI – IMPORTACAO INSUMO INDUSTRIAL – DUAS RODAS – 3,5% DO VALOR FOB' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9860 FTI – IMPORTACAO INSUMO INDUSTRIAL – DUAS RODAS – 3,5% DO VALOR FOB'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9860
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20633, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20634, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9861' , '9861 FTI – FATURAMENTO BRUTO INDUSTRIAL – DUAS RODAS – 0,25%' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9861 FTI – FATURAMENTO BRUTO INDUSTRIAL – DUAS RODAS – 0,25%'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9861
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20635, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20636, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9862' , '9862 FTI – IMPORTACAO INSUMO INDUSTRIAL – ADICIONAL DUAS RODAS' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9862 FTI – IMPORTACAO INSUMO INDUSTRIAL – ADICIONAL DUAS RODAS'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9862
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20637, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20638, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9863' , '9863 FTI – TRANSFERÊNCIA NACIONAL (1%)' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9863 FTI – TRANSFERÊNCIA NACIONAL (1%)'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9863
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20639, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20640, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9864' , '9864 FTI – TRANSFERÊNCIA IMPORTADO (2%)' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9864 FTI – TRANSFERÊNCIA IMPORTADO (2%)'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9864
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20641, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20642, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9865' , '9865 FTI – ADICIONAL PROCESSO PRODUTIVO ELEMENTAR (1% FAT. BRUTO)' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9865 FTI – ADICIONAL PROCESSO PRODUTIVO ELEMENTAR (1% FAT. BRUTO)'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9865
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20643, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20644, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9866' , '9866 FTI – CONTRIBUICAO EXTRAORDINARIA (2% FAT. BRUTO)' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9866 FTI – CONTRIBUICAO EXTRAORDINARIA (2% FAT. BRUTO)'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9866
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20645, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20646, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9867' , '9867 FTI – SOBRE IMPORTACAO INSUMOS IND BF   ENERGETICOS –  (3,5%) DO VALOR FOB' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9867 FTI – SOBRE IMPORTACAO INSUMOS IND BF   ENERGETICOS –  (3,5%) DO VALOR FOB'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9867
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20647, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20648, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9880' , '9880 FMPES – CONTRIBUICAO EXTRA–ORCAMENTARIA–AFEAM' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9880 FMPES – CONTRIBUICAO EXTRA–ORCAMENTARIA–AFEAM'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9880
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20649, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20650, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9881' , '9881 FMPES – PARCELAMENTO' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9881 FMPES – PARCELAMENTO'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9881
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20651, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20652, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9882' , '9882 FMPES – CONTRIBUICAO ORCAMENTARIA' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9882 FMPES – CONTRIBUICAO ORCAMENTARIA'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9882
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20653, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20654, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9883' , '9883 FMPES – EXERCICIOS ANTERIORES' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '9883 FMPES – EXERCICIOS ANTERIORES'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9883
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20655, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20656, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '3863' , '3863 - FUNDO DE PROMOÇÃO SOCIAL E ERRADICAÇÃO DA POBREZA - ENTRADA  NACIONAL' , '01/08/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '3863 - FUNDO DE PROMOÇÃO SOCIAL E ERRADICAÇÃO DA POBREZA - ENTRADA  NACIONAL'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 3863
                AND DT_INI   =  '01/08/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20657, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20658, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '3864' , '3864 - FUNDO DE PROMOÇÃO SOCIAL E ERRADICAÇÃO DA POBREZA - ENTRADA IMPORTADA' , '01/08/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '3864 - FUNDO DE PROMOÇÃO SOCIAL E ERRADICAÇÃO DA POBREZA - ENTRADA IMPORTADA'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 3864
                AND DT_INI   =  '01/08/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20659, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20660, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '3865' , '3865 - FUNDO DE PROMOÇÃO SOCIAL E ERRADICAÇÃO DA POBREZA - SAÍDA COMBUSTÍVEIS' , '01/08/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '3865 - FUNDO DE PROMOÇÃO SOCIAL E ERRADICAÇÃO DA POBREZA - SAÍDA COMBUSTÍVEIS'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 3865
                AND DT_INI   =  '01/08/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20661, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20662, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '3866' , '3866 - FUNDO DE PROMOÇÃO SOCIAL E ERRADICAÇÃO DA POBREZA - SAÍDA CONCENTRADOS' , '01/08/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '3866 - FUNDO DE PROMOÇÃO SOCIAL E ERRADICAÇÃO DA POBREZA - SAÍDA CONCENTRADOS'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 3866
                AND DT_INI   =  '01/08/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20663, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20664, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '3867' , '3867 - FUNDO DE PROMOÇÃO SOCIAL E ERRADICAÇÃO DA POBREZA - SAÍDA TV POR ASSINATURA' , '01/08/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '3867 - FUNDO DE PROMOÇÃO SOCIAL E ERRADICAÇÃO DA POBREZA - SAÍDA TV POR ASSINATURA'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 3867
                AND DT_INI   =  '01/08/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20665, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20666, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '3868' , '3868 - FUNDO DE PROMOÇÃO SOCIAL E ERRADICAÇÃO DA POBREZA - SAÍDA OUTROS' , '01/08/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = '3868 - FUNDO DE PROMOÇÃO SOCIAL E ERRADICAÇÃO DA POBREZA - SAÍDA OUTROS'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 3868
                AND DT_INI   =  '01/08/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20667, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20668, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '1322' , 'ICMS – ESTORNO DE CRÉDITO – OPERAÇÕES NÃO INCENTIVADAS' , '01/02/2019',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = 'ICMS – ESTORNO DE CRÉDITO – OPERAÇÕES NÃO INCENTIVADAS'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 1322
                AND DT_INI   =  '01/02/2019', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20669, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20670, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '3960' , 'FPS – CARTÃO SOCIAL' , '29/10/2020',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = 'FPS – CARTÃO SOCIAL'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 3960
                AND DT_INI   =  '29/10/2020', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20671, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20672, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '3862' , 'CONTRIBUIÇÃO AO FUNDO DE PROMOÇÃO SOCIAL' , '03/03/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = 'CONTRIBUIÇÃO AO FUNDO DE PROMOÇÃO SOCIAL'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 3862
                AND DT_INI   =  '03/03/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20673, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20674, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9830' , 'ICMS - RESTITUÍVEL' , '01/06/2017',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = 'ICMS - RESTITUÍVEL'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9830
                AND DT_INI   =  '01/06/2017', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20675, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20676, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


BEGIN
  INSERT INTO COD_REC_UF (ID, ESTADO_ID, COD_REC, DESC_COD, DT_INI, DT_FIM, VERSAO) 
     VALUES (CODRECUF_SEQ.NEXTVAL, 2 ,  '9868' , 'FTI – TERMO DE ACORDO DE PRODUTOS FARMACÊUTICOS;' , '08/08/2019',  NULL  , 9 ); 
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
       BEGIN
            UPDATE COD_REC_UF
               SET DESC_COD  = 'FTI – TERMO DE ACORDO DE PRODUTOS FARMACÊUTICOS;'
                 , DT_FIM    =  NULL 
                 , VERSAO    = 9
             WHERE ESTADO_ID = 2
               AND COD_REC   = 9868
                AND DT_INI   =  '08/08/2019', 
       EXCEPTION
          WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20677, 'Erro no script 77784.  Erro: ' || sqlerrm) ;
        END;
   WHEN OTHERS THEN
       RAISE_APPLICATION_ERROR(-20678, 'Erro no script 77784.  Erro: ' || sqlerrm);
END;
/


