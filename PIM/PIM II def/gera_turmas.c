#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    // 1. Variáveis para guardar os dados
    char serie[100];
    char professor[100];
    char ras[500]; // Espaço maior para vários RAs
    FILE *arquivo; 

    // 2. Mensagem de boas-vindas
    printf("----------------------------------------\n");
    printf("  Adicionando Nova Turma - ELEVE \n");
    printf("----------------------------------------\n");
    printf("Insira as informacoes solicitadas a seguir:\n\n");

    // 3. Coletar os dados do terminal
    
    printf("Digite a Serie/Nome da Turma (ex: 1A, 1B): ");
    fgets(serie, sizeof(serie), stdin);
    serie[strcspn(serie, "\n")] = 0; 

    printf("Digite o Nome do Professor responsavel: ");
    fgets(professor, sizeof(professor), stdin);
    professor[strcspn(professor, "\n")] = 0; 

    printf("Digite os RAs dos alunos (separados por virgula): ");
    fgets(ras, sizeof(ras), stdin);
    ras[strcspn(ras, "\n")] = 0;

    // 4. Abrir o arquivo no modo "append"
    arquivo = fopen("turmas.txt", "a");

    // 5. Verificar se o arquivo abriu com sucesso
    if (arquivo == NULL) {
        printf("Erro! Nao foi possivel abrir o arquivo turmas.txt.\n");
        return 1; 
    }

    // 6. Escrever os dados no arquivo (com a correção do \n)
    // Nota: Limite de alunos fixados em "30" 
    fprintf(arquivo, "\n%s;%s;30;%s", serie, professor, ras);

    // 7. Fechar o arquivo
    fclose(arquivo);

    // 8. Mensagem de sucesso
    printf("\n----------------------------------------\n");
    printf("SUCESSO: Turma '%s' foi adicionada.\n", serie);
    printf("----------------------------------------\n");

    return 0; 
}