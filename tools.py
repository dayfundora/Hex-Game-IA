# -*- coding: utf8 -*-

__author__ = 'Suilan Estévez Velarde'

class Infinity:
    """Un valor mayor que todos los valores posibles
    de int() para comparaciones en el minimax
    """

    def __init__(self, positive = True):
        self.positive = positive

    def __le__(self, other):
        return not self.positive

    def __ge__(self, other):
        return self.positive

    def __lt__(self, other):
        return not self.positive

    def __gt__(self, other):
        return self.positive

    def __eq__(self, other):
        return False

    def __neg__(self):
        return Infinity(not self.positive)

    def __nonzero__(self):
        return True

# Instancia global de infinito
oo = Infinity()