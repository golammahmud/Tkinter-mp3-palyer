from tkinter import *
import pygame
from tkinter import filedialog
import tkinter.messagebox as Messagebox
from tkinter.ttk import Scale,Label
import time
from mutagen.mp3 import MP3
from PIL import Image,ImageTk
root=Tk()

height=700
width=1200
root.title('tkinter mp3 player')
root.geometry(f"{width}x{height}")
# root.config(bg="gray")
#----------background image--------------
if height<=650 and width<=800:
    image=Image.open('images/music_player.jpg')
    image = image.resize((800, 680), Image.ANTIALIAS)
    background_image=ImageTk.PhotoImage(image=image)
else:
    image = Image.open('images/music_player.jpg')
    image = image.resize((1200, 700), Image.ANTIALIAS)
    background_image = ImageTk.PhotoImage(image=image)
    root.configure(width=1200,height=980)

background_label =Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1,anchor= 'nw')

#----------background image--------------
fm1=Frame(root,bg='#000000',padx=12)
fm1.pack(side='left')
fm2 = Frame(root,width=90)
fm2.pack(side='bottom',ipadx=20,pady=20)

image = Image.open('images.jpg')
# image = image.resize((200, 150), Image.ANTIALIAS)
b_image = ImageTk.PhotoImage(image=image)

b_label =Label(fm2, image=b_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

pygame.mixer.init()

#song duration
def song_duration():
    current_time=pygame.mixer.music.get_pos()/1000
    #now convert current_time to time formate
    global formated_time
    formated_time=time.strftime('%M:%S',time.gmtime(current_time))
    initial_song_time.config(text=formated_time)
    #get song from song box
    song=songbox.get(ACTIVE)
    song_muta=MP3(song)
    total_song_length=song_muta.info.length
    formated_song_length_time = time.strftime('%M:%S', time.gmtime(total_song_length))
    song_time.config(text=formated_song_length_time)

    #get slider position value

    slider_position = int(total_song_length)
    slider_value=int(song_length_slider.get())
    # current_time+=1
    slider_value=slider_value+1

    # print(f'this is current time {int(current_time)} and SLIDER VALUE {slider_value}')
    song_length_slider.config(to=slider_position, value=int(slider_value))
    # if slider_value == int(current_time):
    #     song_length_slider.config(to=slider_position, value=int(current_time))
    #     # fake_label = Label(fm2, text=f'slider value: {slider_value} and current song time: {int(current_time)}')
    #     # fake_label.grid(row=7, column=10)
    #     print('if work')
    #
    # else:
    #     song_length_slider.config(to=slider_position, value=slider_value)
    #     # song_length_slider.config(to=slider_position, value=slider_value)
    #     current_time = time.strftime('%M:%S', time.gmtime(slider_value))
    #     fake_label = Label(fm2, text=f'slider value: {slider_value} and current song time: {current_time}')
    #     fake_label.grid(row=7, column=10)
    #     # increase_slider_value=slider_value+1
    #     # song_length_slider.config(value=increase_slider_value)
    #     print('else work')


    #
    # if int(song_length_slider.get())==int(current_time):
    #     song_length_slider.config(to=slider_position,value=int(current_time))
    #     print('if works')
    #     # fake_label = Label(fm2, text=f'slider value: {int(slider_value)} and current song time: {int(current_time)}')
    #     # fake_label.grid(row=7, column=10)
    # else:
    #     song_length_slider.config(to=slider_position, value=int(song_length_slider.get()))
    #     current_time = time.strftime('%M:%S', time.gmtime(int(song_length_slider.get())))
    #     fake_label = Label(fm2, text=f'slider value: {int(song_length_slider.get())} and current song time: {current_time}')
    #     fake_label.grid(row=7, column=10)
    #     increase_time=int(song_length_slider.get())+1
    #     song_length_slider.config(value=increase_time)
    #     print('else works')

    # song_length_slider.config(to=slider_position, value=int(song_length_slider.get()))
    # current_time = time.strftime('%M:%S', time.gmtime(int(song_length_slider.get())))
    # fake_label = Label(fm2, text=f'slider value: {int(song_length_slider.get())} and current song time: {current_time}')
    # fake_label.grid(row=7, column=10)
    # increase_time = int(song_length_slider.get()) + 1
    # song_length_slider.config(value=increase_time)


    #update every second 1000=1sec
    initial_song_time.after(1000,song_duration)



global song
def add_songs():
    global song
    song=filedialog.askopenfilename(initialdir='audio/',title='choose a song',filetypes=(('mp3 Files','*.mp3'),))
    # song=song.replace('C:/Users/Md Parvez Meherab/Downloads/','')
    # song=song.replace('.mp3','').replace('*/','').replace('/','')
    # print(song)
    songbox.insert(END,song)

global song
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='audio/', title='choose a song', filetypes=(('mp3 Files', '*.mp3'),))
    for song in songs:
        # print(song)
        songbox.insert(END, song)


def play():
    try:
        song=songbox.get(ACTIVE)
        pygame.mixer.music.load(song)
        play=pygame.mixer.music.play(loops=0,start=0)
        play_btn.configure(bg='green',fg='red')
        song_label = Label(root, text=song, width=70, font='lucida 15 italic', foreground='gray', background='#003870')
        song_label.pack(side='bottom')
        if play:
            stop_btn.configure(bg='green', fg='red')
        stop_btn.configure(bg='green', fg='red')
        song_duration()
    except:
        Messagebox.showinfo('Mp3 Player','please select a song')






# def play():

#     # orginal
#     for i in len(songbox):
#         song=songbox.get(i)
#         print(song)
#     # pygame.mixer.music.load(song)
#     # play=pygame.mixer.music.play(loops=0,start=0)
#     # play_btn.configure(bg='green',fg='red')
#     # if play:
#     #     stop_btn.configure(bg='green', fg='red')
#     # stop_btn.configure(bg='green', fg='red')



def next_song():
    try:
        next_one=songbox.curselection()
        next=next_one[0]+1
        song = songbox.get(next)
        try:
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops=0, start=0)
        except EXCEPTION as e:
            print(e)
            forward_btn.configure(bg='red', fg='black')
        songbox.select_clear(0, END)
        songbox.activate(next)
        songbox.selection_set(next,last=None)
        print(next)
        forward_btn.configure(bg='green',fg='red')
    except:
        Messagebox.showinfo('Mp3 Player', 'please select a song')

def back_song():
    try:

        next_one = songbox.curselection()
        next = next_one[0] - 1
        song = songbox.get(next)
        try:
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops=0, start=0)
        except EXCEPTION as e:
            print(e)
            back_btn.configure(bg='red', fg='black')

        songbox.select_clear(0, END)
        songbox.activate(next)
        songbox.selection_set(next, last=None)

        back_btn.configure(bg='green', fg='red')
    except:
        Messagebox.showinfo('Mp3 Player', 'please select a song')

global formated_time
def stop_playing():
    try:
        pygame.mixer.music.stop()
        songbox.select_clear(ACTIVE)
        stop_btn.configure(bg='red', fg='green')
        initial_song_time.config(text='00:00')
    except:
        Messagebox.showinfo('Mp3 Player', 'please select a song')


global paused
paused=False
def pause(is_paused):
    try:
        global paused
        paused=is_paused
        if paused:
            pygame.mixer.music.unpause()
            paused=False
            pause_btn.configure(bg='green', fg='red')
        else:
            pygame.mixer.music.pause()
            paused=True
            pause_btn.configure(bg='red',fg='green')
    except:
        Messagebox.showinfo('Mp3 Player', 'please select a song')

def delete_songs():
    songbox.delete(ANCHOR)
    pygame.mixer.music.stop()
def delete_all_songs():
    songbox.delete(ANCHOR,END)
    pygame.mixer.music.stop()

#hobar effect function
def back_hobar(event):
    back_btn['bg']='white'
    back_label.config(text='previous')

def back_leave(event):
    back_btn['bg'] = 'SystemButtonFace'
    back_label.config(text='')
def play_hobar(event):
    play_btn['bg']='white'
    play_label.config(text='play')

def play_leave(event):
    play_btn['bg'] = 'SystemButtonFace'
    play_label.config(text='')

def pause_hobar(event):
    pause_btn['bg'] = 'white'
    pause_label.config(text='pause')

def pause_leave(event):
    pause_btn['bg'] = 'SystemButtonFace'
    pause_label.config(text='')

def stop_hobar(event):
    stop_btn['bg']='white'
    stop_label.config(text='stop')

def stop_leave(event):
    stop_btn['bg'] = 'SystemButtonFace'
    stop_label.config(text='')


def forward_hobar(event):
    forward_btn['bg']='white'
    forward_label.config(text='next')

def forward_leave(event):
    forward_btn['bg'] = 'SystemButtonFace'
    forward_label.config(text='')


def volume(x):
   volume=vol.get()
   pygame.mixer.music.set_volume(volume)
   current_volume=pygame.mixer.music.get_volume()
   current_volume=int(current_volume*100)
   if current_volume>0 and current_volume<=33:
       volume_frame.config(image=vol2)
   elif current_volume>33 and current_volume<=67:
       volume_frame.config(image=vol3, )
   elif current_volume>67 and current_volume<=100:
       volume_frame.config(image=vol4, )

def mute():
    global volume
    volume=0
    if volume==0:
        pygame.mixer.music.set_volume(volume)
        volume_frame.config(image=vol1)

def s_length(s):
    pass

#---------------listbox ------------------
scroll = Scrollbar(fm1,activebackground='red')
scroll.pack( side = RIGHT, fill = Y)
songbox=Listbox(fm1,bg='#000000',highlightcolor='blue',yscrollcommand= scroll.set,fg='white',width=30,height=25,font='lucida 12 italic',borderwidth=5,relief=RAISED,highlightbackground='#6394C8')#selectbackground='blue',
songbox.pack(fill=Y,ipady=40)
scroll.config( command = songbox.yview )
#---------------listbox ------------------

#button container
back_label=Label(fm2,text='',font='lucida 10 italic')
back_label.grid(row=0,column=4,ipady=8)
back_btn=Button(fm2,text='<<',font='lucida 10 bold',bd=5,relief=RAISED,command=back_song)
back_btn.grid(row=1,column=4,padx=10)


play_label=Label(fm2,text='',font='lucida 10 italic')
play_label.grid(row=0,column=5,ipady=8)
play_btn=Button(fm2,text='play',font='lucida 10 bold',bd=5,relief=RAISED,command=play)
play_btn.grid(row=1,column=5,padx=10)


pause_label=Label(fm2,text='',font='lucida 10 italic')
pause_label.grid(row=0,column=6,ipady=8)
pause_btn=Button(fm2,text='||',font='lucida 10 bold',bd=5,relief=RAISED,command=lambda:pause(paused))
pause_btn.grid(row=1,column=6,padx=10)


stop_label=Label(fm2,text='',font='lucida 10 italic')
stop_label.grid(row=0,column=7,ipady=8)
stop_btn=Button(fm2,text='stop',font='lucida 10 bold',bd=5,relief=RAISED,command=stop_playing)
stop_btn.grid(row=1,column=7,padx=10)


forward_label=Label(fm2,text='',font='lucida 10 italic')
forward_label.grid(row=0,column=8,ipady=8)
forward_btn=Button(fm2,text='>>',font='lucida 10 bold',bd=5,relief=RAISED,command=next_song)
forward_btn.grid(row=1,column=8,padx=10)

# button hobar effect with binding
back_btn.bind('<Enter>',back_hobar)
back_btn.bind('<Leave>',back_leave)

play_btn.bind('<Enter>',play_hobar)
play_btn.bind('<Leave>',play_leave)

pause_btn.bind('<Enter>',pause_hobar)
pause_btn.bind('<Leave>',pause_leave)

stop_btn.bind('<Enter>',stop_hobar)
stop_btn.bind('<Leave>',stop_leave)

forward_btn.bind('<Enter>',forward_hobar)
forward_btn.bind('<Leave>',forward_leave)

#menu
songmenu=Menu(root)
root.config(menu=songmenu)
#add song menu
addmenu=Menu(songmenu, tearoff=0)
addmenu.add_command(label="add one song to play list",command=add_songs)
addmenu.add_command(label="add many song to play list",command=add_many_songs)
songmenu.add_cascade(label='Add songs',menu=addmenu)
#delete song menu
deletemenu=Menu(songmenu, tearoff=0)
deletemenu.add_command(label="Delete one song from play list",command=delete_songs)
deletemenu.add_command(label="Delete all song from play list",command=delete_all_songs)
songmenu.add_cascade(label='Delete songs',menu=deletemenu)

#volum button icon
def volume_hobar(event):
    volume_frame['bg']='white'
    volume_label.config(text='mute')

def volume_leave(event):
    volume_frame['bg'] = 'SystemButtonFace'
    volume_label.config(text='')

global vol0
global vol1
global vol2
global vol3
global vol4
vol0=PhotoImage(file='images/v0.png')
vol1=PhotoImage(file='images/v1.png',height=28)
vol2=PhotoImage(file='images/v2.png',height=27,width=12)
vol3=PhotoImage(file='images/v3.png',height=29)
vol4=PhotoImage(file='images/v4.png',width=20,height=29)

fr4=Frame(fm2)
fr4.grid(row=1,column=10)

volume_label=Label(fm2,text='',font='lucida 10 italic')
volume_label.grid(row=0,column=10,)
volume_frame=Button(fr4,image=vol3,command=mute,)
volume_frame.grid(row=1,column=12,padx=10)

volume_frame.bind('<Enter>',volume_hobar)
volume_frame.bind('<Leave>',volume_leave)
#volum button

vol=Scale(fm2,from_=0,to=1,orient=HORIZONTAL,value=.33,length=160,command=volume)
vol.grid(row=1,column=12)
vol_label_plus=Label(fm2,text='v+',font='lucida 10 bold')
vol_label_plus.grid(row=1,column=14,padx=10)

#song length
song_time_frame=Frame(fm2)
song_time_frame.grid(rowspan=30,columnspan=60,ipady=20)
song_length_slider=Scale(song_time_frame,from_=0,to=100,orient=HORIZONTAL,value=0,length=360,command=s_length)
song_length_slider.grid(rowspan=30,columnspan=60,ipady=20)

initial_song_time=Label(song_time_frame,text='initial time')
initial_song_time.grid(row=26,columnspan=10,)

song_time=Label(song_time_frame,text='song time')
song_time.grid(row=26,column=60,)

root.mainloop()

