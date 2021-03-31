import abc

from constantes import (
    TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO, INCREMENTO_CODIGO_FILA
)


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila: list[str] = []
    clientes_atendidos: list[str] = []
    senha_atual: str = ''

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += INCREMENTO_CODIGO_FILA

    def inseri_cliente(self):
        self.fila.append(self.senha_atual)

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.inseri_cliente()

    @abc.abstractmethod
    def gera_senha_atual(self):
        ...

    @abc.abstractmethod
    def chama_cliente(self, caixa: int):
        ...
