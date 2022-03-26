from televisores.tv import TV
from televisores.control import Control
from televisores.marca import Marca


def testContador():
    TV.setNumTV(0)
    marca = Marca("Semsung")

    tv1 = TV(marca, True)
    tv2 = TV(marca, True)
    tv3 = TV(marca, True)

    assert(TV.getNumTV() == 3)


def testConstructorMarca():

    TV.setNumTV(0)

    marca = Marca("Semsung")

    assert(marca.getNombre() == "Semsung")


def testConstructorTV():
    TV.setNumTV(0)
    marca = Marca("Xiomi")
    tv1 = TV(marca, True)
    ok = False

    if(tv1.getMarca().getNombre() == "Xiomi" and tv1.getEstado()):
        ok = True

    assert(ok)


def testValoresDefecto():

    marca = Marca("Xiomi")

    tv1 = TV(marca, True)

    ok = False
    if(tv1.getPrecio() == 500 and tv1.getCanal() == 1 and tv1.getVolumen() == 1):
        ok = True
    assert(ok)
