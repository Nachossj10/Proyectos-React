import tkinter as tk
import time
from campo import Campo
from lote import Lote
from tipoSuelo import TipoSuelo

class GestorCampo:
  def __init__(self, pant, campos):
    self.pantalla = pant
    self.nombreCampo = None
    self.numeroLote= None
    self.supCampo = None
    self.supLotes = None 
    self.tiposSuelo = None
    self.tipoSueloElegido = None
    self.campos = campos


    self.pedirNombreCampo()

  def pedirNombreCampo(self):
    self.pantalla.pedirNombreCampo()

  def tomarNombreCampo(self, nombre):
    self.nombreCampo = nombre
    print(f"[Gestor] Nombre recibido: {self.nombreCampo}")
    # Aquí continuará el siguiente paso del caso de uso.
    self.validarNombreCampo()
    self.pedirSuperficieCampo()

  def validarNombreCampo(self):
    flagNombreExistente = False
    for campo in self.campos:
      if campo.existeNombre(self.nombreCampo):
        flagNombreExistente = True
        break

    if not flagNombreExistente:  
      print("El nombre: " + self.nombreCampo + " es válido")
      return True
    return

  def pedirSuperficieCampo(self):
    self.pantalla.pedirSuperficieCampo()

  def tomarSuperficieCampo(self, superficie):
     self.supCampo = superficie
     print("Superficie recibida: " + self.supCampo)
    
    

class PantAdmCampo:
    def __init__(self):
        self.gestor = None
        # Inicializamos la ventana principal de Tkinter
        self.root = tk.Tk()
        self.root.title("PantAdmCampo - Administración")
        self.root.geometry("640x400")

        # Componentes visuales iniciales
        self.lbl_bienvenida = tk.Label(self.root, text="Panel de Administración de Campos", font=("Arial", 14))
        self.lbl_bienvenida.pack(pady=10)

        # Botón para iniciar el flujo: opcionRegCampo()
        self.btn_opcion_reg = tk.Button(self.root, text="Opción: Registrar Campo", command=self.opcionRegCampo)
        self.btn_opcion_reg.pack(pady=20)

        # Aquí se pueden agregar los widgets del formulario más adelante.
        self.frame_formulario = None
        self.lbl_nombre = None
        self.entry_nombre = None
        self.btn_confirmar = None
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
        self.gestor = GestorCampo(self, [campo1, campo2, campo3])

    def habilitarVentana(self):
      print("[Pantalla] Ocultando ventana principal y creando la ventana de registro...")
      
      # A) Ocultamos la ventana del menú inicial
      self.root.withdraw()

      # B) Creamos una NUEVA ventana (Toplevel)
      self.ventana_registro = tk.Toplevel(self.root)
      self.ventana_registro.title("Registrar Nuevo Campo")
      self.ventana_registro.geometry("450x400")

      # C) Si el usuario cierra la nueva ventana con la "X", cerramos todo el programa limpiamente
      self.ventana_registro.protocol("WM_DELETE_WINDOW", self.root.destroy)

      # D) Título interno dentro de la nueva ventana
      lbl_titulo = tk.Label(self.ventana_registro, text="Formulario de Registro de Campo", font=("Arial", 12, "bold"))
      lbl_titulo.pack(pady=15)
      
    def pedirNombreCampo(self):

        print("[Pantalla] Mostrando ingreso del nombre.")

        self.lbl_nombre = tk.Label(
            self.ventana_registro,
            text="Nombre del Campo:"
        )
        self.lbl_nombre.pack(pady=5)

        self.entry_nombre = tk.Entry(
            self.ventana_registro,
            width=30
        )
        self.entry_nombre.pack()

        self.btn_confirmar = tk.Button(
            self.ventana_registro,
            text="Aceptar",
            command=self.tomarNombreCampo
        )
        self.btn_confirmar.pack(pady=15)

    def tomarNombreCampo(self):

      nombre = self.entry_nombre.get().strip()

      if nombre == "":
          print("Debe ingresar un nombre.")
          return

      print(f"[Pantalla] Nombre ingresado: {nombre}")

      # Se envía el dato al Gestor
      self.gestor.tomarNombreCampo(nombre)

      # Se deshabilitan los controles solo si todavía existen
      if getattr(self, "entry_nombre", None) is not None and self.entry_nombre.winfo_exists():
          self.entry_nombre.config(state="disabled")
      if getattr(self, "btn_confirmar", None) is not None and self.btn_confirmar.winfo_exists():
          self.btn_confirmar.config(state="disabled")
    
    def interfaz(self):
      self.root.mainloop()

    def pedirSuperficieCampo(self):
        # Ocultamos los controles del nombre
      self.lbl_nombre.destroy()
      self.entry_nombre.destroy()
      self.btn_confirmar.destroy()

      # Creamos los nuevos controles

      self.lbl_superficie = tk.Label(
          self.ventana_registro,
          text="Superficie del Campo (ha):"
      )
      self.lbl_superficie.pack(pady=5)

      self.entry_superficie = tk.Entry(
          self.ventana_registro,
          width=20
      )
      self.entry_superficie.pack()

      self.btn_confirmar_superficie = tk.Button(
          self.ventana_registro,
          text="Aceptar",
          command=self.tomarSuperficieCampo
      )
      self.btn_confirmar_superficie.pack(pady=15)

    def tomarSuperficieCampo(self):
      superficie = self.entry_superficie.get().strip()

      """if superficie == "":
          print("Debe ingresar una superficie.")
          return"""

      """try:
          superficie = float(superficie)
      except ValueError:
          print("La superficie debe ser numérica.")
          return"""

      self.gestor.tomarSuperficieCampo(superficie)

      if getattr(self, "entry_superficie", None) is not None and self.entry_superficie.winfo_exists():
          self.entry_superficie.config(state="disabled")
      if getattr(self, "btn_confirmar_superficie", None) is not None and self.btn_confirmar_superficie.winfo_exists():
          self.btn_confirmar_superficie.config(state="disabled")


if __name__ == "__main__":

  ts1 = TipoSuelo(1, "humedo", "humedo papi")
  ts2 = TipoSuelo(2, "no tan humedo", "ideal para marihuana")

  campo1 = Campo("campo1", Lote(5, 1, ts1), 5, True)
  campo2 = Campo("campo2", [Lote(6, 1, ts2), Lote(1, 2, ts1)], 7, True)
  campo3 = Campo("campo3", Lote(5, 1, ts1), 5, True)
  pantalla = PantAdmCampo()

  print("INICIANDO PANTALLA DE ESCRITORIO")

  pantalla.interfaz()


