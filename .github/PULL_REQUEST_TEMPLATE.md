Melhorias realizadas Gustavo:

Nomes de variáveis e funções: Usei nomes descritivos para variáveis e funções, seguindo boas práticas de programação.
ANTES:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/e1742a8e-6bb8-4ea5-8810-a0cffb50c265)

DEPOIS:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/33bdd349-6c00-4e6d-a6fa-dd401ca61ed3)

Funções com ação úinica: criei a função "clear_screen", para ser chamada sempre que o programador deseja limpar a tela.
ANTES:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/48738bcb-7d07-4a96-8669-44c213b4b379)

DEPOIS:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/a32705aa-07e4-47ad-8e1c-170bc12f3443)

Retirada de constantes não utilizadas: limpei as consts "temporárias", utilizadas somente para leitura do projeto durante a criação do mesmo.
ANTES:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/3e46ce8f-6a48-4877-b738-9900df7f63b0)

DEPOIS:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/c56da004-3458-4ebf-8b8b-0c0771a3192f)

Padronização: atualizei os nomes da variáveis para minusculo separado por underline, conforme combinado com o resto do grupo e criando a correta padronização.
ANTES:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/5c633737-6d03-4081-ab27-4cbe45f34401)

DEPOIS:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/bc830fbe-2d00-4a14-985b-36811610c99b)


Melhorias realizadas Natália:

Nomes de variáveis e funções: Transferi nomes de variáveis para o inglês em padrão minúsculo com underline para melhor padronização
ANTES:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/286e699f-f587-4760-8a74-5c07b5b4408b)

DEPOIS:

- show_rules() Modifiquei o sentido da nomenclatura da função iniciar jogo para: "menu" pois, já havia uma função chamada start_game com o propósito de realmente iniciar a jogatina
ANTES:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/8b27ed42-9841-4317-8084-080582a812a4)

DEPOIS:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/65368916-f63f-4bc9-be75-dfba218eda8b)

- set_table() Modifiquei para torná-la mais legível ao eliminar o loop desnecessário e criar o campo de forma mais direta
ANTES:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/9d527a33-adf7-4e4d-9c65-24169e25efdc)

DEPOIS:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/f2d2057d-292c-45e2-a522-c610a9d36357)

- show_table() eliminei o uso repetido de prints e otimizei a formatação da saída
ANTES:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/9d527a33-adf7-4e4d-9c65-24169e25efdc)
DEPOIS:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/67d42796-b316-4e9b-abc5-c8318a55ab68)

- set_bomb() inicializei a matriz de forma mais direta e usei um conjunto (bomb_positions) para rastrear as posições das bombas 
garantindo que cada posição seja única sem a necessidade de um loop grande
ANTES:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/c0bb4c92-d2de-4d55-9a25-76a687441d53)

DEPOIS:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/53e587bb-6893-4d14-b1cf-180f5fb80be4)


Melhorias realizadas Leontino:

Nomes de variáveis e funções: Usei nomes descritivos para variáveis e funções, seguindo boas práticas de programação.
ANTES:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/1a46f7b1-e0ad-48e4-8af4-1fd225f16683)

DEPOIS:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/7ffcd02b-427e-4758-8c55-dc38f4e1e26c)

Comentários: Adicionei comentários explicativos para cada função e bloco de código.
ANTES:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/c9f0bd15-59d9-45d0-a935-398c6277de79)

DEPOIS:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/53a59081-dc28-4f66-bd2a-dff248c50c23)


Validação de entrada: Adicionei validação de entrada na função input_user para garantir que as coordenadas estejam dentro dos limites do tabuleiro e que sejam valores válidos.
ANTES:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/109298b5-a6f0-41ab-b0bd-d06ed5510f13)

DEPOIS:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/be8fb172-5e3e-4826-8e61-e17da0f9fb15)

Estrutura de repetição: Usei um loop while True no end_game para garantir que o usuário insira uma opção válida (S ou N).
ANTES:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/bdd93f44-080e-4281-b037-53866a68074e)

DEPOIS:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/32be1972-8a47-4499-a06d-c7cea8b76a22)

Condicionais simplificadas: Simplifiquei a lógica de atualização do campo com o operador ternário.
ANTES:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/d12d9efa-48b4-4836-94a6-fcbe18ac00a5)

DEPOIS:
![image](https://github.com/GutiCrespo/cleanCode/assets/105143612/8f0b79cf-9c15-45f8-9c87-f04b42462736)
