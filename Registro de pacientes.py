import json

# *********************** DOCUMENTACION ***********************
# ==== Funcionalidades ====

# - Crea un archivo JSON, lo abre en modo lectura para confirmar si esta vacio
# - Despliega un menu de opciones funcional (1-6)
# - Permite guardar, consultar, actualizar y eliminar los datos de los pacientes y guardarlos en un archivo JSON
# - Manda alertas si no hay ningun dato guardado y te redirecciona nuevamente al menu de opciones
# - Si no seleccionas la opcion 6 que es para cerrar el programa, seguira desplegandose el menu de opciones
# - Las funcionalidades estan regidas en su totalidad por funciones y condiciones
# **************************************************************



print("\n******************** Bienvenido a su registro para pacientes ********************\n")

ARCHIVO = "pacientes.json" #Crea el archivo

# Revisa si el archivo existe.
def revisar_pacientes():
    try:
        with open (ARCHIVO, "r") as file:
            return json.load(file)
    except FileNotFoundError:
     return {}
 
 # Guarda los datos con formato JSON. 
def  archivar_pacientes(pacientes):
    with open(ARCHIVO, "w") as file:
        return json.dump(pacientes, file,indent=4)

# Agrega un paciente nuevo, chequea si hay duplicados y chequea que la edad sea un int
def agregar_paciente_nuevo(pacientes):
    identificacion = input("ID del paciente (cedula o pasaporte): ")
    
    if identificacion in pacientes:
        print("\nLos datos del paciente ya estan en la base de datos, elija otra opcion.\n")
        return
    
    nombre_paciente = input("Coloque el nombre del paciente: ").lower()
    
    try:
        edad_paciente = int(input("Edad del paciente: "))
    except ValueError:
        print("\n!!! La edad debe ser un número. Paciente no agregado !!!.\n")
        return
    direccion_paciente = input("Direccion del paciente: ").lower()
    diagnostico_paciente = input("Agregue el diagnostico: ").lower()
    alergias_paciente = input("Alergias conocidas: ").lower()
    seguro_medico = input("Aseguradora de salud: ").lower()
    
    # crea una lista con los datos que acabamos de poner
    pacientes[identificacion] = {
        "Nombre":nombre_paciente,
        "Edad":edad_paciente,
        "Direccion":direccion_paciente,
        "Diagnostico":diagnostico_paciente,
        "Alergias":alergias_paciente,
        "Seguro medico":seguro_medico 
    }
    
    
    archivar_pacientes(pacientes) # Se llama a la funcion para guardar los datos
    print("\n✅ Datos del pacientes guardados con exito, elija que mas hacer.\n")
    
    
# Muestra el registro si la ID existe.   
def consultar_pacientes (pacientes):
    cedula_o_pasaporte = input("Coloque la idenfiticacion del paciente: ")    
    
    if cedula_o_pasaporte in pacientes:
        informacion_paciente = pacientes[cedula_o_pasaporte]
        print("\n********** Informacion general del paciente **********")
        print(f"Nombre: {informacion_paciente['Nombre']}")
        print(f"Edad: {informacion_paciente['Edad']}")
        print(f"Direccion: {informacion_paciente['Direccion']}")
        print(f"Diagnostico: {informacion_paciente['Diagnostico']}")
        print(f"Alergias: {informacion_paciente['Alergias']}")
        print(f"Seguro medico: {informacion_paciente['Seguro medico']}\n")
    else:
        print("\nPaciente no encontrado")
 
# Aplica cambios solo a los campos que llenemos
def actualizar_paciente(pacientes):
    cedula_o_pasaporte = input("Coloque la idenfiticacion del paciente: ") 
    
    if cedula_o_pasaporte not in pacientes:
        print("\nPaciente no encontrado.\n")
        return
    
    datos_actuales = pacientes[cedula_o_pasaporte]
    
    print("\n********IMPORTANTE***********")  
    print("Si no desea cambiar un  campo en especifico dejelo vacio y presione enter.")
    print("*****************************\n")
    
    nuevo_nombre= input("Coloque el nuevo nombre: ")
    nueva_edad= input("Coloque nueva edad: ")
    nueva_direccion= input("Coloque nueva direccion: ") 
    nuevo_diagnostico= input("Coloque nuevo diagnostico: ")
    nueva_alergias= input("Coloque nueva alergia")
    nuevo_seguro= input("Coloque nuevo seguro o diga que no posee uno: ")
    
    
    if nuevo_nombre:
        datos_actuales["Nombre"] = nuevo_nombre.lower()
    if nueva_edad:
        try:
            datos_actuales["Edad"] = int(nueva_edad)
        except ValueError:
            print("\n!!! La edad debe ser un número. Paciente no agregado !!!.")
    if nueva_direccion:
        datos_actuales["Direccion"] = nueva_direccion.lower()
    if nuevo_diagnostico:
        datos_actuales["Diagnostico"] = nuevo_diagnostico.lower()    
    if nueva_alergias:
        datos_actuales["Alergias"] = nueva_alergias.lower() 
    if nuevo_seguro:
        datos_actuales["Seguro medico"] = nuevo_seguro.lower()      
        
    archivar_pacientes(pacientes) # Llama a la funcion para guardar los cambios
    print("\n✅ Datos actualizados.\n")          


# Borra datos y guarda el archivo con el cambio    
def eliminar_paciente(pacientes):
    cedula_o_pasaporte = input("Coloque la idenfiticacion del paciente: ") 
    
    if cedula_o_pasaporte in pacientes:
        del pacientes[cedula_o_pasaporte]
        archivar_pacientes(pacientes)
        print("\n✅ Paciente eliminado con exito.\n")
    else:
        print("\nPaciente no encontrado.")    


# Muestra todos los paciente en formato JSON        
def mostrar_datos_guardados(pacientes):
    if not pacientes:
        print("\n!!! No hay pacientes registrados !!!.\n")
        return

# Muestra los datos de todos los paciente registrados en formato JSON
    print("\n==== LISTA DE PACIENTES ====")
    for cedula, datos in pacientes.items():
        print(f"{cedula} - {datos['Nombre']} - ({datos['Edad']} años) - {datos['Direccion']} - {datos['Diagnostico']} - {datos['Alergias']} - {datos['Seguro medico']}")
    print("\n")        
    
# Menu de opciones valido para opciones del 1 al 6
def Menu():
    pacientes = revisar_pacientes()
    
    while True:
      print("\n********** MENU **********\n")
      print("Presione (1) para introducir los datos del paciente.")
      print("Presione (2) para consultar pacientes.")
      print("Presione (3) para actualizar los datos del paciente.")
      print("Presione (4) para eliminar paciente.")
      print("Presione (5) para ver la lista de pacientes guardados.")
      print("Presione (6) para salir de la app.\n")
      
      opciones = input("Seleccione una opcion (1-6): ")
      
      if opciones == "1":
          agregar_paciente_nuevo(pacientes)
      elif opciones == "2":
          consultar_pacientes(pacientes)
      elif opciones == "3":
          actualizar_paciente(pacientes)
      elif opciones == "4":
          eliminar_paciente(pacientes)   
      elif opciones == "5":
          mostrar_datos_guardados(pacientes)
      elif opciones == "6":
          print("\n====Gracias por usar el programa, hasta la proxima.====\n") 
          break
      else:
          print("**** Opcion no valida, Elija una opcion del 1 al 6.****")        
Menu()          

