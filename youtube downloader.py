from tkinter import *
import tkinter as tk
from pytube import YouTube

window =tk.Tk()
window.geometry("600x200")
window.config(bg="#1f1d1c")
window.resizable(width=False, height=False)
window.title('Youtube video Downloader')

def Download():
    
    url = YouTube(str(link.get()))
    mp4=url.streams.filter(file_extension='mp4')
    mp4.order_by('resolution').last().download()

    tk.Label(window, text = 'Video donwloaded', font= 'arial 15', fg='white', bg='#1f1d1c').pack()
    

link=tk.StringVar()

tk.Label(bg="#1f1d1c").pack()
tk.Label(window,text='           Youtube Video Downloader           ', font='arial 20 bold',fg='White',bg='#1f1d1c').pack()

tk.Label(window, text = 'Paste link: ',font='arial 10 bold',fg='Blue',bg='#1f1d1c').pack()

link_enter = tk.Entry(window, width = 53, textvariable=link, font = 'arial 12 ',bg="grey").pack()

tk.Button(window, text = "DOWNLOAD", font = 'arial 15 bold',fg='white',bg='Black', padx = 2, command=Download).pack()

window.mainloop()

