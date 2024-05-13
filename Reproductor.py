import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip
import pygame.mixer as mx
import os
from tkinter import ttk
class Reproductor():
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
       
    
   
    
   
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Reproductor de Música")
        self.ventana.config(width=500, height=500)
        self.ventana.resizable(0,0)
        mx.init()

        self.song_paths = [
            r"SONIDOS\sounds\Du-Hast-Rammstein.mp3",
            r"SONIDOS\sounds\Sharp-Dressed-Man-ZZ-top.mp3",
        ]

        self.song_names = [os.path.basename(song_path) for song_path in self.song_paths]

        self.selected_song = tk.IntVar(self.ventana)
        self.selected_song.set(0)

        self.bandera = False
        iconPlay = tk.PhotoImage(file=r"SONIDOS\icons\control_play.png")
        iconPause = tk.PhotoImage(file=r"SONIDOS\icons\control_play_blue.png")
        iconStop = tk.PhotoImage(file=r"SONIDOS\icons\control_stop_blue.png")

        self.btnPlay = tk.Button(self.ventana, image=iconPlay, command=self.play)
        self.btnPlay.place(relx=0.5, rely=1, y=-50, width=25, height=25)
        Tooltip(self.btnPlay, "Presione para iniciar la reproducción")

        self.btnPause = tk.Button(self.ventana, image=iconPause, state="disabled", command=self.pause)
        self.btnPause.place(relx=0.5, rely=1, y=-50, x=50, width=25, height=25)
        Tooltip(self.btnPause, "Presione para pausar la reproducción")

        self.btnStop = tk.Button(self.ventana, image=iconStop, state="disabled", command=self.stop)
        self.btnStop.place(relx=0.5, rely=1, y=-50, x=-50, width=25, height=25)
        Tooltip(self.btnStop, "Presione para detener la reproducción")

        self.lblEstado = tk.Label(self.ventana, text="Cargando...")
        self.lblEstado.place(relx=0.5, rely=0.5, anchor="center")


        song_menu = tk.OptionMenu(self.ventana, self.selected_song, *range(len(self.song_paths)), command=self.update_label)
        song_menu.place(relx=0.5, rely=0.1, anchor="center")

        self.paused = False

        self.ventana.mainloop()

    def update_label(self, value):
        index = int(value)
        song_path = self.song_paths[index]
        self.lblEstado.config(text="Seleccionado: " + os.path.basename(song_path))

