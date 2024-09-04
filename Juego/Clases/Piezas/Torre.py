from .Pieza import PiezaId 

class Torre(PiezaId):

    pieza_blanca = '♖'
    pieza_negra = '♜'

    def __init__(self, color, **kwargs):
        c1 = 1
        c2 = 8
        super().__init__('Torre', color, id=kwargs['id'], c1=c1, c2=c2)

    
    def verificar_movimiento(self, fila, columna):
        return self.es_movimiento_recto(fila, columna)
            