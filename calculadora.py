import tkinter as tk
from tkinter import messagebox

class CalculadoraError:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Modificada - Spyder")
        self.root.geometry("300x400")
        
        self.ecuacion = ""
        self.input_text = tk.StringVar()
        
        input_frame = self.create_display()
        input_frame.pack(side=tk.TOP)
        
        btns_frame = self.create_buttons()
        btns_frame.pack()

    def create_display(self):
        frame = tk.Frame(self.root, bd=0, width=40, height=50, relief=tk.RIDGE)
        input_field = tk.Entry(frame, textvariable=self.input_text, font=('arial', 18, 'bold'),
                               width=20, bd=10, insertwidth=4, bg="powder blue", justify='right')
        input_field.grid(row=0, column=0)
        input_field.pack()
        return frame

    def create_buttons(self):
        frame = tk.Frame(self.root, bd=0, width=40, height=50, relief=tk.RIDGE)
        
        # --- FILA 1: C, * ---
        self.crear_boton(frame, "C", 1, 0, lambda: self.btn_clear())
        self.crear_boton(frame, "*", 1, 1, lambda: self.btn_click("*"))  # BOTÓN DE MULTIPLICAR
        
        # --- FILA 2 ---
        self.crear_boton(frame, "7", 2, 0, lambda: self.btn_click(7))
        self.crear_boton(frame, "8", 2, 1, lambda: self.btn_click(8))
        self.crear_boton(frame, "9", 2, 2, lambda: self.btn_click(9))
        
        # --- FILA 3 ---
        self.crear_boton(frame, "4", 3, 0, lambda: self.btn_click(4))
        self.crear_boton(frame, "5", 3, 1, lambda: self.btn_click(5))
        self.crear_boton(frame, "6", 3, 2, lambda: self.btn_click(6))
        
        # --- FILA 4 ---
        self.crear_boton(frame, "1", 4, 0, lambda: self.btn_click(1))
        self.crear_boton(frame, "2", 4, 1, lambda: self.btn_click(2))
        self.crear_boton(frame, "3", 4, 2, lambda: self.btn_click(3))
        
        # --- FILA 5 ---
        self.crear_boton(frame, "0", 5, 0, lambda: self.btn_click(0))
        tk.Button(frame, text="=", width=21, height=3, bd=0, bg="#eee", cursor="hand2",
                  command=lambda: self.btn_igual()).grid(row=5, column=1, columnspan=2, padx=1, pady=1)

        return frame

    def crear_boton(self, frame, text, row, col, command):
        tk.Button(frame, text=text, width=10, height=3, bd=0, bg="#fff",
                   cursor="hand2", command=command).grid(row=row, column=col, padx=1, pady=1)

    # --- LOGICA ---
    def btn_click(self, item):
        self.ecuacion = self.ecuacion + str(item)
        self.input_text.set(self.ecuacion)

    def btn_clear(self):
        self.ecuacion = ""
        self.input_text.set("")

    def btn_igual(self):
        try:
            resultado = ""
            
            # --- ERROR INTENCIONAL ---
            # SI HAY *, se convierte en un + (trampa)
            if "*" in self.ecuacion:
                ecuacion_adulterada = self.ecuacion.replace("*", "+")
                resultado = str(eval(ecuacion_adulterada)) 
                print(f"[DEBUG] Multiplicación detectada → cambiada por suma: {ecuacion_adulterada}")
            else:
                resultado = str(eval(self.ecuacion))

            self.input_text.set(resultado)
            self.ecuacion = resultado 

        except Exception as e:
            self.input_text.set("Error")
            self.ecuacion = ""

# --- BLOQUE PRINCIPAL ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraError(root)
    root.mainloop()
