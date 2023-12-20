import tkinter as tk #basic gui inter face importing 
from tkinter import filedialog # to select one or more file and return the file object dorectly.
from reportlab.pdfgen import canvas
from PIL import Image
import os

class ImageToPDFConverter:
    def __init__(self, root):
        self.root = root
        self.images_paths = []
        self.pdf_name = tk.StringVar()
        self.selected_images_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.initialize_ui()

    def initialize_ui(self):
        # GUI Initialization
        title_label = tk.Label(self.root, text="Image to PDF Converter", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=20)

        select_images_button = tk.Button(self.root, text="Select Images", command=self.select_images_listbox)
        select_images_button.pack(pady=(0, 10))

        self.selected_images_listbox.pack(pady=(0, 10), fill=tk.BOTH, expand=True)
        
        label = tk.Label(self.root, text="Enter the output PDF name")
        label.pack()
        
        pdf_name_entry = tk.Entry(self.root, textvariable=self.pdf_name, width=40, justify="center")
        pdf_name_entry.pack()

        convert_button = tk.Button(self.root, text="Convert to PDF", command=self.convert_images_to_pdf)
        convert_button.pack(pady=(20, 40))

    def select_images_listbox(self):
        # Function to select images
        self.images_paths = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        self.update_selected_images_listbox()

    def update_selected_images_listbox(self):
        # Update listbox with selected images
        self.selected_images_listbox.delete(0, tk.END)
        for image_path in self.images_paths:
            _, filename = os.path.split(image_path)
            self.selected_images_listbox.insert(tk.END, filename)

    def convert_images_to_pdf(self):
        # Function to convert selected images to PDF
        output_pdf_name = self.pdf_name.get().strip(".pdf") + ".pdf" if self.pdf_name.get() else "output.pdf"
        if not self.images_paths:
            return

        pdf = canvas.Canvas(output_pdf_name, pagesize=(612, 792))

        for image_path in self.images_paths:
            img = Image.open(image_path)
            available_width = 600
            available_height = 750
            scale_factor = min(available_width / img.width, available_height / img.height)
            width, height = int(img.width * scale_factor), int(img.height * scale_factor)
            left = (available_width - width) / 2
            top = (available_height - height) / 2
            pdf.drawImage(image_path, left, top, width, height)
            pdf.showPage()

        pdf.save()

def main():
    # Main function to start the application
    root = tk.Tk()
    root.title("Image to PDF")
    root.geometry("400x600")
    converter = ImageToPDFConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
