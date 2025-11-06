import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.segmentation import watershed
from skimage.feature import peak_local_max
from scipy import ndimage as ndi
import os # Necessário para salvar e rodar o script da Q2


IMAGE_PATHS = {
    'Cena Natural': 'cena_real.jpg',
    'Imagem Médica': 'imagem_medica.webp',
    'Imagem Industrial': 'imagem_industrial.jpg'
}
K_VALUE_Q1 = 4 # Valor K fixo para o K-Means

# --- FUNÇÕES DA QUESTÃO 1: Segmentação ---

def process_image(img_gray, k_value):
    """Aplica todos os algoritmos de segmentação e bordas a uma imagem em escala de cinza."""
    if img_gray is None:
        return None

    gray = img_gray.copy()

    # A. Segmentação por Bordas (Sobel, Laplaciano, Canny)
    gray_float = np.float32(gray)
    sobelx = cv2.Sobel(gray_float, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray_float, cv2.CV_64F, 0, 1, ksize=3)
    sobel_magnitude = cv2.magnitude(sobelx, sobely)
    sobel_res = cv2.convertScaleAbs(sobel_magnitude)
    laplacian = cv2.Laplacian(gray, cv2.CV_16S, ksize=3)
    laplacian_res = cv2.convertScaleAbs(laplacian)
    canny_res = cv2.Canny(gray, threshold1=50, threshold2=150)

    # B. Segmentação por Regiões (Watershed, Region Growing Simulado)
    binary_mask = gray < np.mean(gray)

    if not np.any(binary_mask):
         watershed_display = np.zeros_like(gray)
    else:
        distance = ndi.distance_transform_edt(binary_mask)
        coords = peak_local_max(distance, footprint=np.ones((3, 3)), labels=gray)
        mask = np.zeros(distance.shape, dtype=bool)
        mask[tuple(coords.T)] = True
        markers, _ = ndi.label(mask)
        watershed_res = watershed(-distance, markers, mask=binary_mask)
        max_val = np.max(watershed_res)
        watershed_display = np.uint8(watershed_res * (255 / max_val if max_val > 0 else 0))

    # 5. Region Growing (Simulação K-Means)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    k = k_value  
    pixel_values = gray.reshape((-1, 1))
    pixel_values = np.float32(pixel_values)

    if pixel_values.size < k:
         region_growing_sim = gray
    else:
        try:
            _, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
            centers = np.uint8(centers)
            region_growing_sim = centers[labels.flatten()]
            region_growing_sim = region_growing_sim.reshape(gray.shape)
        except cv2.error:
            region_growing_sim = gray

    return {
        'Original': gray,
        'Sobel': sobel_res,
        'Laplaciano': laplacian_res,
        'Canny': canny_res,
        'Watershed': watershed_display,
        f'Region Growing (K={k_value})': region_growing_sim
    }

# --- Processamento Principal ---
if __name__ == '__main__':
    all_results = {}
    loaded_images = {}

    print("Iniciando Questão 1: Segmentação...")
    for name, path in IMAGE_PATHS.items():
        try:
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                print(f"ERRO: Não foi possível carregar a imagem '{path}'.")
                continue

            h, w = img.shape
            if h > 500 or w > 500:
                scale_percent = 500 / max(h, w)
                img = cv2.resize(img, (int(w * scale_percent), int(h * scale_percent)), interpolation=cv2.INTER_AREA)

            loaded_images[name] = img
            all_results[name] = process_image(img, k_value=K_VALUE_Q1)
            print(f"Processamento de '{name}' concluído.")

        except Exception as e:
            print(f"ERRO grave ao processar {name}: {e}.")

 
    
    image_count = len(all_results)
    if image_count > 0:
        # AQUI VAI O CÓDIGO DE PLOTAGEM DA Q1
        algorithm_titles = ['Original', 'Sobel', 'Laplaciano', 'Canny', 'Watershed', f'Region Growing (K={K_VALUE_Q1})']
        num_cols = len(algorithm_titles)
        fig, axes = plt.subplots(image_count, num_cols, figsize=(num_cols * 3, image_count * 3))

        if image_count == 1: axes = np.array([axes])

        for row_idx, (img_name, results) in enumerate(all_results.items()):
            if results is None: continue
            for col_idx, alg_name in enumerate(algorithm_titles):
                ax = axes[row_idx, col_idx]
                img = results[alg_name]
                if col_idx == 0: ax.set_ylabel(img_name, rotation=90, size='large')
                if row_idx == 0: ax.set_title(alg_name, size='medium')
                
                cmap = 'gray'
                if alg_name.startswith('Watershed'): cmap = 'nipy_spectral'
                
                ax.imshow(img, cmap=cmap)
                ax.axis('off')

        plt.suptitle("Questão 1: Comparação dos Métodos de Segmentação", y=1.02)
        plt.tight_layout()
        plt.show()
    
    # 2. Preparação para a Questão 2 
    if 'Imagem Médica' in all_results:
        mask_to_save = all_results['Imagem Médica'][f'Region Growing (K={K_VALUE_Q1})']
        
        # Salva a máscara para que o script da Q2 possa lê-la
        cv2.imwrite('mask_medica_kmeans.png', mask_to_save) 
        print("\nMáscara segmentada (mask_medica_kmeans.png) salva para a Questão 2.")
    
    # 3. Execução da Questão 2
    try:
        # O sistema operacional executa o script da Q2
        print("Executando o script da Questão 2...")
        os.system('python q2_descricao_geometrica.py') 
    except Exception as e:
        print(f"Erro ao tentar executar q2_descricao_geometrica.py: {e}")