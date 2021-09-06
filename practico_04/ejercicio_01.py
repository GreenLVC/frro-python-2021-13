"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3


def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """
    db = sqlite3.connect("database.db")
    cursor = db.cursor()

    script_sql = "CREATE TABLE IF NOT EXISTS Persona (IdPersona INTEGER PRIMARY KEY, Nombre TEXT(30)," \
                 " FechaNacimiento TEXT(10), DNI INTEGER, Altura INTEGER)"

    cursor.execute(script_sql)
    db.commit()
    cursor.close()
    db.close()


def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada
    anteriormente."""
    db = sqlite3.connect("database.db")
    cursor = db.cursor()

    script_sql = "DROP TABLE IF EXISTS Persona"

    cursor.execute(script_sql)
    cursor.close()
    db.commit()
    db.close()


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
