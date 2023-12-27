import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
from tkinter import simpledialog


class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")

        self.file_path = None
        self.original_image = None
        self.displayed_image = None

        self.open_button = tk.Button(root, text="Open Image", command=self.open_image)
        self.rotate_button = tk.Button(root, text="Rotate 90degree", command=self.rotate_image)
        self.resize_button = tk.Button(root, text="Resize", command=self.resize_image)
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_image)

        self.label = tk.Label(root)

        self.open_button.pack(side=tk.LEFT, padx=5, pady=10)
        self.rotate_button.pack(side=tk.LEFT, padx=5, pady=10)
        self.resize_button.pack(side=tk.LEFT, padx=5, pady=10)
        self.reset_button.pack(side=tk.LEFT, padx=5, pady=10)
        self.label.pack()

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

        if file_path:
            self.file_path = file_path
            self.original_image = cv2.imread(file_path)
            self.display_image(self.original_image)

    def display_image(self, image):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img_tk = ImageTk.PhotoImage(Image.fromarray(image_rgb))
        self.label.config(image=img_tk)
        self.label.image = img_tk

    def rotate_image(self):
        if self.original_image is not None:
            self.original_image = cv2.rotate(self.original_image, cv2.ROTATE_90_CLOCKWISE)
            self.display_image(self.original_image)

    def resize_image(self):
        if self.original_image is not None:
            scale_factor = simpledialog.askfloat("Resize Image", "Enter scale factor:")
            if scale_factor:
                self.original_image = cv2.resize(self.original_image, None, fx=scale_factor, fy=scale_factor)
                self.display_image(self.original_image)

    def reset_image(self):
        if self.file_path:
            self.original_image = cv2.imread(self.file_path)
            self.display_image(self.original_image)

root = tk.Tk()

image_viewer = ImageViewer(root)

root.mainloop()
