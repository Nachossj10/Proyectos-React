import tkinter as tk
from tkinter import ttk
from campo import Campo
from lote import Lote
from tipoSuelo import TipoSuelo

class GestorCampo:
  def __init__(self, pant, campos, tipoS):
    self.pantalla = pant
    self.nombreCampo = None
    self.numeroLote= None
    self.supCampo = None
    self.supLote = None
    self.lotes = []
    self.tiposSuelo = []
    self.tipoSueloElegido = None
    self.campos = campos
    self.tipoSuelo = tipoS


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

  def tomarSuperficieCampo(self, supCampo):
     self.supCampo = supCampo
     print("Superficie recibida: " + self.supCampo)
     self.buscarTiposSuelo()
    
  def buscarTiposSuelo(self):
    for tipo in self.tipoSuelo:
      nombre = tipo.getNombre()
      self.tiposSuelo.append(nombre)
    self.pantalla.pedirDatosLote(self.tiposSuelo)

  def pedirSupLote(self):
    self.pantalla.pedirSupLote()

  def tomarSupLote(self, supLote):
    self.supLote = supLote
    print("Superficie del lote recibida: " + self.supLote)
    self.pantalla.visualizarTiposSuelo()

  def tomarNumeroLote(self, numLot):
    self.numeroLote = numLot
    self.pantalla.pedirSupLote()
    

    

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

    def opcionRegCampo(self):
        print("***Habilitando ventana para el registro de un campo***")

        self.habilitarVentana()
        self.gestor = GestorCampo(self, [campo1, campo2, campo3], [ts1, ts2])

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

    def pedirDatosLote(self, nomTS):
        # Limpiamos los controles anteriores si existen
        if getattr(self, "lbl_superficie", None) is not None and self.lbl_superficie.winfo_exists():
            self.lbl_superficie.destroy()
        if getattr(self, "entry_superficie", None) is not None and self.entry_superficie.winfo_exists():
            self.entry_superficie.destroy()
        if getattr(self, "btn_confirmar_superficie", None) is not None and self.btn_confirmar_superficie.winfo_exists():
            self.btn_confirmar_superficie.destroy()

        self.lbl_numero_lote = tk.Label(
            self.ventana_registro,
            text="Ingrese el número del lote:"
        )
        self.lbl_numero_lote.pack(pady=(10, 5))

        self.frame_lote = tk.Frame(self.ventana_registro)
        self.frame_lote.pack(pady=5)

        def validar_numero(text):
            return text.isdigit() or text == ""

        vcmd = (self.ventana_registro.register(validar_numero), "%P")

        self.entry_numero_lote = tk.Entry(
            self.frame_lote,
            width=15,
            validate="key",
            validatecommand=vcmd
        )
        self.entry_numero_lote.pack(side="left", padx=(0, 10))

        self.btn_siguiente_lote = tk.Button(
            self.frame_lote,
            text="Siguiente",
            command=self.tomarNumeroLote
        )
        self.btn_siguiente_lote.pack(side="left")

    def tomarNumeroLote(self):
        numeroLote = self.entry_numero_lote.get().strip()
        if numeroLote == "":
            print("Debe ingresar el número del lote.")
            return
        print(f"[Pantalla] Número de lote ingresado: {numeroLote}")
        self.gestor.tomarNumeroLote(numeroLote)
        
    def pedirSupLote(self):
      # Ocultamos los controles del nombre
      self.entry_numero_lote.destroy()
      self.lbl_numero_lote.destroy()
      self.frame_lote.destroy()
      self.btn_siguiente_lote.destroy()

      # Creamos los nuevos controles

      self.lbl_superLote = tk.Label(
          self.ventana_registro,
          text="Superficie del Lote (ha):"
      )
      self.lbl_superLote.pack(pady=5)

      self.entry_supLote = tk.Entry(
          self.ventana_registro,
          width=20
      )
      self.entry_supLote.pack()

      self.btn_confirmar_superLote = tk.Button(
          self.ventana_registro,
          text="Siguiente",
          command=self.tomarSupLote
      )
      self.btn_confirmar_superLote.pack(pady=15)
      

    def tomarSupLote(self):
      supLote = self.entry_supLote.get().strip()
      self.gestor.tomarSupLote(supLote)
  
      if getattr(self, "entry_supLote", None) is not None and self.entry_supLote.winfo_exists():
          self.entry_supLote.config(state="disabled")
      if getattr(self, "btn_confirmar_superLote", None) is not None and self.btn_confirmar_superLote.winfo_exists():
          self.btn_confirmar_superLote.config(state="disabled")

    def visualizarTiposSuelo(self, tiposSuelo):
      columnas = ("descripcion", "nombre", "numero")

      # 2. Crear el widget Treeview
      # show="headings" oculta la columna jerárquica por defecto que usa Tkinter
      tabla = ttk.Treeview(self.ventana_registro, columns=columnas, show="headings")

      # 3. Configurar los encabezados (texto que se muestra arriba)
      tabla.heading("legajo", text="Legajo")
      tabla.heading("nombre", text="Nombre")
      tabla.heading("apellido", text="Apellido")

      # 4. Ajustar el ancho y alineación de las columnas
      tabla.column("legajo", width=100, anchor="center")
      tabla.column("nombre", width=180, anchor="w")
      tabla.column("apellido", width=180, anchor="w")
      
      # Insertar filas de datos
      for suelo in tiposSuelo:
          tabla.insert("", tk.END, values=suelo)

      # 6. Agregar una barra de desplazamiento vertical (Scrollbar)
      scrollbar = ttk.Scrollbar(self.ventana_registro, orient="vertical", command=tabla.yview)
      tabla.configure(yscrollcommand=scrollbar.set)

      # Ubicar elementos en la ventana
      tabla.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=10)
      scrollbar.pack(side="right", fill="y", padx=(0, 10), pady=10)



if __name__ == "__main__":

  ts1 = TipoSuelo(1, "humedo", "humedo papi")
  ts2 = TipoSuelo(2, "no tan humedo", "ideal para marihuana")

  campo1 = Campo("campo1", Lote(5, 1, ts1), 5, True)
  campo2 = Campo("campo2", [Lote(6, 1, ts2), Lote(1, 2, ts1)], 7, True)
  campo3 = Campo("campo3", Lote(5, 1, ts1), 5, True)
  pantalla = PantAdmCampo()

  print("INICIANDO PANTALLA DE ESCRITORIO")

  pantalla.interfaz()


