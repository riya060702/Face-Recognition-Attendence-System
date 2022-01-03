from tkinter import*
from tkinter import ttk
import tkinter
from tkinter import messagebox
from PIL import Image,ImageTk
from stu_det import Student
import os
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_Recognition
from attendence_details import Attendence_details
from developer import Developer
from help_desk import Help


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #top left corner image
        img=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\pic1.png")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #top center image
        img1=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\face.jfif")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #top right corner image
        img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\pic2.jpeg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #background image
        img3=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\bg3.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM", font=("rockwell extra bold",35,"underline"),bg="white",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,background="white",foreground="blue")
        lbl.place(x=0,y=0,width=150,height=70)
        time()

        #student details button
        img4=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\student.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4 ,command=self.student_details, cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details" ,command=self.student_details, cursor="hand2", font=("rockwell extra bold",15,"underline"),bg="dark blue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)


        #Face detector Button
        img5=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\face1.png")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5 ,command=self.face_recognition, cursor="hand2")
        b2.place(x=500,y=100,width=220,height=220)

        b2_1=Button(bg_img,text="Face Detector" ,command=self.face_recognition, cursor="hand2", font=("rockwell extra bold",15,"underline"),bg="dark blue",fg="white")
        b2_1.place(x=500,y=300,width=220,height=40)

        #Attendence Button
        img6=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\attendence.png")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6 , cursor="hand2",command=self.atten_det)
        b3.place(x=800,y=100,width=220,height=220)

        b3_1=Button(bg_img,text="Attendence" , cursor="hand2",command=self.atten_det, font=("rockwell extra bold",15,"underline"),bg="dark blue",fg="white")
        b3_1.place(x=800,y=300,width=220,height=40)

        #Help Desk Button
        img7=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\help.png")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7 , cursor="hand2",command=self.help_data)
        b4.place(x=1100,y=100,width=220,height=220)

        b4_1=Button(bg_img,text="Help Desk" , cursor="hand2",command=self.help_data, font=("rockwell extra bold",15,"underline"),bg="dark blue",fg="white")
        b4_1.place(x=1100,y=300,width=220,height=40)

        #train data button
        img8=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\train.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8 , cursor="hand2",command=self.train_data)
        b5.place(x=200,y=370,width=220,height=220)

        b5_1=Button(bg_img,text="Train Data" , cursor="hand2",command=self.train_data, font=("rockwell extra bold",15,"underline"),bg="dark blue",fg="white")
        b5_1.place(x=200,y=590,width=220,height=40)

        #Photos Button
        img9=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\ca,.jfif")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9 , cursor="hand2",command=self.open_image)
        b6.place(x=500,y=370,width=220,height=220)

        b6_1=Button(bg_img,text="Photos" , cursor="hand2",command=self.open_image, font=("rockwell extra bold",15,"underline"),bg="dark blue",fg="white")
        b6_1.place(x=500,y=590,width=220,height=40)

        #Developer Button
        img10=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\developer.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimg10 , cursor="hand2",command=self.dev_data)
        b7.place(x=800,y=370,width=220,height=220)

        b7_1=Button(bg_img,text="Developer" , cursor="hand2",command=self.dev_data, font=("rockwell extra bold",15,"underline"),bg="dark blue",fg="white")
        b7_1.place(x=800,y=590,width=220,height=40)

        #Exit Button
        img11=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b8=Button(bg_img,image=self.photoimg11 , cursor="hand2",command=self.iExit)
        b8.place(x=1100,y=370,width=220,height=220)

        b8_1=Button(bg_img,text="Exit" , cursor="hand2",command=self.iExit, font=("rockwell extra bold",15,"underline"),bg="dark blue",fg="white")
        b8_1.place(x=1100,y=590,width=220,height=40)

    def open_image(self):
        os.startfile("images")

    def iExit(self):
        self.iExit=messagebox.askyesno("Face recognition","Do you want to exit??")
        if self.iExit>0:
            self.root.destroy()
        else:
            return
        

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def atten_det(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence_details(self.new_window)

    def dev_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)    

        

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()