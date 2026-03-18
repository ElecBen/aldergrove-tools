# Notas de diseno

`envuelve()` no parte palabras: si una palabra es mas larga que el
ancho se queda sola en su linea y lo desborda. Partirla obligaria a decidir
donde va el guion, y eso depende del idioma.

`sin_acentos()` descompone en NFKD y tira los combinantes, asi que
tambien convierte la enie en n. Es lo que se quiere para comparar y ordenar,
pero no para mostrar: para eso esta el texto original.

`titulo()` mira la lista MENUDAS en minusculas y nunca la aplica a
la primera palabra. La lista es corta a proposito; ampliarla es cosa de quien
la use, no del modulo.
