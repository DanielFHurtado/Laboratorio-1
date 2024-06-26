import tkinter as tk
from tkinter import *
from tkinter import Scale
from Tooltip import Tooltip
import pygame.mixer as mx
import os
from tkinter import ttk

class Reproductor():
    
    def act_barra_repro(self):
        if mx.music.get_pos():
            pos_actual = mx.music.get_pos() // 1000
            porcentaje = (pos_actual / self.duracion) * 100
            self.barra_repro['value'] = porcentaje
            self.ventana.after(1000, self.act_barra_repro)

    def play(self):
        index = self.selected_song.get()
        song_path = self.song_paths[index]
        self.current_song = song_path
        mx.music.load(song_path)
        mx.music.play()
        self.lblEstado.config(text="Reproduciendo: " + os.path.basename(song_path))
        self.btnPause.config(state="normal")
        self.btnStop.config(state="normal")
        self.btnPlay.config(state="disabled")
        self.duracion = mx.Sound(self.current_song).get_length()
        self.act_barra_repro()
    
    def pause(self):
        if self.paused:
            mx.music.unpause()
            index = self.selected_song.get()
            song_path = self.song_paths[index]
            self.lblEstado.config(text="Reproduciendo: " + os.path.basename(song_path))
            self.btnPause.config(state="normal")
            self.btnStop.config(state="normal")
            self.btnPlay.config(state="disabled")
            self.paused = False
        else:
            mx.music.pause()
            self.lblEstado.config(text="Reproducción Pausada")
            self.btnPause.config(state="normal")
            self.btnStop.config(state="normal")
            self.btnPlay.config(state="disabled")
            self.paused = True

    def stop(self):
        mx.music.stop()
        self.lblEstado.config(text="Reproducción Detenida")
        self.btnPause.config(state="disabled")
        self.btnStop.config(state="disabled")
        self.btnPlay.config(state="normal")
        self.barra_repro['value'] = 0
       
    def saltarCancion(self):
        self.numeroC += 1
        if self.numeroC < len(self.song_paths):
            song_path = self.song_paths[self.numeroC]
            mx.music.load(song_path)
            mx.music.play()
            titulo = os.path.basename(song_path)
            duracion_cancion = mx.Sound(song_path).get_length()
            self.lblEstado.config(text=f"Reproduciendo: {titulo} ({duracion_cancion:.2f} segundos)")
            self.btnPause.config(state="normal")
            self.btnStop.config(state="normal")
            self.btnPlay.config(state="disabled")
        else:
            self.numeroC = 0
            song_path = self.song_paths[self.numeroC]
            mx.music.load(song_path)
            mx.music.play()
            titulo = os.path.basename(song_path)
            duracion_cancion = mx.Sound(song_path).get_length()
            self.lblEstado.config(text=f"Reproduciendo: {titulo} ({duracion_cancion:.2f} segundos)")
            self.btnPause.config(state="normal")
            self.btnStop.config(state="normal")
            self.btnPlay.config(state="disabled")
    def retrocederCancion(self):
        self.numeroC -= 1
        if self.numeroC >= 0:
            song_path = self.song_paths[self.numeroC]
            mx.music.load(song_path)
            mx.music.play()
            titulo = os.path.basename(song_path)
            duracion_cancion = mx.Sound(song_path).get_length()
            self.lblEstado.config(text=f"Reproduciendo: {titulo} ({duracion_cancion:.2f} segundos)")
            self.btnPause.config(state="normal")
            self.btnStop.config(state="normal")
            self.btnPlay.config(state="disabled")
        else:
            self.numeroC = len(self.song_paths) - 1
            song_path = self.song_paths[self.numeroC]
            mx.music.load(song_path)
            mx.music.play()
            titulo = os.path.basename(song_path)
            duracion_cancion = mx.Sound(song_path).get_length()
            self.lblEstado.config(text=f"Reproduciendo: {titulo} ({duracion_cancion:.2f} segundos)")
            self.btnPause.config(state="normal")
            self.btnStop.config(state="normal")
            self.btnPlay.config(state="disabled")   

    def salto10(self):
        posicion = mx.music.get_pos() / 1000
        nuevaP = posicion + 10  
        mx.music.set_pos(nuevaP)  

    def retroceso10(self):
        posicion = mx.music.get_pos() / 1000  
        nuevaP = max(0, posicion - 10) 
        song_path = self.song_paths[self.selected_song.get()]  
        mx.music.load(song_path)  
        mx.music.play(start=nuevaP)  

    def volumen(self, vol):
        volumen = int(vol) / 100
        mx.music.set_volume(volumen)
    
    def reproducir_cancion_selec(self, song_paths):
        
        mx.music.stop()
       
        mx.music.load(song_paths)
       
        mx.music.play()

    def actualizar_cancion(self, event):
        
        seleccion = self.listaCanciones.curselection()
        if seleccion:
           
            index = seleccion[0]
            
            cancion_seleccionada = self.song_paths[index]
           
            self.label.config(text=f"Seleccionaste: {os.path.basename(cancion_seleccionada)}")
            
            self.reproducir_cancion_selec(cancion_seleccionada)
                
   
        
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Reproductor de Música")
        self.ventana.config(width=650, height=450)
        self.ventana.resizable(0, 0)
        mx.init()

        self.fondo = tk.PhotoImage(file=r"Laboratorio-1\imagenes_repro\Imagen Audifonos.png")
        self.label_fondo = Label(self.ventana, image=self.fondo)
        self.label_fondo.place(x=0.5, y=0.5)

        self.song_paths = [
            r"C:\Users\juane\OneDrive\Escritorio\laboratorio_1\Laboratorio-1\sounds\Du-Hast-Rammstein.mp3",
            r"C:\Users\juane\OneDrive\Escritorio\laboratorio_1\Laboratorio-1\sounds\Sharp-Dressed-Man-ZZ-top.mp3",
            r"C:\Users\juane\OneDrive\Escritorio\laboratorio_1\Laboratorio-1\sounds\One-Metallica.mp3"
        ]

        self.song_names = [os.path.basename(song_path) for song_path in self.song_paths]

        self.selected_song = tk.IntVar(self.ventana)
        self.selected_song.set(0)

        self.numeroC = 0  
        self.paused = False

        iconPlay = tk.PhotoImage(file=r"Laboratorio-1\imagenes_repro\control_play.png")
        iconPause = tk.PhotoImage(file=r"Laboratorio-1\imagenes_repro\control_play_blue.png")
        iconStop = tk.PhotoImage(file=r"Laboratorio-1\imagenes_repro\control_stop_blue.png")
        iconPasar = tk.PhotoImage(file=r"Laboratorio-1\imagenes_repro\control_end_blue.png")
        iconRetroceder = tk.PhotoImage(file=r"Laboratorio-1\imagenes_repro\control_start_blue.png")
        iconFasterade10 = tk.PhotoImage(file=r"Laboratorio-1\imagenes_repro\control_fastforward_blue.png")
        iconFasteratr10 = tk.PhotoImage(file=r"Laboratorio-1\imagenes_repro\control_rewind_blue.png")

        self.btnPlay = tk.Button(self.ventana, image=iconPlay, command=self.play)
        self.btnPlay.place(relx=0.5, rely=1, y=-50, width=25, height=25)
        Tooltip(self.btnPlay, "Presione para iniciar la reproducción")

        self.btnPause = tk.Button(self.ventana, image=iconPause, state="disabled", command=self.pause)
        self.btnPause.place(relx=0.5, rely=1, y=-50, x=50, width=25, height=25)
        Tooltip(self.btnPause, "Presione para pausar la reproducción")

        self.btnStop = tk.Button(self.ventana, image=iconStop, state="disabled", command=self.stop)
        self.btnStop.place(relx=0.5, rely=1, y=-50, x=-50, width=25, height=25)
        Tooltip(self.btnStop, "Presione para detener la reproducción")
        
        self.btnPasar = tk.Button(self.ventana, image=iconPasar, command=self.saltarCancion)
        self.btnPasar.place(relx=0.5, rely=1, y=-50, x=80, width=25, height=25)
        Tooltip(self.btnPasar, "Siguiente Canción")
        
        self.btnRetroceder = tk.Button(self.ventana, image=iconRetroceder, command=self.retrocederCancion)
        self.btnRetroceder.place(relx=0.5, rely=1, y=-50, x=-80, width=25, height=25)
        Tooltip(self.btnRetroceder, "Canción Anterior")
        
        self.btnAvanzar =tk.Button(self.ventana, image=iconFasterade10, command=self.salto10)
        self.btnAvanzar.place(relx=0.5, rely=1, y=-50, x=110, width=25, height=25)
        Tooltip(self.btnAvanzar, "+10sg")
        
        self.btnRetroceso =tk.Button(self.ventana, image=iconFasteratr10, command=self.retroceso10)
        self.btnRetroceso.place(relx=0.5, rely=1, y=-50, x=-110, width=25, height=25)
        Tooltip(self.btnRetroceso, "-10sg")
        
        self.lblEstado = tk.Label(self.ventana, text="Cargando...")
        self.lblEstado.place(relx=0.52, y=325, anchor="center")

      

        self.listaCanciones = tk.Listbox(self.ventana)
        self.listaCanciones.place(relx=0.7, y=40, relwidth=0.25, relheight=0.4)

        for song in self.song_names:
            self.listaCanciones.insert(tk.END, os.path.basename(song))

        
        self.label = tk.Label(self.ventana, text="Seleccione una canción")
        self.label.place(relx=0.7, y=10)

      
        self.listaCanciones.bind("<<ListboxSelect>>", self.actualizar_cancion)
        
        self.barra_repro = ttk.Progressbar(self.ventana, orient='horizontal', length=300, mode='determinate')
        self.barra_repro.place(relx=0.28, y=350)

        self.btnVolumen = Scale(self.ventana, from_=100, to=0, orient=VERTICAL, command=self.volumen)
        self.btnVolumen.set(50)
        self.btnVolumen.place(relx=0.9, y=300, relwidth=0.4)
        Tooltip(self.btnVolumen, "Subir o Bajar el volumen")

        self.ventana.mainloop()
    
    
