Projeto: Comparador de Maior/Menor Número (Python)

Este é um projeto simples em Python que pede ao usuário três números inteiros e determina qual deles é o maior e qual é o menor.

O principal objetivo deste projeto é demonstrar as boas práticas de desenvolvimento de software, separando a lógica de negócio (o cálculo) da interface do usuário para permitir a criação de testes unitários robustos. O código original foi refatorado para corrigir bugs de lógica e de digitação.

Estrutura do Projeto

O projeto é dividido em dois arquivos principais:

1.  comparador.py
    * Contém a lógica de negócio isolada nas funções.
    * Contém a função rodar_programa_principal() que lida com a interação do usuário e o tratamento de erros.

2.  test_comparador.py
    * Contém a suíte de testes unitários que valida as funções de lógica.
    * Os testes cobrem múltiplos cenários e casos de borda (números iguais, negativos, zero, etc.).

---

Como Usar

1. Executar o Programa Principal

Para executar o programa e interagir com ele no terminal:
python comparador.py
