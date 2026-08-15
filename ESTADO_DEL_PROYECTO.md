# Estado Actual del Proyecto: Language Library

Este documento detalla el estado actual del desarrollo de la aplicación de escritorio **Language Library**, construida con **Python 3**, **PySide6** y **SQLite3**.

---

## 1. Resumen Ejecutivo

- **Objetivo del Proyecto:** Crear un repositorio personal sencillo y funcional de palabras y frases en diferentes idiomas, con persistencia local en SQLite sin ORMs ni complejidades adicionales.
- **Estado General:** 
  - Capa de base de datos (language_library/database.py) implementada.
  - Se detectó un pequeño error de referencia en database.py (sqlite.IntegrityError en lugar de sqlite3.IntegrityError) a corregir.
  - Pendiente la creación física/verificación de los archivos de interfaz gráfica (language_library/ui/main_window.py) y del punto de entrada (main.py).

---

## 2. Estructura de Archivos

### Estructura Planificada vs. Actual

`
language_library/
├── main.py                          # [Pendiente de crear] Punto de entrada de la aplicación
├── language_library/
│   ├── __init__.py                  # [Creado] Paquete Python
│   ├── database.py                  # [Creado] Módulo de interacción SQLite3
│   └── ui/
│       ├── __init__.py              # [Pendiente de crear]
│       └── main_window.py           # [Pendiente de crear] Interfaz gráfica con PySide6
└── language_library.db              # [Se genera automáticamente al iniciar] Base de datos SQLite
`

---

## 3. Estado de Componentes

### 3.1 Base de Datos (language_library/database.py)
- **Tablas implementadas:**
  - languages: id (INTEGER PK AUTOINCREMENT), 
ame (TEXT NOT NULL UNIQUE).
  - entries: id (INTEGER PK AUTOINCREMENT), language_id (INTEGER FK), 	ext (TEXT NOT NULL), created_at (TEXT), updated_at (TEXT).
- **Operaciones disponibles:**
  - init_db(): Inicializa y crea tablas si no existen.
  - get_languages(): Obtiene idiomas ordenados alfabéticamente.
  - dd_language(name): Inserta un idioma evitando nombres vacíos o duplicados.
  - get_entries(language_id): Obtiene palabras/frases de un idioma por orden de creación.
  - dd_entry(language_id, text): Inserta una entrada con fecha de creación y actualización en ISO-8601 UTC.
  - update_entry(entry_id, new_text): Modifica el texto de una entrada y renueva updated_at.
- **Detalle a corregir:** En la línea 53 se usó sqlite.IntegrityError en lugar de sqlite3.IntegrityError.

### 3.2 Interfaz Gráfica (language_library/ui/main_window.py)
- **Estado:** Código diseñado pero pendiente de guardar en disco.
- **Diseño funcional:**
  - QStackedWidget con 2 pantallas:
    1. **Pantalla de Idiomas:** Lista de idiomas existentes + Botón + Nuevo idioma (con diálogo de texto). Doble clic para abrir el idioma.
    2. **Pantalla de Entradas:** Título del idioma seleccionado + Lista de frases/palabras + Botón + Agregar + Botón ← Volver. Doble clic sobre una frase para editarla.
  - Validaciones de campos vacíos mediante cuadros de diálogo (QMessageBox.warning).

### 3.3 Punto de Entrada (main.py)
- **Estado:** Código diseñado pero pendiente de guardar en disco.
- **Función:** Ejecuta init_db(), instancia QApplication y LanguageLibraryWindow y arranca el bucle de eventos.

---

## 4. Requisitos y Dependencias

- **Python:** 3.8+
- **Bibliotecas requeridas:**
  - PySide6
  - sqlite3 (incluido en la biblioteca estándar de Python)

---

## 5. Próximos Pasos para Finalizar la V1

1. **Corrección de database.py:** Cambiar sqlite.IntegrityError por sqlite3.IntegrityError.
2. **Generar archivos faltantes:**
   - Crear language_library/ui/__init__.py
   - Crear language_library/ui/main_window.py
   - Crear main.py
   - Eliminar archivo redundante database.py de la raíz si no es necesario.
3. **Prueba de Ejecución:**
   - Ejecutar python main.py
   - Validar creación de idiomas, duplicados, agregar entradas, editar entradas y persistencia tras reiniciar la aplicación.
