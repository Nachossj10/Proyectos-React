class TipoSuelo:
  def __init__(self, num, nom, desc):
    self.descripcion = desc
    self.nombre = nom
    self.numero = num

  def getNombre(self):
    return self.nombre

  def mostrarDescripcion(self):
    return str(self.descripcion)

  def mostrarNumero(self):
    return str(self.numero)