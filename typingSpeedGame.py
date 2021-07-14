
from tkinter import*
import  random
from tkinter import messagebox


screen=Tk()

screen.maxsize(width=800,height=600)
screen.minsize(width=500,height=400)
screen.configure(bg='powder blue')
screen.title('typing speed increase game')
words=['mango','orange','tv','laptop','Patato','Milk','silk','table'',''blockbuster','After','front','applE','oranGe'
                                                                     ]

def labelslider():
    global count,sliderwords
    text ='welcome to typing speed increse game'
    if (count>=len(text)):
        count=0
        sliderwords=''
    sliderwords+=text[count]
    count+=1
    fontLabel.configure(text=sliderwords)
    fontLabel.after(150,labelslider)
def time():
   global timeleft,score,miss
   if timeleft>=11:
       pass
   else:
       timeLabelcount.configure(fg='red')
   if timeleft>0:
       timeleft-=1
       timeLabelcount.configure(text=timeleft)
       timeLabelcount.after(1000,time)
   else:
      gameplaydetail.configure(text='hit={},miss={},total score={},'.format(score,miss,score-miss))
      n=messagebox.askretrycancel('notification','For Play again press retry button')
      if n==True:
           score=0
           timeleft=60
           miss=0
           timeLabelcount.configure(text=timeleft)
           wordLable.configure(text=words[0])
           scoreLabelcount.configure(text=score)





def StartGame(e):
    global score,miss
    if timeleft==60:
     time()
    gameplaydetail.configure(text='')
    if wordentry.get()==wordLable['text']:
        score+=1
        scoreLabelcount.configure(text=score)
    else:
       miss+=1
       print('miss',miss)
    random.shuffle(words)
    wordLable.configure(text=words[0])
    wordentry.delete(0,END)
###########################3
score=0
timeleft=60
count=0
sliderwords=''
miss=0

########################
fontLabel=Label(screen,text='',font=('arial',15,'italic bold'),bg='powder blue',width=30)
fontLabel.place(x=90,y=20)
labelslider()
random.shuffle(words)
wordLable=Label(screen,text=words[0],font=('arial',20,'italic bold'),bg='powder blue',bd=10,)
wordLable.place(x=210,y=200)
scoreLabel=Label(screen,text='your score:',font=('arial',15,'italic bold'),bg='powder blue',fg='blue')
scoreLabel.place(x=20,y=60)

timeLabel=Label(screen,text='Time Left:',font=('arial',15,'italic bold'),bg='powder blue',fg='blue')
timeLabel.place(x=380,y=60)

scoreLabelcount=Label(screen,text=score,font=('arial',15,'italic bold'),bg='powder blue',fg='blue')
scoreLabelcount.place(x=40,y=90)

timeLabelcount=Label(screen,text=timeleft,font=('arial',15,'italic bold'),bg='powder blue',fg='blue')
timeLabelcount.place(x=420,y=90)
gameplaydetail=Label(screen,text='Type word and Hit Enter Button',font=('arial',15,'italic bold'),bg='powder blue',fg='dark gray')
gameplaydetail.place(x=120,y=350)

screen.bind('<Return>',StartGame)


wordentry=Entry(screen,font=('arial',20,'italic bold'),bg='powder blue',bd=10,justify='center')
wordentry.place(x=110,y=250)
screen.mainloop()