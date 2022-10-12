from tkinter import *
from tkinter import ttk
from watermark_module import Marker


def open_image():
    watermarker.pick_image()
    watermarker.resize_image_to_window()
    panel = Label(root, image=watermarker.resized_image)
    panel.image = watermarker.resized_image
    panel.grid(row=4, column=0, columnspan=4)


def get_text():
    text = watermark_text.get()
    color = color_choice.get()
    watermarker.get_text(text)
    watermarker.set_color(color)


def get_location():
    location = position_choice.get()
    watermarker.get_location(location)


def show_image():
    watermarker.watermarking_image()


root = Tk()
root.geometry("900x700+300+150")
root.resizable(width=True, height=True)
root.title("Watermarking Desktop App")
watermarker = Marker()

btn = Button(root, text='open image', command=open_image)
btn.grid(row=0, column=2)
watermark_text = Entry(root, width=35)
watermark_text.grid(row=1, column=1)
btn_confirm_text = Button(root, text="Confirm Text", command=get_text)
btn_confirm_text.grid(row=1, column=3)
text_color = StringVar()
color_choice = ttk.Combobox(root, textvariable=text_color)
color_choice.config(values=("White Text", "Black Text"), state="readonly")
color_choice.set("White Text")
color_choice.grid(column=2, row=1)
text_label = Label(root, text="Enter Watermark Text:")
text_label.grid(row=1, column=0)
position_label = Label(text="Choose Watermark Position")
position_label.grid(row=2, column=0)
position = StringVar()
position_choice = ttk.Combobox(root, textvariable=position)
position_choice.config(values=("Center", "Top-Left", "Top-Right", "Bottom-Left", "Bottom-Right"), state="readonly")
position_choice.set("Center")
position_choice.grid(row=2, column=2)
btn_confirm_position = Button(text="Confirm Position", command=get_location)
btn_confirm_position.grid(row=2, column=3)
btn_show = Button(text="Show", command=show_image)
btn_show.grid(row=3, column=2)

root.mainloop()
