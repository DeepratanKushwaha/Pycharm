from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3

root = Tk()
root.geometry("1100x500+130+100")
root.title("Music Player")
root.iconbitmap('music.ico')
root.resizable(0, 0)
root.configure(bg="lightskyblue")

audioTrack = StringVar()
currentVol = 0
browse = 0
play = 0
stop = 0
pause = 0
volumeUp = 0
volumeDown = 0
resume = 0
mute = 0
unMute = 0
audioStatusLabel = ''
progressBarVolumeLabel = 0
progressBarVolume = ''
progressBarLabel = ''
progressBarMusicLabel = ''
totalSongLength = 0
progressBarMusic = ''
progressBarMusicEndTimeLabel = ''
progressBarMusicStartTimeLabel = ''


def playMusic():
    global audioStatusLabel, totalSongLength, progressBarMusic
    adt = audioTrack.get()
    mixer.music.load(adt)
    progressBarLabel.grid()
    root.muteButton.grid()
    progressBarMusicLabel.grid()
    mixer.music.set_volume(0.4)
    progressBarVolume['value'] = 40
    progressBarVolumeLabel['text'] = '40%'
    mixer.music.play()
    audioStatusLabel.configure(text='Playing...')

    Song = MP3(adt)
    totalSongLength = int(Song.info.length)
    progressBarMusic['maximum'] = totalSongLength
    progressBarMusicEndTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=totalSongLength))))

    def progressBarMusicTick():
        currentSongLength = mixer.music.get_pos()/1000
        progressBarMusic['value'] = currentSongLength
        progressBarMusicStartTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=currentSongLength))))
        progressBarMusic.after(2, progressBarMusicTick)

    progressBarMusicTick()


def pauseMusic():
    mixer.music.pause()
    root.pauseButton.grid_remove()
    root.resumeButton.grid()
    audioStatusLabel.configure(text='Paused...')


def resumeMusic():
    root.resumeButton.grid_remove()
    root.pauseButton.grid()
    mixer.music.unpause()
    audioStatusLabel.configure(text='Playing...')


def stopMusic():
    global progressBarMusicStartTimeLabel
    mixer.music.stop()
    audioStatusLabel.configure(text='Stopped...')
    progressBarMusicStartTimeLabel.configure(text='0:00:0')


def volumeInc():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol + 0.05)

    progressBarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    progressBarVolume['value'] = mixer.music.get_volume()*100


def volumeDec():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol - 0.05)

    progressBarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume() * 100)))
    progressBarVolume['value'] = mixer.music.get_volume() * 100


def muteMusic():
    global currentVol
    currentVol = mixer.music.get_volume()
    mixer.music.set_volume(0)
    root.muteButton.grid_remove()
    root.unMuteButton.grid()


def unMuteMusic():
    global currentVol
    mixer.music.set_volume(currentVol)
    root.unMuteButton.grid_remove()
    root.muteButton.grid()


def musicUrl():
    try:
        dd = filedialog.askopenfilename(initialdir='C:/Users/deepr_000/Downloads/meme/audio', title='Select Audio File',
                                        filetype=(('MP3', '*.mp3'), ('WAV', '*.wav')))
    except:
        dd = filedialog.askopenfilename(title='Select Audio File', filetype=(('MP3', '*.mp3'), ('WAV', '*.wav')))

    audioTrack.set(dd)


def createWidget():
    global browse, play, stop, pause, volumeUp, volumeDown, resume, mute, unMute
    global audioStatusLabel, progressBarVolumeLabel, progressBarLabel, progressBarVolume, progressBarMusicLabel, \
        progressBarMusic, progressBarMusicEndTimeLabel, progressBarMusicStartTimeLabel

    # add images
    browse = PhotoImage(file='browsing.png')
    play = PhotoImage(file='play.png')
    stop = PhotoImage(file='stop.png')
    pause = PhotoImage(file='pause.png')
    volumeUp = PhotoImage(file='volume-up.png')
    volumeDown = PhotoImage(file='volume-down.png')
    resume = PhotoImage(file='resume.png')
    mute = PhotoImage(file='mute.png')
    unMute = PhotoImage(file='no-sound.png')

    # change size of image
    browse = browse.subsample(18, 18)
    play = play.subsample(18, 18)
    stop = stop.subsample(18, 18)
    pause = pause.subsample(18, 18)
    volumeUp = volumeUp.subsample(18, 18)
    volumeDown = volumeDown.subsample(18, 18)
    resume = resume.subsample(18, 18)
    mute = mute.subsample(18, 18)
    unMute = unMute.subsample(18, 18)

    trackLabel = Label(root, text="Select Audio Track :", bg='lightskyblue', font="arial 15 italic bold")
    trackLabel.grid(row=0, column=0, padx=20, pady=20)

    audioStatusLabel = Label(root, text='', bg='lightskyblue', font='arial 15 italic bold')
    audioStatusLabel.grid(row=2, column=1)

    trackLabelEntry = Entry(root, font="arial 16 italic bold", width=35, textvariable=audioTrack)
    trackLabelEntry.grid(row=0, column=1, padx=20)

    browseButton = Button(root, text="Search", bg="deep pink", font="arial 10 italic bold", width=200, bd=5,
                          activebackground="purple4", image=browse, compound=RIGHT, command=musicUrl)
    browseButton.grid(row=0, column=2, padx=20)

    playButton = Button(root, text="Play", bg="green2", font="arial 10 italic bold", width=200, bd=5,
                        activebackground="purple4", image=play, compound=RIGHT, command=playMusic)
    playButton.grid(row=1, column=0, padx=20, pady=20)

    root.pauseButton = Button(root, text="Pause", bg="yellow", font="arial 10 italic bold", width=200, bd=5,
                              activebackground="purple4", image=pause, compound=RIGHT, command=pauseMusic)
    root.pauseButton.grid(row=1, column=1, padx=20, pady=20)

    root.resumeButton = Button(root, text="Resume", bg="yellow", font="arial 10 italic bold", width=200, bd=5,
                               activebackground="purple4", image=resume, compound=RIGHT, command=resumeMusic)
    root.resumeButton.grid(row=1, column=1, padx=20, pady=20)
    root.resumeButton.grid_remove()

    root.muteButton = Button(root, text="Mute", width=100, bg='yellow', font="arial 10 italic bold", bd=5,
                             activebackground='purple4', image=mute, compound=RIGHT, command=muteMusic)
    root.muteButton.grid(row=3, column=3)
    root.muteButton.grid_remove()

    root.unMuteButton = Button(root, text="UnMute", width=100, bg='yellow', font="arial 10 italic bold", bd=5,
                               activebackground='purple4', image=unMute, compound=RIGHT, command=unMuteMusic)
    root.unMuteButton.grid(row=3, column=3)
    root.unMuteButton.grid_remove()

    volumeUpButton = Button(root, text="VolumeUp", bg="blue", font="arial 10 italic bold", width=200, bd=5,
                            activebackground="purple4", image=volumeUp, compound=RIGHT, command=volumeInc)
    volumeUpButton.grid(row=1, column=2, padx=20, pady=20)

    stopButton = Button(root, text="Stop", bg="red", font="arial 10 italic bold", width=200, bd=5,
                        activebackground="purple4", image=stop, compound=RIGHT, command=stopMusic)
    stopButton.grid(row=2, column=0, padx=20, pady=20)

    volumeDownButton = Button(root, text="VolumeDown", bg="blue", font="arial 10 italic bold", width=200, bd=5,
                              activebackground="purple4", image=volumeDown, compound=RIGHT, command=volumeDec)
    volumeDownButton.grid(row=2, column=2, padx=20, pady=20)

    progressBarLabel = Label(root, text='', bg='red')
    progressBarLabel.grid(row=0, column=3, rowspan=3, padx=20, pady=20)
    progressBarLabel.grid_remove()

    progressBarVolume = Progressbar(progressBarLabel, orient=VERTICAL, mode='determinate', value=0, length=190)
    progressBarVolume.grid(row=0, column=0, ipadx=5)

    progressBarVolumeLabel = Label(progressBarLabel, text='0%', bg='light grey', width=3)
    progressBarVolumeLabel.grid(row=0, column=0)

# ==============================================================================================

    progressBarMusicLabel = Label(root, text='', bg='red')
    progressBarMusicLabel.grid(row=3, column=0, columnspan=3, padx=20, pady=20)
    progressBarMusicLabel.grid_remove()

    progressBarMusicStartTimeLabel = Label(progressBarMusicLabel, text='0:00:0', bg='red', width=10)
    progressBarMusicStartTimeLabel.grid(row=0, column=0)

    progressBarMusic = Progressbar(progressBarMusicLabel, orient=HORIZONTAL, mode='determinate', value=0)
    progressBarMusic.grid(row=0, column=1, ipadx=370, ipady=3)

    progressBarMusicEndTimeLabel = Label(progressBarMusicLabel, text='0:00:0', bg='red')
    progressBarMusicEndTimeLabel.grid(row=0, column=2)


string = "Developed by Deep"
count = 0
text = ''
sliderLabel = Label(root, text=string, bg="lightskyblue", font="arial 40 italic bold")
sliderLabel.grid(row=5, column=0, padx=20, pady=20, columnspan=3)


def introLabel():
    global count, text
    if count >= len(string):
        count = -1
        text = ''
        sliderLabel.configure(text=text)
    else:
        text = text + string[count]
        sliderLabel.configure(text=text)
    count += 1
    sliderLabel.after(200, introLabel)


if __name__ == '__main__':
    introLabel()
    mixer.init()
    createWidget()

    root.mainloop()
