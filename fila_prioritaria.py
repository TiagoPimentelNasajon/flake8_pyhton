from typing import Dict, List, Union

from fila_base import FilaBase
from constantes import CODIGO_PRIORITARIO


class FilaPrioritaria(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return('Cliente atual : {} --> Caixa {}'.format(cliente_atual, caixa))

    def estatisticas(self, dia: str, agencia: int, flag: str) -> dict:
        dados: Dict[str, Union[List[str], str, int]] = {}
        if flag != 'detail':
            dados[f'{agencia}-{dia}'] = len(self.clientes_atendidos)
        else:
            dados['dia'] = dia
            dados['agencia'] = agencia
            dados['clientes_atendidos'] = self.clientes_atendidos
            dados['quantidade_clientes_atendidos'] = (
                len(self.clientes_atendidos)
            )

        return dados
