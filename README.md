# 🏥 Registro de Pacientes en Python

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![JSON](https://img.shields.io/badge/JSON-Database-green?style=for-the-badge)
![Status](https://img.shields.io/badge/STATUS-FUNCIONAL-success?style=for-the-badge)

Sistema de gestión de pacientes desarrollado en Python utilizando archivos JSON para almacenar la información de manera persistente.

---

# 📌 Características

✅ Registro de pacientes  
✅ Consulta de pacientes por ID  
✅ Actualización de información  
✅ Eliminación de pacientes  
✅ Visualización completa de registros  
✅ Validación de datos  
✅ Persistencia usando JSON  
✅ Menú interactivo en consola  

---

# 🧠 Tecnologías Utilizadas

| Tecnología | Uso |
|---|---|
| Python 3 | Lógica del programa |
| JSON | Almacenamiento de datos |

---

▶️ Cómo Ejecutar el Proyecto
1️⃣ Clonar el repositorio
git clone https://github.com/tuusuario/registro-pacientes.git
2️⃣ Entrar a la carpeta
cd registro-pacientes
3️⃣ Ejecutar el programa
python "Registro de pacientes.py"
o
python3 "Registro de pacientes.py"

#  🖥️ Vista del Menú
********** MENU **********

Presione (1) para introducir los datos del paciente.
Presione (2) para consultar pacientes.
Presione (3) para actualizar los datos del paciente.
Presione (4) para eliminar paciente.
Presione (5) para ver la lista de pacientes guardados.
Presione (6) para salir de la app.

# 💾 Formato de Almacenamiento

Los datos se guardan automáticamente dentro del archivo:

pacientes.json

Ejemplo:

{
    "001-0000000-1": {
        "Nombre": "juan perez",
        "Edad": 25,
        "Direccion": "santo domingo",
        "Diagnostico": "gripe",
        "Alergias": "penicilina",
        "Seguro medico": "senasa"
    }
}

# 🔍 Funciones Principales

Función	Descripción
revisar_pacientes()	Verifica y carga pacientes
archivar_pacientes()	Guarda los datos en JSON
agregar_paciente_nuevo()	Registra nuevos pacientes
consultar_pacientes()	Busca pacientes por ID
actualizar_paciente()	Modifica información existente
eliminar_paciente()	Elimina registros
mostrar_datos_guardados()	Lista todos los pacientes
Menu()	Controla el sistema principal

# 🛡️ Validaciones Implementadas

✔️ Evita IDs duplicadas
✔️ La edad debe ser numérica
✔️ Verifica existencia del archivo JSON
✔️ Control de pacientes inexistentes

# 🚀 Posibles Mejoras Futuras

Interfaz gráfica con Tkinter
Base de datos MySQL o SQLite
Búsqueda por nombre
Historial clínico
Exportar a Excel/PDF
Login de usuarios
Sistema de citas

# 👨‍💻 Autor
Sandy Junior Perez Mendoza

# Proyecto desarrollado con Python para práctica de:

Funciones
JSON
CRUD
Manejo de archivos
Validaciones
Menús 

# 📜 Licencia

Este proyecto es libre para uso educativo y aprendizaje.

⭐ Si te gustó este proyecto

Puedes darle una estrella ⭐ en GitHub.
