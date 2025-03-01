import os
import ctypes
import sys
import tkinter as tk
from tkinter import messagebox, ttk
from utils.device_manager import disable_device, enable_device, list_devices, list_files_in_use, corrupt_file

class SecurityToolGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("USB Camera Blocker")
        self.root.geometry("1000x600")
        self.root.resizable(False, False)

        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12), padding=6)

        ttk.Label(root, text="Controle de Dispositivos", font=("Arial", 16, "bold")).pack(pady=10)

        self.status_label = ttk.Label(root, text="Status: Aguardando ação", font=("Arial", 12))
        self.status_label.pack(pady=5)

        self.tab_control = ttk.Notebook(root)

        self.tabs = {}
        for device_type in ["camera", "microphone", "audio", "network", "disabled"]:
            frame = ttk.Frame(self.tab_control)
            self.tab_control.add(frame, text=device_type.capitalize())
            self.tabs[device_type] = self.create_device_list(frame, device_type)

        self.tab_control.pack(expand=1, fill='both')

        self.update_device_list(self.tabs["disabled"], "disabled")

    def create_device_list(self, frame, device_type):
        ttk.Label(frame, text=f"Dispositivos {device_type.capitalize()} Detectados", font=("Arial", 12, "bold")).pack(pady=5)

        tree = ttk.Treeview(frame, columns=("#1", "#2", "#3"), show="headings", height=10)
        tree.heading("#1", text="Nome do Dispositivo")
        tree.column("#1", width=500, anchor=tk.W)
        tree.heading("#2", text="Status")
        tree.column("#2", width=150, anchor=tk.CENTER)
        tree.heading("#3", text="Device ID")
        tree.column("#3", width=300, anchor=tk.CENTER)
        tree.pack(padx=10, pady=5)

        control_frame = ttk.Frame(frame)
        control_frame.pack(pady=10)

        ttk.Button(control_frame, text="Desativar", command=lambda: self.disable_selected(tree, device_type)).grid(row=0, column=0, padx=10, pady=5)
        ttk.Button(control_frame, text="Reativar", command=lambda: self.enable_selected(tree, device_type)).grid(row=0, column=1, padx=10, pady=5)
        ttk.Button(control_frame, text="Corromper Arquivo", command=self.corrupt_selected_file).grid(row=0, column=2, padx=10, pady=5)

        self.update_device_list(tree, device_type)
        return tree

    def update_device_list(self, tree, device_type):
        tree.delete(*tree.get_children())
        for device_id, device_name, status in list_devices(device_type):
            tree.insert("", tk.END, values=(device_name, status, device_id), iid=device_id)

    def get_selected_device(self, tree):
        try:
            item = tree.selection()[0]
            return tree.item(item, "values"), item
        except:
            messagebox.showerror("Erro", "Nenhum dispositivo selecionado!")
            return None, None

    def disable_selected(self, tree, device_type):
        device, device_id = self.get_selected_device(tree)
        if device and disable_device(device_id):
            self.update_device_list(tree, device_type)
            self.update_device_list(self.tabs["disabled"], "disabled")

    def enable_selected(self, tree, device_type):
        device, device_id = self.get_selected_device(tree)
        if device and enable_device(device_id):
            self.update_device_list(tree, device_type)
            self.update_device_list(self.tabs["disabled"], "disabled")

    def corrupt_selected_file(self):
        files = list_files_in_use()
        if not files:
            messagebox.showinfo("Nenhum Arquivo", "Nenhum arquivo de gravação foi detectado.")
            return

        for process_name, process_id in files:
            file_path = f"/Users/Public/Videos/{process_name}_recorded.mp4"
            if corrupt_file(file_path):
                messagebox.showinfo("Arquivo Corrompido", f"O arquivo {file_path} foi corrompido com sucesso.")
            else:
                messagebox.showerror("Erro", f"Falha ao corromper {file_path}.")

if __name__ == "__main__":
    if not ctypes.windll.shell32.IsUserAnAdmin():
        messagebox.showerror("Erro", "É necessário executar como Administrador.")
        sys.exit(1)

    root = tk.Tk()
    app = SecurityToolGUI(root)
    root.mainloop()