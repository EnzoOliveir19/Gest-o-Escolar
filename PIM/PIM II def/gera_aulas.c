#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    // 1. Variáveis para guardar os dados
    char turma[100];
    char data[100];
    char descricao[500]; // Espaço maior para a descrição
    FILE *arquivo; 

    // 2. Mensagem de boas-vindas
    printf("----------------------------------------\n");
    printf("  Adicionando Nova Aula - ELEVE \n");
    printf("----------------------------------------\n");
    printf("Insira as informacoes solicitadas a seguir:\n\n");

    // 3. Coletar os dados do terminal
    
    printf("Digite a Turma (ex: 1A): ");
    fgets(turma, sizeof(turma), stdin);
    turma[strcspn(turma, "\n")] = 0; 

    printf("Digite a Data da Aula (DD/MM/AAAA): ");
    fgets(data, sizeof(data), stdin);
    data[strcspn(data, "\n")] = 0; 

    printf("Digite a Descricao da Aula: ");
    fgets(descricao, sizeof(descricao), stdin);
    descricao[strcspn(descricao, "\n")] = 0;

    // 4. Abrir o arquivo no modo "append"
    arquivo = fopen("aulas.txt", "a");

    // 5. Verificar se o arquivo abriu com sucesso
    if (arquivo == NULL) {
        printf("Erro! Nao foi possivel abrir o arquivo aulas.txt.\n");
        return 1; 
    }

    // 6. Escrever os dados no arquivo
    fprintf(arquivo, "\n%s|%s|%s", turma, data, descricao);

    // 7. Fechar o arquivo
    fclose(arquivo);

    // 8. Mensagem de sucesso
    printf("\n----------------------------------------\n");
    printf("SUCESSO: Aula para a turma '%s' foi adicionada.\n", turma);
    printf("----------------------------------------\n");

    return 0; 
}