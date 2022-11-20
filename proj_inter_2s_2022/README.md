# IFSP Projeto Interdisciplinar 2S.2022
![App Screenshot](https://uploaddeimagens.com.br/images/000/705/999/original/League-Of-Legends-Logo-3.jpg?1472669894)

## O que é League?
League of Legends (abreviado como LoL e comumente referido como League) é um jogo eletrônico do gênero multiplayer online battle arena (MOBA) desenvolvido e publicado pela Riot Games.

No jogo, duas equipes de cinco jogadores batalham em um combate jogador contra jogador (PvP), com cada equipe ocupando e defendendo sua metade do mapa.

Cada um dos dez jogadores controla um personagem, conhecido como "campeão", com habilidades únicas e diferentes estilos de jogo. 

Durante uma partida, os campeões se tornam mais poderosos ao coletarem pontos de experiência, ganharem ouro e comprarem itens a fim de derrotar a equipe adversária. 

No modo principal, Summoner's Rift, o objetivo primário é avançar até a base inimiga e destruir uma grande estrutura localizada em seu centro, sob o nome de "Nexus.

## Qual o Objetivo deste projeto?

As escolhas acontecem por turnos e sempre haverá uma pessoa que escolherá por último. 
Nesse sentido, qual seria a melhor escolha para ela pensando em otimizar a chance do time ganhar?

## Etapas de desenvolvimento

A extração dos dados aconteceu através da API da Riot ( https://developer.riotgames.com/ ), onde extraimos **35309 registros de partida com 82 colunas** sendo que após um tratamento inicial dos dados chegamos a um total de  **27477** partidas a serem analisadas.

Os dados foram coletados por um mês ( 1 vez por semana) sendo estes dados referentes aos 200 melhores jogadores do Brasil segundo o rankingo do jogo. 

A descrição dos dados esta no notebook.

Os dados Inicialmente foram armazenados localmente e em seguida armazenados em um bucket no amazon S3 seguindo a arquitetura.

![App Screenshot](https://github.com/LucasPieroo/Pos-IFSP/blob/main/proj_inter_2s_2022/Imagens/arquitetura.PNG?raw=true)

E a o bloco de anotações com as seguintes configurações :

![App Screenshot](https://github.com/LucasPieroo/Pos-IFSP/blob/main/proj_inter_2s_2022/Imagens/config_ba.PNG?raw=true)

A análise de dados foi feita toda pelo Amazon SageMaker e seguiu as etapa seguintes começando pela criação de um modelo de previsão de vitória:

- Exploração dos dados
- Seleção inicial de modelos
- otimização de hyperparametros
- Otimização de thresholds
- Definição de pipeline para tratamento de dados
- Modelo de voto majoritório a partir de 3 modelos

Após esses passos obtemos um modelo consistente na previsão de vitória

Para o Modelo de recomendação rodamos a partir de 9 escolhas qual seria o personagem restante que otimizaria a chance de vitória do time dele.

## Resultados

O modelo de previsão de vitória teve bons resultados, porém o sistema de recomendação foi falho e precisa ser revisto e melhorado
