import random
import os
import tkinter as tk
from tkinter import messagebox, simpledialog, PhotoImage
from tkinter.ttk import Frame, Label, Button, Entry, Separator, Style

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
    topo.pack(pady=5)
    try:
        logo_img = PhotoImage(file=r"C:\Users\Jhonatan\OneDrive\Desktop\PIM\logoeleve.PNG")
        logo_img = logo_img.subsample(2, 2)
        label_logo = Label(topo, image=logo_img, background=BRANCO)
        label_logo.image = logo_img  # manter referência
        label_logo.pack()
    except tk.TclError:
           return topo

###### CRIAR LOGO ALUNO
def logoalu(janela):
    topo = Frame(janela, style='Borda.TFrame')
    topo.pack(pady=5)
    try:
        logo_img = PhotoImage(file=r"C:\Users\Jhonatan\OneDrive\Desktop\PIM\logoalu.png")
        logo_img = logo_img.subsample(2, 2)
        label_logo = Label(topo, image=logo_img, background=BRANCO)
        label_logo.image = logo_img  # manter referência
        label_logo.pack()
    except tk.TclError:
           return topo

###### CRIAR LOGO DOCENTE
def logodoc(janela):
    topo = Frame(janela, style='Borda.TFrame')
    topo.pack(pady=5)
    try:
        logo_img = PhotoImage(file=r"C:\Users\Jhonatan\OneDrive\Desktop\PIM\logodoc.png")
        logo_img = logo_img.subsample(2, 2)
        label_logo = Label(topo, image=logo_img, background=BRANCO)
        label_logo.image = logo_img  # manter referência
        label_logo.pack()
    except tk.TclError:
           return topo    

# FUNCOES DE LOGIN, AUTENTICACAO 
def autenticar_usuario(usuario, senha):
    try:
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                parts = linha.strip().split(";")
                if len(parts) != 3:
                    continue
                u, s, cargo = parts
                if usuario == u and senha == s:
                    return u, cargo
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de usuários não encontrado.")
    return None


def autenticar_alunos(nome, senha, nasc, cpf, email, end, ra):
    try:
        with open("alunos.txt", "r", encoding="utf-8") as arquivo2:
            for linha in arquivo2:
                parts = linha.strip().split(";")
                if len(parts) != 7:
                    continue  # ignora linhas mal formatadas

                nome_arq, senha_arq, nasc_arq, cpf_arq, email_arq, end_arq, ra_arq = parts

                if (
                    nome == nome_arq and
                    senha == senha_arq and
                    nasc == nasc_arq and
                    cpf == cpf_arq and
                    email == email_arq and
                    end == end_arq and
                    ra == ra_arq
                ):
                    return True  # autenticação bem-sucedida
        return False  # nenhum registro corresponde
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de alunos não encontrado.")
        return None

def autenticar_alunos_por_ra_e_senha(ra, senha):
    try:
        with open("alunos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(";")
                if len(partes) == 7:
                    nome_arq, senha_arq, _, _, _, _, ra_arq = [p.strip() for p in partes]
                    if ra_arq == ra.strip() and senha_arq == senha.strip():
                        return nome_arq
        return None
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de alunos não encontrado.")
        return None

def cadastrar_usuario():
    novo_usuario = simpledialog.askstring("Novo Usuário", "Digite o nome do usuário:")
    if not novo_usuario:
        return

    while True:
        nova_senha = simpledialog.askstring("Senha", "Digite uma senha forte (mínimo 6 caracteres):", show="*")
        if not nova_senha:
            return
        if len(nova_senha) < 6:
            messagebox.showwarning("Senha fraca", "A senha deve ter pelo menos 6 caracteres!")
        else:
            break

    cargos = ["Admin", "Coordenador", "Professor","aluno"]
    cargo_str = "\n".join(f"{i+1}. {c}" for i, c in enumerate(cargos))
    while True:
        escolha = simpledialog.askinteger("Cargo", f"Escolha o cargo:\n{cargo_str}")
        if escolha in [1,2,3,4]:
            cargo = cargos[escolha-1]
            break
        else:
            messagebox.showerror("Erro", "Escolha inválida!")

    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{novo_usuario};{nova_senha};{cargo}\n")

    messagebox.showinfo("Sucesso", f"Usuário {novo_usuario} ({cargo}) criado com sucesso!")


####CADASTRAR ALUNO
def gerar_ra_unico():
    existente = set()

    if os.path.exists("alunos.txt"):
        with open("alunos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(";")
                if len(partes) == 6:
                    existente.add(partes[7])  # RA

    while True:
        ra = str(random.randint(1000, 9999))  # 4 dígitos
        if ra not in existente:
            return ra

def cadastrar_aluno():
    nome = simpledialog.askstring("Cadastro de Aluno", "Digite o nome do aluno:")
    if not nome:
        return

    # Validação da senha
    while True:
        senha = simpledialog.askstring("Senha", "Digite uma senha forte (mínimo 6 caracteres):", show="*")
        if not senha:
            return
        if len(senha) < 6:
            messagebox.showwarning("Senha fraca", "A senha deve ter pelo menos 6 caracteres!")
        else:
            break

    nasc = simpledialog.askstring("Nascimento", "Digite a data de nascimento (DD/MM/AAAA):")
    if not nasc:
        return

    cpf = simpledialog.askstring("CPF", "Digite o CPF do aluno:")
    if not cpf:
        return

    email = simpledialog.askstring("Email", "Digite o email do aluno:")
    if not email:
        return

    end = simpledialog.askstring("Endereço", "Digite o endereço do aluno:")
    if not end:
        return

    # Gerar RA aleatório único
    ra = gerar_ra_unico()

    # Gravar no arquivo alunos
    try:
        with open("alunos.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{nome};{senha};{nasc};{cpf};{email};{end};{ra}\n")

        messagebox.showinfo("Sucesso", f"Olá, {nome}!\nSeu RA é este: {ra}\nGuarde com segurança!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar aluno: {e}")
###DEFININDO LOGIN DO DOCENTE E DO ALUNO
def abrir_login_docente():
    global et_email, et_senha  # para usar nos comandos

    janela = tk.Toplevel()
    janela.title("ELEVE - Login Docente")
    janela.geometry("400x550+100+100")
    janela.configure(bg=BRANCO)

    # Estilos ttk (já existentes)
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


###CRIACAO DE TELAS DOS DOCENTES
def abrir_menu_admin(nome_usuario):
    janela = tk.Toplevel()
    janela.title("ELEVE - Admin")
    janela.geometry("850x600+100+100")
    janela.configure(bg=BRANCO)

    logodoc(janela)

    corpo = Frame(janela, style='TFrame')
    corpo.pack(pady=20, fill='both', expand=True)

    Label(corpo, text=f"Bem-vindo, {nome_usuario}\nO que você deseja fazer?", font=("Calibri", 14), background=BRANCO, foreground=AZUL).pack(pady=5)
    Button(corpo, text="Criar novo usuário", command=cadastrar_usuario, width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Alunos", command=cadastrar_aluno,width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Turmas", width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Aulas", width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Relatório", width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Sair", command=janela.destroy, width=25, style='Sair.TButton').pack(pady=10)

def abrir_menu_coord(nome_usuario):
    janela = tk.Toplevel()
    janela.title("ELEVE - Coordenador")
    janela.geometry("850x550+100+100")
    janela.configure(bg=BRANCO)

    logodoc(janela)

    corpo = Frame(janela, style='TFrame')
    corpo.pack(pady=20, fill='both', expand=True)

    Label(corpo, text=f"Bem-vindo(a), Coordenador(a) {nome_usuario}", font=("Calibri", 14), background=BRANCO, foreground=AZUL).pack(pady=10)
    Button(corpo, text="Alunos",command=cadastrar_aluno, width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Turmas", width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Aulas", width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Relatório", width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Sair", command=janela.destroy, width=25, style='Sair.TButton').pack(pady=10)

def abrir_menu_prof(nome_usuario):
    janela = tk.Toplevel()
    janela.title("ELEVE - Professor")
    janela.geometry("850x550+100+100")
    janela.configure(bg=BRANCO)

    logodoc(janela)

    corpo = Frame(janela, style='TFrame')
    corpo.pack(pady=20, fill='both', expand=True)

    Label(corpo, text=f"Bem-vindo(a), Professor(a) {nome_usuario}", font=("Calibri", 14), background=BRANCO, foreground=AZUL).pack(pady=10)
    Button(corpo, text="Aulas", width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Relatório", width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Sair", command=janela.destroy, width=25, style='Sair.TButton').pack(pady=10)

###CRIACAO DE TELA DO ALUNO
def abrir_menu_aluno(nome_usuario,ra):
    janela = tk.Toplevel()
    janela.title("ELEVE - Area do Aluno")
    janela.geometry("850x550+100+100")
    janela.configure(bg=BRANCO)

    logoalu(janela)

    corpo = Frame(janela, style='TFrame')
    corpo.pack(pady=20, fill='both', expand=True)

    Label(corpo, text=f"Bem-vindo(a), {nome_usuario}\nRegistro do Aluno: {ra}", font=("Calibri", 14), background=BRANCO, foreground=AZUL).pack(pady=10)
    Button(corpo, text="Aulas", width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Relatório", width=25, style='TButton').pack(pady=10)
    Button(corpo, text="Sair", command=janela.destroy, width=25, style='Sair.TButton').pack(pady=10)

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