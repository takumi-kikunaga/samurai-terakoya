#音楽再生アプリ　tkinter

import tkinter
from tkinter import filedialog
from tkinter import END
from tkinter import ANCHOR
#音楽再生。必要pip install pygame
import pygame.mixer as pymix

root=tkinter.Tk()
root.title("音楽再生アプリ")
# root.iconbitmap()
root.geometry("500x600")
root.resizable(0,0)

#フォントの定義
basicFont=("Times New Roman",12)
listFont=("Times New Roman",15)

#関数定義
def addItem():
  #ダイヤログに表示したいファイルの種類を指定する。
  fileType=[("","*")]
  
  fileName=filedialog.askopenfilename(filetypes=fileType,initialdir="./")
  print(fileName)
  #リストボックスの末尾にファイルパスを追加する。
  myListBox.insert(END,fileName)
  
def removeItem():
  myListBox.delete(ANCHOR)

def clearList():
  myListBox.delete(0,END)

#音楽再生用の関数
def play():
  #現在再生中の音楽がある場合は、まず中断処理。入れないと重なって再生される。
  pymix.quit()
  #再生するファイルのパスを取得

  n=myListBox.curselection()
  soundFile=myListBox.get(n)
  list1=myListBox.get(1)
  print(n,soundFile)

  #音楽再生
  #pymixの初期化
  pymix.init()
  sounds=pymix.Sound(soundFile)
  global musicPlayer
  musicPlayer = sounds.play()
  musicPlayer.set_volume(0.1) #0.01刻みで0.00～1.00まで選択可能。


def stop():
  pymix.pause()

def restart():
  pymix.unpause()

def adjustvolume(volume):

  #音量調節
  musicPlayer.set_volume(float(volume)) #0.01刻みで0.00～1.00まで選択可能。



#ウインドウを４つのフレームに分割する。
inputFrame=tkinter.Frame(root)#ボタンの配置用
outputFrame=tkinter.Frame(root)#リストボックス用
buttonFrame=tkinter.Frame(root)
volFrame=tkinter.Frame(root)#スケールバー

inputFrame.pack()
outputFrame.pack()
buttonFrame.pack()
volFrame.pack()

#ファイルに関するボタンを作成
listAddButton=tkinter.Button(inputFrame,text="追加",borderwidth=2,font=basicFont,command=addItem)
listRemoveButton=tkinter.Button(inputFrame,text="選択削除",borderwidth=2,font=basicFont,command=removeItem)
listClearButton=tkinter.Button(inputFrame,text="一括削除",borderwidth=2,font=basicFont,command=clearList)

listAddButton.grid(row=0,column=0,padx=2,pady=15,ipadx=5)
listRemoveButton.grid(row=0,column=1,padx=2,pady=15,ipadx=5)
listClearButton.grid(row=0,column=2,padx=2,pady=15,ipadx=5)

#スクロールバーの追加
myScrollBar=tkinter.Scrollbar(outputFrame)

#音楽リストボックスの作成→outputFrameに配置,スクロールバーとの紐づけ
myListBox=tkinter.Listbox(outputFrame,width=45,height=15,yscrollcommand=myScrollBar.set)
myListBox.config(borderwidth=3,font=listFont)
myListBox.grid(row=0,column=0)
#スクロールバーとリストボックスも紐づけ
myScrollBar.config(command=myListBox.yview)
myScrollBar.grid(row=0,column=1,sticky="NS") #リストボックスの隣のcolumnにgridする

#音楽再生に関するボタン作成
playButton=tkinter.Button(buttonFrame,text="再生",borderwidth=3,font=basicFont,command=play)
stopButton=tkinter.Button(buttonFrame,text="一時停止",borderwidth=3,font=basicFont,command=stop)
restartButton=tkinter.Button(buttonFrame,text="再開",borderwidth=3,font=basicFont,command=restart)

playButton.grid(row=0,column=0,padx=5,pady=15,ipadx=5)
stopButton.grid(row=0,column=1,padx=5,pady=15,ipadx=5)
restartButton.grid(row=0,column=2,padx=5,pady=15,ipadx=5)

#音量調整（スケールバーの作成）横方向・・・
volLabel=tkinter.Label(volFrame,text="音量")
#Scaleオブジェクトに関数(command=)を設定する場合。関数に自動でカーソル値が引数として渡される。
volScale=tkinter.Scale(volFrame,orient="horizontal",length=300,from_=0.0,to=1.0,resolution=0.01,showvalue=0,command=adjustvolume)
volScale.set(0.4)
volLabel.grid(row=0,column=0,padx=10)
volScale.grid(row=0,column=1,padx=10)



#ループ処理の実行
root.mainloop()