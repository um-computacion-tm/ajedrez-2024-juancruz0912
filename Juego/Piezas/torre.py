from .pieza import PiezaId 

class Torre(PiezaId):

    pieza_blanca = '♖'
    pieza_negra = '♜'
    c1 = 1
    c2 = 8
    
    def __init__(self, color, **kwargs):
        super().__init__('Torre', color, id=kwargs['id'], movimiento='Recto')

    def movimiento_especifico(self, fila, columna):
        return self.es_movimiento_recto(fila, columna)
            