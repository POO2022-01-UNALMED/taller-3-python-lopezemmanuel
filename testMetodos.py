from televisores.tv import TV
from televisores.control import Control
from televisores.marca import Marca


def testMetodoCanal():

    marca = Marca("Semsung")
    tv1 = TV(marca, True)

    tv1.setCanal(100)
    tv1.canalDown()

    tv2 = TV(marca, False)
    control = Control()
    control.enlazar(tv2)
    control.setCanal(50)
    control.turnOn()
    control.canalUp()

    tv3 = TV(marca, False)
    tv2.setCanal(121)

    ok = False

    if(tv1.getCanal() == 99 and tv2.getCanal() == 2 and tv3.getCanal() == 1):
        ok = True
    assert(ok)


def testMetodoVolumen():

    marca = Marca("Semsung")
    tv1 = TV(marca, True)

    tv1.setVolumen(5)
    tv1.volumenUp()

    tv2 = TV(marca, False)
    control = Control()
    control.enlazar(tv2)
    control.turnOn()
    control.volumenUp()

    tv3 = TV(marca, True)
    tv3.setVolumen(7)
    tv3.volumenUp()

    ok = False

    if(tv1.getVolumen() == 6 and tv2.getVolumen() == 2 and tv3.getVolumen() == 7):
        ok = True
    assert(ok)


def testMetodoEstado():
    marca = Marca("Semsung")
    tv1 = TV(marca, False)
    tv1.turnOff()

    assert(not tv1.getEstado())
