from typing import List, Dict, Union


class EstatisticaDetalhada:
    def __init__(self, dia: str, agencia: int) -> None:
        self.dia = dia
        self.agencia = agencia

    def roda_estatistica(self, clientes_atendidos: List[str]) -> Dict:
        dados: Dict[str, Union[List[str], str, int]] = {}

        dados['dia'] = self.dia
        dados['agencia'] = self.agencia
        dados['clientes_atendidos'] = clientes_atendidos
        dados['quantidade_clientes_atendidos'] = (len(clientes_atendidos))

        return dados
