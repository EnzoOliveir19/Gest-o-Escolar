import random
import os
import subprocess
from tkinter import messagebox, simpledialog
from datetime import datetime
import tkinter as tk

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
        mensagem = (
            f"Nome: {usuario['nome']}\n"
            f"Cargo: {usuario['cargo']}\n"
        )
        # Evita mostrar a senha
        return f"Usuário encontrado:\n\n{mensagem}"
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
                if len(partes) == 7:
                    existente.add(partes[6])  # RA

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

def buscar_aluno_por_ra(ra_procurado): #NOVO
    """Verifica se um aluno existe com base no RA."""
    alunos = carregar_aluno() # Reusa a função existente
    for aluno in alunos:
        if aluno['ra'].strip() == ra_procurado.strip():
            return aluno # Retorna o dicionário do aluno
    return None # Não encontrou

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
    #FIM NOVO


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
            a['email'] = novo_email
            a['endereco'] = novo_endereco
            a['ra'] = novo_ra
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

########### GERENCIAMENTO DE BOLETINS (NOTAS) NOVO

def verificar_boletim_existente(ra):
    """Verifica se o arquivo CSV do boletim para um RA já existe."""
    nome_arquivo = f"boletim_{ra}.csv"
    return os.path.exists(nome_arquivo)

def carregar_dados_boletim(ra):
    """
    Lê os dados de um arquivo de boletim CSV.
    Retorna uma lista de dicionários com os dados salvos.
    """
    if not verificar_boletim_existente(ra):
        return None
    
    nome_arquivo = f"boletim_{ra}.csv"
    dados_boletim = []
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            # Pula o cabeçalho
            next(f) 
            for linha in f:
                partes = linha.strip().split(";")
                # Carrega os dados brutos como foram digitados
                if len(partes) >= 5: # Materia;N1;N2;N3;Frequencia...
                    dados_boletim.append({
                        "materia": partes[0],
                        "n1": partes[1],
                        "n2": partes[2],
                        "n3": partes[3],
                        "frequencia": partes[4]
                    })
        return dados_boletim
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao ler boletim: {e}")
        return None

def salvar_boletim_aluno(ra, dados_materias):
    """
    Salva (ou sobrescreve) o arquivo CSV do boletim de um aluno.
    'dados_materias' é uma lista de dicionários vinda da interface, ex:
    [{"materia": "Portugues", "n1": "10", "n2": "8", "n3": "9", "frequencia": "80"}, ...]
    """
    nome_arquivo = f"boletim_{ra}.csv"
    
    # Regras da escola
    MEDIA_MINIMA = 6.0
    FREQ_MINIMA = 75.0

    try:
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            # Escreve o cabeçalho
            f.write("Materia;N1;N2;N3;Frequencia;Media;Status\n")
            
            for item in dados_materias:
                materia = item['materia']
                
                # Tenta converter os dados para float, se falhar (ex: "abc"), usa 0.0
                try: n1 = float(item['n1'].replace(",", "."))
                except (ValueError, TypeError): n1 = 0.0
                try: n2 = float(item['n2'].replace(",", "."))
                except (ValueError, TypeError): n2 = 0.0
                try: n3 = float(item['n3'].replace(",", "."))
                except (ValueError, TypeError): n3 = 0.0
                try: freq = float(item['frequencia'].replace(",", "."))
                except (ValueError, TypeError): freq = 0.0

                # Cálculo da média
                media = (n1 + n2 + n3) / 3.0
                
                # Cálculo do Status (Aprovado/Reprovado)
                status = "Aprovado"
                if media < MEDIA_MINIMA or freq < FREQ_MINIMA:
                    status = "Reprovado"
                
                # Salva a linha no CSV
                # (Usamos os valores originais 'item' para N1,N2,N3,Freq para não perder a digitação original)
                f.write(
                    f"{materia};"
                    f"{item['n1']};{item['n2']};{item['n3']};{item['frequencia']};"
                    f"{media:.2f};" # Salva a média formatada com 2 casas
                    f"{status}\n"
                )
        return True
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar boletim: {e}")
        return False
#FIM NOVO 

########### GERENCIAMENTO DE TURMAS
# --- LISTAR TURMAS ---
def listar_turmas():
    turmas = []
    if not os.path.exists("turmas.txt"):
        return turmas

    with open("turmas.txt", "r", encoding="utf-8") as f:
        for linha in f:
            partes = linha.strip().split(";")
            if len(partes) < 4:
                continue

            nome = partes[0]
            professor = partes[1]
            limite = partes[2]
            alunos = partes[3].split(",") if partes[3] else []

            turmas.append({
                "nome": nome,
                "professor": professor,
                "limite": int(limite) if limite.isdigit() else 0,
                "lista": alunos
            })
    return turmas


# --- SALVAR TURMAS ---
def salvar_turmas(turmas):
    with open("turmas.txt", "w", encoding="utf-8") as f:
        for t in turmas:
            alunos_str = ",".join(t.get("lista", []))
            f.write(f"{t['nome']};{t['professor']};{t['limite']};{alunos_str}\n")


# --- EXCLUIR TURMA ---
def excluir_turma(nome_turma):
    """Remove uma turma pelo nome"""
    turmas = listar_turmas()
    novas_turmas = [t for t in turmas if t["nome"] != nome_turma]
    salvar_turmas(novas_turmas)
    return True  # interface mostra a mensagem


# --- LISTAR PROFESSORES ---
def listar_professores():
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


# --- LISTAR ALUNOS ---
def listar_alunos():
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


# --- VERIFICAÇÃO SE ALUNO JÁ ESTÁ EM TURMA ---
def aluno_em_turma(ra_aluno):
    turmas = listar_turmas()
    for turma in turmas:
        if ra_aluno in turma["lista"]:
            return True
    return False


# --- CRIAR TURMA AUTOMÁTICA ---
def criar_turma_auto(professor, alunos_selecionados, limite=30):
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

    return nova_turma

# --- GERENCIADOR DE AULAS ---
# --- LISTAR AULAS ---
def listar_aulas():
    aulas = []
    if not os.path.exists("aulas.txt"):
        return aulas

    with open("aulas.txt", "r", encoding="utf-8") as f:
        for linha in f:
            partes = linha.strip().split("|")
            if len(partes) < 3:
                continue
            turma = partes[0]
            data = partes[1]
            conteudo = partes[2]
            aulas.append({
                "turma": turma,
                "data": data,
                "conteudo": conteudo
            })
    return aulas


# --- SALVAR AULAS ---
def salvar_aulas(aulas):
    with open("aulas.txt", "w", encoding="utf-8") as f:
        for aula in aulas:
            f.write(f"{aula['turma']}|{aula['data']}|{aula['conteudo']}\n")


# --- ADICIONAR AULA ---
def adicionar_aula(turma, conteudo):
    data_hoje = datetime.now().strftime("%d/%m/%Y")
    aulas = listar_aulas()

    nova_aula = {
        "turma": turma,
        "data": data_hoje,
        "conteudo": conteudo.strip()
    }

    aulas.append(nova_aula)
    salvar_aulas(aulas)
    messagebox.showinfo("Sucesso", f"Aula adicionada para a turma {turma} em {data_hoje}!")


# --- EDITAR AULA ---
def editar_aula(turma, data, novo_conteudo):
    aulas = listar_aulas()
    alterada = False

    for aula in aulas:
        if aula["turma"] == turma and aula["data"] == data:
            aula["conteudo"] = novo_conteudo.strip()
            alterada = True
            break

    if alterada:
        salvar_aulas(aulas)
        messagebox.showinfo("Sucesso", f"Aula do dia {data} da turma {turma} foi atualizada!")
    else:
        messagebox.showwarning("Aviso", "Aula não encontrada.")


# --- REMOVER AULA ---
def remover_aula(turma, data):
    aulas = listar_aulas()
    novas_aulas = [a for a in aulas if not (a["turma"] == turma and a["data"] == data)]

    if len(novas_aulas) < len(aulas):
        salvar_aulas(novas_aulas)
        messagebox.showinfo("Sucesso", f"Aula da turma {turma} no dia {data} foi removida!")
    else:
        messagebox.showwarning("Aviso", "Aula não encontrada.")