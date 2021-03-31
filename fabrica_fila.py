from typing import Union

from constantes import TP_FILA_NORMAL, TP_FILA_PRIORITARIA
from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria


class FabricaFila:
    @staticmethod
    def pega_fila(tipo_fila: int) -> Union[FilaNormal, FilaPrioritaria]:
        if tipo_fila == TP_FILA_NORMAL:
            return FilaNormal()
        elif tipo_fila == TP_FILA_PRIORITARIA:
            return FilaPrioritaria()
        else:
            raise NotImplementedError('Tipo de Fila não existe.')
