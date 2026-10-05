
import cv2

# Cargar la imagen
imagen = cv2.imread("C:\IA_Gpo3H\VA_0074\p8-filtro-va-0074\imagenes/cocodrilo0074.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro de mediana
imagen_filtrada = cv2.medianBlur(
    imagen,
    5
)

# Mostrar imágenes
cv2.imshow("Imagen original 0074", imagen)
cv2.imshow("Imagen con filtro de mediana 0074", imagen_filtrada)

# Guardar resultado
cv2.imwrite(
    "../resultados/paisaje_mediana.jpg",
    imagen_filtrada
)

print("Filtro de mediana aplicado correctamente.")
print("Resultado guardado en:")
print("../resultados/paisaje_mediana.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()
print("Programa raealizado por Jaquez Andres 0074")