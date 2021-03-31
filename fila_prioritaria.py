from typing import Union

from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada

from fila_base import FilaBase
from constantes import CODIGO_PRIORITARIO


classes = Union[EstatisticaResumida, EstatisticaDetalhada]


class FilaPrioritaria(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return('Cliente atual : {} --> Caixa {}'.format(cliente_atual, caixa))

    def estatisticas(self, return_estatistica) -> dict:
        return return_estatistica.roda_estatistica(self.clientes_atendidos)
