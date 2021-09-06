"""Base de Datos SQL - Baja"""

import datetime
import sqlite3

from practico_04.ejercicio_01 import reset_tabla
from practico_04.ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    """Implementar la funcion borrar_persona, que elimina un registro en la 
    tabla Persona. Devuelve un booleano en base a si encontro el registro y lo 
    borro o no."""
    db = sqlite3.connect("database.db")
    cursor = db.cursor()

    script_sql = 'DELETE FROM Persona WHERE IdPersona= ? '
    cursor.execute(script_sql, (id_persona,))
    rs = cursor.rowcount
    db.commit()
    cursor.close()
    db.close()
    if rs >= 1:
        return True
    return False


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False


if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
