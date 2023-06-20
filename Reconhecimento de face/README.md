# 🏆️ Competição de Reconhecimento de Faces - IFSP Campinas  (Entrega: Lucas Piero, CP3016315)

## Introdução

Este Jupyter Notebook apresenta nossa abordagem para a competição de Reconhecimento de Faces do Instituto Federal de São Paulo (IFSP) - Campus Campinas, realizada como parte das atividades avaliativas da disciplina Aplicações em Ciência de Dados (D3APL 2023), integrante do curso de Especialização em Ciência de Dados. 

Link para competição: https://www.kaggle.com/competitions/ifsp-d3apl-2023-face-recognition/overview

O principal objetivo deste trabalho é criar um modelo de rede neural capaz de identificar corretamente os rostos de 83 indivíduos a partir de imagens fornecidas. Para alcançar esse objetivo, vamos usar técnicas avançadas de aprendizado de máquina e processamento de imagens.

No notebook [Brainstorm](https://github.com/LucasPieroo/Pos-IFSP/blob/main/Reconhecimento%20de%20face/Brainstorm.ipynb) você pode encontrar os testes que foram feitos até se chegar na solução final, enquanto no [modelos_finais](https://github.com/LucasPieroo/Pos-IFSP/blob/main/Reconhecimento%20de%20face/modelos_finais.ipynb) você encontra apenas o melhor modelo que foi usado para submissão

## 🎯 Objetivo

Nosso objetivo é desenvolver um modelo de aprendizado de máquina, particularmente uma rede neural, que seja capaz de identificar corretamente um rosto em uma imagem. A partir de uma imagem dada, nosso modelo deve determinar corretamente a quem o rosto pertence, dentre um total de 83 possíveis pessoas.

## 🗄️ Dataset

Para treinar e avaliar nosso modelo, vamos utilizar o conjunto de dados PubFig83, que contém imagens coloridas de rostos de 83 artistas, totalizando 13.840 imagens coletadas da internet. Todas as imagens foram previamente redimensionadas para 100x100 pixels e alinhadas de acordo com a posição dos olhos das pessoas retratadas.

O conjunto de dados de treinamento, denominado `train.zip` e `train.csv`, contém um total de 12.180 imagens rotuladas, distribuídas em 83 classes (pessoas).

O desempenho do nosso modelo será avaliado usando um conjunto de testes não rotulado, contendo um total de 1.660 imagens, chamado `test.zip` e `test.csv`.

## Metodologia

1. Pré-processamento dos dados
2. Construção e avaliação de modelos para comparação
3. Treinamento do modelo final

Esta abordagem servirá como um roteiro para a nossa investigação. Agora, vamos começar a explorar nossos dados!
