#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import requests
import json
import os


# ---------------------------------------------------------------------------- #
# CONSTANTES


API_KEY_FILE = f"/home/{os.environ['USER']}/.omdb-gui-key.txt"
APIKEY = ''
BGCOLOR = '#6E6D97'
LABELFONTS = 'TkMenuFont 15'
TEXTFONT = 'TkTextFont 10'


# ---------------------------------------------------------------------------- #
# FUNÇÔES


def clear_frames(frame1, frame2, frame3):
    '''Função para limpar os frames ao se trocar de um para o outro.'''

    for item in (
        frame1.winfo_children(),
        frame2.winfo_children(),
        frame3.winfo_children()
    ):
        for widget in item:
            widget.destroy()


def read_config_file():
    '''Função para lêr arquivo com chave da API e colocar-la em variável.'''
    with open(API_KEY_FILE, 'r') as f:
        return f.readline()


def save_api_key(api_key):
    '''Função para salvar chave da API em arquivo.'''
    with open(API_KEY_FILE, 'a') as f:
        f.write(api_key)


def parse_arguments(title, type, plot, year):
    '''Função para tratar e validar os argumentos.'''
    url_composition = dict()

    # Título é obrigatório
    if title.get() == '':
        load_error_frame('ERRO! Não especificou o Título.')
    else:
        url_composition['title'] = title.get()

        if type.get() == 'Filme':
            type = type.get().replace('Filme', 'movie')
        else:
            type = type.get().replace('Série', 'series')

        url_composition['type'] = type

        if plot.get() == 'Breve':
            plot = plot.get().replace('Breve', 'short')
        else:
            plot = plot.get().replace('Completa', 'full')

        url_composition['plot'] = plot

        if year.get() != '':
            url_composition['year'] = year.get()

        make_request(**url_composition)


def make_request(**url_composition):
    '''Função que faz de fato a requisição'''
    base_url = 'https://omdbapi.com/?'
    APIKEY = read_config_file()

    requisition = f"{base_url}t={url_composition['title']}"
    requisition = f"{requisition}&type={url_composition['type']}"
    requisition = f"{requisition}&plot={url_composition['plot']}"


    if 'year' in url_composition.keys():
        requisition = f"{requisition}&y={url_composition['year']}"

    requisition = f'{requisition}&apikey={APIKEY}'

    # Não tenho muita certeza desta parte.
    # Ainda não entendi bem estas exceções..
    try:
        response = requests.get(requisition)
    except requests.exceptions.ConnectionError:
        load_error_frame(
            'ERRO! Teve algum erro na conexão. Por favor tente mais tarde.'
        )
    except requests.exceptions.Timeout:
        load_error_frame('Requisição demorou tempo demais.')
    except Exception as err:
        load_error_frame('Erro desconhecido. Por favor tente mais tarde.')
    else:
        js = json.loads(response.text)
        load_output_frame(**js)


def load_input_frame():
    '''Carrega a tela de input.'''
    clear_frames(output_frame, error_frame, api_frame)
    input_frame.tkraise()
    input_frame.grid_propagate(False)
    input_frame.pack_propagate(False)

    # A Imagem. No meu Linux Mint, para executar sem usar o
    # Python e o pillow do ambiente virtual, tive que fazer:
    # sudo apt install python3-pil.imagetk
    # mesmo o Mint vindo com o pillow já instalado...
    img = ImageTk.PhotoImage(file='download.jpeg')
    img_label = Label(input_frame, image=img, bg=BGCOLOR)
    img_label.image = img

    # Aqui centraliza a imagem no ecra
    img_label.place_configure(x=405, y=200, anchor='center')

    # Título
    title_label = Label(
        input_frame,
        text='Título',
        font=LABELFONTS,
        bg=BGCOLOR
    )
    title_label.grid_configure(row=0, column=0, padx=5, pady=10)
    title_entry = Entry(input_frame)
    title_entry.grid_configure(row=1, column=0, padx=5, pady=10)
    title_entry.focus_set()

    # Tipo (Filme/Série)
    type_target = StringVar()
    type_label = Label(
        input_frame,
        text='Filme/Série',
        font=LABELFONTS,
        bg=BGCOLOR,
    )
    type_label.grid_configure(row=0, column=1, padx=5, pady=10)

    type_combobox = ttk.Combobox(
        input_frame,
        values=('Filme', 'Série'),
        textvariable=type_target
    )
    type_combobox.set('Filme')
    type_combobox.grid_configure(row=1, column=1, padx=5, pady=10)

    # Plot (Sinópse)
    plot_target = StringVar()
    plot_label = Label(
        input_frame,
        text='Sinópse',
        font=LABELFONTS,
        bg=BGCOLOR
    )
    plot_label.grid_configure(row=0, column=2, padx=5, pady=10)

    plot_combobox = ttk.Combobox(
        input_frame,
        values=('Breve', 'Completa'),
        textvariable=plot_target
    )
    plot_combobox.set('Breve')
    plot_combobox.grid_configure(row=1, column=2, padx=5, pady=10)

    # Ano de Lancamento
    year_label = Label(
        input_frame,
        text='Lançamento',
        font=LABELFONTS,
        bg=BGCOLOR
    )
    year_label.grid_configure(row=0, column=3, padx=5, pady=10)

    year_entry = Entry(input_frame)
    year_entry.grid_configure(row=1, column=3, padx=5, pady=10)

    search_button = Button(
        input_frame,
        text='Pesquisar',
        font=LABELFONTS,
        bg=BGCOLOR,
        activebackground=BGCOLOR,
        bd=2, relief='raised',
        command=lambda: parse_arguments(
            title_entry, type_target,
            plot_target, year_entry
        )
    )
    search_button.pack_configure(side=RIGHT, anchor='s')

    quit_button = Button(
        input_frame,
        text='Sair',
        font=LABELFONTS,
        bg=BGCOLOR,
        activebackground=BGCOLOR,
        bd=2, relief='raised',
        command=root.destroy
    )
    quit_button.pack_configure(side=RIGHT, anchor='s')


def load_output_frame(**js):
    '''Função que carrega o segundo frame com o output formatado.'''
    clear_frames(input_frame, error_frame, api_frame)
    output_frame.tkraise()

    text_entry = Text(
        output_frame,
        bg=BGCOLOR,
        bd=2,
        font=TEXTFONT,
        wrap=WORD
    )
    text_entry.pack_configure(fill=BOTH)

    # Se digitar errado o titulo aqui, dá um monte de erro feio!!!
    try:
        output = f"{'Title:':<8}\t\t{js['Title']:<8}\n"
    except Exception as err:
        load_error_frame('Título parece ter sido digitado errado.')
    else:
        # Deve ter forma mais elegante de fazer isto não? kk
        output += f"{'Year:':<8}\t\t{js['Year']:<8}\n"
        output += f"{'Released:':<8}\t\t{js['Released']:<8}\n"
        output += f"{'Runtime:':<8}\t\t{js['Runtime']:<8}\n"
        output += f"{'Genre:':<8}\t\t{js['Genre']:<8}\n"
        output += f"{'Director:':<8}\t\t{js['Director']:<8}\n"
        output += f"{'Writer:':<8}\t\t{js['Writer']:<8}\n"
        output += f"{'Actors:':<8}\t\t{js['Actors']:<8}\n"
        output += f"{'Language:':<8}\t\t{js['Language']:<8}\n"
        output += f"{'Country:':<8}\t\t{js['Country']:<8}\n"
        output += f"{'Awards:':<8}\t\t{js['Awards']:<8}\n"
        output += f"{'Rating:':<8}\t\t{js['imdbRating']:<8}\n"
        output += f"{'Type:':<8}\t\t{js['Type']:<8}\n"

        if 'totalSeasons' in js.keys():
            output += f"{'Total Seasons:':<8}\t\t{js['totalSeasons']:<8}\n"

        output += '\n\nPlot:\n\n'
        output += js['Plot']

        text_entry.insert(1.0, output)
        text_entry['state'] = 'disabled'

    back_button = Button(
        output_frame,
        text='Voltar',
        font=LABELFONTS,
        bg=BGCOLOR,
        activebackground=BGCOLOR,
        bd=2, relief='raised',
        command=load_input_frame
    )
    back_button.pack_configure(anchor='s', side=RIGHT)


def load_error_frame(error_message):
    '''Função para mostrar mensagens de erro em seu próprio frame.'''
    clear_frames(input_frame, output_frame, api_frame)
    error_frame.tkraise()

    error_entry = Text(
        error_frame,
        bg=BGCOLOR,
        bd=2,
        font=TEXTFONT,
        wrap=WORD
    )
    error_entry.pack_configure(fill=BOTH)

    error_entry.insert(1.0, error_message)
    error_entry['state'] = 'disabled'

    back_button = Button(
        error_frame,
        text='Voltar',
        font=LABELFONTS,
        bg=BGCOLOR,
        activebackground=BGCOLOR,
        bd=2, relief='raised',
        command=load_input_frame
    )
    back_button.pack_configure(anchor='s', side=RIGHT)


def load_api_frame():
    '''Função para inserir e gravar chave da API'''
    clear_frames(input_frame, output_frame, error_frame)
    api_frame.tkraise()
    api_frame.grid_propagate(False)
    api_frame.pack_propagate(False)

    api_key_label = Label(
        api_frame,
        text='Insira sua chave da API',
        font=LABELFONTS,
        bg=BGCOLOR
    )
    api_key_label.pack_configure(pady=10)

    api_key_entry = Entry(api_frame)
    api_key_entry.pack_configure(pady=10)
    api_key_entry.focus_set()

    submit_button = Button(
        api_frame,
        text='Submeter',
        font=LABELFONTS,
        bg=BGCOLOR,
        activebackground=BGCOLOR,
        bd=2, relief='raised',
        command=lambda: [
            save_api_key(api_key_entry.get()),
            load_input_frame()
        ]
    )
    submit_button.pack_configure(anchor='s', side=RIGHT)


# ---------------------------------------------------------------------------- #
# JANELA PRINCIPAL


root = Tk()
root.wm_title('Omdb-Gui')
root.wm_resizable(0, 0)


# Fica esquisito no meu monitor, mais no canto inferior
# direito do que no centro kk, onde é suposto estar..
root.eval('tk::PlaceWindow . center')


# ---------------------------------------------------------------------------- #
# FRAMES


# frame input
input_frame = Frame(root, width=810, height=400, bg=BGCOLOR)
input_frame.grid_configure(row=0, column=0, sticky=NSEW)


# Frame para output (resposta)
output_frame = Frame(root, bg=BGCOLOR)
output_frame.grid_configure(row=0, column=0, sticky=NSEW)


# Frame para mensagens de erro
error_frame = Frame(root, bg=BGCOLOR)
error_frame.grid_configure(row=0, column=0, sticky=NSEW)


# Frame para inserção e guardar chave da API
api_frame = Frame(root, bg=BGCOLOR)
api_frame.grid_configure(row=0, column=0, sticky=NSEW)


# ---------------------------------------------------------------------------- #
# CHAVE DA API


if not os.path.exists(API_KEY_FILE):
    load_api_frame()
else:
    load_input_frame()


# ---------------------------------------------------------------------------- #
# MAINLOOP


root.mainloop()
