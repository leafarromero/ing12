from main.simulacion import Simulacion, Finalizacion
from main.politica_alquiler_rig import UnaPoliticaAlquilerRig
from main.politica_bombeo import UnaPoliticaBombeo
from main.politica_construccion_tanques_agua import PoliticaAguaPost80
from main.politica_construccion_tanques_gas import PoliticaGasPost80
from main.politica_construccion_tanques_sep import PoliticaSepPost80
from main.politica_excavacion import UnaPoliticaExcavacion
from main.politica_venta_gas import UnaPoliticaVentaGas

def ejecutar():
	sim = Simulacion(UnaPoliticaAlquilerRig(), UnaPoliticaExcavacion(), UnaPoliticaBombeo(50,4,"log2.txt",8), PoliticaSepPost80(), PoliticaAguaPost80(), PoliticaGasPost80(), UnaPoliticaVentaGas(),Finalizacion(8))
	while not (sim.finalize()):
		sim.simularDia()
ejecutar()