import tkinter as tk
from tkinter import messagebox, simpledialog, PhotoImage
from tkinter.ttk import Frame, Label, Button, Entry, Separator, Style
from PIL import Image, ImageTk
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
        logo_img = PhotoImage(file=r"C:\Users\Jhonatan\OneDrive\Desktop\PIM\logoeleve.PNG")
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
        logo_img = PhotoImage(file=r"C:\Users\Jhonatan\OneDrive\Desktop\PIM\logoalu.png")
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
        logo_img = PhotoImage(file=r"C:\Users\Jhonatan\OneDrive\Desktop\PIM\logodoc.png")
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
    Button(base, text='SAIR AGORA?', command=janela.destroy, style='Small.TButton', cursor='hand2').pack(side='left')

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
    Button(base, text='SAIR AGORA?', command=janela.destroy, style='Small.TButton', cursor='hand2').pack(side='left')

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
    Button(corpo, text="Gerenciar usuários", command=abrir_gerenciador_usuarios, width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Gerenciar Alunos", command=abrir_gerenciador_alunos,width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Turmas", width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Aulas", width=25, style='TButton').pack(pady=10)
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
    Button(corpo, text="Gerenciar Alunos", command=abrir_gerenciador_alunos,width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Turmas", width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Aulas", width=25, style='TButton').pack(pady=10)
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
    Button(corpo, text="Aulas", width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Relatório", width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Sair", command=janela.destroy, width=5, style='Sair.TButton').pack(pady=10)

###CRIACAO DE TELA DO ALUNO
def abrir_menu_aluno(nome_usuario,ra):
    janela = tk.Toplevel()
    janela.title("ELEVE - Area do Aluno")
    janela.attributes('-fullscreen', True)
    janela.configure(bg=BRANCO)

    logoalu(janela, aumentar=True)

    corpo = Frame(janela, style='TFrame')
    corpo.pack(pady=20, fill='both', expand=True)

    Label(corpo, text=f"Bem-vindo(a), {nome_usuario}\nRegistro do Aluno: {ra}", font=("Calibri", 14), background=BRANCO, foreground=AZUL).pack(pady=10)
    Button(corpo, text="Aulas", width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Relatório", width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Sair", command=janela.destroy, width=5, style='Sair.TButton').pack(pady=10)

###FAZER LOGIN
def fazer_login():
    usuario = et_email.get().strip()
    senha = et_senha.get().strip()

    # Se for um RA (4 dígitos numéricos), tenta login como aluno
    if usuario.isdigit() and len(usuario) == 4:
        nome_aluno = autenticar_alunos_por_ra_e_senha(usuario, senha)
        if nome_aluno:
            messagebox.showinfo("Login", f"Bem-vindo, {nome_aluno}!")
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
