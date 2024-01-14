import tkinter
import random

def click_btn():
    label["text"]=random.choice(["ごくらくマグロ","しんみりホタテ","ぶっとびチキン","えいゆうシャケ","ゆめみるシラス","たけだけビーフ","やせるターキー"])
    label.update()

root = tkinter.Tk()
root.title("幸運の猫缶")
root.resizable(False,False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()

gazou = tkinter.PhotoImage(file="omikuji_haikei02.png")
canvas.create_image(400,300,image=gazou)
label = tkinter.Label(root,text="ねこかんみくじ",font=("System",40),bg="white")
label.place(x=400,y=150)
button = tkinter.Button(root, text="猫缶を引く",
font=("System,24"),command=click_btn,bg="white")
button.place(x=550,y=450)
root.mainloop()

