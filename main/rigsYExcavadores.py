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
        parcela.pozo.excavar(parcela, self._modelo.metrosPorDia())

    def diasRestantes(self):
        return self._fechaFinDeAlquiler

    def pasarDia(self):
        self._diasRestantes = self._diasRestantes - 1


class Excavador:
    def __init__(self, log, dolaresPorLitroDeCombustible):
        self.dolaresPorLitroDeCombustible = dolaresPorLitroDeCombustible
        self.log = log

    def excavar(self, parcela, rig):
        rig.excavar(parcela)
        self.log.escribirLinea("Efectuada excavacion\n")
        self.log.gasto(rig.litrosCombustiblePorDia * self.dolaresPorLitroDeCombustible)
        if parcela.tienePozo():
            self.log.escribirLinea("Pozo terminado\n")


class RigManager:
    def __init__(self, log, administradorDeRig):
        self.log = log
        self.administradorDeRig = administradorDeRig

    def alquilar(self, modelo, cantidadDeDias, administradorDeRig):
        self.log.escribirLinea("Nuevo rig alquilado, modelo: " + modelo.nombre() + "\n")
        self.log.gasto((modelo.costoAlquilerPorDia()) * cantidadDeDias)
        self.administradorDeRig.agregarRig(Rig(modelo, cantidadDeDias))

    def pasarDia(self):
        rigsCauducados = self.administradorDeRig.pasarDia()
        for rigCauducado in rigsCauducados:
            self.log.escribirLinea("rig cauduco alquiler, modelo: " + rigCauducado.modelo().nombre()+"\n")


class AdministradorDeRigs:
    def __init__(self):
        self.rigs = {}

    def agregarRig(self, rig):
        self.rigs.add(rig)

    def pasarDia(self):
        rigsABorrar = {}
        for rig in self.rigs:
            rig.pasarDia()
            if diasRestantes == 0:
                rigsABorrar.add(rig)
        for rig in rigsABorrar:
            self.rigs.discart(rig)
        return rigsABorrar
