# Ejemplos de Aplicación de la Programación Orientada a Objetos en Contextos del Mundo Real

## Introducción

La Programación Orientada a Objetos (POO) constituye un paradigma fundamental en el desarrollo de software moderno, permitiendo modelar sistemas complejos mediante la representación de entidades del mundo real como objetos interactivos. Su correcta aplicación favorece la modularidad, reusabilidad y mantenibilidad del código, aspectos críticos en entornos académicos y profesionales.

El presente directorio reúne cuatro implementaciones en Python que demuestran la utilización de POO en escenarios no triviales y diversos: gestión educativa, logística urbana, plataformas digitales y comunicación social. Estos ejemplos fueron diseñados con el propósito de ilustrar la abstracción de dominios reales, la interacción entre objetos y la aplicación coherente de los principios de encapsulamiento, composición y polimorfismo, evitando enfoques genéricos o sobrerrepresentados (como sistemas bancarios o figuras geométricas).

La selección de contextos responde a criterios de originalidad, aplicabilidad práctica y potencial de extensión, garantizando que cada programa funcione de forma autónoma y esté debidamente documentado.

## Desarrollo

Los cuatro programas incluidos se describen a continuación, destacando su estructura, funcionalidades y aplicación de conceptos POO.

### 1. Sistema de Gestión de Biblioteca (`1_gestion_biblioteca.py`)

Modela el flujo operativo de una biblioteca universitaria, centrándose en el ciclo de préstamo y devolución de libros. Las clases `Libro`, `Usuario` y `Prestamo` establecen una relación clara de responsabilidades:  
- `Libro` gestiona su estado de disponibilidad.  
- `Usuario` administra sus préstamos activos.  
- `Prestamo` actúa como objeto intermedio que registra fechas y controla vencimientos.  

La interacción se manifiesta cuando un usuario solicita un libro: el sistema valida disponibilidad, genera un préstamo y actualiza estados de forma coherente, ejemplificando **encapsulamiento** y **composición**.

### 2. Sistema de Gestión de Parqueaderos (`2_sistema_parqueaderos.py`)

Simula un parqueadero automatizado en un entorno urbano, con tipificación de espacios y vehículos. Las clases `Vehiculo`, `Espacio` y `Parqueadero` permiten:  
- Asignación dinámica de espacios según compatibilidad.  
- Cálculo de tarifas basado en tipo de vehículo y tiempo transcurrido.  
- Control de ocupación mediante métodos explícitos (`ocupar()`, `liberar()`).  

Este ejemplo destaca el uso de **abstracción funcional** (el parqueadero no conoce detalles del vehículo, solo su tipo) y **validación de estado** para prevenir operaciones inválidas.

### 3. Plataforma de Cursos en Línea (`3_plataforma_cursos.py`)

Representa un sistema de aprendizaje digital (LMS) con seguimiento de progreso académico. Las clases `Curso`, `Leccion` y `Estudiante` colaboran para:  
- Registrar inscripciones y progreso por lección.  
- Calcular porcentajes de avance de forma contextualizada.  
- Determinar elegibilidad para certificación (≥80% completado).  

La lógica reside en el `Curso`, que consulta el progreso del `Estudiante`, ilustrando **delegación de responsabilidades** y diseño cohesivo.

### 4. Red Social Minimalista (`4_red_social_simple.py`)

Implementa una red social básica con mecanismos de interacción y privacidad. Las clases `Usuario`, `Publicacion` y `Comentario` permiten:  
- Establecer relaciones de seguimiento unidireccionales.  
- Publicar contenido con visibilidad pública o restringida.  
- Generar *feeds* personalizados basados en redes de seguimiento.  

El método `visible_para(usuario)` ejemplifica **polimorfismo contextual**: su comportamiento varía según el estado (`es_privado`) y las relaciones entre objetos.

Cada programa incluye un bloque de demostración ejecutable (`if __name__ == "__main__":`) que valida su funcionalidad sin dependencias externas.

## Conclusión

Los ejemplos presentados demuestran de manera efectiva la aplicabilidad de la Programación Orientada a Objetos en la resolución de problemas del mundo real, con un enfoque centrado en la claridad conceptual y la solidez técnica. Cada implementación respeta los pilares del paradigma — abstracción, encapsulamiento, composición y polimorfismo — y evita soluciones redundantes o sobrerrepresentadas en la literatura introductoria.

El diseño modular permite futuras extensiones: incorporación de herencia (ej: `CursoAvanzado`), persistencia en base de datos, o integración con interfaces gráficas, sin modificar la lógica central. Asimismo, la documentación interna y la estructura del `README` facilitan la comprensión y reutilización del código.

En conjunto, este conjunto de programas constituye una base sólida para la enseñanza y evaluación de competencias en programación avanzada, destacando la capacidad de traducir requisitos del dominio en modelos computacionales coherentes y mantenibles.