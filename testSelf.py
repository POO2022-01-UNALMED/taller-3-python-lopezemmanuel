from televisores.tv import TV
from televisores.control import Control
from televisores.marca import Marca


def testEnlazar():
    marca = Marca("Semsung")

    tv = TV(marca, True)
    control = Control()
    control.enlazar(tv)
    assert(tv.getControl() != None)


def testEnlazarControl():
    marca = Marca("Semsung")

    tv = TV(marca, True)
    control = Control()

    control.enlazar(tv)

    assert(control.getTv() != None)
