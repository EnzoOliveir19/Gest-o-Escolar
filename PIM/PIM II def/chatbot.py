import tkinter as tk
from tkinter import scrolledtext 
from tkinter.ttk import Frame, Button, Entry
import threading # Para executar tarefas em segundo plano 
import google.generativeai as genai # I.A
import unicodedata # Para formatação da pergunta
from fuzzywuzzy import fuzz # PAra matching nas perguntas

# Configurações do chatbot
genai_key = "AIzaSyAocryQ0T-1GGLQRuTpEa5hBUfixJBzVU0" # "Chave API aqui"
genai.configure(api_key=genai_key)

# Base de conhecimento: Respostas pré estabelecidas com listas de palavras-chave
base_de_conhecimento = {
    "documentos para confirmar matrícula e rematrícula": {
        "keywords": ["documentos", "confirmar", "matrícula", "rematrícula", "entregar"],
        "resposta": "Para alunos já matriculados (rematrícula), basta o responsável financeiro assinar o contrato na secretaria. Para alunos novos, os documentos são: cópia do RG e CPF do aluno e dos responsáveis, comprovante de residência, histórico escolar da escola anterior e 2 fotos 3x4 recentes. O período de matrículas e rematrícula para o próximo semestre letivo ocorre geralmente nas duas últimas semanas de Dezembro e de Julho. Fique atento aos comunicados oficiais nos murais da escola para saber as datas exatas!"
    },
    "declaração de matrícula": {
        "keywords": ["declaração", "matrícula", "solicitar",],
        "resposta": "Você pode solicitar sua declaração de matrícula diretamente na secretaria da escola. O documento fica pronto em até 2 dias úteis."
    },
    "trancar a matrícula": {
        "keywords": ["trancar", "trancamento"],
        "resposta": "Para o trancamento de matrícula, o responsável legal do aluno deve comparecer à secretaria para preencher um requerimento, explicando o motivo. O prazo máximo para o trancamento é de um ano letivo."
    },
    "notas, frequência e boletim": {
        "keywords": ["notas", "frequência", "boletim"],
        "resposta": "Suas notas e o registro de frequência são lançados pelos professores e podem ser consultados a qualquer momento através da Área do Aluno, disponível no sistema oficial da escola. O acesso é feito com seu número de matrícula e senha."
    },
    "histórico escolar": {
        "keywords": ["histórico", "escolar"],
        "resposta": "O seu histórico escolar completo pode ser solicitado na secretaria da escola. O prazo para a emissão do documento é de 5 dias úteis. Para consultas rápidas, um boletim simplificado está disponível no Área do Aluno."
    },
    "justificar falta com atestado": {
        "keywords": ["justificar", "falta", "atestado", "médico"],
        "resposta": "Para justificar uma falta por motivos médicos, você deve entregar um atestado na secretaria em até 48 horas após o seu retorno às aulas. Outros tipos de ausência devem ser comunicados previamente à coordenação para análise."
    },
    "limite de faltas para reprovação": {
        "keywords": ["limite", "faltas", "reprovado"],
        "resposta": "Conforme a Lei de Diretrizes e Bases da Educação, o aluno é reprovado na disciplina se tiver um número de faltas superior a 25% do total de aulas dadas no período letivo. Acompanhe sua frequência pela Área do Aluno para não perder o controle!"
    }, 
    "vencimento da mensalidade": {
        "keywords": ["vencimento", "mensalidade", "alteração"],
        "resposta": "As mensalidades da Escola Eleve têm vencimento padrão no dia 10 de cada mês, e são enviados por email, o responsável financeiro pode solicitar a alteração do vencimento diretamente na secretaria'."
    },
    "começam aulas inicio da aula": {
        "keywords": ["começam", "aulas", "início", "calendário", "acadêmico"],
        "resposta": "O calendário acadêmico completo, com as datas de início e término das aulas, períodos de férias e feriados, está sempre disponível para consulta nos murais da Escola Eleve. Geralmente, iniciamos na primeira semana de fevereiro."
    },
    "solicitar carteirinha de estudante": {
        "keywords": ["carteirinha", "carteira", "estudante"],
        "resposta": "A sua primeira carteirinha de estudante é emitida automaticamente após a confirmação da matrícula. Caso precise de uma segunda via por perda ou dano, você pode solicitar na secretaria."
    },
    "wifi senha": {
        "keywords": ["wifi", "senha", "conectar", "rede"],
        "resposta": "A senha de acesso a rede wifi é 'Elevealunos@006'. Na secretaria, você pode retirar um folheto com o passo a passo para se conectar à nossa rede Wi-Fi 'Eleve_Alunos'. As instruções também estão disponíveis nos murais da escola."
    },
    "horário de atendimento secretaria": {
        "keywords": ["horário", "atendimento", "secretaria"],
        "resposta": "O horário de atendimento da nossa secretaria é de segunda a sexta-feira, das 7h30 às 17h30, sem intervalo para o almoço."
    },
    "reunião com coordenador": {
        "keywords": ["coordenador", "falar" , "reunião", "horário"],
        "resposta": "Você pode agendar um horário com o coordenador diretamente na secretaria."
    },
    "guia": {
        "keywords": ["guia"],
        "resposta": "\nGuia de Assuntos da Escola Eleve\n"
"Aqui estão os temas sobre os quais posso conversar. Você pode perguntar sobre:\n\n"
"° Secretaria e Documentação\n"
"Matrícula e rematrícula\n"
"Declaração de matrícula ou histórico escolar\n"
"Trancamento de matrícula\n"
"Solicitar carteirinha de estudante\n"
"Horário de atendimento da secretaria\n\n"

"° Vida Acadêmica\n"
"Consultar notas, boletim e frequência\n"
"Justificar falta com atestado\n"
"Limite de faltas\n"
"Início das aulas (calendário)\n\n"

"° Informações Gerais e Financeiro\n"
"Senha do Wi-Fi\n"
"Vencimento de mensalidade\n"
"Reunião com coordenador\n"
"Digite sua pergunta relacionada a um desses tópicos!\n\n"
    }}

# Função auxiliar para remover acentos
def remover_acentos(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])
 
# Verifica com matching baseado em palavras-chave, tolerante a erros leves
def buscar_resposta_predefinida(pergunta_usuario):
    """
    Verifica se a pergunta do usuário contém palavras-chave suficientes (ou similares) de uma entrada da base_de_conhecimento.
    Para cada palavra da pergunta, calcula similaridade fuzzy com as keywords e conta como match se score >= 80%.
    Retorna a resposta se houver match suficiente, ou None.
    """
    # Remove acentos e converte para minúsculas
    pergunta_normalizada = remover_acentos(pergunta_usuario).lower()
    palavras_pergunta = pergunta_normalizada.split()  # Lista de palavras da pergunta
    
    melhor_match = None
    melhor_score = 0
    
    for entrada in base_de_conhecimento.values():
        keywords = entrada["keywords"]
        resposta = entrada["resposta"]
        
        matches = 0  # Conta quantas palavras da pergunta "batem" com keywords
        for palavra in palavras_pergunta:
            for keyword in keywords:
                # Similaridade entre palavra e chave
                score = fuzz.ratio(palavra, keyword)
                if score >= 75:  # Nível de threshold para erro leve (ex.: "justifcar" vs "justificar")
                    matches += 1
                    break  # Para de procurar para essa palavra
        
        if keywords:  # Evita divisão por zero
            score_total = (matches / len(keywords)) * 100  # Porcentagem de keywords "encontradas"
            
            # Atualiza se for o melhor score
            if score_total > melhor_score:
                melhor_score = score_total
                melhor_match = resposta
    
    # Threshold geral: Pelo menos 30% das keywords devem ter matches (ajustável)
    if melhor_score >= 30:
        return melhor_match
    return None  # Nenhum match encontrado

# Função principal para abrir o chatbot (comando para botão "I.A Eleve")
def abrir_chatbot():
    # Cria um novo chat para cada sessão (histórico não persiste entre aberturas)
    model = genai.GenerativeModel("gemini-flash-latest")   
    # Damos uma "instrução de sistema" para a IA
    instrucao_sistema = (
        "Seja um assistente prestativo. Formate todas as suas respostas "
        "apenas como TEXTO SIMPLES. "
        "NÃO use Markdown (como **, *, ##). "
        "NÃO use LaTeX (como \frac, \sqrt, $$). "
        "Você PODE usar símbolos Unicode simples (como ², ³, √, °, →, etc.) "
        "quando ajudarem na legibilidade."
    )
    
    # Começamos o chat com a IA já sabendo a regra
    chat = model.start_chat(history=[
        {'role': 'user', 'parts': [instrucao_sistema]},
        {'role': 'model', 'parts': ["Entendido. Responderei apenas em texto simples com símbolos Unicode, sem Markdown ou LaTeX."]}])
    
    janela_chat = tk.Toplevel()
    janela_chat.title("ELEVE - Chatbot IA")
    janela_chat.geometry("700x600")
    janela_chat.configure(bg='#f2f2f2')  # Fundo branco
    
    # Área de texto para conversa
    chat_area = scrolledtext.ScrolledText(janela_chat, wrap=tk.WORD, font=('Montserrat', 10), bg='#D3D3D3', fg='black')
    chat_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    chat_area.insert(tk.END, "ELEVE: Bem-vindo ao Chatbot da ELEVE!\n\nEscolha entre modo ELEVE e IA GERAL clicando nos botões abaixo:\nModo ELEVE: Informações sobre a Escola ELEVE\nModo IA GERAL: Consulta geral com IA\n\nVocê pode alterar o modo a qualquer momento clicando nos botões.\n\n")
    chat_area.config(state=tk.DISABLED)
    
    # Campo de entrada
    entrada_frame = Frame(janela_chat)
    entrada_frame.pack(fill=tk.X, padx=10, pady=5)
    
    entrada = Entry(entrada_frame, font=('Montserrat', 12))
    entrada.pack(side=tk.LEFT, fill=tk.X, expand=True)
    
    # Variável para modo
    modo = [None]
    
    def enviar_mensagem():
        pergunta = entrada.get().strip()
        if not pergunta:
            return
        entrada.delete(0, tk.END)
        
        # Adicionar pergunta ao chat
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"Você: {pergunta}\n")
        chat_area.config(state=tk.DISABLED)
        chat_area.see(tk.END)
        
        # Processar em thread
        threading.Thread(target=processar_resposta, args=(pergunta, chat_area, modo, chat)).start()
    
    Button(entrada_frame, text="Enviar", command=enviar_mensagem).pack(side=tk.RIGHT, padx=(5,0))
    
    # Bind da tecla Enter para enviar mensagem
    entrada.bind('<Return>', lambda event: enviar_mensagem())
    
    # Botões para escolher modo
    botoes_frame = Frame(janela_chat)
    botoes_frame.pack(pady=5)
    Button(botoes_frame, text="Modo ELEVE", command=lambda: escolher_modo(1, chat_area, modo)).pack(side=tk.LEFT, padx=5)
    Button(botoes_frame, text="Modo IA Geral", command=lambda: escolher_modo(2, chat_area, modo)).pack(side=tk.LEFT, padx=5)
    
    # Botão Sair abaixo
    sair_frame = Frame(janela_chat)
    sair_frame.pack(pady=5)
    Button(sair_frame, text="Sair", command=janela_chat.destroy).pack()

def escolher_modo(modo_escolhido, chat_area, modo):
    modo[0] = modo_escolhido
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"ELEVE: Modo selecionado: {'ELEVE (informações escolares)' if modo_escolhido == 1 else 'IA Geral'}. Digite sua pergunta!\nDigite 'GUIA' no modo ELEVE se quer ajuda sobre o que perguntar!\n\n")
    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)

def processar_resposta(pergunta, chat_area, modo, chat): 
    
    if modo[0] is None:
        resposta = "Por favor, escolha um modo primeiro (ELEVE ou I.A Geral)."
    elif modo[0] == 1:
        # Modo ELEVE (rápido, sem "Pensando...")
        resposta_pronta = buscar_resposta_predefinida(pergunta)
        if resposta_pronta:
            resposta = resposta_pronta
        else:
            resposta = ("Desculpe, não tenho informações sobre isso na base de conhecimento da escola." 
                        "Tente reformular a pergunta ou clique no botão 'Modo IA Geral' para consultar a IA.")
    else:
        # Esta função é agendada para rodar na thread principal
        def mostrar_pensando():
            chat_area.config(state=tk.NORMAL)
            chat_area.insert(tk.END, "ELEVE: Pensando...\n") # Adiciona a mensagem
            chat_area.see(tk.END) # Garante que a tela role para baixo
            chat_area.config(state=tk.DISABLED)
        
        # Agenda a função acima para executar o mais rápido possível (0ms)
        chat_area.after(0, mostrar_pensando)

        # A thread atual espera a IA (enquanto "Pensando..." está na tela)
        try: 
           resposta_ia = chat.send_message(pergunta)
           resposta = resposta_ia.text
        except Exception as e:
           resposta = f"ELEVE: Desculpe, houve um erro ao consultar a IA. Erro: {str(e)}"
    
    # Ela vai substituir a mensagem "Pensando..." pela resposta final
    def troca_pensando_pela_resposta(resposta_final):
        chat_area.config(state=tk.NORMAL)
        
        # Procura pelo texto "Pensando..."
        # (index "end-2c" significa "do final, volte 2 caracteres" para garantir que pegamos a linha)
        index = chat_area.search("ELEVE: Pensando...\n", "end-2c", backwards=True, stopindex="1.0")
        
        if index:
            # Se achou o "Pensando...", deleta aquela linha
            line_start = index
            line_end = f"{index.split('.')[0]}.end" # Pega o fim daquela linha
            chat_area.delete(line_start, line_end)
        
        # Insere a resposta final (seja do Modo ELEVE ou da IA)
        chat_area.insert(tk.END, f"ELEVE: {resposta_final}\n\n")
        chat_area.see(tk.END)
        chat_area.config(state=tk.DISABLED)

    # Agenda a função de substituição para rodar o mais rápido possível
    chat_area.after(0, lambda:troca_pensando_pela_resposta(resposta))