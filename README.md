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

---

## 🧩 Questões Abordadas

### **Questão 1: Segmentação e Detecção de Bordas**
- **Métodos Comparados:** Sobel, Laplaciano, Canny, Watershed e K-Means (Simulação de Region Growing).  
- **Contexto:** Análise do desempenho de cada algoritmo em três contextos visuais distintos (Cena Natural, Imagem Médica e Imagem Industrial).

### **Questão 2: Representação e Descrição Geométrica**
- **Técnicas Aplicadas:** Aproximação Poligonal (Douglas-Peucker) e Fecho Convexo (Convex Hull).  
- **Objetivo:** Descrever a geometria do objeto isolado (a figura humana da Imagem Médica), compactando sua forma para análise de características.

---

# 🛠️ Setup e Execução

## 📋 Requisitos

O projeto requer a instalação das seguintes bibliotecas Python:

```bash
pip install opencv-python numpy matplotlib scikit-image scipy
▶️ Instruções de Execução
O fluxo de trabalho é iniciado executando-se apenas o script da Questão 1, que automaticamente encadeia a execução da Questão 2.

Certifique-se de que todas as dependências estão instaladas.

Verifique se as imagens de entrada estão no diretório raiz.

Execute o script principal no terminal:

Bash

python q1_segmentacao.py
📈 Saídas Esperadas
A execução gerará duas janelas de plotagem do Matplotlib:

Comparação da Q1: Uma matriz comparando os 6 métodos de segmentação/borda nas 3 imagens de contexto.

Descrição Geométrica da Q2: A visualização do objeto segmentado com o Fecho Convexo (azul) e a Aproximação Poligonal (verde) sobrepostos ao contorno refinado.

📝 Análise Técnica (Destaques)
Desempenho dos Algoritmos de Segmentação (Q1) O K-Means (K=4) demonstrou ser o método mais eficaz para isolar o objeto principal na Imagem Médica, realizando uma segmentação foreground/background eficiente. O Canny foi o mais eficiente na detecção de bordas finas e conectadas, ideal para análise estrutural.

Representação Geométrica (Q2) A Aproximação Poligonal foi utilizada como técnica de compactação de dados, reduzindo o contorno de milhares de pontos para dezenas de vértices, preservando a silhueta principal. Refinamento Essencial: Foi aplicada uma filtragem morfológica (Abertura) antes da descrição geométrica, removendo artefatos de fundo do K-Means e mantendo apenas a figura humana. O Fecho Convexo (azul) representa a convexidade geral da forma e serve como base para avaliar as concavidades do corpo.
```

👤 Autor e Documentação
Desenvolvedor: Guilherme Eduardo Matos Drumond

Relatório Técnico Completo: [https://www.overleaf.com/read/tttyhkxhwrkt#821bc3])


