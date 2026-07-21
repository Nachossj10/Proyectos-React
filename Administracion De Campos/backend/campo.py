class Campo:
    def __init__(self, nombre, lote, cantHect, habilitado):
        self.nombre = nombre
        self.cantHectareas = cantHect
        self.habilitado = habilitado
        self.lote = lote
    
    def existeNombre(self, nombreCampoACrear):
      if self.nombre != nombreCampoACrear:
        return False
      else:
        return True