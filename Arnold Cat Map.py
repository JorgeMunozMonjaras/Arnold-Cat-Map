import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def arnold_cat_map(image, iterations):
    """
    Jorge Luis Muñoz Monjarás 178945
    """
    image = image.convert('RGB')
    width, height = image.size
    assert width == height, "La imagen debe ser cuadrada."

    img_array = np.array(image)
    N = width
    result = np.copy(img_array)

    for _ in range(iterations):
        new_img = np.zeros_like(result)
        for x in range(N):
            for y in range(N):
                new_x = (x + y) % N
                new_y = (x + 2*y) % N
                new_img[new_x, new_y] = result[x, y]
        result = new_img

    return Image.fromarray(result)

# === USO ===
if __name__ == "__main__":
    ruta_imagen = "Arnold.jpeg"  # Debe ser cuadrada (ej: 256x256)
    iteraciones = 10

    original = Image.open(ruta_imagen)
    resultado = arnold_cat_map(original, iteraciones)

    # Mostrar
    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(original)
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title(f"Arnold Cat Map ({iteraciones})")
    plt.imshow(resultado)
    plt.axis('off')

    plt.tight_layout()
    plt.show()

    # Guardar resultado
    resultado.save("Transformada.jpg")
