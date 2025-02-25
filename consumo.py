import tkinter as tk
from tkinter import messagebox

# Función para calcular el consumo eléctrico
def calcular_consumo():
    try:
        consumo = float(entry_consumo.get())
        adicional = float(entry_adicional.get())
        
        # Costo por kilovatio-hora
        kilowat = 0.6742
        
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
            mensaje_redondeo = "El resultado es menor a 5 \n no aplica redondeo."
        
        # Mostrar resultados
        resultado = (
            f"Kilovatio-hora:      {kilowat:.4f} \n"
            f"Consumo mas kilowat: {costo_electricidad:.4f} \n"
            f"Costo mas adicional: {costo_electricidad_adicional:.4f} \n"
            f"Mas el IGV (18%):    {igv:.4f} \n"
            f"Monto a pagar:       {total:.4f} \n" 
            f"\n"
            f"{mensaje_redondeo}\n\n"
            f"Total a pagar:       S/.{redondeo} soles\n\n"
            )

        resultado_text.set(resultado)
        
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

def limpiar():
    entry_consumo.delete(0, tk.END)
    entry_adicional.delete(0, tk.END)

def salir():
    root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Consumo Eléctrico")

# Crear y colocar los widgets
label_consumo = tk.Label(root, text="Consumo eléctrico del inquilino:")
label_consumo.grid(row=0, column=0, padx=10, pady=10)

entry_consumo = tk.Entry(root)
entry_consumo.grid(row=0, column=1, padx=10, pady=10)

label_adicional = tk.Label(root, text="Adicional (baño, hall, lavandería):")
label_adicional.grid(row=1, column=0, padx=10, pady=10)

entry_adicional = tk.Entry(root)
entry_adicional.grid(row=1, column=1, padx=10, pady=10)

boton_calcular = tk.Button(root, text="Calcular", command=calcular_consumo)
boton_calcular.grid(row=2, column=0, columnspan=2, padx=10, pady=2)

boton_limpiar = tk.Button(root, text="Limpiar", command=limpiar)
boton_limpiar.grid(row=3, column=0, columnspan=2, padx=10, pady=2)

boton_salir = tk.Button(root, text="Salir", command=salir)
boton_salir.grid(row=4, column=0, columnspan=2, ipadx=10, pady=2)


resultado_text = tk.StringVar()
label_resultado = tk.Label(root, textvariable=resultado_text, justify=tk.LEFT, font=("Courier",12))
label_resultado.grid(row=5, column=0, columnspan=2, ipadx=10)

# Iniciar el bucle principal de la aplicación
root.mainloop()

