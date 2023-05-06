# # Which is As Follows: EMI = (P X R/12) X [(1+R/12) ^N] / [(1+R/12) ^N-1]. 


# import tkinter as tk

# main=tk.Tk(className="emi calculator")
# main.geometry("400x400")

# def call():
#     input_value=txt1.get()
#     print(input)

# # def call():
# #     input_value=txt2.get()
# #     print(input)

# name1=tk.Label(main,text="python")
# txt1=tk.Entry(main)
# btn1=tk.Button(main,text="submit",command=call)



# name1.grid(row=0,column=0)
# txt1.grid(row=0,column=1)



import tkinter as tk

main=tk.Tk(className="student id ")
main.geometry("400x400")
# main.configure(bg="#FF69B4")

def call():
    input_name=txt1.get()
    print(input_name)
    input_id=txt2.get()
    print(input_id)
    input_rol_no=txt3.get()
    print(input_rol_no)
    input_DOB=txt4.get()
    print(input_DOB)
   
    



name=tk.Label(main,text="student name").grid(row=0,column=0)
txt1=tk.Entry(main).grid(row=0,column=1)
id=tk.Label(main,text="student id").grid(row=1,column=0)
txt2=tk.Entry(main).grid(row=1,column=1)
rol_no=tk.Label(main,text="student ROLL NUMBER").grid(row=2,column=0)
txt3=tk.Entry(main).grid(row=2,column=1)
DOB=tk.Label(main,text="student DOB").grid(row=3,column=0)
txt4=tk.Entry(main).grid(row=3,column=1)
btn1=tk.Button(main,text="submit",command=call).grid(row=4,column=1)
student_information=tk.Label(main,text="STUDENT INFORMATION").grid(row=5,column=1)
student_name=tk.Label(main,text="student name").grid(row=6,column=1)
txt5=tk.Label(main,text=input_name).grid(row=7,column=1)
student_id=tk.Label(main,text="student id").grid(row=8,column=1)






main.mainloop()




