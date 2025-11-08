import random
import os
import string
from tkinter import messagebox, simpledialog, PhotoImage

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
### --- CADASTRAR USUARIO
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

    cargos = ["Admin", "Coordenador", "Professor"]
    cargo_str = "\n".join(f"{i+1}. {c}" for i, c in enumerate(cargos))
    while True:
        escolha = simpledialog.askinteger("Cargo", f"Escolha o cargo:\n{cargo_str}")
        if escolha in [1,2,3,]:
            cargo = cargos[escolha-1]
            break
        else:
            messagebox.showerror("Erro", "Escolha inválida!")

    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{novo_usuario};{nova_senha};{cargo}\n")

    messagebox.showinfo("Sucesso", f"Usuário {novo_usuario} ({cargo}) criado com sucesso!")

def salvar_usuarios(usuarios):
    with open("usuarios.txt", "w") as arquivo:
        for u in usuarios:
            arquivo.write(f"{u['nome']};{u['senha']};{u['cargo']}\n")

def carregar_usuarios():
    usuarios = []
    try:
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(";")
                if len(partes) == 3:
                    usuarios.append({"nome": partes[0], "senha": partes[1], "cargo": partes[2]})
    except FileNotFoundError:
        pass
    return usuarios
###----PROCURAR USUARIO
def procurar_usuario(nome):
    usuarios = carregar_usuarios()
    for u in usuarios:
        if u['nome'].lower() == nome.lower():
            return u
    return None

def mostrar_busca_usuario(nome):
    if not nome.strip():
        return "Digite um nome para buscar."

    usuario = procurar_usuario(nome)
    if usuario:
        return f"Usuário encontrado:\n{usuario}"
    else:
        return "Usuário não encontrado."

###----EDITAR USUARIO
def editar_usuario(nome_antigo, novo_nome, nova_senha, novo_cargo):
    usuarios = carregar_usuarios()
    for u in usuarios:
        if u['nome'].lower() == nome_antigo.lower():
            u['nome'] = novo_nome
            u['senha'] = nova_senha
            u['cargo'] = novo_cargo
            salvar_usuarios(usuarios)
            return True, "Usuário editado com sucesso."
    return False, "Usuário não encontrado."

def editar_usuario2():
    nome_antigo = simpledialog.askstring("Editar Usuário", "Informe o nome antigo do usuário:")
    if not nome_antigo:
        return

    novo_nome = simpledialog.askstring("Editar Usuário", "Informe o novo nome do usuário:")
    if novo_nome is None:
        return

    nova_senha = simpledialog.askstring("Editar Usuário", "Informe a nova senha (ou deixe vazio):", show='*')
    if nova_senha is None:
        return

    novo_cargo = simpledialog.askstring("Editar Usuário", "Informe o novo cargo do usuário:")
    if novo_cargo is None:
        return

    if nova_senha == "":
        usuarios = carregar_usuarios()
        for u in usuarios:
            if u['nome'].lower() == nome_antigo.lower():
                nova_senha = u['senha']
                break
    sucesso, mensagem = editar_usuario(nome_antigo, novo_nome, nova_senha, novo_cargo)
    messagebox.showinfo("Resultado da edição", mensagem)

##------REMOVER USUARIO
def remover_usuario(nome):
    usuarios = carregar_usuarios()
    usuarios_novos = [u for u in usuarios if u['nome'].lower() != nome.lower()]
    if len(usuarios) == len(usuarios_novos):
        return False, "Usuário não encontrado."
    salvar_usuarios(usuarios_novos)
    return True, "Usuário removido com sucesso."

def remover_usuario2():
    nome = simpledialog.askstring("Remover Usuário", "Informe o nome completo do usuário a remover:")
    if not nome:
        return  # Cancelado ou vazio

    usuarios = carregar_usuarios()
    usuario_encontrado = None
    for u in usuarios:
        if u['nome'].lower() == nome.lower():
            usuario_encontrado = u
            break

    if not usuario_encontrado:
        messagebox.showinfo("Remover Usuário", f"Usuário '{nome}' não encontrado.")
        return

    info = (f"Nome: {usuario_encontrado['nome']}\n"
            f"Cargo: {usuario_encontrado['cargo']}\n")

    resposta = messagebox.askquestion("Confirmar remoção",
                                      f"Usuário encontrado:\n\n{info}\n\nDeseja remover esse usuário?")

    if resposta == 'yes':
        confirmacao = messagebox.askyesno("Confirmação Final",
                                          "Você tem certeza? Esta ação NÃO poderá ser desfeita.")

        if confirmacao:
            sucesso, mensagem = remover_usuario(nome)
            messagebox.showinfo("Remover Usuário", mensagem)
        else:
            messagebox.showinfo("Remover Usuário", "Ação cancelada.")
    else:
        messagebox.showinfo("Remover Usuário", "Ação cancelada.")


### ---- ALUNOS
def carregar_aluno():
    alunos = []
    try:
        with open("alunos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(";")
                if len(partes) == 7:
                    alunos.append({
                        "nome": partes[0],
                        "senha": partes[1],  
                        "Data de Nascimento": partes[2],
                        "CPF": partes[3],
                        "email": partes[4],
                        "endereco": partes[5],
                        "ra": partes[6]
                    })
    except FileNotFoundError:
        pass
    return alunos

def salvar_aluno(alunos):
    with open("alunos.txt", "w", encoding="utf-8") as arquivo:
        for aluno in alunos:
            linha = ";".join([
                aluno["nome"],
                aluno["senha"],
                aluno["Data de Nascimento"],
                aluno["CPF"],
                aluno["email"],
                aluno["endereco"],
                aluno["ra"]
            ])
            arquivo.write(linha + "\n")


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

#### ---- BUSCAR ALUNO

###----PROCURAR ALUNO
def procurar_aluno(nome):
    aluno = carregar_aluno()
    for a in aluno:
        if a['nome'].lower() == nome.lower():
            return a
    return None

def mostrar_busca_aluno(nome):
    if not nome.strip():
        return "Digite um nome para buscar."

    aluno = procurar_aluno(nome)
    if aluno:
        # Montar a mensagem sem mostrar a senha
        mensagem = (
            f"Nome: {aluno['nome']}\n"
            f"Data de Nascimento: {aluno['Data de Nascimento']}\n"
            f"CPF: {aluno['CPF']}\n"
            f"E-Mail: {aluno['email']}\n"
            f"Endereço: {aluno['endereco']}\n"
            f"R.A: {aluno['ra']}"
        )
        return f"Aluno encontrado:\n\n{mensagem}"
    else:
        return "Aluno não encontrado."


##------REMOVER ALUNO
def remover_aluno(nome):
    alunos = carregar_aluno()
    alunos_novos = [a for a in alunos if a ['nome'].lower() != nome.lower()]
    if len(alunos) == len(alunos_novos):
        return False, "Aluno não encontrado."
    salvar_aluno(alunos_novos)
    return True, "Aluno removido com sucesso!"
    

def remover_aluno2():
    nome = simpledialog.askstring("Remover Aluno", "Informe o nome completo do aluno a remover:")
    if not nome:
        return  # Cancelado ou vazio

    alunos = carregar_aluno()
    aluno_encontrado = None
    for a in alunos:
        if a['nome'].lower() == nome.lower():
            aluno_encontrado = a
            break

    if not aluno_encontrado:
        messagebox.showinfo("Remover Aluno", f"Aluno '{nome}' não encontrado.")
        return

    info = (f"Nome: {aluno_encontrado['nome']}\n"
            f"Matricula: {aluno_encontrado.get('matricula',{6})}\n")

    resposta = messagebox.askquestion("Confirmar remoção",
                                      f"Aluno encontrado:\n\n{info}\n\nDeseja remover esse aluno?")

    if resposta == 'yes':
        confirmacao = messagebox.askyesno("Confirmação Final",
                                          "Você tem certeza? Esta ação NÃO poderá ser desfeita.")

        if confirmacao:
            sucesso, mensagem = remover_aluno(nome)
            messagebox.showinfo("Remover Aluno", mensagem)
        else:
            messagebox.showinfo("Remover Aluno", "Ação cancelada.")
    else:
        messagebox.showinfo("Remover Aluno", "Ação cancelada.")

###--- EDITAR ALUNO

def editar_aluno(nome_antigo, novo_nome, nova_senha, nova_data, novo_cpf, novo_email, novo_endereco, novo_ra):
    alunos = carregar_aluno()
    for a in alunos:
        if a['nome'].lower() == nome_antigo.lower():
            a['nome'] = novo_nome
            a['senha'] = nova_senha
            a['Data de Nascimento'] = nova_data
            a['CPF'] = novo_cpf
            a['E-Mail'] = novo_email
            a['Endereço'] = novo_endereco
            a['R.A'] = novo_ra
            salvar_aluno(alunos)
            return True, "Aluno editado com sucesso."
    return False, "Aluno não encontrado."

def editar_aluno2():
    nome_antigo = simpledialog.askstring("Editar Aluno", "Informe o nome atual do aluno:")
    if not nome_antigo:
        return

    novo_nome = simpledialog.askstring("Editar Aluno", "Novo nome do aluno:")
    if novo_nome is None:
        return

    nova_senha = simpledialog.askstring("Editar Aluno", "Nova senha (ou deixe em branco):", show='*')
    if nova_senha is None:
        return

    nova_data = simpledialog.askstring("Editar Aluno", "Nova data de nascimento:")
    if nova_data is None:
        return

    novo_cpf = simpledialog.askstring("Editar Aluno", "Novo CPF:")
    if novo_cpf is None:
        return

    novo_email = simpledialog.askstring("Editar Aluno", "Novo E-Mail:")
    if novo_email is None:
        return

    novo_endereco = simpledialog.askstring("Editar Aluno", "Novo endereço:")
    if novo_endereco is None:
        return

    novo_ra = simpledialog.askstring("Editar Aluno", "Novo R.A:")
    if novo_ra is None:
        return

    # Se senha estiver em branco, manter a antiga
    if nova_senha == "":
        alunos = carregar_aluno()
        for a in alunos:
            if a['nome'].lower() == nome_antigo.lower():
                nova_senha = a['senha']
                break

    sucesso, mensagem = editar_aluno(nome_antigo, novo_nome, nova_senha, nova_data, novo_cpf, novo_email, novo_endereco, novo_ra)
    messagebox.showinfo("Resultado da Edição", mensagem)


########### GERENCIAMENTO DE TURMAS
def listar_turmas():
    turmas = []
    if not os.path.exists("turmas.txt"):
        return turmas

    with open("turmas.txt", "r", encoding="utf-8") as f:
        for linha in f:
            partes = linha.strip().split(";")

            nome = partes[0]
            professor = partes[1].replace("professor=", "")
            alunos = partes[2].replace("alunos=", "")

            limite = 0
            if len(partes) > 3:
                limite = partes[3].replace("limite=", "")

            turmas.append({
                "nome": nome,
                "professor": professor,
                "alunos": int(alunos) if alunos.isdigit() else 0,
                "limite": int(limite) if str(limite).isdigit() else 0
            })

    return turmas


def salvar_turmas(turmas):
    with open("turmas.txt", "w", encoding="utf-8") as f:
        for t in turmas:
            alunos_str = ",".join(t.get("lista", []))  
            f.write(f"{t['nome']};{t['professor']};{t['limite']};{alunos_str}\n")


def criar_turma(nome, professor, limite):
    if not nome or not professor or not limite:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    try:
        limite = int(limite)
    except:
        messagebox.showwarning("Aviso", "O limite deve ser um número.")
        return

    with open("turmas.txt", "a", encoding="utf-8") as f:
        f.write(f"{nome};{professor};{limite};\n")

    messagebox.showinfo("Sucesso", f"Turma '{nome}' criada com sucesso!")


def adicionar_aluno_turma_ui(lista_turmas, atualizar_lista):
    indice = lista_turmas.curselection()
    if not indice:
        messagebox.showwarning("Aviso", "Selecione uma turma.")
        return
    turmas = listar_turmas()
    turma = turmas[indice[0]]

    alunos = alunos.txt
    nomes = [a['nome'] for a in alunos]

    aluno_nome = simpledialog.askstring("Adicionar Aluno", f"Digite o nome do aluno:\nDisponíveis: {', '.join(nomes)}")

    aluno = next((a for a in alunos if a['nome'] == aluno_nome), None)
    if not aluno:
        messagebox.showerror("Erro", "Aluno não encontrado.")
        return

    if len(turma["lista"]) >= turma["limite"]:
        messagebox.showwarning("Aviso", "Turma já está no limite de alunos.")
        return

    turma["lista"].append(aluno["ra"])
    salvar_turmas(turmas)
    messagebox.showinfo("Sucesso", f"Aluno '{aluno_nome}' adicionado!")
    atualizar_lista()


def remover_aluno_turma_ui(lista_turmas, atualizar_lista):
    indice = lista_turmas.curselection()
    if not indice:
        messagebox.showwarning("Aviso", "Selecione uma turma.")
        return

    turmas = listar_turmas()
    turma = turmas[indice[0]]

    if not turma["lista"]:
        messagebox.showinfo("Info", "Nenhum aluno para remover.")
        return

    aluno_ra = simpledialog.askstring("Remover Aluno", f"RAs atuais: {', '.join(turma['lista'])}\nDigite o RA para remover:")
    if aluno_ra not in turma["lista"]:
        messagebox.showerror("Erro", "RA não encontrado nesta turma.")
        return

    turma["lista"].remove(aluno_ra)
    salvar_turmas(turmas)
    messagebox.showinfo("Sucesso", f"Aluno RA {aluno_ra} removido!")
    atualizar_lista()

    return turmas

def listar_professores():
    """Lê o arquivo usuarios.txt e retorna apenas os professores"""
    professores = []
    try:
        with open("usuarios.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(";")
                if len(partes) == 3:
                    nome, senha, cargo = partes
                    if cargo.strip().lower() == "professor":
                        professores.append(nome.strip())
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de usuários não encontrado.")
    return professores

def listar_alunos():
    """Lê o arquivo alunos.txt e retorna a lista de alunos"""
    alunos = []
    try:
        with open("alunos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(";")
                if len(partes) == 7:
                    alunos.append({
                        "nome": partes[0],
                        "ra": partes[6]
                    })
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de alunos não encontrado.")
    return alunos

def aluno_em_turma(ra_aluno):
    """Verifica se o aluno já pertence a alguma turma"""
    turmas = listar_turmas()
    for turma in turmas:
        if ra_aluno in turma["lista"]:
            return True
    return False


def criar_turma_auto(professor, alunos_selecionados, limite=30):
    """Cria automaticamente turmas com nomes sequenciais (1A, 1B, 1C...)"""
    turmas = listar_turmas()

    # Gera nome automático (1A, 1B, 1C...)
    prefixo = "1"
    sufixo = chr(65 + len(turmas))  # A, B, C, ...
    nome_turma = f"{prefixo}{sufixo}"

    nova_turma = {
        "nome": nome_turma,
        "professor": professor,
        "limite": limite,
        "lista": [a["ra"] for a in alunos_selecionados]
    }

    turmas.append(nova_turma)
    salvar_turmas(turmas)
    messagebox.showinfo("Sucesso", f"Turma '{nome_turma}' criada com sucesso!")

    return nova_turma


def excluir_turma(nome_turma):
    """Remove uma turma pelo nome"""
    turmas = listar_turmas()
    novas_turmas = [t for t in turmas if t["nome"] != nome_turma]
    salvar_turmas(novas_turmas)
    messagebox.showinfo("Sucesso", f"Turma '{nome_turma}' removida com sucesso!")