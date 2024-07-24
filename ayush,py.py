from tkinter import *
import random
import threading
import time

win = Tk()
win.title("Simon Game")
win.geometry('232x410')
win.resizable(width=0, height=0)

global Green
global Red
global Yellow
global Blue
global watch
global count
global tmp
global gameover
global timer_count
global score
score = 0
timer_count = 0
watch = True
gameover = False
stt = []
tmp = len(stt)
tmp_stt = []


if gameover == False:

	def ChangeColor(i=1):
		global stt
		global watch
		global count
		global timer_count
		count = len(stt)
		
		for i in stt:
			time.sleep(0.2)

			if i == 1:
				win.after((timer_count+300), lambda: Green.config(bg='green'))
				win.after((timer_count+500), lambda: Green.config(bg = '#003300'))

			elif i == 2:
				win.after((timer_count+300), lambda: Red.config(bg='red'))
				win.after((timer_count+500), lambda: Red.config(bg = '#550000'))

			elif i == 3:
				win.after((timer_count+300), lambda: Yellow.config(bg='yellow'))
				win.after((timer_count+500), lambda: Yellow.config(bg = '#555500'))

			elif i == 4:
				win.after((timer_count+300), lambda: Blue.config(bg='blue'))
				win.after((timer_count+500), lambda: Blue.config(bg = '#000055'))


			timer_count += 220


	def press(num = 1):
		global watch
		global gameover
		global count
		global score
		if count > 0 and watch == False:
			if watch == False:
				if num == 1:
					tmp_stt.append(1)
					check(count, (len(tmp_stt)-1), num)
					count -= 1

				elif num == 2:
					tmp_stt.append(2)
					check(count, (len(tmp_stt)-1), num)
					count -= 1

				elif num == 3:
					tmp_stt.append(3)
					check(count, (len(tmp_stt)-1), num)
					count -= 1

				elif num == 4:
					tmp_stt.append(4)
					check(count, (len(tmp_stt)-1), num)
					count -= 1

		if count <= 0 and gameover == False:
			score += 1
			l0.config(text=score)
			watch = True
			tmp_stt.clear()
			start(watch, gameover)


	def check(count=100, x=0, num=1):
		global stt
		global gameover
		if stt[x] != num:
			gameover = True
			l1.configure(text="GAMEOVER")


l0 = Label(win, text="0", font=("Courier", 25))
l0.grid(padx=10, pady=2, row=0, columnspan=2)

l1 = Label(win, text="WATCH first, PLAY after")
l1.grid(padx=10, pady=2, row=1, columnspan=2)

Green = Button(win, text="", font=1, bg="#003300", activebackground='green', width=8, height=6, command=lambda: press(1))
Green.grid(padx=5, pady=10, row=2, column=0)

Red = Button(win, text="", font=1, bg="#550000", activebackground='red', width=8, height=6, command=lambda: press(2))
Red.grid(padx=5, pady=10, row=2, column=1)

Yellow = Button(win, text="", font=1, bg="#555500", activebackground='yellow', width=8, height=6, command=lambda: press(3))
Yellow.grid(padx=5, pady=10, row=3, column=0)

Blue = Button(win, text="", font=1, bg="#000055", activebackground='blue' ,width=8, height=6, command=lambda: press(4))
Blue.grid(padx=5, pady=10, row=3, column=1)


def first():
	global watch
	global gameover
	if watch == True and gameover == False:
		tmp = random.randint(1, 4)
		stt.append(tmp)
		#print("stt=", stt)
		win.after(1000, ChangeColor)
		watch = False
		

def start(a=True, b=False):
	global watch
	global stt
	if a == True and b == False:
		tmp = random.randint(1, 4)
		stt.append(tmp)
		#print("stt=", stt)
		ChangeColor()
		watch = False


if __name__ == "__main__":
	first()
	mainloop()
