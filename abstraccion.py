class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura='caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')

    def _anadir_jabon(self):
        print('Aniadiendo Jabon!!')

    def _lavar(self):
        print('Lavando...')

    def _centrifugar(self):
        print('Centirgugando...')


if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()
