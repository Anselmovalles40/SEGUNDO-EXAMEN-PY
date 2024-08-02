import cv2

# Cargar la imagen desde un archivo
imagen_color = cv2.imread('goat.jpg')

# Convertir la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2GRAY)

# Mostrar la imagen en escala de grises
cv2.imshow('Imagen en escala de grises', imagen_gris)

# Guardar la imagen en escala de grises
cv2.imwrite('imagen_gris.jpg', imagen_gris)

# Esperar a que se presione una tecla y cerrar la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()