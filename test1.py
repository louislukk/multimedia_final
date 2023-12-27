import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title('簡易圖片修改器')
root.geometry('200x200')

def show():
    file_path = filedialog.askopenfilename()
    print(file_path)

btn = tk.Button(root,
                text='開啟檔案',
                font=('Arial',20,'bold'),
                command=show
              )
btn.pack()

root.mainloop()
