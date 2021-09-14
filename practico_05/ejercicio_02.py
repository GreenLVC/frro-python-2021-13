"""Base de Datos - ORM"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import false
from ejercicio_01 import Base, Socio

from typing import List, Optional
engine=create_engine('sqlite:///:memory:')

Session=sessionmaker(bind=engine)
session=Session()

class DatosSocio():

    def __init__(self):
        self.id_socio = Socio.id
        self.dni_socio= Socio.dni
        self.nombre= Socio.nombre
        self.apellido= Socio.apellido


    def buscar(self, id_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su id. Devuelve None si no 
        encuentra nada.
        """
        if socio in session.query(Socio).filter(Socio.id.match(id_socio)):
            return socio
        else:
            return None

    def buscar_dni(self, dni_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su dni. Devuelve None si no 
        encuentra nada.
        """
        if socio in session.query(Socio).filter(Socio.dni.match(dni_socio)):
            return socio
        else:
            return None
        
    def todos(self) -> List[Socio]:
        """Devuelve listado de todos los socios en la base de datos."""
        listado = session.query(Socio).all()
        return listado

    def borrar_todos(self) -> bool:
        """Borra todos los socios de la base de datos. Devuelve True si el 
        borrado fue exitoso.
        """
        session.query(Socio).delete()
        if session.query(Socio).first() == None:
            return False
        else:
            return True

    def alta(self, socio: Socio) -> Socio:
        """Agrega un nuevo socio a la tabla y lo devuelve"""
        session.add(socio)
        return 'Id Socio {} dni {} nombre {} apellido {}'.format(self.id_socio,self.dni_socio,self.nombre, self.apellido)

    def baja(self, id_socio: int) -> bool:
        """Borra el socio especificado por el id. Devuelve True si el borrado 
        fue exitoso.
        """
        s = DatosSocio.buscar(id_socio)
        if s == None:  
            return False
        else:
            session.query(Socio).delete(s)
            return True
        

    def modificacion(self, socio: Socio) -> Socio:
        """Guarda un socio con sus datos modificados. Devuelve el Socio 
        modificado.
        """
        s = DatosSocio.buscar(socio.id)
        s = socio
        return s
    
    def contarSocios(self) -> int:
        """Devuelve el total de socios que existen en la tabla"""
        r = session.query(Socio).count()
        return r



# NO MODIFICAR - INICIO

# Test Creación
datos = DatosSocio()

# Test Alta
socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
assert socio.id > 0

# Test Baja
assert datos.baja(socio.id) == True

# Test Consulta
socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
assert datos.buscar(socio_2.id) == socio_2

# Test Buscar DNI
socio_2 = datos.alta(Socio(dni=12345670, nombre='Carlos', apellido='Perez'))
assert datos.buscar_dni(socio_2.dni) == socio_2

# Test Modificación
socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
socio_3.nombre = 'Moria'
socio_3.apellido = 'Casan'
socio_3.dni = 13264587
datos.modificacion(socio_3)
socio_3_modificado = datos.buscar(socio_3.id)
assert socio_3_modificado.id == socio_3.id
assert socio_3_modificado.nombre == 'Moria'
assert socio_3_modificado.apellido == 'Casan'
assert socio_3_modificado.dni == 13264587

# Test Conteo
assert len(datos.todos()) == 3

# Test Delete
datos.borrar_todos()
assert len(datos.todos()) == 0

# NO MODIFICAR - FIN