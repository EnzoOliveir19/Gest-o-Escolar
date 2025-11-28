import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog, PhotoImage, END
from tkinter.ttk import Frame, Label, Button, Entry, Separator, Style, Combobox
from tkinter import Listbox, Scrollbar
from tkinter.scrolledtext import ScrolledText
from back import *
from chatbot import *

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

    Label(centro, text='Nome de Usuário:').pack(anchor='w', pady=(10,0))
    et_email = Entry(centro, font=('Montserrat', 12, 'bold'), foreground='#666')
    et_email.pack(fill='x')
    Separator(centro, orient='horizontal').pack(fill='x')

    Label(centro, text='Senha:').pack(anchor='w', pady=(10,0))
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
    Button(corpo, text="Aulas",command=abrir_gerenciador_aulas, width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Inserir Notas", command=abrir_janela_inserir_notas, width=25, style='TButton').pack(pady=10) #NOVO
    Button(corpo, text="Relatório", command=abrir_visualizar_boletim_docente, width=25, style='TButton').pack(pady=10) #NOVO
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
    Button(corpo, text="Aulas",command=abrir_gerenciador_aulas, width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Inserir Notas", command=abrir_janela_inserir_notas, width=25, style='TButton').pack(pady=10) #NOVO
    Button(corpo, text="Relatório", command=abrir_visualizar_boletim_docente, width=25, style='TButton').pack(pady=10) #NOVO
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
    Button(corpo, text="Aulas",command=abrir_gerenciador_aulas, width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Inserir Notas", command=abrir_janela_inserir_notas, width=25, style='TButton').pack(pady=10) #NOVO
    Button(corpo, text="Relatório", command=abrir_visualizar_boletim_docente, width=25, style='TButton').pack(pady=10) #NOVO AQUI TBM
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

#NOVO
    Button(
        corpo,
        text="Relatório",
        command=lambda: abrir_visualizar_boletim_aluno(ra),  
        width=25,
        style='TButton'
    ).pack(pady=10)
#FIM NOVO

    Button(
        corpo,
        text="I.A Eleve",
        command=abrir_chatbot,
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
    janela.attributes('-fullscreen',True)
    janela.configure(bg=BRANCO)

    corpo = Frame(janela, style='TFrame')
    corpo.pack(pady=20, fill='both', expand=True)

    logodoc(corpo)

    centro = Frame(corpo)
    centro.pack(pady=10)

    Label(corpo, text="Gerenciador de Alunos", font=("Calibri", 16), background=BRANCO, foreground=AZUL).pack(pady=5)
    
    # ---BOTÕES PRINCIPAIS
    Button(corpo, text="Listar Turmas", command=lambda: abrir_listar_turmas(janela),width=25,style='TButton').pack(pady=10)
    Button(corpo, text="Adicionar Nova Turma", command=lambda: adicionar_turma(janela),width=25,style='TButton').pack(pady=10)
    Button(corpo, text="Remover Turma", command=lambda: remover_turma_interface(janela),width=25,style='TButton').pack(pady=10)
    Button(corpo, text="Voltar", command=janela.destroy,width=5,style='Sair.TButton').pack(pady=10)
    
    
# --- LISTAR TURMAS ---
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

# --- REMOVER TURMA
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

    logodoc(corpo)

    Label(corpo, text="Remover Turma", font=("Calibri", 16), background=BRANCO, foreground=AZUL).pack(pady=10)
    Label(corpo, text="Selecione a turma para excluir", font=("Montserrat", 9, "italic"), style='TLabel').pack(padx=10, anchor='w')

    combo_turma = ttk.Combobox(corpo, values=nomes, state="readonly", width=40)
    combo_turma.pack(pady=5)

    def confirmar_exclusao():
        turma = combo_turma.get()
        if not turma:
            messagebox.showwarning("Aviso", "Selecione uma turma.")
            return

        confirmar = messagebox.askyesno("Confirmação", f"Deseja realmente excluir a turma '{turma}'?")
        if confirmar:
            excluir_turma(turma)
            messagebox.showinfo("Sucesso", f"A turma '{turma}' foi removida com sucesso.")
            janela_remover.destroy()

    Button(corpo, text="Remover Turma", command=confirmar_exclusao, width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Cancelar", command=janela_remover.destroy, width=10, style='Sair.TButton').pack(pady=10)

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
    janela_edit.geometry("700x600")
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
    
    #######3 GERENCIADOR DE NOTAS (BOLETIM) NOVO

# Esta é a janela principal que o docente verá 
def abrir_janela_inserir_notas():
    # 1. Solicita o RA
    ra = simpledialog.askstring("Inserir Notas", "Digite o RA do aluno:")
    if not ra:
        return # Cancelou

    # 2. Verifica se o RA existe no alunos.txt
    aluno = buscar_aluno_por_ra(ra)
    if not aluno:
        messagebox.showerror("Erro", f"Aluno com RA '{ra}' não encontrado no sistema.")
        return
    
    # 3. Verifica se o boletim já existe
    dados_atuais = None
    if verificar_boletim_existente(ra):
        resposta = messagebox.askyesno("Boletim Existente",
                                       f"O boletim para {aluno['nome']} (RA: {ra}) já foi criado.\n\n"
                                       "Deseja editar as notas existentes?")
        if not resposta:
            return # Escolheu "Não"
        
        # Se sim, carrega os dados atuais para preencher os campos
        dados_atuais = carregar_dados_boletim(ra)
    
    # Se 'dados_atuais' for None, é um boletim novo.
    # Se tiver dados, é uma edição.
    
    # Chama a sub-janela para de fato mostrar os campos
    criar_janela_edicao_notas(ra, aluno['nome'], dados_atuais)


# Esta é a janela Toplevel com os campos de entrada (Entry) 
def  criar_janela_edicao_notas(ra, nome_aluno, dados_atuais=None):
    
    janela_notas = tk.Toplevel()
    janela_notas.title(f"Lançamento de Notas - {nome_aluno} (RA: {ra})")
    janela_notas.geometry("600x550")
    janela_notas.configure(bg=BRANCO)

    corpo = Frame(janela_notas, style='TFrame')
    corpo.pack(pady=20, fill='both', expand=True)

    logodoc(corpo) # Mantendo a identidade visual
    
    Label(corpo, text=f"Editando notas de: {nome_aluno}", font=("Calibri", 16), background=BRANCO, foreground=AZUL).pack(pady=5)
    Label(corpo, text="Insira as notas (ex: 8.5) e a frequência (ex: 80 para 80%)", font=("Montserrat", 9, "italic"), style='TLabel').pack()

    # Frame para os cabeçalhos da tabela
    frame_cabecalho = Frame(corpo, style='TFrame')
    frame_cabecalho.pack(pady=(10, 0), fill='x', padx=50)
    
    # Define pesos das colunas para alinhamento
    frame_cabecalho.grid_columnconfigure(0, weight=2) # Matéria
    frame_cabecalho.grid_columnconfigure(1, weight=1) # N1
    frame_cabecalho.grid_columnconfigure(2, weight=1) # N2
    frame_cabecalho.grid_columnconfigure(3, weight=1) # N3
    frame_cabecalho.grid_columnconfigure(4, weight=1) # Frequência
    
    # Cabeçalhos
    Label(frame_cabecalho, text="Matéria", font=("Montserrat", 10, "bold"), background=BRANCO).grid(row=0, column=0, sticky='w')
    Label(frame_cabecalho, text="N1", font=("Montserrat", 10, "bold"), background=BRANCO).grid(row=0, column=1)
    Label(frame_cabecalho, text="N2", font=("Montserrat", 10, "bold"), background=BRANCO).grid(row=0, column=2)
    Label(frame_cabecalho, text="N3", font=("Montserrat", 10, "bold"), background=BRANCO).grid(row=0, column=3)
    Label(frame_cabecalho, text="Frequência (%)", font=("Montserrat", 10, "bold"), background=BRANCO).grid(row=0, column=4)

    # Frame principal para as matérias
    frame_materias = Frame(corpo, style='TFrame')
    frame_materias.pack(pady=5, fill='x', padx=50)
    
    # Define pesos das colunas aqui também
    frame_materias.grid_columnconfigure(0, weight=2)
    frame_materias.grid_columnconfigure(1, weight=1)
    frame_materias.grid_columnconfigure(2, weight=1)
    frame_materias.grid_columnconfigure(3, weight=1)
    frame_materias.grid_columnconfigure(4, weight=1)

    materias = ["Português", "Matemática", "Geografia", "História"]
    # 'entradas' vai guardar os 16 objetos Entry para podermos ler depois
    entradas = {} 

    # Cria as 4 linhas de matérias
    for i, materia in enumerate(materias):
        # Armazena { "materia": "Portugues", "n1": "0", "n2": "0", ... }
        dados_materia = {}
        
        # Verifica se estamos editando e se há dados para essa matéria
        if dados_atuais:
            for d in dados_atuais:
                if d['materia'] == materia:
                    dados_materia = d
                    break
        
        # Label da Matéria
        Label(frame_materias, text=materia, font=("Calibri", 12), background=BRANCO).grid(row=i, column=0, sticky='w', pady=5)
        
        # Entry N1
        ent_n1 = Entry(frame_materias, font=('Montserrat', 12), width=5)
        ent_n1.insert(0, dados_materia.get('n1', '')) # Pega o valor salvo ou usa '0'
        ent_n1.grid(row=i, column=1, padx=5)
        
        # Entry N2
        ent_n2 = Entry(frame_materias, font=('Montserrat', 12), width=5)
        ent_n2.insert(0, dados_materia.get('n2', ''))
        ent_n2.grid(row=i, column=2, padx=5)
        
        # Entry N3
        ent_n3 = Entry(frame_materias, font=('Montserrat', 12), width=5)
        ent_n3.insert(0, dados_materia.get('n3', ''))
        ent_n3.grid(row=i, column=3, padx=5)
        
        # Entry Frequência
        ent_freq = Entry(frame_materias, font=('Montserrat', 12), width=5)
        ent_freq.insert(0, dados_materia.get('frequencia', ''))
        ent_freq.grid(row=i, column=4, padx=5)
        
        # Guarda os objetos Entry para ler depois
        entradas[materia] = (ent_n1, ent_n2, ent_n3, ent_freq)

    # --- Ação do Botão Salvar ---
    def acao_salvar():
        # 1. Coletar os 16 valores da tela
        dados_para_salvar = []
        for materia, campos_entry in entradas.items():
            n1 = campos_entry[0].get()
            n2 = campos_entry[1].get()
            n3 = campos_entry[2].get()
            freq = campos_entry[3].get()
            
            dados_para_salvar.append({
                "materia": materia,
                "n1": n1,
                "n2": n2,
                "n3": n3,
                "frequencia": freq
            })
        
        # 2. Mandar para o back.py salvar
        sucesso = salvar_boletim_aluno(ra, dados_para_salvar)
        
        if sucesso:
            messagebox.showinfo("Sucesso", f"Boletim do aluno {nome_aluno} (RA: {ra}) foi salvo com sucesso!")
            janela_notas.destroy()
        # Se der erro, a própria função 'salvar_boletim_aluno' já mostra o messagebox de erro.

    # --- Botões de Ação ---
    frame_botoes = Frame(corpo, style='TFrame')
    frame_botoes.pack(pady=20)
    
    Button(frame_botoes, text="Salvar Boletim", command=acao_salvar, style='TButton', width=20).pack(side='left', padx=10)
    Button(frame_botoes, text="Cancelar", command=janela_notas.destroy, style='Sair.TButton', width=10).pack(side='left', padx=10)

def abrir_visualizar_boletim_docente():
    """Pede um RA e exibe o arquivo de boletim (CSV) numa tela de texto."""
    
    # 1. Solicita o RA
    ra = simpledialog.askstring("Visualizar Boletim", "Digite o RA do aluno:")
    if not ra:
        return # Cancelou

    # 2. Verifica se o RA existe
    aluno = buscar_aluno_por_ra(ra)
    if not aluno:
        messagebox.showerror("Erro", f"Aluno com RA '{ra}' não encontrado.")
        return
        
    # 3. Verifica se o boletim foi gerado
    if not verificar_boletim_existente(ra):
        messagebox.showwarning("Aviso", f"O boletim para {aluno['nome']} (RA: {ra}) ainda não foi gerado.")
        return

    # 4. Se chegou aqui, o boletim existe. Vamos lê-lo.
    nome_arquivo = f"boletim_{ra}.csv"
    conteudo_boletim = ""
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            conteudo_boletim = f.read()
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao ler o arquivo {nome_arquivo}.\nErro: {e}")
        return

    # 5. Cria a janela para exibir o texto
    janela_boletim = tk.Toplevel()
    janela_boletim.title(f"Boletim - {aluno['nome']} (RA: {ra})")
    janela_boletim.geometry("750x550")
    janela_boletim.configure(bg=BRANCO)

    corpo = Frame(janela_boletim, style='TFrame')
    corpo.pack(pady=10, padx=10, fill='both', expand=True)

    Label(corpo, text=f"Visualizando Boletim", font=("Calibri", 16), background=BRANCO, foreground=AZUL).pack(pady=5)

    # Área de texto com rolagem
    texto_area = ScrolledText(corpo, wrap=tk.WORD, font=('Courier New', 10), bg=CINZA, fg='black')
    texto_area.pack(pady=10, padx=10, fill='both', expand=True)
    texto_area.insert(tk.END, conteudo_boletim)
    texto_area.config(state=tk.DISABLED) # Bloqueia a edição

    Button(corpo, text="Fechar", command=janela_boletim.destroy, width=10, style='Sair.TButton').pack(pady=10)
    
def abrir_visualizar_boletim_aluno(ra_aluno):
    """
    Exibe o boletim formatado para o aluno logado.
    Calcula o status final (Aprovado/Reprovado).
    """
    
    # 1. Verifica se o boletim existe
    if not verificar_boletim_existente(ra_aluno):
        messagebox.showwarning("Boletim", "Seu boletim ainda não foi gerado pela secretaria.")
        return

    # 2. Carrega o nome do aluno (para o título da janela)
    aluno = buscar_aluno_por_ra(ra_aluno)
    nome_aluno = aluno['nome'] if aluno else f"RA: {ra_aluno}"

    # 3. Lê o arquivo CSV e prepara a exibição
    nome_arquivo = f"boletim_{ra_aluno}.csv"
    conteudo_formatado = f"Boletim de: {nome_aluno}\nRA: {ra_aluno}\n\n"
    conteudo_formatado += "="*50 + "\n"
    
    status_geral = "Aprovado" # Assume aprovado até encontrar uma reprovação
    
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            # Pula o cabeçalho
            cabecalho = next(f).strip().split(';')
            
            # Formata o cabeçalho para exibição
            # Usando f-string com alinhamento: <20 (20 espaços, alinhado à esquerda)
            conteudo_formatado += f"{cabecalho[0]:<15} {cabecalho[1]:<5} {cabecalho[2]:<5} {cabecalho[3]:<5} {cabecalho[4]:<10} {cabecalho[5]:<7} {cabecalho[6]:<10}\n"
            conteudo_formatado += "-"*70 + "\n"

            for linha in f:
                partes = linha.strip().split(";")
                if len(partes) < 7:
                    continue
                
                mat, n1, n2, n3, freq, media, status = partes
                
                # Formata a linha da matéria
                conteudo_formatado += f"{mat:<15} {n1:<5} {n2:<5} {n3:<5} {freq:<10} {media:<7} {status:<10}\n"
                
                # Verifica o status geral
                if status == "Reprovado":
                    status_geral = "Reprovado"

    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao ler seu boletim.\nErro: {e}")
        return

    # Adiciona o Resumo Final
    conteudo_formatado += "\n" + "="*50 + "\n"
    conteudo_formatado += "Resumo Final:\n"
    conteudo_formatado += f"Média da escola: 6.0\n"
    conteudo_formatado += f"Frequência mínima: 75%\n\n"
    
    if status_geral == "Aprovado":
        conteudo_formatado += "STATUS GERAL: APROVADO\n"
        conteudo_formatado += "Parabéns! Você atingiu todas as médias e frequências necessárias."
    else:
        conteudo_formatado += "STATUS GERAL: REPROVADO\n"
        conteudo_formatado += "Você não atingiu a média ou a frequência mínima em uma ou mais matérias e foi reprovado nelas."
        
    # 5. Cria a janela para exibir o texto
    janela_boletim = tk.Toplevel()
    janela_boletim.title(f"Meu Boletim - {nome_aluno}")
    janela_boletim.geometry("700x500")
    janela_boletim.configure(bg=BRANCO)

    corpo = Frame(janela_boletim, style='TFrame')
    corpo.pack(pady=10, padx=10, fill='both', expand=True)

    Label(corpo, text="Meu Boletim", font=("Calibri", 16), background=BRANCO, foreground=AZUL).pack(pady=5)

    texto_area = ScrolledText(corpo, wrap=tk.WORD, font=('Courier New', 11), bg=BRANCO, fg='black', relief='flat')
    texto_area.pack(pady=10, padx=10, fill='both', expand=True)
    texto_area.insert(tk.END, conteudo_formatado)
    texto_area.config(state=tk.DISABLED)

    Button(corpo, text="Fechar", command=janela_boletim.destroy, width=10, style='Sair.TButton').pack(pady=10)
#FIM NOVO

### --- AULAS DO ALUNO ---
def abrir_aulas_aluno(ra_aluno):
    # Verifica turma
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

    # Buscar aulas da turma
    aulas_turma = []
    if os.path.exists("aulas.txt"):
        with open("aulas.txt", "r", encoding="utf-8") as arq:
            for linha in arq:
                dados = linha.strip().split("|")
                if len(dados) >= 3:
                    nome_turma, data, conteudo = [x.strip() for x in dados[:3]]
                    if nome_turma == turma_encontrada:
                        aulas_turma.append(f"{data} - {conteudo}")

    if not aulas_turma:
        messagebox.showinfo("Aulas", "Nenhuma aula registrada para sua turma.")
        return
    


    # Exibir as aulas
    janela_aulas = tk.Toplevel()
    janela_aulas.title(f"Aulas - Turma {turma_encontrada}")
    janela_aulas.geometry("600x500")
    janela_aulas.configure(bg=BRANCO)

    corpo = Frame(janela_aulas, style='TFrame')
    corpo.pack(pady=20, fill='both', expand=True)

    Label(corpo, text=f"Aulas da Turma {turma_encontrada}", font=("Calibri", 14), background=BRANCO, foreground=AZUL).pack(pady=10)

    lista_aulas = tk.Listbox(corpo, width=80, height=20, font=("Montserrat", 10))
    for aula in aulas_turma:
        lista_aulas.insert(tk.END, aula)
    lista_aulas.pack(pady=5)


### --- TELA SOBRE O SISTEMA ---
def abrir_sobre_sistema(pai):
    janela = tk.Toplevel(pai)
    janela.title("Sobre o Sistema")
    janela.attributes('-fullscreen', True)
    janela.configure(bg=BRANCO)
    janela.resizable(False, False)

    corpo = tk.Frame(janela, bg=BRANCO)
    corpo.pack(fill="both", expand=True, padx=30, pady=30)

    logo(corpo)

    tk.Label(corpo, text="Sobre o Sistema", font=("Segoe UI", 18, "bold"), bg=BRANCO, fg=AZUL).pack(pady=(0, 15))

    texto_sobre = ( """💡 Um sistema completo de **gestão escolar**, 
desenvolvido para auxiliar no controle de alunos, usuários e relatórios acadêmicos. 
     
🚀 **Funcionalidades**
- 👨‍🎓 Cadastro e gerenciamento de alunos
- 🧾 Geração de boletins e relatórios (.txt, .exe, .c)
- 💬 Chatbot ELEVE — assistente virtual que ajuda na navegação
- 🧠 Integração entre módulos (frontend, backend e banco de dados)
- 🔐 Gerenciamento de usuários e permissões
- 🪶 Interface amigável e intuitiva

⚙️ **Tecnologias Utilizadas**

| Tecnologia | Descrição |
|-------------|------------|
| 🐍 Python 3.x | Linguagem principal do projeto |
| 🧩 Tkinter / PyQt | Criação da interface gráfica |
| 🤖 Chatbot (ELEVE) | Assistente virtual integrado |
| 🗂️ Manipulação de arquivos (.txt, .exe, .c) | Armazenamento e relatórios |
| 💾 Git & GitHub | Controle de versão e repositório |

👨‍💻 **Autores**
Enzo Gabriel, Pedro Bueno, Jhonatan Henrique, Renata, Luiz e Nickolas.

📘 Projeto acadêmico — Sistema de Gestão Escolar ELEVE 
💬 “Facilitando a administração escolar com tecnologia e automação.”
""" )

    frame_texto = tk.Frame(corpo, bg=BRANCO)
    frame_texto.pack(fill="both", expand=True)

    texto = tk.Text(frame_texto, wrap="word", font=("Segoe UI", 11), height=10, bg=BRANCO, relief="flat")
    texto.insert("1.0", texto_sobre)
    texto.config(state="disabled")

    scroll = tk.Scrollbar(frame_texto, command=texto.yview)
    texto.config(yscrollcommand=scroll.set)
    scroll.pack(side="right", fill="y")
    texto.pack(fill="both", expand=True)

    frame_botao = tk.Frame(janela, bg=BRANCO)
    frame_botao.pack(side="bottom", pady=20)

    ttk.Button(frame_botao, text="⬅ Voltar", command=janela.destroy, width=20).pack()
###TELA INICIAL
def abrir_tela_inicial():
    root = tk.Tk()
    root.title("ELEVE - Página Inicial")
    root.geometry("400x550+100+100")
    root.configure(bg=BRANCO)

    borda = Frame(root, style='Borda.TFrame')
    borda.pack(fill='x', expand=True)

    logo(borda)
    tk.Button(root, text="ℹ️", font=("Calibri", 18, "bold"), bg=BRANCO, fg=AZUL,
          activebackground=BRANCO, activeforeground=AZUL, bd=0, cursor="hand2",
          command=lambda: abrir_sobre_sistema(root)).place(relx=0.95, rely=0.05, anchor="ne")



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
