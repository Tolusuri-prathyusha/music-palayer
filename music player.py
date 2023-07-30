from tkinter import *
from tkinter import filedialog
from pygame import mixer

def add_songs():
    temp_songs = filedialog.askopenfilenames(initialdir="Music/", title="Choose songs", filetypes=(("MP3 Files", "*.mp3"),))
    songs_list.insert(END, *temp_songs)

def delete_song():
    selected_song = songs_list.curselection()
    songs_list.delete(selected_song)

def play():
    song = songs_list.get(ACTIVE)
    mixer.music.load(song)
    mixer.music.play()

def pause():
    mixer.music.pause()

def stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

def resume():
    mixer.music.unpause()

def previous():
    prev_song = songs_list.curselection()[0] - 1
    songs_list.select_clear(0, END)
    songs_list.activate(prev_song)
    songs_list.select_set(prev_song)
    play()

def next_song():
    next_song = songs_list.curselection()[0] + 1
    songs_list.select_clear(0, END)
    songs_list.activate(next_song)
    songs_list.select_set(next_song)
    play()

root = Tk()
root.title('Simple Music Player')
root.geometry("500x400")

# Background color for the main music player window
root.config(bg="blue")

mixer.init()
songs_list = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=('Arial', 15), height=12, width=47, selectbackground="blue", selectforeground="black")
songs_list.grid(columnspan=9)

play_button = Button(root, text="Play", width=7, command=play, bg="green", fg="white")
play_button.grid(row=1, column=0)

pause_button = Button(root, text="Pause", width=7, command=pause, bg="orange", fg="white")
pause_button.grid(row=1, column=1)

stop_button = Button(root, text="Stop", width=7, command=stop, bg="red", fg="white")
stop_button.grid(row=1, column=2)

resume_button = Button(root, text="Resume", width=7, command=resume, bg="blue", fg="white")
resume_button.grid(row=1, column=3)

previous_button = Button(root, text="Previous", width=7, command=previous, bg="purple", fg="white")
previous_button.grid(row=1, column=4)

next_button = Button(root, text="Next", width=7, command=next_song, bg="purple", fg="white")
next_button.grid(row=1, column=5)

my_menu = Menu(root)
root.config(menu=my_menu)
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=add_song_menu)
add_song_menu.add_command(label="Add songs", command=add_songs)
add_song_menu.add_command(label="Delete song", command=delete_song)

root.mainloop()
