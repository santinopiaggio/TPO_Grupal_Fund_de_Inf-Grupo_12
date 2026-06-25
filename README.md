# TPO - Entrega final
## Velocity Racing Team - Grupo 12

Repositorio correspondiente al Trabajo Práctico Obligatorio de la materia **Fundamentos de Informática**.

**Proyecto:** Velocity Racing Team  
**Grupo:** 12  
**Repositorio:** https://github.com/santinopiaggio/TPO_Grupal_Fund_de_Inf-Grupo_12

---

## Integrantes

- PRIVIDERA, Dante
- CARBONE CIOLA, Agustín
- POLETTI, Agustín Santiago
- RODRIGUEZ, Gonzalo
- PIAGGIO, Santino

---

## Alcance funcional - Entrega final

El sistema desarrollado permite gestionar información deportiva relacionada con pilotos, vehículos y rendimiento dentro de una escudería de competición.

En esta versión se implementan las funcionalidades principales solicitadas para el proyecto **Velocity Racing Team**:

1. Registrar pilotos.
2. Eliminar pilotos existentes.
3. Modificar puntos acumulados o tiempo promedio por vuelta.
4. Visualizar un informe general de pilotos.
5. Salir del sistema.

El sistema trabaja con datos almacenados en memoria utilizando listas, respetando los contenidos trabajados en la materia.

---

## Información administrada

Para cada piloto se registra la siguiente información:

- Nombre del piloto.
- Número identificatorio del monoplaza.
- Escudería asociada.
- Puntos acumulados en el campeonato.
- Tiempo promedio por vuelta.
- Presupuesto asignado.
- Cantidad de abandonos en la temporada.

---

## Estructura del proyecto

El proyecto está dividido en archivos Python para mantener una organización modular:

- `main.py`: contiene el programa principal y el menú de interacción con el usuario.
- `funciones.py`: contiene las funciones utilizadas para validar datos, registrar pilotos, modificar información, eliminar registros y generar reportes matriciales ordenados.
