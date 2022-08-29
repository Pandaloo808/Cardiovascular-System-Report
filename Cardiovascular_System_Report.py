from tkinter import *
root=Tk()
root.title("Cardiovascular System Report")
root.geometry("600x500")
root.configure(bg="#eb9c7c")

#Q1

q1_response=StringVar(value="0")

q1=Label(root,text="Do you experience shortness of breath during routine activities?",bg="#eb9c7c")
q1.pack()
q1_r1=Radiobutton(root,text="yes",variable=q1_response,value="yes",bg="#eb9c7c")
q1_r1.pack()
q1_r2=Radiobutton(root,text="no",variable=q1_response,value="no",bg="#eb9c7c")
q1_r2.pack()

#Q2

q2_response=StringVar(value="0")

q2=Label(root,text="Do you have swelling in the feet/ankles/legs (shoes feel tighter) or abdomen?",bg="#eb9c7c")
q2.pack()
q2_r1=Radiobutton(root,text="yes",variable=q2_response,value="yes",bg="#eb9c7c")
q2_r1.pack()
q2_r2=Radiobutton(root,text="no",variable=q2_response,value="no",bg="#eb9c7c")
q2_r2.pack()

#Q3

q3_response=StringVar(value="0")

q3=Label(root,text="Do you feel any of the following symptoms: confusion, disorientation or loss of memory?",bg="#eb9c7c")
q3.pack()
q3_r1=Radiobutton(root,text="yes",variable=q3_response,value="yes",bg="#eb9c7c")
q3_r1.pack()
q3_r2=Radiobutton(root,text="no",variable=q3_response,value="no",bg="#eb9c7c")
q3_r2.pack()

#Q4

q4_response=StringVar(value="0")

q4=Label(root,text="Do you experience shortness of breath while at rest or lying down?",bg="#eb9c7c")
q4.pack()
q4_r1=Radiobutton(root,text="yes",variable=q4_response,value="yes",bg="#eb9c7c")
q4_r1.pack()
q4_r2=Radiobutton(root,text="no",variable=q4_response,value="no",bg="#eb9c7c")
q4_r2.pack()

#Q5

q5_response=StringVar(value="0")

q5=Label(root,text="Do you experience persistent wheezing/coughing that produces white or pink blood tinged mucus?",bg="#eb9c7c")
q5.pack()
q5_r1=Radiobutton(root,text="yes",variable=q5_response,value="yes",bg="#eb9c7c")
q5_r1.pack()
q5_r2=Radiobutton(root,text="no",variable=q5_response,value="no",bg="#eb9c7c")
q5_r2.pack()

def fever_score():
    score=0
    if q1_response.get()=="yes":
        score=score+10
    if q2_response.get()=="yes":
        score=score+10
    if q3_response.get()=="yes":
        score=score+10
    if q4_response.get()=="yes":
        score=score+10
    if q5_response.get()=="yes":
        score=score+10
        
    if score<=10:
        messagebox.showinfo("Report!","Congrats lucky person! You do not need to go to the doctor and face needles today.")
    elif score>10 and score<=30:
        messagebox.showinfo("Report!","You might need to visit a doctor and face needles, depends.")
    else:
        messagebox.showinfo("Report!","Today you must face needles citizen! Be careful were you step...")

btn=Button(root,text="Show Result",command=fever_score,bg="#95f0e1")
btn.pack()

root.mainloop()