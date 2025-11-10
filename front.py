import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog, PhotoImage, END
from tkinter.ttk import Frame, Label, Button, Entry, Separator, Style, Combobox
from tkinter import Listbox, Scrollbar
from tkinter.scrolledtext import ScrolledText
from back import *

# Cores
AZUL = '#1E88E5'
AZULCLARO = "#ADD8E6"
BRANCO = '#f2f2f2'
VERDE = '#4CAF50'
VERDECLARO = "#90EE90"
VERMELHO = '#E74C3C'
VERMELHOCLARO = "#FF7F7F"
CINZA = '#D3D3D3'

###### CRIAR LOGO 1 
def logo(janela):
    topo = Frame(janela, style='Borda.TFrame')
    topo.pack(pady=5,padx=10)
    try:
        logo_img = PhotoImage(file=r"logoeleve.PNG")
        logo_img = logo_img.subsample(2, 2)
        label_logo = Label(topo, image=logo_img, background=BRANCO)
        label_logo.image = logo_img  # manter referência
        label_logo.pack()
    except tk.TclError:
           return topo

###### CRIAR LOGO ALUNO
def logoalu(janela, aumentar=False):
    topo = Frame(janela, style='Borda.TFrame')
    topo.pack(pady=5, padx=10)
    try:
        logo_img = PhotoImage(file=r"logoalu.png")
        if not aumentar:
            logo_img = logo_img.subsample(2, 2)  # reduz tamanho padrão
        # se aumentar=True, não reduz, fica tamanho original
        label_logo = Label(topo, image=logo_img, background=BRANCO)
        label_logo.image = logo_img  # manter referência
        label_logo.pack()
    except tk.TclError:
        return topo

###### CRIAR LOGO DOCENTE
def logodoc(janela, aumentar=False):
    topo = Frame(janela, style='Borda.TFrame')
    topo.pack(pady=5,padx=10)
    try:
        logo_img = PhotoImage(file=r"logodoc.png")
        if not aumentar:
            logo_img = logo_img.subsample(2, 2)  # reduz tamanho padrão
        # se aumentar=True, mostra tamanho original (maior)
        label_logo = Label(topo, image=logo_img, background=BRANCO)
        label_logo.image = logo_img  # manter referência
        label_logo.pack()
    except tk.TclError:
        return topo
    

###LOGIN DO DOCENTE
def abrir_login_docente():
    global et_email, et_senha

    janela = tk.Toplevel()
    janela.title("ELEVE - Login Docente")
    janela.geometry("400x550+100+100")
    janela.configure(bg=BRANCO)

    style = Style()
    style.theme_use('default')
    style.configure('TFrame', background=BRANCO)
    style.configure('Borda.TFrame', width=300)
    style.configure('TLabel', justify='right', font=('Montserrat', 10), background=BRANCO, foreground='#808080')
    style.configure('Small.TLabel', font=('Montserrat', 8))
    style.configure('TButton', padding=(60,7), font=('Montserrat', 12, 'bold'), foreground=BRANCO, background=VERDE, relief='flat')
    style.configure('Small.TButton', padding=(0,-3), font=('Montserrat', 8), foreground=AZUL, background=BRANCO, relief='flat')
    style.configure('TSeparator', background='#bafafa')
    style.configure('Sair.TButton', padding=(60,7), font=('Montserrat', 12, 'bold'), foreground=BRANCO, background=VERMELHO, relief='flat')
    style.map('TButton', background=[('active', VERDECLARO)], foreground=[('active', BRANCO)])
    style.map('Sair.TButton', background=[('active', VERMELHOCLARO)], foreground=[('active', VERMELHO)])
    style.map('Small.TButton', background=[('active', BRANCO)], foreground=[('active', AZULCLARO)])

    borda = Frame(janela, style='Borda.TFrame')
    borda.pack(fill='x', expand=True)

    logodoc(borda)

    centro = Frame(borda)
    centro.pack(pady=10)

    Label(centro, text='E-mail').pack(anchor='w', pady=(10,0))
    et_email = Entry(centro, font=('Montserrat', 12, 'bold'), foreground='#666')
    et_email.pack(fill='x')
    Separator(centro, orient='horizontal').pack(fill='x')

    Label(centro, text='Senha').pack(anchor='w', pady=(10,0))
    et_senha = Entry(centro, show='*', font=('Montserrat', 12, 'bold'), foreground='#666')
    et_senha.pack(fill='x')
    Separator(centro, orient='horizontal').pack(fill='x', pady=(0,20))

    base = Frame(borda)
    base.pack(pady=10)

    Button(base, text='ENTRAR', command=fazer_login, style='TButton').pack(fill='x', pady=(0,10))
    Label(base, text='Você deseja ', style='Small.TLabel').pack(side='left')
    Button(base, text='SAIR AGORA |', command=janela.destroy, style='Small.TButton', cursor='hand2').pack(side='left')
    Button(base, text="SOU ALUNO", command=lambda: [janela.withdraw(), abrir_login_aluno()], style='Small.TButton', cursor='hand2').pack(side='left')
###LOGIN DO ALUNO
def abrir_login_aluno():
    global et_email, et_senha  

    janela = tk.Toplevel()
    janela.title("ELEVE - Login Aluno")
    janela.geometry("490x550+100+100")
    janela.configure(bg=BRANCO)

    style = Style()
    style.theme_use('default')
    style.configure('TFrame', background=BRANCO)
    style.configure('TLabel', justify='right', font=('Montserrat', 10), background=BRANCO, foreground='#808080')
    style.configure('TButton', padding=(60, 7), font=('Montserrat', 12, 'bold'), foreground=BRANCO, background=VERDE, relief='flat')
    style.configure('Small.TButton', padding=(0,-3), font=('Montserrat', 8), foreground=AZUL, background=BRANCO, relief='flat')
    style.map('TButton', background=[('active', VERDECLARO)], foreground=[('active', BRANCO)])
    style.map('Small.TButton', background=[('active', BRANCO)], foreground=[('active', AZULCLARO)])

    borda = Frame(janela, style='Borda.TFrame')
    borda.pack(fill='x', expand=True)

    logoalu(borda)

    centro = Frame(borda)
    centro.pack(pady=10)

    Label(centro, text='RA').pack(anchor='w', pady=(10,0))
    et_email = Entry(centro, font=('Montserrat', 12, 'bold'), foreground='#666')  # et_email representa o RA aqui
    et_email.pack(fill='x')
    Separator(centro, orient='horizontal').pack(fill='x')

    Label(centro, text='Senha').pack(anchor='w', pady=(10,0))
    et_senha = Entry(centro, show='*', font=('Montserrat', 12, 'bold'), foreground='#666')
    et_senha.pack(fill='x')
    Separator(centro, orient='horizontal').pack(fill='x', pady=(0,20))

    base = Frame(borda)
    base.pack(pady=10)

    Button(base, text='ENTRAR', command=fazer_login, style='TButton').pack(fill='x', pady=(0,10))
    Label(base, text='Você deseja ', style='Small.TLabel').pack(side='left')
    Button(base, text='SAIR AGORA |', command=janela.destroy, style='Small.TButton', cursor='hand2').pack(side='left')
    Button(base, text="SOU DOCENTE", command=lambda: [janela.withdraw(), abrir_login_docente()], style='Small.TButton', cursor='hand2').pack(side='left')
###MENUS PRINCIPAIS

def abrir_menu_admin(nome_usuario):
    janela = tk.Toplevel()
    janela.title("ELEVE - Admin")
    janela.attributes('-fullscreen', True)
    janela.configure(bg=BRANCO)

    logodoc(janela, aumentar=True)
    

    corpo = Frame(janela, style='TFrame')
    corpo.pack(pady=20, fill='both', expand=True)
    
    Label(corpo, text=f"Bem-vindo, {nome_usuario}\nO que você deseja fazer?", font=("Calibri", 14), background=BRANCO, foreground=AZUL).pack(pady=5)
    Button(corpo, text="Usuários", command=abrir_gerenciador_usuarios, width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Alunos", command=abrir_gerenciador_alunos,width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Turmas", command=abrir_gerenciador_turmas, width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Aulas", command=abrir_gerenciador_aulas,width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Relatório", width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Sair", command=janela.destroy, width=5, style='Sair.TButton').pack(pady=10)

def abrir_menu_coord(nome_usuario):
    janela = tk.Toplevel()
    janela.title("ELEVE - Coordenador")
    janela.attributes('-fullscreen', True)
    janela.configure(bg=BRANCO)

    logodoc(janela, aumentar=True)

    corpo = Frame(janela, style='TFrame')
    corpo.pack(pady=20, fill='both', expand=True)

    Label(corpo, text=f"Bem-vindo(a), Coordenador(a) {nome_usuario}", font=("Calibri", 14), background=BRANCO, foreground=AZUL).pack(pady=10)
    Button(corpo, text="Alunos", command=abrir_gerenciador_alunos,width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Turmas", command=abrir_gerenciador_turmas, width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Aulas", command=abrir_gerenciador_aulas,width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Relatório", width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Sair", command=janela.destroy, width=5, style='Sair.TButton').pack(pady=10)

def abrir_menu_prof(nome_usuario):
    janela = tk.Toplevel()
    janela.title("ELEVE - Professor")
    janela.attributes('-fullscreen', True)
    janela.configure(bg=BRANCO)
    (janela)

    logodoc(janela, aumentar=True)
    
    corpo = Frame(janela, style='TFrame')
    corpo.pack(pady=20, fill='both', expand=True)

    Label(corpo, text=f"Bem-vindo(a), Professor(a) {nome_usuario}", font=("Calibri", 14), background=BRANCO, foreground=AZUL).pack(pady=10)
    Button(corpo, text="Aulas", command=abrir_gerenciador_aulas,width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Relatório", width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Sair", command=janela.destroy, width=5, style='Sair.TButton').pack(pady=10)

###CRIACAO DE TELA DO ALUNO
def abrir_menu_aluno(nome_usuario, ra):
    janela = tk.Toplevel()
    janela.title("ELEVE - Área do Aluno")
    janela.attributes('-fullscreen', True)
    janela.configure(bg=BRANCO)

    logoalu(janela, aumentar=True)

    corpo = Frame(janela, style='TFrame')
    corpo.pack(pady=20, fill='both', expand=True)

    Label(
        corpo,
        text=f"Bem-vindo(a), {nome_usuario}\nRegistro do Aluno: {ra}",
        font=("Calibri", 14),
        background=BRANCO,
        foreground=AZUL
    ).pack(pady=10)

    # ---- Botões ----
    Button(
        corpo,
        text="Aulas",
        command=lambda: abrir_aulas_aluno(ra),
        width=25,
        style='TButton'
    ).pack(pady=10)

    Button(
        corpo,
        text="Relatório",
        width=25,
        style='TButton'
    ).pack(pady=10)

    # ---- Botão Sair ----
    def sair_aluno():
        import os
        if os.path.exists("aluno_logado.txt"):
            os.remove("aluno_logado.txt")
        janela.destroy()
        messagebox.showinfo("Logout", "Você saiu do portal do aluno.")

    Button(
        corpo,
        text="Sair",
        command=sair_aluno,
        width=5,
        style='Sair.TButton'
    ).pack(pady=10)

    # Garante limpeza ao fechar no X
    janela.protocol("WM_DELETE_WINDOW", sair_aluno)

###FAZER LOGIN
def fazer_login():
    usuario = et_email.get().strip()
    senha = et_senha.get().strip()

    # Se for um RA (4 dígitos numéricos), tenta login como aluno
    if usuario.isdigit() and len(usuario) == 4:
        nome_aluno = autenticar_alunos_por_ra_e_senha(usuario, senha)
        if nome_aluno:
            messagebox.showinfo("Login", f"Bem-vindo, {nome_aluno}!")

            # 🔹 Salva o aluno logado em um arquivo para ser usado depois
            with open("aluno_logado.txt", "w", encoding="utf-8") as f:
                f.write(f"{nome_aluno};{usuario}")

            abrir_menu_aluno(nome_aluno, usuario)
        else:
            messagebox.showerror("Erro", "RA ou senha incorretos.")
    else:
        # Caso contrário, tenta login de usuário normal
        resultado = autenticar_usuario(usuario, senha)
        if resultado:
            nome_usuario, cargo = resultado
            messagebox.showinfo("Login", f"Bem-vindo, {nome_usuario}!")
            cargo = cargo.lower()
            if cargo == "admin":
                abrir_menu_admin(nome_usuario)
            elif cargo == "coordenador":
                abrir_menu_coord(nome_usuario)
            elif cargo == "professor":
                abrir_menu_prof(nome_usuario)
            else:
                messagebox.showinfo("Menu", f"Menu para {cargo} ainda não implementado.")
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")


#### ----- Gerenciador de USUARIOS
def abrir_gerenciador_usuarios():
    janela = tk.Toplevel()
    janela.title("Gerenciador de Usuários")
    janela.attributes('-fullscreen', True)
    janela.configure(bg=BRANCO)

    corpo = Frame(janela, style='TFrame')
    corpo.pack(pady=20, fill='both', expand=True)

    logodoc(corpo)

    centro = Frame(corpo)
    centro.pack(pady=10)

    Label(corpo, text="Gerenciador de Usuários", font=("Calibri", 16), background=BRANCO, foreground=AZUL).pack(pady=5)
    
    Label(corpo, text="Buscar usuário:",font=("Montserrat", 9, "italic"), style='TLabel').pack(padx=10,anchor='w')

    busca_frame = Frame(corpo)
    busca_frame.pack(fill='x', pady=(0, 10))

    entrada_busca = tk.Entry(busca_frame, font=('Montserrat', 12), width=35)
    entrada_busca.pack(side='left', padx=(10, 5), pady=5)

    Button(busca_frame, text="Buscar 🔍", command=lambda: resultado_label.config(text=mostrar_busca_usuario(entrada_busca.get())), style='Small.TButton', cursor='hand2').pack(side='left')

    resultado_frame = Frame(corpo, style='TFrame')
    resultado_frame.pack(fill='both', expand=True, pady=(20,0))

    resultado_label = Label(resultado_frame, text="Resultados aparecerão aqui...", style='TLabel', justify='left')
    resultado_label.pack(anchor='nw')

    Button(corpo, text="Adicionar Novo Usuário", command=cadastrar_usuario, width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Editar Usuário", command=editar_usuario2, width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Remover Usuário", command=remover_usuario2, width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Voltar", command=janela.destroy, width=5, style='Sair.TButton').pack(pady=10)


### ----- GERENCIADOR DE ALUNOS
def abrir_gerenciador_alunos():
    janela = tk.Toplevel()
    janela.title("Gerenciador de Alunos")
    janela.attributes('-fullscreen', True)
    janela.configure(bg=BRANCO)

    corpo = Frame(janela, style='TFrame')
    corpo.pack(pady=20, fill='both', expand=True)

    logodoc(corpo)

    centro = Frame(corpo)
    centro.pack(pady=10)

    Label(corpo, text="Gerenciador de Alunos", font=("Calibri", 16), background=BRANCO, foreground=AZUL).pack(pady=5)
    
    Label(corpo, text="Buscar Aluno:",font=("Montserrat", 9, "italic"), style='TLabel').pack(padx=10,anchor='w')

    busca_frame = Frame(corpo)
    busca_frame.pack(fill='x', pady=(0, 10))

    entrada_busca = tk.Entry(busca_frame, font=('Montserrat', 12), width=35)
    entrada_busca.pack(side='left', padx=(10, 5), pady=5)

    Button(busca_frame, text="Buscar 🔍", command=lambda: resultado_label.config(text=mostrar_busca_aluno(entrada_busca.get())), style='Small.TButton', cursor='hand2').pack(side='left')

    resultado_frame = Frame(corpo, style='TFrame')
    resultado_frame.pack(fill='both', expand=True, pady=(20,0))

    resultado_label = Label(resultado_frame, text="Resultados aparecerão aqui...", style='TLabel', justify='left')
    resultado_label.pack(anchor='nw')

    Button(corpo, text="Adicionar Novo Aluno", command=cadastrar_aluno, width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Editar Aluno", command=editar_aluno2, width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Remover Aluno", command=remover_aluno2, width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Voltar", command=janela.destroy, width=5, style='Sair.TButton').pack(pady=10)



###GERENCIADOR DE TURMAS
def abrir_gerenciador_turmas():
    janela = tk.Toplevel()
    janela.title("Gerenciador de Turmas")
    janela.attributes('-fullscreen', True)
    janela.configure(bg=BRANCO)

    corpo = Frame(janela, style='TFrame')
    corpo.pack(pady=20, fill='both', expand=True)

    logodoc(corpo)

    Label(corpo, text="Gerenciador de Turmas", font=("Calibri", 16), background=BRANCO, foreground=AZUL).pack(pady=5)

    # --- BOTÕES PRINCIPAIS ---
    Button(corpo, text="Listar Turmas", command=lambda: abrir_listar_turmas(janela), width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Adicionar Nova Turma", command=lambda: adicionar_turma(janela), width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Remover Turma", command=lambda: remover_turma_interface(janela), width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Voltar", command=janela.destroy, width=5, style='Sair.TButton').pack(pady=10)


# --- JANELA SECUNDÁRIA: LISTAR / BUSCAR TURMAS ---
def abrir_listar_turmas(janela=None): 
    janela_lista = tk.Toplevel()
    janela_lista.title("Listar Turmas")
    janela_lista.geometry("900x600")
    janela_lista.configure(bg=BRANCO)

    corpo = Frame(janela_lista, style='TFrame')
    corpo.pack(pady=20, fill='both', expand=True)

    Label(corpo, text="Listagem de Turmas", font=("Calibri", 16), background=BRANCO, foreground=AZUL).pack(pady=10)

    resultado_frame = Frame(corpo, style='TFrame')
    resultado_frame.pack(fill='both', expand=True, padx=10, pady=(20, 0))

    colunas = ("nome", "professor", "qtd_alunos", "limite")
    tabela = ttk.Treeview(resultado_frame, columns=colunas, show="headings", height=10)
    tabela.heading("nome", text="Nome da Turma")
    tabela.heading("professor", text="Professor")
    tabela.heading("qtd_alunos", text="Qtd. de Alunos")
    tabela.heading("limite", text="Limite")

    tabela.column("nome", width=200)
    tabela.column("professor", width=200)
    tabela.column("qtd_alunos", width=150, anchor="center")
    tabela.column("limite", width=100, anchor="center")
    tabela.pack(fill='both', expand=True)

    def atualizar_tabela():
        for linha in tabela.get_children():
            tabela.delete(linha)

        turmas = listar_turmas()
        for turma in turmas:
            tabela.insert("", "end", values=(
                turma["nome"],
                turma["professor"],
                len(turma["lista"]),
                turma["limite"]
            ))

    atualizar_tabela()

    botoes_frame = Frame(corpo, style='TFrame')
    botoes_frame.pack(pady=20)

    Button(botoes_frame, text="Voltar", command=janela_lista.destroy, style='Sair.TButton', width=10).pack(side='left', padx=10)


# --- ADICIONAR TURMA ---
def adicionar_turma(pai):
    professores = listar_professores()
    alunos = listar_alunos()

    if not professores:
        messagebox.showwarning("Aviso", "Nenhum professor encontrado.")
        return

    # Remove alunos já vinculados a alguma turma
    alunos_disponiveis = [a for a in alunos if not aluno_em_turma(a["ra"])]

    janela_add = tk.Toplevel(pai)
    janela_add.title("Nova Turma")
    janela_add.geometry("600x600")
    janela_add.configure(bg=BRANCO)

    corpo = Frame(janela_add, style='TFrame')
    corpo.pack(pady=20, fill='both', expand=True)

    Label(corpo, text="Nova Turma", font=("Calibri", 16), background=BRANCO, foreground=AZUL).pack(pady=10)

    # Nome automático da turma
    turmas_existentes = listar_turmas()
    prefixo = "1"
    sufixo = chr(65 + len(turmas_existentes))
    nome_turma = f"{prefixo}{sufixo}"

    Label(corpo, text=f"Nome da Turma: {nome_turma}", font=("Montserrat", 10, "bold"), background=BRANCO, foreground="black").pack(pady=5)

    # Campo Professor
    Label(corpo, text="Professor:", font=("Montserrat", 9, "italic"), background=BRANCO).pack(padx=10, anchor='w')
    combo_prof = ttk.Combobox(corpo, values=professores, state="readonly", width=40)
    combo_prof.pack(pady=5)

    # Campo Alunos
    Label(corpo, text="Selecione Alunos:", font=("Montserrat", 9, "italic"), background=BRANCO).pack(padx=10, anchor='w')

    lista = tk.Listbox(corpo, selectmode="multiple", width=50, height=10, font=('Montserrat', 10))
    for a in alunos_disponiveis:
        lista.insert(tk.END, f"{a['nome']} - {a['ra']}")
    lista.pack(pady=5)

    def confirmar():
        professor = combo_prof.get()
        indices = lista.curselection()
        alunos_sel = [alunos_disponiveis[i] for i in indices]

        if not professor:
            continuar = messagebox.askyesno(
                "Sem Professor",
                "Nenhum professor foi selecionado.\nDeseja criar a turma mesmo assim?"
            )
            if not continuar:
                return
            professor = "Não definido"

        if not alunos_sel:
            continuar = messagebox.askyesno(
                "Sem Alunos",
                "Nenhum aluno foi selecionado.\nDeseja criar a turma mesmo assim?"
            )
            if not continuar:
                return

        # 🔹 Salva com o nome gerado na tela
        turmas = listar_turmas()
        nova_turma = {
            "nome": nome_turma,
            "professor": professor,
            "limite": 30,
            "lista": [a["ra"] for a in alunos_sel]
        }
        turmas.append(nova_turma)
        salvar_turmas(turmas)

        messagebox.showinfo("Sucesso", f"Turma '{nome_turma}' criada com sucesso!")
        janela_add.destroy()

    Button(corpo, text="Criar Turma", command=confirmar, width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Cancelar", command=janela_add.destroy, width=10, style='Sair.TButton').pack(pady=10)
# --- REMOVER TURMA ---
def remover_turma_interface(pai):
    turmas = listar_turmas()
    nomes = [t["nome"] for t in turmas]

    if not nomes:
        messagebox.showwarning("Aviso", "Nenhuma turma cadastrada.")
        return

    janela_remover = tk.Toplevel(pai)
    janela_remover.title("Remover Turma")
    janela_remover.geometry("600x400")
    janela_remover.configure(bg=BRANCO)

    corpo = Frame(janela_remover, style='TFrame')
    corpo.pack(pady=20, fill='both', expand=True)

    logodoc(corpo)  # usa a mesma logo que você usa em adicionar_turma

    Label(
        corpo, text="Remover Turma", 
        font=("Calibri", 16), 
        background=BRANCO, 
        foreground=AZUL
    ).pack(pady=10)

    Label(
        corpo, text="Selecione a turma para excluir:", 
        font=("Montserrat", 9, "italic"), 
        style='TLabel'
    ).pack(padx=10, anchor='w')

    combo_turma = ttk.Combobox(corpo, values=nomes, state="readonly", width=40)
    combo_turma.pack(pady=5)

    def confirmar_exclusao():
        turma = combo_turma.get()
        if not turma:
            messagebox.showwarning("Aviso", "Selecione uma turma.")
            return

        excluir_turma(turma)
        messagebox.showinfo("Sucesso", f"Turma '{turma}' removida com sucesso.")
        janela_remover.destroy()

    Button(
        corpo, text="Remover Turma", 
        command=confirmar_exclusao, 
        width=25, style='TButton'
    ).pack(pady=10)

    Button(
        corpo, text="Cancelar", 
        command=janela_remover.destroy, 
        width=10, style='Sair.TButton'
    ).pack(pady=10)

###GERENCIADOR DE AULAS
def _data_por_extenso(dt: date):
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]
    return f"{dt.day} de {meses[dt.month - 1]} de {dt.year}"


# --- GERENCIADOR DE AULAS ---
def abrir_gerenciador_aulas():
    janela = tk.Toplevel()
    janela.title("Gerenciador de Aulas")
    janela.attributes('-fullscreen', True)
    janela.configure(bg=BRANCO)

    corpo = Frame(janela, style='TFrame')
    corpo.pack(pady=20, fill='both', expand=True)

    logodoc(corpo)  # Usa a mesma função da logo

    Label(corpo, text="Gerenciador de Aulas", font=("Calibri", 16), background=BRANCO, foreground=AZUL).pack(pady=5)

    Button(corpo, text="Listar Aulas", command=lambda: abrir_listar_aulas(janela), width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Adicionar Nova Aula", command=lambda: adicionar_aula_interface(janela), width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Editar Aula", command=lambda: editar_aula_interface(janela), width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Remover Aula", command=lambda: remover_aula_interface(janela), width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Voltar", command=janela.destroy, width=5, style='Sair.TButton').pack(pady=10)


# --- LISTAR AULAS ---
def abrir_listar_aulas(pai=None):
    janela_lista = tk.Toplevel()
    janela_lista.title("Listar Aulas")
    janela_lista.geometry("900x600")
    janela_lista.configure(bg=BRANCO)

    corpo = Frame(janela_lista, style='TFrame')
    corpo.pack(pady=20, fill='both', expand=True)

    Label(corpo, text="Listagem de Aulas", font=("Calibri", 16), background=BRANCO, foreground=AZUL).pack(pady=10)

    resultado_frame = Frame(corpo, style='TFrame')
    resultado_frame.pack(fill='both', expand=True, padx=10, pady=(20, 0))

    colunas = ("turma", "data", "conteudo")
    tabela = ttk.Treeview(resultado_frame, columns=colunas, show="headings", height=10)
    tabela.heading("turma", text="Turma")
    tabela.heading("data", text="Data")
    tabela.heading("conteudo", text="Conteúdo")

    tabela.column("turma", width=150, anchor="center")
    tabela.column("data", width=150, anchor="center")
    tabela.column("conteudo", width=500)
    tabela.pack(fill='both', expand=True)

    def atualizar_tabela():
        for linha in tabela.get_children():
            tabela.delete(linha)

        aulas = listar_aulas()
        for aula in aulas:
            tabela.insert("", "end", values=(aula["turma"], aula["data"], aula["conteudo"]))

    atualizar_tabela()

    Button(corpo, text="Voltar", command=janela_lista.destroy, width=10, style='Sair.TButton').pack(pady=20)


# --- ADICIONAR AULA ---
def adicionar_aula_interface(pai):
    turmas = [t["nome"] for t in listar_turmas()]
    if not turmas:
        messagebox.showwarning("Aviso", "Nenhuma turma cadastrada.")
        return

    janela_add = tk.Toplevel(pai)
    janela_add.title("Adicionar Aula")
    janela_add.geometry("600x600")
    janela_add.configure(bg=BRANCO)

    corpo = Frame(janela_add, style='TFrame')
    corpo.pack(pady=20, fill='both', expand=True)

    logodoc(corpo)
    Label(corpo, text="Adicionar Aula", font=("Calibri", 16), background=BRANCO, foreground=AZUL).pack(pady=10)

    Label(corpo, text="Selecione a Turma:", font=("Montserrat", 9, "italic"), background=BRANCO).pack(padx=10, anchor='w')
    combo_turma = ttk.Combobox(corpo, values=turmas, state="readonly", width=40)
    combo_turma.pack(pady=5)

    Label(corpo, text="Conteúdo da Aula:", font=("Montserrat", 9, "italic"), background=BRANCO).pack(padx=10, anchor='w')
    texto_conteudo = tk.Text(corpo, width=60, height=10, font=('Montserrat', 10))
    texto_conteudo.pack(pady=5)

    def confirmar():
        turma = combo_turma.get()
        conteudo = texto_conteudo.get("1.0", tk.END).strip()

        if not turma or not conteudo:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
            return

        confirmar = messagebox.askyesno("Confirmação", f"Deseja adicionar esta aula para a turma {turma}?")
        if confirmar:
            adicionar_aula(turma, conteudo)
            janela_add.destroy()

    Button(corpo, text="Salvar Aula", command=confirmar, width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Cancelar", command=janela_add.destroy, width=10, style='Sair.TButton').pack(pady=10)


# --- EDITAR AULA ---
def editar_aula_interface(pai):
    aulas = listar_aulas()
    if not aulas:
        messagebox.showwarning("Aviso", "Nenhuma aula cadastrada.")
        return

    janela_edit = tk.Toplevel(pai)
    janela_edit.title("Editar Aula")
    janela_edit.geometry("700x500")
    janela_edit.configure(bg=BRANCO)

    corpo = Frame(janela_edit, style='TFrame')
    corpo.pack(pady=20, fill='both', expand=True)

    logodoc(corpo)
    Label(corpo, text="Editar Aula", font=("Calibri", 16), background=BRANCO, foreground=AZUL).pack(pady=10)

    opcoes = [f"{a['turma']} - {a['data']}" for a in aulas]
    Label(corpo, text="Selecione a Aula:", font=("Montserrat", 9, "italic"), background=BRANCO).pack(anchor='w', padx=10)
    combo_aula = ttk.Combobox(corpo, values=opcoes, state="readonly", width=60)
    combo_aula.pack(pady=5)

    texto_conteudo = tk.Text(corpo, width=70, height=10, font=('Montserrat', 10))
    texto_conteudo.pack(pady=5)

    def carregar_conteudo(event=None):
        selecao = combo_aula.get()
        if not selecao:
            return
        turma, data = selecao.split(" - ")
        for a in aulas:
            if a["turma"] == turma and a["data"] == data:
                texto_conteudo.delete("1.0", tk.END)
                texto_conteudo.insert(tk.END, a["conteudo"])
                break

    combo_aula.bind("<<ComboboxSelected>>", carregar_conteudo)

    def salvar_edicao():
        selecao = combo_aula.get()
        if not selecao:
            messagebox.showwarning("Aviso", "Selecione uma aula.")
            return
        turma, data = selecao.split(" - ")
        novo_conteudo = texto_conteudo.get("1.0", tk.END).strip()
        if not novo_conteudo:
            messagebox.showwarning("Aviso", "O conteúdo não pode estar vazio.")
            return
        confirmar = messagebox.askyesno("Confirmação", f"Deseja salvar as alterações na aula de {data}?")
        if confirmar:
            editar_aula(turma, data, novo_conteudo)
            janela_edit.destroy()

    Button(corpo, text="Salvar Alterações", command=salvar_edicao, width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Cancelar", command=janela_edit.destroy, width=10, style='Sair.TButton').pack(pady=10)


# --- REMOVER AULA ---
def remover_aula_interface(pai):
    aulas = listar_aulas()
    if not aulas:
        messagebox.showwarning("Aviso", "Nenhuma aula cadastrada.")
        return

    janela_remover = tk.Toplevel(pai)
    janela_remover.title("Remover Aula")
    janela_remover.geometry("600x400")
    janela_remover.configure(bg=BRANCO)

    corpo = Frame(janela_remover, style='TFrame')
    corpo.pack(pady=20, fill='both', expand=True)

    logodoc(corpo)
    Label(corpo, text="Remover Aula", font=("Calibri", 16), background=BRANCO, foreground=AZUL).pack(pady=10)

    opcoes = [f"{a['turma']} - {a['data']}" for a in aulas]
    combo_aula = ttk.Combobox(corpo, values=opcoes, state="readonly", width=50)
    combo_aula.pack(pady=5)

    def confirmar_remocao():
        selecao = combo_aula.get()
        if not selecao:
            messagebox.showwarning("Aviso", "Selecione uma aula.")
            return
        turma, data = selecao.split(" - ")
        confirmar = messagebox.askyesno("Confirmação", f"Deseja remover a aula do dia {data} da turma {turma}?")
        if confirmar:
            remover_aula(turma, data)
            janela_remover.destroy()

    Button(corpo, text="Remover Aula", command=confirmar_remocao, width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Cancelar", command=janela_remover.destroy, width=10, style='Sair.TButton').pack(pady=10)

##AULAS ALUNOS
def abrir_aulas_aluno(ra_aluno):
    # Verifica em qual turma esse aluno está
    turma_encontrada = None
    if not os.path.exists("turmas.txt"):
        messagebox.showwarning("Aviso", "Nenhuma turma cadastrada.")
        return

    with open("turmas.txt", "r", encoding="utf-8") as arq:
        for linha in arq:
            dados = linha.strip().split(";")
            if len(dados) >= 4:
                nome_turma, professor, limite, alunos = dados[0], dados[1], dados[2], dados[3]
                lista_alunos = [x.strip() for x in alunos.split(",") if x.strip()]
                if ra_aluno in lista_alunos:
                    turma_encontrada = nome_turma.strip()
                    break
    if not turma_encontrada:
        messagebox.showwarning("Aviso", "Você ainda não está vinculado a nenhuma turma.")
        return


    # Cria a janela
    janela = tk.Toplevel()
    janela.title("Aulas da Turma")
    janela.attributes('-fullscreen', True)
    janela.configure(bg=BRANCO)

    corpo = Frame(janela, style='TFrame')
    corpo.pack(pady=20, fill='both', expand=True)

    logodoc(corpo)

    Label(corpo, text=f"Aulas da Turma {turma_encontrada}", font=("Calibri", 16),
          background=BRANCO, foreground=AZUL).pack(pady=5)

    # Frame de exibição
    frame_lista = Frame(corpo, style='TFrame')
    frame_lista.pack(fill='both', expand=True, padx=20, pady=10)

    texto = tk.Text(frame_lista, wrap="word", font=("Montserrat", 10),
                    width=80, height=20, bg="#F7F7F7", state="normal")
    texto.pack(padx=10, pady=10)
    texto.insert("end", f"🗓️ Aulas registradas para {turma_encontrada}:\n\n")

    # Lê as aulas da turma no arquivo aulas.txt
    try:
        with open("aulas.txt", "r", encoding="utf-8") as arq:
            aulas = [l.strip() for l in arq.readlines()]
    except FileNotFoundError:
        aulas = []

    encontrou = False
    for aula in aulas:
        dados = [x.strip() for x in aula.split("|")]  # remove espaços extras
    if len(dados) >= 3:
        turma, data, conteudo = dados[0], dados[1], dados[2]
        if turma == turma_encontrada:
            texto.insert("end", f"📅 {data}\n{conteudo}\n\n")
            encontrou = True

    if not encontrou:
        texto.insert("end", "Nenhuma aula registrada ainda.\n")

    texto.config(state="disabled")  # Somente leitura

    Button(corpo, text="Voltar", command=janela.destroy,
           width=15, style='Sair.TButton').pack(pady=20)
###TELA INICIAL
def abrir_tela_inicial():
    root = tk.Tk()
    root.title("ELEVE - Página Inicial")
    root.geometry("400x550+100+100")
    root.configure(bg=BRANCO)

    borda = Frame(root, style='Borda.TFrame')
    borda.pack(fill='x', expand=True)

    logo(borda)

    centro = Frame(borda)
    centro.pack(pady=10)
    # Estilos já existentes
    style = Style()
    style.theme_use('default')
    style.configure('TFrame', background=BRANCO)
    
    style.configure('TButton', padding=(60, 10), font=('Montserrat', 12, 'bold'), foreground=BRANCO, background=VERDE, relief='flat')
    style.map('TButton',
              background=[('active', VERDECLARO)],
              foreground=[('active', BRANCO)])
    style.configure('Small.TButton', padding=(0,-3), font=('Montserrat', 8), foreground=AZUL, background=BRANCO, relief='flat')
    frame = Frame(root, style='TFrame')
    frame.pack(expand=True)

    Label(frame, text="Selecione seu perfil:", font=("Montserrat", 14, "bold"), background=BRANCO, foreground=AZUL).pack(pady=(20, 5))

    Button(frame, text="Sou Docente", command=lambda: [root.withdraw(), abrir_login_docente()], style='TButton').pack(pady=10)
    Button(frame, text="Sou Aluno", command=lambda: [root.withdraw(), abrir_login_aluno()], style='TButton').pack(pady=10)
    Button(frame, text='SAIR AGORA?', command=root.destroy, style='Small.TButton', cursor='hand2').pack(side='left')



if __name__ == "__main__":
    abrir_tela_inicial()
    tk.mainloop()  # Só um mainloop aqui
