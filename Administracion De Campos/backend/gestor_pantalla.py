import time 

class GestorCampo:
  def __init__(self, pant):
    self.pantalla = pant
    self.nombreCampo = None
    self.numeroLote= None
    self.supCampo = None
    self.supLotes = None 
    self.tiposSuelo = None
    self.tipoSueloElegido = None

  def pedirNombreCampo(self):
    self.pantalla.pedirNombreCampo()


class PantAdmCampo:
  def __init__(self):
    self.gestor = None
    self.comboTiposSuelo = None
    self.grillaLote = None
    self.lblNombreCampo = None
    self.NroLote = None
    self.lblSuperficieCampo = None
    self.lblSuperficieLote = None
    self.txtNombreCampo = None
    self.txtNroLote = None
    self.txtSupCampo = None
    self.txtTipoSuelo = None

  def opcionRegCampo(self):
    print("***Habilitando ventana para el registro de un campo***")
    self.habilitarVentana()
    self.gestor = GestorCampo(self)
    self.gestor.pedirNombreCampo()

  def pedirNombreCampo(self):
    print("Notificando a la pantalla...")
  
  def habilitarVentana(self):
    pass