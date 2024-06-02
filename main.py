import tkinter as tk
from tkinter import messagebox

class ObjetivosApp:
    def __init__(self, root, objetivos):
        self.root = root
        self.root.title("Objetivos Diários")
        self.root.geometry("400x400")
        self.root.attributes('-topmost', True)  # Sempre por cima
        self.root.iconbitmap('icon.ico')
        self.root.configure(bg='lightblue')
        
        self.checkboxes = []
        self.objetivos = objetivos.split('\n')

        self.create_widgets()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_widgets(self):
        # Criar frame principal para conter o canvas e a scrollbar
        main_frame = tk.Frame(self.root, bg='lightblue')
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Criar canvas e scrollbar
        canvas = tk.Canvas(main_frame, bg='lightblue')
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(main_frame, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        scrollable_frame = tk.Frame(canvas, bg='lightblue')
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Adicionar os checkboxes
        for objetivo in self.objetivos:
            if objetivo.strip():
                var = tk.BooleanVar()
                chk = tk.Checkbutton(scrollable_frame, text=objetivo, variable=var, bg='lightblue', activebackground='lightblue')
                chk.pack(anchor='w', padx=10, pady=5)
                self.checkboxes.append(var)

        # Criar e posicionar o frame dos botões na parte inferior
        button_frame = tk.Frame(self.root, bg='lightblue')
        button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        tk.Button(button_frame, text="Marcar Todos", command=self.marcar_todas).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Desmarcar Todas", command=self.desmarcar_todas).pack(side=tk.RIGHT, padx=5)



    def on_closing(self):
        if all(var.get() for var in self.checkboxes):
            if messagebox.askokcancel("Sair", "Você tem certeza que deseja sair?"):
                self.root.destroy()
        else:
            messagebox.showwarning("Aviso", "Você deve concluir todas as tarefas antes de sair.")

    def marcar_todas(self):
        for var in self.checkboxes:
            var.set(True)

    def desmarcar_todas(self):
        for var in self.checkboxes:
            var.set(False)

class ObjetivosDialog:
    def __init__(self, parent):
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Objetivos Diários")
        self.dialog.geometry("400x300")
        self.dialog.attributes('-topmost', True)  # Sempre por cima
        self.dialog.iconbitmap('icon.ico')
        self.dialog.configure(bg='lightblue')

        self.objetivos = []
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.dialog, text="Digite um objetivo:", bg='lightblue').pack(pady=10)
        self.text_box = tk.Text(self.dialog, height=2, width=50)
        self.text_box.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)
        
        tk.Button(self.dialog, text="Adicionar", command=self.add_objetivo).pack(pady=5)
        tk.Button(self.dialog, text="Concluir", command=self.concluir).pack(pady=5)

        tk.Label(self.dialog, text="Você pode pressionar Enter para adicionar um objetivo.", bg='lightblue').pack(pady=10)
        tk.Label(self.dialog, text="Você pode pressionar Espaço para concluir.", bg='lightblue').pack(pady=5)

        self.text_box.bind("<Return>", lambda event: self.add_objetivo() or 'break')
        self.text_box.bind("<Control-Return>", self.concluir)

    def add_objetivo(self, event=None):
        objetivo = self.text_box.get("1.0", tk.END).strip()
        if objetivo:
            self.objetivos.append(f"- {objetivo[0].upper() + objetivo[1:].lower()}")
            self.text_box.delete("1.0", tk.END)

    def concluir(self, event=None):
        self.dialog.destroy()

def main():
    root = tk.Tk()
    root.withdraw()  # Esconder a janela principal inicialmente

    dialog = ObjetivosDialog(root)
    root.wait_window(dialog.dialog)
    objetivos = "\n".join(dialog.objetivos)

    if objetivos.strip() == "":
        messagebox.showinfo("Nenhum objetivo", "Nenhum objetivo foi fornecido.")
        return

    root.deiconify()  # Mostrar a janela principal após fechar o diálogo
    app = ObjetivosApp(root, objetivos)
    root.mainloop()

if __name__ == "__main__":
    main()
