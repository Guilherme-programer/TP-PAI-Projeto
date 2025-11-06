import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Nome do arquivo salvo pelo script Q1
INPUT_MASK_FILE = 'mask_medica_kmeans.png'

# --- FUNÇÃO DA QUESTÃO 2: Descrição Geométrica ---

def describe_shape(mask, approx_epsilon_factor=0.03):
    """
    Aplica Aproximação Poligonal e Fecho Convexo a um objeto em uma máscara binária, 
    após pré-processamento para remoção de ruído.
    """
    mask_bin = cv2.convertScaleAbs(mask)
    
    # Isolar o objeto principal (a pessoa/jaleco) binarizando a região mais clara
    # Mantemos o limiar em 128
    _, mask_target = cv2.threshold(mask_bin, 128, 255, cv2.THRESH_BINARY)
    
    # --- CORREÇÃO APLICADA: FILTRAGEM MORFOLÓGICA (Abertura) ---
    # Kernel 5x5 para operação de Abertura (Erosão seguida de Dilatação).
    # Isso remove blobs brancos pequenos (ruído) sem alterar muito o objeto grande.
    kernel = np.ones((5,5),np.uint8) 
    mask_cleaned = cv2.morphologyEx(mask_target, cv2.MORPH_OPEN, kernel, iterations=1)
    
    # Encontrar o maior contorno na MÁSCARA LIMPA
    contours, _ = cv2.findContours(mask_cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        return None, 0, 0

    c = max(contours, key=cv2.contourArea)
    
    # Se o maior contorno ainda for muito pequeno (só ruído), ignora.
    if cv2.contourArea(c) < 500: 
        return None, 0, 0
    
    # Prepara a imagem de exibição (RGB) usando a máscara limpa
    img_display = cv2.cvtColor(mask_cleaned, cv2.COLOR_GRAY2BGR)
    
    # 1. Fecho Convexo (Azul)
    hull = cv2.convexHull(c)
    cv2.drawContours(img_display, [hull], -1, (255, 0, 0), 2)
    
    # 2. Aproximação Poligonal (Verde)
    perimeter = cv2.arcLength(c, True) 
    epsilon = approx_epsilon_factor * perimeter 
    approx = cv2.approxPolyDP(c, epsilon, True)

    # Desenhar contorno original (Vermelho, fino) e Polígono (Verde, grosso)
    cv2.drawContours(img_display, [c], -1, (0, 0, 255), 1)
    cv2.drawContours(img_display, [approx], -1, (0, 255, 0), 3)

    return img_display, len(c), len(approx)

# --- Processamento Principal da Q2 ---
if __name__ == '__main__':
    if not os.path.exists(INPUT_MASK_FILE):
        print(f"ERRO: Arquivo de entrada '{INPUT_MASK_FILE}' não encontrado.")
        print("Certifique-se de que 'q1_segmentacao.py' foi executado primeiro e salvou a máscara.")
    else:
        mask_q2 = cv2.imread(INPUT_MASK_FILE, cv2.IMREAD_GRAYSCALE)

        print("\nIniciando Questão 2: Descrição Geométrica...")
        
        img_description, original_points, approx_points = describe_shape(mask_q2, approx_epsilon_factor=0.03)

        if img_description is not None:
            fig2, ax2 = plt.subplots(1, 1, figsize=(6, 6))
            
            ax2.imshow(cv2.cvtColor(img_description, cv2.COLOR_BGR2RGB)) 
            ax2.set_title("Questão 2: Representação Geométrica (Imagem Médica - Refinada)")
            ax2.set_xlabel(f"Original: {original_points} pts | Poligonal (ε=3%): {approx_points} vértices | Fecho Convexo: Azul")
            ax2.axis('off')
            plt.tight_layout()
            plt.show()
            print("Visualização da Questão 2 concluída.")
        else:
            print("Não foi possível gerar a visualização da Questão 2. O contorno pode ter sido removido pela filtragem.")