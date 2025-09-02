# Tarea Dudo TDD

Simulador del juego Dudo Chileno implementado con metodología TDD usando Python.

## Integrantes
    - Martin Tapia
    - Benjamin Espinoza
    - Juan Umaña

## Descripción

Este proyecto implementa la lógica core del juego tradicional **Dudo en Cacho**, con apuestas, dudas, calces, manejo de dados, reglas especiales de los Ases y rondas especiales para jugadores con un dado.  
El desarrollo se realizó aplicando TDD (Desarrollo guiado por pruebas), asegurando calidad mediante pruebas automáticas y métricas de cobertura.

## Instalación
Debes clonar nuestro repositorio:
```git
    https://github.com/CondorPepinillo/tarea-dudo-TDD12.git
```    
## Requisitos del sistemas
Recuerda que  debes instalar los requerimientos en un entorno virtual

- Python 3.8 o superior
- pytest >= 7.0.0
- pytest-cov >= 4.0.0
- pytest-mock >= 3.14.1

#### Instalar dependencias:
Una vez creado, se debe activar el entorno virtual y ejecutar el siguiente comando:
```bash
pip install -r requirements.txt
```


## Ejecucion Tests
Para la correcta ejecucion de los tests debes usar el siguiente comando.
```bash
python pytest 
```
Si deseas hacer un analisis de la covertura de nuestros test:
```bash
python pytest --cov=src --cov-report=term-missing
```
Ademas hemos agregado reportes html, los cuales se encuentran en la carpeta "htmlcov" y deberias abrir un archivo "index.html" la cual es una pagina navegable para una facil comprension de estos