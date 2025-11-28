#include <stdio.h>  // Para printf, fgets, fopen, fclose, fprintf
#include <stdlib.h> // Para exit()
#include <string.h> // Para strcspn() (para remover o \n)

int main() {
    // 1. Variáveis para guardar os dados
    char nome[100];
    char senha[100];
    char cargo[100];
    FILE *arquivo; // Ponteiro para o arquivo

    // 2. Mensagem de boas-vindas
    printf("----------------------------------------\n");
    printf("  Adicionando Novo Docente - ELEVE \n");
    printf("----------------------------------------\n");
    printf("Insira as informacoes solicitadas a seguir:\n\n");

    // 3. Coletar os dados do terminal
    
    // NOME
    printf("Digite o Nome: ");
    fgets(nome, sizeof(nome), stdin);
    nome[strcspn(nome, "\n")] = 0; // Remove a quebra de linha que o fgets captura

    // SENHA
    printf("Digite a Senha: ");
    fgets(senha, sizeof(senha), stdin);
    senha[strcspn(senha, "\n")] = 0; 

    // CARGO
    printf("Digite o Cargo (Admin, Coordenador, Professor): ");
    fgets(cargo, sizeof(cargo), stdin);
    cargo[strcspn(cargo, "\n")] = 0;

    // 4. Abrir o arquivo no modo "append" (anexar)
    // "a" significa que ele vai escrever no *final* do arquivo, sem apagar nada.
    arquivo = fopen("usuarios.txt", "a");

    // 5. Verificar se o arquivo abriu com sucesso
    if (arquivo == NULL) {
        printf("Erro! Nao foi possivel abrir o arquivo usuarios.txt.\n");
        return 1; // Encerra o programa com um código de erro
    }

    // 6. Escrever os dados no arquivo
    // Adicionamos o \n no final para a próxima vez que o programa rodar
    fprintf(arquivo, "\n%s;%s;%s", nome, senha, cargo);

    // 7. Fechar o arquivo
    fclose(arquivo);

    // 8. Mensagem de sucesso
    printf("\n----------------------------------------\n");
    printf("SUCESSO: Docente '%s' foi adicionado.\n", nome);
    printf("----------------------------------------\n");

    return 0;
}