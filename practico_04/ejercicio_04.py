"""Base de Datos SQL - Búsqueda"""

import datetime
import sqlite3

from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    """Implementar la funcion buscar_persona, que devuelve el registro de una 
    persona basado en su id. El return es una tupla que contiene sus campos: 
    id, nombre, nacimiento, dni y altura. Si no encuentra ningun registro, 
    devuelve False."""
    db = sqlite3.connect("database.db")
    cursor = db.cursor()

    script_sql = "SELECT * FROM Persona WHERE IdPersona= ? "
    cursor.execute(script_sql, (id_persona,))
    rs = cursor.fetchone()

    if rs is None:
        return False
    id, nombre, fecha_nac, dni, altura = rs[0], rs[1], datetime.datetime.strptime(rs[2], '%Y-%m-%d %H:%M:%S'), \
                                         rs[3], rs[4]
    cursor.close()
    db.close()
    return id, nombre, fecha_nac, dni, altura


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False


if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
