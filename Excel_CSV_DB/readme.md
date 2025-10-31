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
  pip install pandas openpyxl sqlalchemy tabulate xlsxwriter xlrd numpy lxml tabulate
--
## 🧠 Uso Básico
```bash
   python PersonalDataWareHouse.py
```

Ou passando parâmetros personalizados:
```bash
   python PersonalDataWareHouse.py ArquivoDeParametros.cfg
```
---
## 🧰 Tecnologias Utilizadas
- Python 3.x
- Pandas
- SQLite
- SQLAlchemy
- OpenPyXL
- JSON Configs
---
## 🧭 Roadmap (Próximos Passos)
- Integração com MongoDB
- Interface Web (Flask Dashboard)
- Agendador de cargas
- Análises financeiras automatizadas
- Exportação direta para Google Sheets
---
## 📚 Motivação
Este projeto nasceu da necessidade de organizar dados pessoais dispersos em planilhas, extratos e arquivos manuais, aplicando os mesmos princípios de Business Intelligence e Data Warehousing usados em grandes corporações.

É, no fundo, um exercício de autonomia digital: 
> “Se os dados são o novo petróleo, o PDW é a tua refinaria particular.”

---

## 👨‍💻 Autor
Carlin, Luiz A..'.  
M.'.M.'.  
Especialista em sistemas de Billing e integração de dados corporativos
Entusiasta de ETL, Oracle, Linux, Tarot de Thoth e boa engenharia de software.

---

## 🧾 Licença
Este projeto é distribuído sob a MIT License.
Consulte o arquivo LICENSE  para mais detalhes.

---

## 🌌 Citação Final
“A verdadeira inteligência de dados não está no código, mas na curiosidade de quem decide olhar para os próprios números.”
