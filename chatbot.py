import google.generativeai as genai # IA
import os
import unicodedata  # Para remover acentos
from fuzzywuzzy import fuzz  # Para matching fuzzy em palavras individuais
import re  # Para limpeza de fórmulas)

# Variável com a chave api
genai_key = "chave api aqui"

# Configurando minha chave API:
genai.configure(api_key=genai_key)

# Escolhendo meu modelo de IA
model = genai.GenerativeModel("gemini-flash-latest") 
chat = model.start_chat(history=[])

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
        "keywords": ["coordenador", "Falar", "reunião", "agendar", "horário"],
        "resposta": "Você pode agendar um horário com o coordenador diretamente na secretaria."
    }
}

# Função auxiliar para remover acentos
def remove_accents(input_str):
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
    pergunta_normalizada = remove_accents(pergunta_usuario).lower()
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
                if score >= 80:  # Nível de threshold para erro leve (ex.: "justifcar" vs "justificar")
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

# Função para limpar respostas da IA (fórmulas matemáticas) - Apenas para IA Geral
def limpar_resposta_ia(resposta):
    """
    Pós-processa a resposta da IA para tornar fórmulas matemáticas mais legíveis.
    Substitui símbolos Unicode comuns por texto em português.
    """
    # Dicionário de substituições para símbolos matemáticos
    substituicoes = {
        '√': 'raiz quadrada de ',
        '²': ' ao quadrado ',
        '³': ' ao cubo ',
        '±': ' mais ou menos ',
        '×': ' vezes ',
        '÷': ' dividido por ',
        '≠': ' diferente de ',
        '≤': ' menor ou igual a ',
        '≥': ' maior ou igual a ',
        '≈': ' aproximadamente ',
        'π': ' pi ',
        '∞': ' infinito ',
        '∑': ' somatório ',
        '∫': ' integral de ',
        '∂': ' derivada parcial de ',
        'Δ': ' delta ',
        'α': ' alfa ',
        'β': ' beta ',
        'γ': ' gama ',
        'δ': ' delta ',
        'θ': ' teta ',
        'λ': ' lambda ',
        'μ': ' mi ',
        'σ': ' sigma ',
        'τ': ' tau ',
        'φ': ' fi ',
        'ω': ' omega ',
        # Frações simples (ex.: ½ -> 1/2)
        '½': ' 1/2 ',
        '⅓': ' 1/3 ',
        '¼': ' 1/4 ',
        '¾': ' 3/4 ',
        '⅔': ' 2/3 ',
        '⅕': ' 1/5 ',
        '⅖': ' 2/5 ',
        '⅗': ' 3/5 ',
        '⅘': ' 4/5 ',
        '⅙': ' 1/6 ',
        '⅚': ' 5/6 ',
        '⅛': ' 1/8 ',
        '⅜': ' 3/8 ',
        '⅝': ' 5/8 ',
        '⅞': ' 7/8 ',
    }
    
    # Aplica substituições
    for simbolo, texto in substituicoes.items():
        resposta = resposta.replace(simbolo, texto)
    
    # Remove quebras de linha extras ou formatação LaTeX básica (ex.: $...$)
    resposta = re.sub(r'\$\$(.*?)\$\$', r'\1', resposta)  # Remove $$...$$
    resposta = re.sub(r'\$(.*?)\$', r'\1', resposta)     # Remove $...$
    resposta = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'\1/\2', resposta)  # \frac{a}{b} -> a/b
    resposta = re.sub(r'\\sqrt\{([^}]+)\}', r'raiz quadrada de \1', resposta)  # \sqrt{x} -> raiz quadrada de x
    resposta = re.sub(r'\\([a-zA-Z]+)\{([^}]+)\}', r'\2 (\1)', resposta)  # Outros comandos LaTeX simples
    
    return resposta.strip()

# Escolha inicial do modo
print("Bem-vindo ao Chatbot da ELEVE!")
print("Escolha o modo:")
print("1. Informações sobre a Escola ELEVE (base de conhecimento pré-definida)")
print("2. Consulta geral com IA")

while True:
    try:
        modo = int(input("Digite 1 ou 2: "))
        if modo == 1:
            modo_nome = "ELEVE (informações escolares)"
            break
        elif modo == 2:
            modo_nome = "IA Geral"
            break
        else:
            print("Opção inválida. Digite 1 ou 2.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

print(f"{os.linesep}Modo selecionado: {modo_nome}. Digite 'fim' para sair ou 'mudar' para trocar de modo.")

# Loop principal do chat
while True:
    pergunta = input(f"{os.linesep}Olá, como posso te ajudar?{os.linesep}")

    if pergunta.lower() == "fim":
        print(f"{os.linesep}Até logo!")
        break
    elif pergunta.lower() == "mudar":
        # Permite trocar de modo
        print("Escolha o novo modo:")
        print("1. Informações sobre a Escola ELEVE")
        print("2. Consulta geral com IA")
        while True:
            try:
                modo = int(input("Digite 1 ou 2: "))
                if modo == 1:
                    modo_nome = "ELEVE (informações escolares)"
                    print("Modo alterado para ELEVE.")
                    break
                elif modo == 2:
                    modo_nome = "IA Geral"
                    print("Modo alterado para IA Geral.")
                    break
                else:
                    print("Opção inválida.")
            except ValueError:
                print("Entrada inválida.")
        continue

    if modo == 1:  # Modo ELEVE: só base de conhecimento
        resposta_pronta = buscar_resposta_predefinida(pergunta)
        if resposta_pronta:
            print("ELEVE:", resposta_pronta)
        else:
            print("ELEVE: Desculpe, não tenho informações sobre isso na base de conhecimento da escola. Tente reformular a pergunta ou digite 'mudar' para consultar a IA geral.")
    else:  # Modo IA Geral: só IA (com limpeza de fórmulas)
        try:
            # Ajusta o prompt para pedir fórmulas em texto plano
            prompt_ajustado = pergunta + " (Por favor, forneça fórmulas matemáticas em texto simples, sem LaTeX ou símbolos Unicode especiais, para facilitar a leitura.)"
            print("ELEVE: (Consultando IA geral...)\n")
            resposta = chat.send_message(prompt_ajustado)
            resposta_limpa = limpar_resposta_ia(resposta.text)
            print(resposta_limpa)
        except Exception as e:
            print("ELEVE: Desculpe, houve um erro ao consultar a IA. Tente novamente mais tarde. Erro: ", str(e))
