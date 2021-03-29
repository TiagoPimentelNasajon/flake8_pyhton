class FilaPrioritaria:
    codigo: int = 0
    fila: list[str] = []
    clientes_atendidos: list[str] = []
    senha_atual: str = ''

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'PR{self.codigo}'

    def reseta_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return('Cliente atual : {} --> Caixa {}'.format(cliente_atual, caixa))

    def estatisticas(self, dia: str, agencia: int, flag: str) -> dict:
        if flag != 'detail':
            dados = {f'{agencia}-{dia}': len(self.clientes_atendidos)}
        else:
            dados = {}
            dados['dia'] = dia
            dados['agencia'] = agencia
            dados['clientes_atendidos'] = self.clientes_atendidos
            dados['qnt_clientes_atendidos'] = len(self.clientes_atendidos)

        return dados

