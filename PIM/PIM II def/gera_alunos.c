#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// --- (REQUISITO DESEJAVEL: Struct) ---
struct Aluno {
    char nome[100];
    char senha[100];
    char nasc[100]; 
    char cpf[100];
    char email[100];
    char endereco[300];
    char ra[100];
};

// --- (REQUISITO: Funcao separada da main) ---
void coletarDadosAluno(struct Aluno *aluno) {
    printf("\nDigite o Nome do Aluno: ");
    fgets(aluno->nome, sizeof(aluno->nome), stdin);
    aluno->nome[strcspn(aluno->nome, "\n")] = 0; 

    printf("Digite a Senha de login: ");
    fgets(aluno->senha, sizeof(aluno->senha), stdin);
    aluno->senha[strcspn(aluno->senha, "\n")] = 0; 

    printf("Digite a Data de Nascimento (DD/MM/AAAA): ");
    fgets(aluno->nasc, sizeof(aluno->nasc), stdin);
    aluno->nasc[strcspn(aluno->nasc, "\n")] = 0;

    printf("Digite o CPF: ");
    fgets(aluno->cpf, sizeof(aluno->cpf), stdin);
    aluno->cpf[strcspn(aluno->cpf, "\n")] = 0;

    printf("Digite o E-mail: ");
    fgets(aluno->email, sizeof(aluno->email), stdin);
    aluno->email[strcspn(aluno->email, "\n")] = 0;

    printf("Digite o Endereco: ");
    fgets(aluno->endereco, sizeof(aluno->endereco), stdin);
    aluno->endereco[strcspn(aluno->endereco, "\n")] = 0;

    printf("Digite o RA (ex: 1168): ");
    fgets(aluno->ra, sizeof(aluno->ra), stdin);
    aluno->ra[strcspn(aluno->ra, "\n")] = 0;
}

// --- (REQ: Leitura de arquivo) ---
int verificarRaExistente(char* ra) {
    FILE *arquivo = fopen("alunos.txt", "r"); 
    if (arquivo == NULL) {
        return 0; 
    }

    char linha[500];
    char raParaBuscar[105];
    
    // Formata o RA para buscar (ex: ";1168")
    // O RA é o último campo, então buscamos pelo final da linha
    sprintf(raParaBuscar, ";%s", ra); 

    while (fgets(linha, sizeof(linha), arquivo)) {
        // Verifica se a linha termina com o raParaBuscar
        int lenLinha = strlen(linha);
        int lenRa = strlen(raParaBuscar);
        if (lenLinha >= lenRa) {
            // Compara os últimos N caracteres da linha
            if (strcmp(linha + lenLinha - lenRa, raParaBuscar) == 0) {
                 fclose(arquivo);
                 return 1; 
            }
        }
    }

    fclose(arquivo);
    return 0; 
}


// --- (REQ: Salvar dados em arquivo) ---
void salvarAlunoNoArquivo(struct Aluno aluno) {
    FILE *arquivo; 
    
    arquivo = fopen("alunos.txt", "a");

    if (arquivo == NULL) {
        printf("Erro! Nao foi possivel abrir o arquivo alunos.txt.\n");
        return; 
    }

    fprintf(arquivo, "\n%s;%s;%s;%s;%s;%s;%s", 
            aluno.nome, aluno.senha, aluno.nasc, 
            aluno.cpf, aluno.email, aluno.endereco, aluno.ra);

    fclose(arquivo);

    printf("\n----------------------------------------\n");
    printf("SUCESSO: Aluno '%s' foi adicionado.\n", aluno.nome);
    printf("----------------------------------------\n");
}


// --- Função Principal ---
int main() {
    char opcao = 'S';
    while (opcao == 'S' || opcao == 's') {
        
        if (opcao == 'S' || opcao == 's') {
            struct Aluno novoAluno; 

            printf("----------------------------------------\n");
            printf("  Adicionando Novo Aluno - ELEVE \n");
            printf("----------------------------------------\n");

            coletarDadosAluno(&novoAluno);

            if (verificarRaExistente(novoAluno.ra)) {
                printf("\n!!! ERRO: O RA '%s' ja esta cadastrado. O aluno NAO foi salvo.\n", novoAluno.ra);
            } else {
                salvarAlunoNoArquivo(novoAluno);
            }
        }

        printf("\nDeseja adicionar outro aluno? (S/N): ");
        fgets(&opcao, 3, stdin); 
        if(strchr(&opcao, '\n') == NULL) {
             while(getchar()!='\n');
        }

    } // Fim do loop 'while'

    printf("\nSaindo do programa de cadastro...\n");
    return 0; 
}