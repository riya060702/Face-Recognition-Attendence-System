from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class Student:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #variables
        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_rollno=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_phone=StringVar()
        self.var_email=StringVar()
        self.var_pwd=StringVar()
        self.var_category=StringVar()
        self.var_address=StringVar()

        #top left corner image
        img=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\st4.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #top center image
        img1=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\st2.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #top right corner image
        img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\st3.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #background image
        img3=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\bg4.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM", font=("rockwell extra bold",35,"underline"),bg="white",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=650)

        #Left Label Frame

        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE, text="Student Details", font=("rockwell extra bold",12,"underline"))
        left_frame.place(x=10,y=10,width=760,height=580)

        img_left=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\sdbg.jfif")
        img_left=img_left.resize((750,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=750,height=130)

        #Course Details

        current_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE, text="Current Course Information", font=("rockwell extra bold",12))
        current_frame.place(x=10,y=160,width=750,height=120)

        #Department
        dep_label=Label(current_frame,text="Department",font=("rockwell",12), bg="white")
        dep_label.grid(row=0,column=0,sticky=W)

        dep_combo=ttk.Combobox(current_frame,textvariable=self.var_dept, font=("rockwell",12),width=20,state="readonly")
        dep_combo["values"]=("Select","Mechanical","IT","CSE","ECE","Architecture")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1, padx=2,pady=10,sticky=W)

        #course
        course_label=Label(current_frame,text="Course",font=("rockwell",12), bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_frame,textvariable=self.var_course, font=("rockwell",12),width=20,state="readonly")
        course_combo["values"]=("Select","B.Tech","B.E","BBA","M.Tech","Dual Degree")
        course_combo.current(0)
        course_combo.grid(row=0,column=3, padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(current_frame,text="Year",font=("rockwell",12), bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_frame,textvariable=self.var_year, font=("rockwell",12),width=20,state="readonly")
        year_combo["values"]=("Select","1st","2nd","3rd","4th","Final Year")
        year_combo.current(0)
        year_combo.grid(row=1,column=1, padx=2,pady=10,sticky=W)

        #Semester
        semester_label=Label(current_frame,text="Semester",font=("rockwell",12), bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_frame,textvariable=self.var_semester, font=("rockwell",12),width=20,state="readonly")
        semester_combo["values"]=("Select","1st","2nd","3rd","4th","5th","6th","7th","8th","other")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3, padx=2,pady=10,sticky=W)

        #Student Details

        student_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE, text="Student Details", font=("rockwell extra bold",12))
        student_frame.place(x=10,y=280,width=750,height=300)
    
        #Student Id
        id_label=Label(student_frame,text="Student ID",font=("rockwell",12), bg="white")
        id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(student_frame,textvariable=self.var_id, width=20,font=("rockwell",12))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student Name
        name_label=Label(student_frame,text="Student Name",font=("rockwell",12), bg="white")
        name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(student_frame,textvariable=self.var_name, width=20,font=("rockwell",12))
        name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Student Phone no
        phone_label=Label(student_frame,text="Phone No",font=("rockwell",12), bg="white")
        phone_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(student_frame,textvariable=self.var_phone, width=20,font=("rockwell",12))
        phone_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Student Roll No.
        rollno_label=Label(student_frame,text="Student Roll No",font=("rockwell",12), bg="white")
        rollno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        rollno_entry=ttk.Entry(student_frame,textvariable=self.var_rollno, width=20,font=("rockwell",12))
        rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Student Gender
        gender_label=Label(student_frame,text="Gender",font=("rockwell",12), bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(student_frame,textvariable=self.var_gender, font=("rockwell",12),width=18,state="readonly")
        gender_combo["values"]=("Select","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Student Date Of Birth
        dob_label=Label(student_frame,text="Date Of birth",font=("rockwell",12), bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(student_frame,textvariable=self.var_dob, width=20,font=("rockwell",12))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Student email id
        email_label=Label(student_frame,text="Email ID",font=("rockwell",12), bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(student_frame,textvariable=self.var_email, width=20,font=("rockwell",12))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Student Address
        address_label=Label(student_frame,text="Residential Address",font=("rockwell",12), bg="white")
        address_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(student_frame,textvariable=self.var_address, width=20,font=("rockwell",12))
        address_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Student Category
        category_label=Label(student_frame,text="Category",font=("rockwell",12), bg="white")
        category_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        category_combo=ttk.Combobox(student_frame,textvariable=self.var_category, font=("rockwell",12),width=18,state="readonly")
        category_combo["values"]=("Select","General","SC/ST","OBC","EWS")
        category_combo.current(0)
        category_combo.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Student pwd
        pwd_label=Label(student_frame,text="Person with Disability",font=("rockwell",12), bg="white")
        pwd_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        pwd_combo=ttk.Combobox(student_frame,textvariable=self.var_pwd, font=("rockwell",12),width=18,state="readonly")
        pwd_combo["values"]=("Select","No","Yes")
        pwd_combo.current(0)
        pwd_combo.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #Radio Buttons  
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(student_frame ,variable=self.var_radio1, text="Take Photo Sample",value="yes")
        radiobtn1.grid(row=6,column=0,padx=10,pady=5,sticky=W)

        radiobtn2=ttk.Radiobutton(student_frame ,variable=self.var_radio1, text="No Photo Sample",value="no")
        radiobtn2.grid(row=6,column=1,padx=10,pady=5,sticky=W)   

        #Buttons Frame
        btn_frame=Frame(student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=200,width=720,height=35)

        #save Button
        save_btn=Button(btn_frame,text="Save", command=self.add_data, width=17,font=("rockwell",12,"bold"),bg="dark blue",fg="white")
        save_btn.grid(row=0,column=0)

         #update Button
        update_btn=Button(btn_frame,text="Update",command=self.update_data, width=17,font=("rockwell",12,"bold"),bg="dark blue",fg="white")
        update_btn.grid(row=0,column=1)

         #delete Button
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data, width=17,font=("rockwell",12,"bold"),bg="dark blue",fg="white")
        delete_btn.grid(row=0,column=2)

         #reset Button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("rockwell",12,"bold"),bg="dark blue",fg="white")
        reset_btn.grid(row=0,column=3)

        #Buttons Frame
        btn1_frame=Frame(student_frame,bd=2,relief=RIDGE,bg="white")
        btn1_frame.place(x=10,y=240,width=720,height=35)

        #Take Photo Sample Button
        photo_btn=Button(btn1_frame,text="Take Photo",command=self.generate_dataset, width=35,font=("rockwell",12,"bold"),bg="dark blue",fg="white")
        photo_btn.grid(row=1,column=0)

        #Update Photo Button
        up_btn=Button(btn1_frame,text="Update Photo",width=35,font=("rockwell",12,"bold"),bg="dark blue",fg="white")
        up_btn.grid(row=1,column=1)
        

        #Right Label Frame

        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE, text="Student Details", font=("rockwell extra bold",12,"underline"))
        right_frame.place(x=780,y=10,width=660,height=580)

        img_right=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognition\Project_Images\stu.jpg")
        img_right=img_right.resize((750,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        r_lbl=Label(right_frame,image=self.photoimg_right)
        r_lbl.place(x=5,y=0,width=750,height=130)

        # xxxxxxxxxx   Search System     xxxxxxxxxxxxxxxx
        system_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE, text="Search System", font=("rockwell extra bold",12))
        system_frame.place(x=5,y=130,width=650,height=65)

        search_label=Label(system_frame,text="Search By",font=("rockwell",12), bg="green",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(system_frame, font=("rockwell",12),width=15,state="readonly")
        search_combo["values"]=("Select","ID","Roll No","Name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1, padx=2,pady=10,sticky=W)

        #Search Button
        search_btn=Button(system_frame,text="Search",width=12,font=("rockwell",12,"bold"),bg="dark blue",fg="white")
        search_btn.grid(row=0,column=3)

        #ShowAll Button
        showall_btn=Button(system_frame,text="Show All",width=12,font=("rockwell",12,"bold"),bg="dark blue",fg="white")
        showall_btn.grid(row=0,column=4)

        search_entry=ttk.Entry(system_frame,width=12,font=("rockwell",12))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        #table Frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=200,width=650,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","rollno","gender","dob","phone","email","pwd","category","address","photos"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("rollno",text="Roll No.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="Date of Birth")
        self.student_table.heading("phone",text="Contact No.")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("pwd",text="PWD")
        self.student_table.heading("category",text="Category")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photos",text="Photos Uploaded")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("pwd",width=100)
        self.student_table.column("category",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photos",width=100)
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    

    #Function Declaration
    def add_data(self):
        if self.var_dept.get()=="Select" or self.var_name.get()=="" or self.var_id.get=="":
            messagebox.showerror("Error","Fill all fields",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root" , password="mysqloracle", database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                self.var_dept.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_id.get(),
                self.var_name.get(),
                self.var_rollno.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_phone.get(),
                self.var_email.get(),
                self.var_pwd.get(),
                self.var_category.get(),
                self.var_address.get(),
                self.var_radio1.get()
              ))           
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Data Successfully Added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}", parent=self.root)

    ########### Fetch Data ####################
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root" , password="mysqloracle", database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    ########### Get Cursor  ##################################3
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dept.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_id.set(data[4])
        self.var_name.set(data[5])
        self.var_phone.set(data[9])
        self.var_rollno.set(data[6])
        self.var_gender.set(data[7])
        self.var_dob.set(data[8])
        self.var_email.set(data[10])
        self.var_address.set(data[13])
        self.var_category.set(data[12])
        self.var_pwd.set(data[11])
        self.var_radio1.set(data[14])

    #####################################  Update Function   ################################################
    def update_data(self):
        if self.var_dept.get()=="Select" or self.var_name.get()=="" or self.var_id.get=="":
            messagebox.showerror("Error","Fill all fields",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update details?", parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost", username="root" , password="mysqloracle", database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dept=%s,Course=%s,Year=%s,Semester=%s,Name=%s,RollNo=%s,Gender=%s,DateOfBirth=%s,ContactNo=%s, Email=%s,PWD=%s,Category=%s,Address=%s,PhotoSample=%s where StudentId=%s", (
                self.var_dept.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_name.get(),
                self.var_rollno.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_phone.get(),
                self.var_email.get(),
                self.var_pwd.get(),
                self.var_category.get(),
                self.var_address.get(),
                self.var_radio1.get(),
                self.var_id.get()
                    ))

                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Details Successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            
            except Exception as es:
                messagebox.showerror("Error","Fill all fields correctly",parent=self.root)
                
            
        ##############   Delete Function #######################33

    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student Id required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Permission Required","Do you want to delete this student details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost", username="root" , password="mysqloracle", database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where StudentId=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                    
                
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Details successfully deleted",parent=self.root)
                
            
            except Exception as es:
                messagebox.showerror("Error","Student Id required",parent=self.root)

    ################  Reset Function  #####################
    def reset_data(self):
        self.var_dept.set("Select")
        self.var_course.set("Select")
        self.var_year.set("Select")
        self.var_semester.set("Select")
        self.var_id.set("")
        self.var_name.set("")
        self.var_phone.set("")
        self.var_rollno.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_category.set("Select")
        self.var_pwd.set("Select")
        self.var_radio1.set("")
        
##################   Generate Data Set or take photo sample    ################################

    def generate_dataset(self):
        if self.var_dept.get()=="Select" or self.var_name.get()=="" or self.var_id.get=="":
            messagebox.showerror("Error","Fill all fields",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root" , password="mysqloracle", database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                my_result=my_cursor.fetchall()
                id=0
                for x in my_result:
                    id+=1
                my_cursor.execute("update student set Dept=%s,Course=%s,Year=%s,Semester=%s,Name=%s,RollNo=%s,Gender=%s,DateOfBirth=%s,ContactNo=%s, Email=%s,PWD=%s,Category=%s,Address=%s,PhotoSample=%s where StudentId=%s", (
                self.var_dept.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_name.get(),
                self.var_rollno.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_phone.get(),
                self.var_email.get(),
                self.var_pwd.get(),
                self.var_category.get(),
                self.var_address.get(),
                self.var_radio1.get(),
                self.var_id.get()==id+1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load Predefined data on Face Frontals by opencv

                face_classifier=cv2.CascadeClassifier("C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,myframe=cap.read()
                    if face_cropped(myframe) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(myframe),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="C:\\Users\\HP\\OneDrive\\Desktop\\Face Recognition\\images\\user_"+str(id)+"_"+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data Set Completed", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error","Error Occured",parent=self.root)

            






if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()

