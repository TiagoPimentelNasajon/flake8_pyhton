from typing import List, Dict, Union


class EstatisticaResumida:
    def __init__(self, dia: str, agencia: int) -> None:
        self.dia = dia
        self.agencia = agencia

    def roda_estatistica(self, clientes_atendidos: List[str]) -> Dict:
        dados: Dict[str, Union[List[str], str, int]] = {}

        dados[f'{self.agencia}-{self.dia}'] = len(clientes_atendidos)

        return dados