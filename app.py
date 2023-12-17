import tkinter as tk
from tkinter import filedialog
import os

class ImageToPDFConverter:
    def __init__(self, root):
        self.root = root
        self.images_path = []
        self.pdf_name = tk.StringVar()
        self.selected_images_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.initialize_ui()

    def initialize_ui(self):  # Corrected method name
        title_label = tk.Label(self.root, text="Image to PDF Converter", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=20)

def main():
    root = tk.Tk()  # Corrected the case of 'Tk'
    root.title("Image to PDF")
    root.geometry("400x600")  # Corrected geometry dimensions
    converter = ImageToPDFConverter(root)  # Create an instance of ImageToPDFConverter
    root.mainloop()

if __name__ == "__main__":
    main()  # Corrected spacing and called main function
