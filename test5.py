import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance
from tkinter import messagebox

root = tk.Tk()
root.title('Image Viewer')
root.geometry('800x600')

img_path = ""
initial_img = None
img = None
saved_enhance_values = {}

def show_image(update_scales=True, updated_img=None):
    global img
    if updated_img:
        img = updated_img
    w, h = img.size
    tk_img = ImageTk.PhotoImage(img)
    canvas.delete('all')
    canvas.config(scrollregion=(0, 0, w, h))
    canvas.create_image(0, 0, anchor='nw', image=tk_img)
    canvas.tk_img = tk_img

    if update_scales:
        scale_1.set(0)
        scale_2.set(0)
        scale_3.set(0)
        scale_4.set(0)
def enhance(e):
    saved_enhance_values['scale_1'] = int(scale_1.get())
    saved_enhance_values['scale_2'] = int(scale_2.get())
    saved_enhance_values['scale_3'] = int(scale_3.get())
    saved_enhance_values['scale_4'] = int(scale_4.get())
    
    output = img.copy()
    brightness = ImageEnhance.Brightness(output)
    output = brightness.enhance(1 + saved_enhance_values['scale_1'] / 100)
    contrast = ImageEnhance.Contrast(output)
    output = contrast.enhance(1 + saved_enhance_values['scale_2'] / 100)
    color = ImageEnhance.Color(output)
    output = color.enhance(1 + saved_enhance_values['scale_3'] / 100)
    sharpness = ImageEnhance.Sharpness(output)
    output = sharpness.enhance(1 + saved_enhance_values['scale_4'] / 10)

    tk_img = ImageTk.PhotoImage(output)
    canvas.delete('all')
    canvas.create_image(0, 0, anchor='nw', image=tk_img)
    canvas.tk_img = tk_img                                 

def open_file():
    global img, img_path, initial_img
    try:
        img_path = filedialog.askopenfilename(filetypes=[("Image files", ".png;.jpg;.jpeg;.gif")])
        img = Image.open(img_path)
        initial_img = img.copy() if img else None  
        show_image()
    except Exception as e:
        messagebox.showerror('Error', str(e))

def save():
    global output
    try:
        img_path = filedialog.asksaveasfile(filetypes = [('png', '*.png'),('jpg', '*.jpg'),('gif', '*.gif')]).name  
        img_type = img_path.split('.')[1]    
        output.save(img_path, img_type)
        messagebox.showinfo('showinfo', '儲存完成')
    except:
        pass


def exit():
    print('exit')
    root.destroy()
    
def rotate_image():
    global img
    img = img.rotate(-90)
    show_image()

def reset_image():
    global img
    if initial_img:
        img = initial_img.copy()
        show_image()
def adjust_red(inc):
    global img
    if img:
        img_copy = img.copy()  
        img_copy = img_copy.convert('RGB')
        r, g, b = img_copy.split()
        r = r.point(lambda i: i + int(inc))
        img_copy = Image.merge('RGB', (r, g, b))
        show_image(update_scales=True, updated_img=img_copy)  

def adjust_green(inc):
    global img
    if img:
        img_copy = img.copy()
        img_copy = img_copy.convert('RGB')
        r, g, b = img_copy.split()
        g = g.point(lambda i: i + int(inc))
        img_copy = Image.merge('RGB', (r, g, b))
        show_image(update_scales=True, updated_img=img_copy) 

def adjust_blue(inc):
    global img
    if img:
        img_copy = img.copy()
        img_copy = img_copy.convert('RGB')
        r, g, b = img_copy.split()
        b = b.point(lambda i: i + int(inc))
        img_copy = Image.merge('RGB', (r, g, b))
        show_image(update_scales=True, updated_img=img_copy) 

menu = tk.Menu(root)                           
menubar = tk.Menu(menu)
menubar.add_command(label="開啟", command=open_file) 
menubar.add_command(label="儲存", command=save) 
menubar.add_command(label="結束", command=exit)  
menu.add_cascade(label='檔案', menu=menubar)    
root.config(menu=menu)

frame = tk.Frame(root, width=300, height=300)   
frame.place(x=10,y=10)

canvas = tk.Canvas(frame, width=400, height=300, bg='#fff')  

scrollX = tk.Scrollbar(frame, orient='horizontal')
scrollX.pack(side='bottom', fill='x')
scrollX.config(command=canvas.xview)

scrollY = tk.Scrollbar(frame, orient='vertical')      
scrollY.pack(side='right', fill='y')
scrollY.config(command=canvas.yview)

canvas.config(xscrollcommand=scrollX.set, yscrollcommand=scrollY.set)   
canvas.pack(side='left')

# 亮度
scale_1 = tk.Scale(root, from_=-100, to=100, orient='horizontal', length=150, label='亮度', command=enhance)
scale_1.place(x=10,y=335)
scale_1.set(0)

# 對比
scale_2 = tk.Scale(root, from_=-100, to=100, orient='horizontal', length=150, label='對比', command=enhance)
scale_2.place(x=180,y=335)
scale_2.set(0)

# 飽和度
scale_3 = tk.Scale(root, from_=-100, to=100, orient='horizontal', length=150, label='飽和度', command=enhance)
scale_3.place(x=10,y=410)
scale_3.set(0)

# 銳度
scale_4 = tk.Scale(root, from_=0, to=100, orient='horizontal', length=150, label='銳利度', command=enhance)
scale_4.place(x=180,y=410)
scale_4.set(0)

rotate_button = tk.Button(root, text='旋轉90度', command=rotate_image)
rotate_button.place(x=10, y=490)


reset_button = tk.Button(root, text='一鍵重整', command=lambda: show_image(updated_img=initial_img))
reset_button.place(x=100, y=490)

red_inc_button = tk.Button(root, text='增加紅色', command=lambda: adjust_red(10))
red_inc_button.place(x=190, y=490)

red_dec_button = tk.Button(root, text='減少紅色', command=lambda: adjust_red(-10))
red_dec_button.place(x=280, y=490)


green_inc_button = tk.Button(root, text='增加綠色', command=lambda: adjust_green(10))
green_inc_button.place(x=10, y=520)

green_dec_button = tk.Button(root, text='減少綠色', command=lambda: adjust_green(-10))
green_dec_button.place(x=100, y=520)


blue_inc_button = tk.Button(root, text='增加藍色', command=lambda: adjust_blue(10))
blue_inc_button.place(x=190, y=520)

blue_dec_button = tk.Button(root, text='減少藍色', command=lambda: adjust_blue(-10))
blue_dec_button.place(x=280, y=520)


root.mainloop()
