from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
from time import strftime
from datetime import datetime
import numpy as np
import cv2


class Face_Recognition:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="FACE RECOGNITION", font=("rockwell extra bold",35,"underline"),bg="white",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\boy.jpg")
        img_top=img_top.resize((765,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=765,height=700)

        img_bottom=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\scan.jpg")
        img_bottom=img_bottom.resize((800,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        b_lbl=Label(self.root,image=self.photoimg_bottom)
        b_lbl.place(x=765,y=55,width=800,height=700)

        btn=Button(b_lbl,text="Face Recognition", cursor="hand2",command=self.face_recog, font=("rockwell",18,"bold"),bg="dark blue",fg="white")
        btn.place(x=280,y=600,width=250,height=40)

    def mark_attendence(self,i,r,n,d):
        with open("attendence.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            names_list=[]
            for line in myDataList:
                entry=line.split((","))
                names_list.append(entry[0])
            if((i not in names_list) and (r not in names_list) and (d not in names_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n {i},{r},{d},{n},{dtString},{d1},Present")




    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost", username="root" , password="mysqloracle", database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select Name from student where StudentId="+str(id))
                n=my_cursor.fetchone()
                n=str(n)
                

                my_cursor.execute("select RollNo from student where StudentId="+str(id))
                r=my_cursor.fetchone()
                r=str(r)

                my_cursor.execute("select Dept from student where StudentId="+str(id))
                d=my_cursor.fetchone()
                d=str(d)

                my_cursor.execute("select StudentId from student where StudentId="+str(id))
                i=my_cursor.fetchone()
                i=str(i)

                if confidence>77:
                    cv2.putText(img,f"Student Id.:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll No.:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            
            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()







if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()