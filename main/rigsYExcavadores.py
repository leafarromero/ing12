from .modeloDeRig import ModeloDeRig, cargarModelosDeRig

class Rig:
    def __init__(self, modelo, diasRestantes):
        self._modelo = modelo
        self._diasRestantes = diasRestantes

    def modelo(self):
        return self._modelo

    def costoAlquiler(self):
        return self._modelo.costoAlquiler()

    def litrosCombustiblePorDia(self):
        return self._modelo.litrosCombustiblePorDia()

    def excavar(self, parcela):
        parcela.pozo().excavar(self._modelo.metrosPorDia() * parcela.resistencia())

    def diasRestantes(self):
        return self._diasRestantes

    def pasarDia(self):
        self._diasRestantes = self._diasRestantes - 1


class Excavador:
    def __init__(self, log, confPath):
        archivo = confPath + "excavador.txt"
        with open(archivo, "r") as as_file:
            linea = as_file.readline()
            self._dolaresPorLitroDeCombustible = float(linea)
        self.log = log

    def excavar(self, parcela, rig):
        rig.excavar(parcela)
        self.log.escribirLinea("Efectuada excavacion\n")
        self.log.gasto(rig.litrosCombustiblePorDia * self._dolaresPorLitroDeCombustible)
        if parcela.tienePozo():
            self.log.escribirLinea("Pozo terminado\n")


class RigManager:
    def __init__(self, log, administradorDeRig):
        self.log = log
        self.administradorDeRig = administradorDeRig

    def alquilar(self, modelo, cantidadDeDias):
        self.log.escribirLinea("Nuevo rig alquilado, modelo: " + modelo.nombre() + "\n")
        self.log.gasto((modelo.costoAlquiler()) * cantidadDeDias)
        self.administradorDeRig.agregarRig(Rig(modelo, cantidadDeDias))


class AdministradorDeRigs:
    def __init__(self,confPath):
        self._rigs = set()
        self._modelosDeRigs = cargarModelosDeRig(confPath)

    def rigs(self):
    	return self._rigs

    def modelosDeRigs(self):
        return set(self._modelosDeRigs)

    def agregarRig(self, rig):
        self._rigs.add(rig)

    def pasarDia(self,log):
        rigsABorrar = set()
        for rig in self._rigs:
            rig.pasarDia()
            if rig.diasRestantes() == 0:
                log.escribirLinea("rig cauduco alquiler, modelo: " + rig.modelo().nombre()+"\n")
                rigsABorrar.add(rig)
        for rig in rigsABorrar:
            self._rigs.discard(rig)
        return rigsABorrar
