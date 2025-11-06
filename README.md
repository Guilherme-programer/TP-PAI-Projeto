# 🔬 TP PAI: Segmentação e Descrição Geométrica de Imagens

## 🌟 Visão Geral do Projeto

Este projeto é o Trabalho Prático (TP) da disciplina de **Processamento e Análise de Imagens (PAI)**, focado na implementação e comparação de técnicas fundamentais para a análise visual: **Segmentação**, **Detecção de Bordas** e **Representação Estrutural de Formas**.

O trabalho demonstra um pipeline completo, desde a filtragem e isolamento de regiões de interesse até a descrição geométrica de um objeto segmentado.

---

## 🚀 Estrutura e Conteúdo

O projeto é dividido em dois módulos principais que se comunicam através da gravação de um arquivo intermediário (a máscara segmentada).

### 📂 Estrutura de Arquivos

/TP-PAI-Projeto/
├── q1_segmentacao.py
├── q2_descricao_geometrica.py
├── README.md
├── imagem_medica.jpeg
├── cena_real.jpg
├── imagem_industria.webp
└── mask_medica_kmeans.png (Gerado após a execução da Q1)

yaml
Copiar código

---

## 🧩 Questões Abordadas

### **Questão 1: Segmentação e Detecção de Bordas**
- **Métodos Comparados:** Sobel, Laplaciano, Canny, Watershed e K-Means (Simulação de Region Growing).  
- **Contexto:** Análise do desempenho de cada algoritmo em três contextos visuais distintos (Cena Natural, Imagem Médica e Imagem Industrial).

### **Questão 2: Representação e Descrição Geométrica**
- **Técnicas Aplicadas:** Aproximação Poligonal (Douglas-Peucker) e Fecho Convexo (Convex Hull).  
- **Objetivo:** Descrever a geometria do objeto isolado (a figura humana da Imagem Médica), compactando sua forma para análise de características.

---

## 🛠️ Setup e Execução

### 📋 Requisitos

O projeto requer a instalação das seguintes bibliotecas Python:

```bash
pip install opencv-python numpy matplotlib scikit-image scipy
▶️ Instruções de Execução
O fluxo de trabalho é iniciado executando-se apenas o script da Questão 1.

Certifique-se de que todas as imagens de entrada estão no mesmo diretório do script.

Execute o script principal no seu terminal:

bash
Copiar código
python q1_segmentacao.py
O script irá:

Processar a Questão 1 e exibir a matriz comparativa.

Salvar a máscara da Imagem Médica (K-Means) em mask_medica_kmeans.png.

Executar automaticamente o q2_descricao_geometrica.py, exibindo o resultado da Questão 2.

📊 Análise Técnica dos Resultados
1. Desempenho dos Algoritmos de Segmentação (Questão 1)
A matriz comparativa demonstrou a alta dependência dos métodos ao contexto da imagem:

Método	Desempenho Chave	Contexto de Sucesso
K-Means (K=4)	Melhor desempenho na segmentação. Isolou com eficácia regiões de interesse baseadas em classes de intensidade (ex: jaleco branco) e provou ser robusto para foreground/background.	Imagem Médica
Watershed	Falha por supersegmentação. Devido à extrema sensibilidade a gradientes locais, o método gerou inúmeras regiões irrelevantes e ruído topológico em todas as cenas.	Nenhuma das cenas
Canny	Melhor definição de bordas. Produziu bordas finas e conectadas, ideal para análises subsequentes que dependem de contornos bem definidos.	Imagem Industrial e Cena Natural

2. Descrição Geométrica Refinada (Questão 2)
O objeto segmentado (figura humana) foi submetido à análise geométrica.

📢 Processo de Refinamento Necessário
Devido aos ruídos no fundo da imagem médica (artefatos do K-Means), foi implementado um passo de filtragem morfológica (operação de Abertura) no script da Q2 para isolar a silhueta principal.

📈 Resultados da Compactação
Representação	Pontos de Contorno (Original)	Vértices do Polígono (ε=3%)
Contorno Inicial	[Insira o valor de 'original_points']	N/A
Aproximação Poligonal	N/A	[Insira o valor de 'approx_points']

A Aproximação Poligonal (em verde) alcançou uma compactação de [Calcule a Porcentagem de Redução]% dos dados, mantendo a geometria essencial para o reconhecimento de forma.

O Fecho Convexo (em azul) demonstrou a convexidade geral da forma, com as diferenças em relação ao contorno real indicando as concavidades do corpo (ex: axilas).

👤 Autor
Desenvolvedor: Guilherme Eduardo Matos Drumond
