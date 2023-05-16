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

def call():
    
    input_label=(Txt1.get())
    print(input_label)
    input_label2=(txt2.get())
    print(input_label2)
    input_label3=(txt3.get())
    print(input_label3)
    input_label4=(txt4.get())
    print(input_label4)
    input_label5=(txt5.get())
    print(input_label5)
    input_label6=(txt6.get())
    print(input_label6)


main=tk.Tk(className="student id ")
main.geometry("400x400")



label1=tk.Label(main,text="student Name").grid(row=0,column=0)
Txt1=tk.Entry(main).grid(row=0,column=1)

label2=tk.Label(main,text="STUDENT CLASS").grid(row=1,column=0)
txt2=tk.Entry(main).grid(row=1,column=1)

label3=tk.Label(main,text="STUDENT ROLL NUMBER").grid(row=2,column=0)
txt3=tk.Entry(main).grid(row=2,column=1)

labe4=tk.Label(main,text="STUDENT DOB").grid(row=3,column=0)
txt4=tk.Entry(main).grid(row=3,column=1)

labe5=tk.Label(main,text="STUDENT AREA").grid(row=4,column=0)
txt5=tk.Entry(main).grid(row=4,column=1)

labe6=tk.Label(main,text="PHONE NUMBER").grid(row=5,column=0)
txt6=tk.Entry(main).grid(row=5,column=1)

btn1=tk.Button(main,text="SUBMIT",command=call).grid(row=6,column=1)


main.mainloop()




