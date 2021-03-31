from typing import Union

from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada
from fila_base import FilaBase
from constantes import CODIGO_NORMAL

classes = Union[EstatisticaResumida, EstatisticaDetalhada]


class FilaNormal(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_NORMAL}{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return('Cliente atual : {} --> Caixa {}'.format(cliente_atual, caixa))

    def estatisticas(self, return_estatistica: classes) -> dict:
        return return_estatistica.roda_estatistica(self.clientes_atendidos)
