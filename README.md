# Arnold-Cat-Map
Este repositorio contiene una implementación en Python del algoritmo Arnold Cat Map, una transformación caótica que reorganiza los píxeles de una imagen cuadrada de forma reversible. Es ideal para experimentos con teoría del caos, criptografía visual y procesamiento de imágenes. 
# Arnold Cat Map en Python

Este proyecto implementa el algoritmo **Arnold Cat Map**, una transformación caótica y reversible que reordena los píxeles de una imagen cuadrada. Es útil para explorar conceptos de teoría del caos, cifrado visual y manipulación de imágenes.

## 📷 Ejemplo

| Original | Después de 10 iteraciones |
|----------|----------------------------|
| ![original](ruta/a/tu/imagen_original.jpg) | ![transformada](ruta/a/tu/imagen_transformada.jpg) |

> *Nota: Después de cierto número de iteraciones, la imagen vuelve a su estado original.*

---

## ¿Qué es el Arnold Cat Map?

El Arnold Cat Map es una transformación bidimensional definida por:
(x', y') = ((x + y) % N, (x + 2y) % N)

Donde `x, y` son las coordenadas originales del píxel y `N` es el tamaño de la imagen (debe ser cuadrada).

---

## 🛠Requisitos

- Python 3.7 o superior
- [Pillow](https://pillow.readthedocs.io/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

Instálalos con:

pip install pillow matplotlib numpy

