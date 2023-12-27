import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk 

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

    if file_path:
        print(file_path)
        image = cv2.imread(file_path)
        
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        height, width, _ = image.shape
        if width > 800 or height > 600:
            image_rgb = cv2.resize(image_rgb, (800, 600))

        img_tk = ImageTk.PhotoImage(Image.fromarray(image_rgb))

        label.config(image=img_tk)
        label.image = img_tk
        label.file_path = file_path 

root = tk.Tk()
root.title("Image Viewer")

open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(pady=10)

label = tk.Label(root)
label.pack()

root.mainloop()
