Melhorias realizadas Gustavo:

Nomes de variáveis e funções: Usei nomes descritivos para variáveis e funções, seguindo boas práticas de programação.
Funções com ação úinica: criei a função "clear_screen", para ser chamada sempre que o programador deseja limpar a tela.
Retirada de constantes não utilizadas: limpei as consts "temporárias", utilizadas somente para leitura do projeto durante a criação do mesmo.
Comentários: Adicionei comentários explicativos em algumas funções, para facilitar a compreensão.
Padronização: atualizei os nomes da variáveis para minusculo separado por underline, conforme combinado com o resto do grupo e criando a correta padronização.


Melhorias realizadas Natália:

Nomes de variáveis e funções: Transferi nomes de variáveis para o inglês em padrão minúsculo com underline para melhor padronização
- show_rules() Modifiquei o sentido da nomenclatura da função iniciar jogo para: "menu" pois, já havia uma função chamada start_game com o propósito de realmente
iniciar a jogatina
- set_table() Modifiquei para torná-la mais legível ao eliminar o loop desnecessário e criar o campo de forma mais direta
- show_table() eliminei o uso repetido de prints e otimizei a formatação da saída
- set_bomb() inicializei a matriz de forma mais direta e usei um conjunto (bomb_positions) para rastrear as posições das bombas 
garantindo que cada posição seja única sem a necessidade de um loop grande


Melhorias realizadas Leontino:

Nomes de variáveis e funções: Usei nomes descritivos para variáveis e funções, seguindo boas práticas de programação.
Comentários: Adicionei comentários explicativos para cada função e bloco de código.
Validação de entrada: Adicionei validação de entrada na função input_user para garantir que as coordenadas estejam dentro dos limites do tabuleiro e que sejam valores válidos.
Estrutura de repetição: Usei um loop while True no end_game para garantir que o usuário insira uma opção válida (S ou N).
Condicionais simplificadas: Simplifiquei a lógica de atualização do campo com o operador ternário.
