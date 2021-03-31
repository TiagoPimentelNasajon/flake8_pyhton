# from constantes import TP_FILA_NORMAL
from constantes import TP_FILA_PRIORITARIA
from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida


fila = FabricaFila.pega_fila(TP_FILA_PRIORITARIA)

fila.atualiza_fila()
fila.atualiza_fila()
fila.atualiza_fila()
fila.atualiza_fila()

print(fila.chama_cliente(10))
print(fila.chama_cliente(20))
print(fila.chama_cliente(20))

print(fila.estatisticas('29/03/2021', 204, EstatisticaResumida))
print(fila.estatisticas('29/03/2021', 204, EstatisticaDetalhada))
