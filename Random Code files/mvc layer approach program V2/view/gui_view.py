import tkinter as tk
from tkinter import filedialog, messagebox

class GUIView:
    def __init__(self, root):
        self.root = root
        self.root.title("Thumbnail Generator GUI")
        self.input_folder = ""
        self.output_folder = ""
        
        tk.Label(root, text="Input Folder:").pack()
        self.input_entry = tk.Entry(root, width=80)
        self.input_entry.pack()
        tk.Button(root, text="Browse", command=self.browse_input).pack()

        tk.Label(root, text="Output Folder:").pack()
        self.output_entry = tk.Entry(root, width=80)
        self.output_entry.pack()
        tk.Button(root, text="Browse", command=self.browse_output).pack()

        tk.Button(root, text="Generate Thumbnails", command=self.start_process).pack(pady=10)
        self.status = tk.Text(root, height=15, width=90)
        self.status.pack()

    def browse_input(self):
        folder = filedialog.askdirectory()
        if folder:
            self.input_folder = folder
            self.input_entry.delete(0,"end")
            self.input_entry.insert(0, folder)

    def browse_output(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_folder = folder
            self.output_entry.delete(0,"end")
            self.output_entry.insert(0, folder)

    def start_process(self):
        if not self.input_folder or not self.output_folder:
            messagebox.showerror("Error","Select both input and output folders")
            return
        self.root.update()
        from controller.thumbnail_controller import ThumbnailController
        controller = ThumbnailController(self.input_folder, self.output_folder, view=self)
        controller.process()
        messagebox.showinfo("Done","All thumbnails generated!")

    def show_generated(self, name):
        self.status.insert("end", f"Generated: {name}\n")
        self.status.see("end")
        self.root.update()

    def done(self, count, folder):
        self.status.insert("end", f"\nDone! Total {count} thumbnails in folder: {folder}\n")
        self.status.see("end")
        self.root.update()
