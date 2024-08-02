import cv2

# Cargar la imagen desde un archivo
imagen = cv2.imread('777.jpg')

# Convertir la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar el detector de bordes de Canny
# Los umbrales 100 y 200 son valores que puedes ajustar según la imagen y el nivel de detalle deseado
bordes = cv2.Canny(imagen_gris, 100, 200)

# Mostrar la imagen con los bordes detectados
cv2.imshow('Bordes detectados', bordes)

# Guardar la imagen con los bordes detectados
cv2.imwrite('bordes_detectados.jpg', bordes)

# Esperar a que se presione una tecla y cerrar la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()