# from constantes import TP_FILA_NORMAL, TP_FILA_PRIORITARIA
from fabrica_fila import FabricaFila


fila = FabricaFila.pega_fila(1)

fila.atualiza_fila()
fila.atualiza_fila()
fila.atualiza_fila()
fila.atualiza_fila()
fila.atualiza_fila()
fila.atualiza_fila()
fila.atualiza_fila()
fila.atualiza_fila()
fila.atualiza_fila()
fila.atualiza_fila()
fila.atualiza_fila()

print(fila.chama_cliente(10))
print(fila.chama_cliente(20))
print(fila.chama_cliente(20))
print(fila.chama_cliente(10))
print(fila.chama_cliente(20))

# print(fila_teste_2.estatisticas('29/03/2021', '126995', 'detail'))
