# 🌌 Multiverso: Órbitas  
**Proyecto de Estructuras de Datos — Visualización Interactiva en 3D**

Este proyecto representa un **multiverso** donde cada universo está organizado en **órbitas de nodos**, cumpliendo con las siguientes características:

✔ Cada universo puede conectar hasta 6 universos  
✔ Las conexiones son **unidireccionales**  
✔ **No se puede volver atrás** al viajar  
✔ Mínimo **36 universos**  
✔ Tamaño ilimitado, con opción de **crear** y **destruir**  
✔ Visualización 3D totalmente interactiva  
✔ Hecho con HTML + JavaScript + Three.js  

La interfaz permite *insertar*, *eliminar*, *buscar*, y *obtener el ID* de cualquier nodo, mientras se actualiza la simulación 3D en tiempo real.

---
## 🚀 Demo en línea

Puedes ejecutar el proyecto directamente desde GitHub Pages aquí:  
👉 **https://<TU-USUARIO>.github.io/<TU-REPO>**
---

## 🧩 Características principales

### 🔧 Estructura de datos implementada
- Uso de una estructura tipo **órbitas circulares** (listas enlazadas y nodos con referencia orbital).
- Cada órbita tiene:
  - Capacidad dinámica
  - Nodos iniciales obligatorios
  - Enlaces entre órbitas (Orb_Anterior y Orb_Siguiente)
  - Posibilidad de eliminar o expandir

### 🌐 Simulación visual
- Renderizado con **Three.js**
- Órbitas animadas
- Nodos como planetas giratorios
- El Sol como centro del sistema
- Colores dinámicos para cada órbita
- Zoom y rotación de la cámara con mouse o touch
- Consola visual integrada

### 🧭 Funciones interactivas
- **Insertar** un universo/nodo
- **Eliminar** por ID
- **Buscar** animadamente un nodo
- **Obtener ID** por (órbita, posición)
- Se representan solo nodos válidos (los vacíos no aparecen)

## 👥 Integrantes:
- Juan David Amado Rubio  
- Pablo Andrés Beltrán Perez  
- Jesús David Cáceres Fonseca  
- David Nickolai Parra Ariza 
---
