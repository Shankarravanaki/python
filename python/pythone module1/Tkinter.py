# # # Which is As Follows: EMI = (P X R/12) X [(1+R/12) ^N] / [(1+R/12) ^N-1]. 


# # import tkinter as tk

# # main=tk.Tk(className="emi calculator")
# # main.geometry("400x400")

# # def call():
# #     input_value=txt1.get()
# #     print(input)

# # # def call():
# # #     input_value=txt2.get()
# # #     print(input)

# # name1=tk.Label(main,text="python")
# # txt1=tk.Entry(main)
# # btn1=tk.Button(main,text="submit",command=call)



# # name1.grid(row=0,column=0)
# # txt1.grid(row=0,column=1)

# student_information=tk.Label(main,text="STUDENT INFORMATION").grid(row=5,column=1)
# student_name=tk.Label(main,text="student name").grid(row=6,column=1)
# txt5=tk.Label(main,text="input_name").grid(row=7,column=1)
# student_id=tk.Label(main,text="student id").grid(row=8,column=1)


# from tkinter import *
import tkinter as tk

main=tk.Tk(className="customer details ")
main.geometry("400x400")
main_lst=[]

def add():
    lst=[Name.get(),age.get(),contact.get()]
    main_lst.append(lst)

with open["C:/Users/User/Desktop/customer details.csv","w"]


label1=tk.Label(main,text="Name").grid(row=0,column=1)
Txt1=tk.Entry(main).grid(row=0,column=2)

label1=tk.Label(main,text="Age").grid(row=1,column=1)
Txt1=tk.Entry(main).grid(row=1,column=2)

label1=tk.Label(main,text="Contact").grid(row=2,column=1)
Txt1=tk.Entry(main).grid(row=2,column=2)

btn1=tk.Button(main,text="submit").grid(row=3,column=2)

main.mainloop()

