# 🧠 Personal Data Warehouse (PDW)

**PersonalDataWareHouse.py** é um sistema de ETL (Extract, Transform, Load) desenvolvido em **Python**, projetado para centralizar, padronizar e analisar dados pessoais a partir de múltiplas fontes como planilhas Excel, CSVs e bancos de dados locais.  
O objetivo é simples (e ambicioso): transformar o caos de dados do cotidiano em informação estruturada, acessível e útil.

---

## 🚀 Visão Geral

O **PDW** foi criado para quem deseja tratar seus próprios dados com o mesmo rigor que empresas tratam seus Data Warehouses corporativos.  
Ele automatiza tarefas repetitivas de importação, normalização e consolidação, permitindo que relatórios e análises sejam gerados em poucos segundos.

Em essência:
> "Você fornece os dados brutos, o PDW entrega inteligência."

---

## 🧩 Funcionalidades Principais

- **Importação inteligente de planilhas** (Excel `.xlsx` ou `.xls` e CSVs)
- **Criação automática de tabelas SQLite**
- **Transformação e limpeza de dados**
- **Geração de relatórios analíticos**
- **Exportação em múltiplos formatos** (`Excel`, `CSV`, `JSON`, `SQLite`)
- **Controle de histórico e versionamento de cargas**
- **Configuração modular** via arquivos `.json`
- **Execução automatizada** via linha de comando ou scripts agendados

---

## 🏗️ Arquitetura e Componentes

O projeto segue o padrão **ETL modularizado**, com cada etapa bem definida:

| Etapa | Módulo | Descrição |
|:------|:--------|:-----------|
| **Extract** | `extractor.py` | Lê e interpreta arquivos de entrada (Excel, CSV, etc.) |
| **Transform** | `transformer.py` | Padroniza colunas, normaliza dados e aplica regras de negócio |
| **Load** | `loader.py` | Insere os dados tratados em bancos SQLite ou exporta para outros formatos |
| **Utils** | `helpers.py`, `logger.py` | Funções auxiliares, logs e tratamento de erros |
| **Main** | `PersonalDataWareHouse.py` | Controla o fluxo geral de execução e as dependências |

---

## ⚙️ Instalação

Pré-requisitos:
- Python 3.10+
- Bibliotecas:
  ```bash
  pip install pandas openpyxl sqlalchemy tabulate
