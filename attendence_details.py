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
import csv
from tkinter import filedialog


mydata=[]


class Attendence_details:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendence=StringVar()        

        img_top=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\class1.jpg")
        img_top=img_top.resize((800,200),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=0,width=800,height=200)

        img_bottom=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\class2.jpg")
        img_bottom=img_bottom.resize((800,200),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        b_lbl=Label(self.root,image=self.photoimg_bottom)
        b_lbl.place(x=800,y=0,width=800,height=200)

        img3=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\bg4.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl=Label(self.root,text="ATTENDENCE MANAGEMENT SYSTEM", font=("rockwell extra bold",30,"underline"),bg="white",fg="dark blue")
        title_lbl.place(x=0,y=200,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)

        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE, text="Student Attendence Details", font=("rockwell extra bold",12,"underline"))
        left_frame.place(x=10,y=10,width=760,height=580)

        img_left=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\sdbg.jfif")
        img_left=img_left.resize((750,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=750,height=130)

        left_inside_frame=Frame(left_frame,bd=2, relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=135,width=750,height=350)

        attendenceid_label=Label(left_inside_frame,text="ATTENDENCE ID",font=("rockwell",12), bg="white")
        attendenceid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendenceID_entry=ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_id,font=("rockwell",12))
        attendenceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        rollno_label=Label(left_inside_frame,text="ROLL NO.",font=("rockwell",12), bg="white")
        rollno_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        rollno_entry=ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_roll,font=("rockwell",12))
        rollno_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        name_label=Label(left_inside_frame,text="NAME",font=("rockwell",12), bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_name, font=("rockwell",12))
        name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        department_label=Label(left_inside_frame,text="DEPARTMENT",font=("rockwell",12), bg="white")
        department_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        department_entry=ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_dep, font=("rockwell",12))
        department_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        date_label=Label(left_inside_frame,text="DATE",font=("rockwell",12), bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        date_entry=ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_date, font=("rockwell",12))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        time_label=Label(left_inside_frame,text="TIME",font=("rockwell",12), bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        time_entry=ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_time, font=("rockwell",12))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        attendence_label=Label(left_inside_frame,text="ATTENDENCE STATUS", font=("rockwell",12), bg="white")
        attendence_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendence, font=("rockwell",12),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=300,width=720,height=35)

        importcsv_btn=Button(btn_frame,text="IMPORT CSV",command=self.importcsv, width=17,font=("rockwell",12,"bold"),bg="dark blue",fg="white")
        importcsv_btn.grid(row=0,column=0)

        
        exportcsv_btn=Button(btn_frame,text="EXPORT CSV",command=self.exportcsv, width=17,font=("rockwell",12,"bold"),bg="dark blue",fg="white")
        exportcsv_btn.grid(row=0,column=1)

       
        update_btn=Button(btn_frame,text="UPDATE", width=17,font=("rockwell",12,"bold"),bg="dark blue",fg="white")
        update_btn.grid(row=0,column=2)

         #reset Button
        reset_btn=Button(btn_frame,text="RESET",command=self.reset_data, width=17,font=("rockwell",12,"bold"),bg="dark blue",fg="white")
        reset_btn.grid(row=0,column=3)

        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE, text="Attendence Details", font=("rockwell extra bold",12,"underline"))
        right_frame.place(x=780,y=10,width=660,height=580)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=650,height=445)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendenceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("id",text="ATTENDENCE ID.")
        self.AttendenceReportTable.heading("roll",text="ROLL NO.")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("department",text="DEPARTMENT")
        self.AttendenceReportTable.heading("time",text="TIME")
        self.AttendenceReportTable.heading("date",text="DATE")
        self.AttendenceReportTable.heading("attendence",text="ATTENDENCE STATUS")
        self.AttendenceReportTable["show"]="headings"

        self.AttendenceReportTable.column("id",width=100)
        self.AttendenceReportTable.column("roll",width=100)
        self.AttendenceReportTable.column("name",width=100)
        self.AttendenceReportTable.column("department",width=100)
        self.AttendenceReportTable.column("time",width=100)
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendence",width=100)
        
        self.AttendenceReportTable.pack(fill=BOTH,expand=1)
        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)

    def fetch_data(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)

    def importcsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All Files","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All Files","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimeter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data is exported"+os.path.basename(fln)+"successfully")

        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}", parent=self.root)
            
    def get_cursor(self,event=""):
        cursor_row=self.AttendenceReportTable.focus()
        content=self.AttendenceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendence.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendence.set("")

    
        

        

if __name__=="__main__":
    root=Tk()
    obj=Attendence_details(root)
    root.mainloop()