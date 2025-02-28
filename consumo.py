import tkinter as tk
import webbrowser
from tkinter import messagebox
from tkinter import font

# Función para abrir la web
def abrir_url(event):
    webbrowser.open("https://dextre.xyz")

# Función para calcular el consumo eléctrico
def calcular_consumo():
    try:
        consumo = float(entry_consumo.get())
        adicional = float(entry_adicional.get())
        
        # Costo por kilovatio-hora
        kilowat = 0.64
        
        # Calcular el costo total de electricidad
        costo_electricidad = consumo * kilowat
        costo_electricidad_adicional = costo_electricidad + adicional
        
        # Calcular el IGV del 18%
        igv = costo_electricidad_adicional * 0.18
        
        # Calcular el total a pagar
        total = costo_electricidad_adicional + igv
        
        # Redondeo
        parte_entera = int(total)
        parte_decimal = total - parte_entera
        
        if parte_decimal >= 0.5:
            redondeo = parte_entera + 1
            mensaje_redondeo = "El resultado es mayor o igual \na 5, se aplica el redondeo."
        
        else:
            redondeo = parte_entera
            mensaje_redondeo = "El resultado es menor a 5 \nno aplica redondeo."
        
        # Mostrar resultados
        resultado = (
            f"Kilovatio-hora:      {kilowat:.4f} \n"
            f"Consumo mas kilowat: {costo_electricidad:.4f} \n"
            f"Costo mas adicional: {costo_electricidad_adicional:.4f} \n"
            f"Mas el IGV (18%):    {igv:.4f} \n"
            f"Monto a pagar:       {total:.4f} \n" 
            f"\n"
            f"{mensaje_redondeo}\n"
            )

        resultado_text.set(resultado)

       # Mostrar "Total a pagar" en negrita
        label_total.config(text=f"Total a pagar:       S/.{redondeo} soles")        
        
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

def limpiar():
    entry_consumo.delete(0, tk.END)
    entry_adicional.delete(0, tk.END)
    resultado_text.set("")
    label_total.config(text="")
    entry_consumo.focus()  # Colocar el foco en entry_consumo después de limpiar

def salir():
    root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Consumo Eléctrico")

# Establecer un tamaño fijo para la ventana (ancho x alto)
root.geometry("420x390")  # Por ejemplo, 400 píxeles de ancho y 300 de alto

# Crear y colocar los widgets
label_consumo = tk.Label(root, text="Consumo eléctrico del inquilino:")
label_consumo.grid(row=0, column=0, padx=10, pady=10)

entry_consumo = tk.Entry(root)
entry_consumo.grid(row=0, column=1, padx=10, pady=10)

label_adicional = tk.Label(root, text="Adicional (baño, hall, lavandería):")
label_adicional.grid(row=1, column=0, padx=10, pady=10)

entry_adicional = tk.Entry(root)
entry_adicional.grid(row=1, column=1, padx=10, pady=10)

# Crear un frame para contener los botones
frame_botones = tk.Frame(root)
frame_botones.grid(row=2, column=0, columnspan=2, pady=10)

# Crear los botones y colocarlos en el frame
boton_calcular = tk.Button(frame_botones, text="Calcular", command=calcular_consumo)
boton_calcular.pack(side=tk.LEFT, padx=5)

boton_limpiar = tk.Button(frame_botones, text="Limpiar", command=limpiar)
boton_limpiar.pack(side=tk.LEFT, padx=5)

boton_salir = tk.Button(frame_botones, text="Salir", command=salir)
boton_salir.pack(side=tk.LEFT, padx=5)

resultado_text = tk.StringVar()
label_resultado = tk.Label(root, textvariable=resultado_text, justify=tk.LEFT, font=("Courier",12))
label_resultado.grid(row=5, column=0, columnspan=2, ipadx=10)

# se crea fuente negrita
fuente_negrita = font.Font(weight="bold")

# etiqueta para "total a pagar" en negrita
label_total = tk.Label(root, font=fuente_negrita)
label_total.grid(row=6, column=0, columnspan=2, ipadx=10, ipady=5)

# Colocar el foco en entry_consumo al iniciar el programa
entry_consumo.focus()

# Autor
root.grid_rowconfigure(7, weight=1)

label_autor = tk.Label(root, text="Creado por: Jenrry Soto Dextre\n", font=("Arial", 9))
label_autor.grid(row=7, column=0, columnspan=2, pady=5, sticky="s")

# Etiqueta del enlace
label_enlace = tk.Label(root, text="Web: dextre.xyz", font=("Arial", 9), fg="blue", cursor="hand2")
label_enlace.grid(row=7, column=0, columnspan=2, pady=5, sticky="s")

# vincular el boton al hacer click en la url
label_enlace.bind("<Button-1>", abrir_url)

# Iniciar el bucle principal de la aplicación
root.mainloop()

