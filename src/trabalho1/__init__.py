"""
Introdução ao Processamento de Imagens

Trabalho 1

Questao 1.
Use uma imagem sua de 720p. E implemente o seguinte:
   1.	Faca um laço nas linha por linha e remova um os pixels com posição impar (assumindo que as primeira posição e  0)
   2.	Faca a mesma coisa coluna por coluna
   3.	Mostre a imagem
   4.	Faca um laco linha por linha e crie o pixel removido como a media dos pixels vizinhos, caso so tiver um pixel por ser o último da linha copie igual ao anterior
   5.	Faca a mesma coisa coluna por coluna. Mostre o resultado
   6.	Compra pixel por pixel com a imagem original (fazendo a diferença)  e mostre a media quadrática do erro.

Questao 2.
    Use  a mesma imagem. E Faco um filtro de media tamanho 5x5 no domínio espacial,
    faco a filtragem utilizando um filtro gaussiano no domínio da frequência mudando a frequência de corte ate obter um filtro com resultado o mais parecido possível ao do domínio espacial.
    Para isso use a métrica de erro quadrático médio feito na questão um.
"""

import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter
import scipy.ndimage

class Questao1:
    def __init__(self, image_path: str):
        self.image = Image.open(image_path)
        self.image_array = np.array(self.image)
        self.original_image = self.image_array.copy()

    def _remover_pixels_impares(self):
        # Remover pixels em posições ímpares linha por linha
        self.image_array = self.image_array[:, ::2]

        # Remover pixels em posições ímpares coluna por coluna
        self.image_array = self.image_array[::2, :]

    def _restaurar_pixels(self):
        # Restaurar pixels linha por linha
        linhas, colunas, rgb = self.image_array.shape
        imagem_restaurada = np.zeros(
            (linhas, colunas * 2, rgb), dtype=self.image_array.dtype
        )
        imagem_restaurada[:, ::2, :] = self.image_array

        for i in range(linhas):
            for j in range(1, colunas * 2, 2):
                if j == colunas * 2 - 1:
                    imagem_restaurada[i, j, :] = imagem_restaurada[
                        i, j - 1, :
                    ]  # Copiando o pixel anterior caso seja o último
                else:
                    pixel_anterior = imagem_restaurada[i, j - 1, :]
                    pixel_sucessor = imagem_restaurada[i, j + 1, :]
                    media_pixel = np.mean([pixel_anterior, pixel_sucessor], axis=0)
                    imagem_restaurada[i, j, :] = media_pixel
        self.image_array = imagem_restaurada
        
        # Restaurar pixels coluna por coluna
        linhas, colunas, rgb = self.image_array.shape
        imagem_restaurada = np.zeros(
            (linhas * 2, colunas, rgb), dtype=self.image_array.dtype
        )
        imagem_restaurada[::2, :, :] = self.image_array
        
        for j in range(colunas):
            for i in range(1, linhas * 2, 2):
                if i == linhas * 2 - 1:
                    imagem_restaurada[i, j, :] = imagem_restaurada[
                        i - 1, j, :
                    ]  # Copiando o pixel anterior caso seja o último
                else:
                    pixel_anterior = imagem_restaurada[i - 1, j, :]
                    pixel_sucessor = imagem_restaurada[i + 1, j, :]
                    media_pixel = np.mean([pixel_anterior, pixel_sucessor], axis=0)
                    imagem_restaurada[i, j, :] = media_pixel
        self.image_array = imagem_restaurada

    def _calcular_erro_quadratico_medio(self, first_image: np.ndarray, second_image: np.ndarray):
        # Calcular o erro quadrático médio
        mse = np.mean((first_image - second_image) ** 2)
        return mse

    def _mostrar_imagem(self, image: np.ndarray, title: str):
        fig, ax = plt.subplots()
        ax.imshow(image.astype(np.uint8))
        ax.set_title(title)
        ax.axis("off")
        
        ax.set_xlim(image.shape[1], image.shape[1] * 0.90)
        ax.set_ylim(image.shape[0], image.shape[0] * 0.95)

        plt.show()

    def executar(self):
        self._mostrar_imagem(self.original_image, "Image original")

        self._remover_pixels_impares()
        self._mostrar_imagem(self.image_array, "Imagem com pixels ímpares removidos")

        self._restaurar_pixels()
        self._mostrar_imagem(self.image_array, "Imagem com pixels restaurados")

        mse = self._calcular_erro_quadratico_medio(self.original_image, self.image_array)
        print(f"Erro Quadrático Médio: {mse}")

class Questao2(Questao1):
    def __init__(self, image_path: str):
        super().__init__(image_path)
        # Implementação da Questão 2 pode ser adicionada aqui
        pass

    def executar(self):
        # Filtragem espacial usando um filtro de média 5x5
        filtragem_espacial = np.array(self.image.filter(ImageFilter.BoxBlur(2)))  # Filtro de média 5x5
        self._mostrar_imagem(filtragem_espacial, "Filtragem Espacial 5x5")
        
        # Filtragem no domínio da frequência usando um filtro gaussiano
        sigma = 0
        filtragem_frequencia = np.zeros_like(self.image_array)
        mse = float('inf')
        for sigma_atual in [i * 0.1 for i in range(1, 21)]:  # σ variando de 1 a 2
            filtragem_frequencia_atual = scipy.ndimage.gaussian_filter(self.image_array, sigma=(sigma_atual, sigma_atual, 0))
            
            # self._mostrar_imagem(filtragem_frequencia_atual, f"Filtragem Frequência (sigma={sigma_atual})")
            
            mse_atual = self._calcular_erro_quadratico_medio(filtragem_espacial, filtragem_frequencia_atual)

            if mse_atual < mse:
                sigma = sigma_atual
                mse = mse_atual
                filtragem_frequencia = filtragem_frequencia_atual
            
        self._mostrar_imagem(filtragem_frequencia, f"Filtragem em Frequência (σ={sigma})")
        
        print(f"Erro Quadrático Médio: {mse} com σ={sigma}")

print("-=-=-= Questão 1 =-=-=-")
questao1 = Questao1("src/trabalho1/img.jpg")
questao1.executar()

print("-=-=-= Questão 2 =-=-=-")
questao2 = Questao2("src/trabalho1/img.jpg")
questao2.executar()

__version__ = "0.1.0"
