from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class Developer:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPER", font=("rockwell extra bold",35,"underline"),bg="white",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\project1.jfif")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_dev=Image.open(r"C:\Users\HP\OneDrive\Pictures\riya.jpg")
        img_dev=img_dev.resize((200,200),Image.ANTIALIAS)
        self.photoimg_dev=ImageTk.PhotoImage(img_dev)

        f_lbl=Label(main_frame,image=self.photoimg_dev)
        f_lbl.place(x=300,y=0,width=200,height=200)

        dev_label=Label(main_frame,text="Hello,My name is Riya",font=("rockwell",12,"bold"), bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="Developer of this project",font=("rockwell",12,"bold"), bg="white")
        dev_label.place(x=0,y=35)

        img1=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\dev_1.jfif")
        img1=img1.resize((500,400),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(main_frame,image=self.photoimg1)
        f_lbl.place(x=0,y=210,width=490,height=380)

        
if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()