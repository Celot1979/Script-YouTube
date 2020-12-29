import builtins
from tkinter import * 
import pytube
#Nota: Imprescindible descargar la librería pytube

"""Primero creamos la función. Lo más importante es saber la ruta donde queremos
descargar el video"""
def Descarga():
    video_url= Url.get()
    try:
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.first()
        video.download("C:\Users\zata_\Downloads\Descargas You Tube")
        notif.config(fg="green", text="Descarga Completa")
    except Exception as e:
        print(e)
        notif.config(fg="red", text="No se pudo descargar el video")

""" A partir de aquí, es simplemente usar la librería Tkinter para darle una apariencia a nuestra app.
Se puede reconfigurar a nuestro gusto."""
master = Tk()
master.title("Script Descargas")
Label(master, text="Convertidor de video YouTube", fg= "red", font=("calibri", 15)).grid( sticky=N, padx=100, row=0)
Label(master, text="Por favor ingrese el enlace:  ", font=("calibri", 12)).grid( sticky=N,row=1, pady=15)
notif = Label(master, font = ("calibri", 12))
notif.grid(sticky=N, pady=1, row=4)

Url = StringVar()

Entry(master, width=50, textvariable=Url).grid(sticky=N, row=2)
Button(master, width=20, text="Descarga", font=("Calibri", 12),command=Descarga).grid(sticky=N, row=3,pady=15)


master.mainloop()