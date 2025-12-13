# Comparación: Programación Tradicional vs. Programación Orientada a Objetos en Python

## Introducción

La resolución de problemas computacionales admite distintos enfoques metodológicos, entre los que destacan la programación tradicional (estructurada) y la programación orientada a objetos (POO). Ambos paradigmas ofrecen rutas viables para implementar soluciones funcionales, pero difieren en organización, escalabilidad y aplicación de principios de diseño. Esta comparación se fundamenta en la implementación de un programa para el cálculo del promedio semanal de temperaturas, evidenciando las implicaciones técnicas de cada aproximación.

## Desarrollo

### Organización y encapsulamiento de datos

En la programación tradicional, los datos y la lógica se manejan de forma separada: las funciones reciben parámetros explícitos y retornan resultados, sin conservar estado entre llamadas. Por ejemplo, la lista de temperaturas se genera en una función y se pasa como argumento a otra para su procesamiento. Este enfoque resulta intuitivo para tareas simples, pero no protege la integridad del estado ante modificaciones accidentales.

En contraste, la POO agrupa datos y comportamiento en clases. En la solución propuesta, la clase `ClimaSemanal` encapsula la lista de temperaturas como atributo privado (`__temperaturas`), restringiendo su acceso directo y exigiendo su manipulación mediante métodos definidos (`ingresar_temperaturas`, `obtener_promedio`). Este diseño favorece la cohesión y reduce el acoplamiento, facilitando la verificación y corrección de errores.

### Reutilización mediante herencia y polimorfismo

La programación tradicional no dispone de mecanismos nativos para extender funcionalidades sin duplicar o modificar código existente. Cada nueva característica (por ejemplo, detección de temperaturas extremas) implicaría crear funciones adicionales con lógica parcialmente repetida.

La POO, en cambio, permite la especialización mediante herencia. La subclase `ClimaSemanalConUmbral` hereda todos los atributos y métodos de `ClimaSemanal`, incorporando únicamente la lógica específica del umbral. Además, sobrescribe el método `mostrar_resultado` para adaptar su comportamiento sin alterar la clase base, ilustrando polimorfismo: distintos objetos responden de forma particular a la misma llamada de método, manteniendo una interfaz común.

### Mantenibilidad y escalabilidad

La solución tradicional se vuelve progresivamente frágil conforme aumenta la complejidad: añadir promedios mensuales, persistencia de datos o múltiples registros climáticos exige coordinar múltiples listas y funciones, incrementando la probabilidad de inconsistencias.

Por su parte, la POO favorece la modularidad. Cada semana climática puede representarse como una instancia independiente, lo que simplifica la gestión de múltiples conjuntos de datos. Asimismo, la incorporación de nuevas capacidades (como exportación a formato JSON o integración con sensores IoT) puede implementarse como nuevos métodos o clases derivadas, sin afectar el núcleo existente.

## Conclusión

Ambos enfoques logran el objetivo funcional planteado, pero con diferentes implicaciones a largo plazo. La programación tradicional es adecuada para scripts pequeños, de propósito único y vida útil limitada. La programación orientada a objetos, aunque requiere una planificación inicial más estructurada, aporta ventajas sustanciales en términos de encapsulamiento, extensibilidad y mantenimiento — cualidades esenciales en sistemas destinados a evolucionar, como los encontrados en aplicaciones de monitoreo ambiental, dispositivos biomédicos o plataformas de salud digital. La elección del paradigma debe basarse no en la brevedad del código, sino en los requisitos de robustez, colaboración y sostenibilidad del proyecto.