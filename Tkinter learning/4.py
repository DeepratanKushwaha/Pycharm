from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("GUI")

# important Label option
# text = adds the text
# bd = background
# fg = foreground
# font = sets the font
# 1 font=("ariel", 15, "underline")
# 2 font="ariel 10 bold"
# padx = x padding
# pady = y padding
# relief = border styling- SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text='''Kohli captained India Under-19s to victory at the 2008 Under-19 World Cup in Malaysia. 
\nAfter a few months later, he made his ODI debut for India against Sri Lanka at the age of 19. Initially having played 
\nas a reserve batsman in the Indian team, he soon established himself as a regular in the ODI middle-order and was 
\npart of the squad that won the 2011 World Cup. He made his Test debut in 2011 and shrugged off the tag of "ODI 
\nspecialist" by 2013 with Test hundreds in Australia and South Africa.[4] Having reached the number one spot in the 
\nICC rankings for ODI batsmen for the first time in 2013,[5] Kohli also found success in the Twenty20 format, 
\nwinning the Man of the Tournament twice at the ICC World Twenty20 (in 2014 and 2016).''', bg="red", foreground="white"
                    , padx=100, pady=80, font=("ariel", 15, "underline"), borderwidth=15, relief=RIDGE)

# important pack option
# anchor= nw
# side = top, bottom, left, right |by default= top
# fill
# padx
# pady

title_label.pack(anchor="nw", side=LEFT, fill=Y, padx=50, pady=50)

root.mainloop()
