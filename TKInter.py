import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo
show = tkinter.Tk()

show.title("Project PAS : Account ")
show.configure(bg="pink")
show.geometry("300x300")
show.resizable(False,False)

frame = ttk.Frame(show)
#pengaturan tampilan : pack, pad,place
frame.pack(padx=15, pady=15, fill="x", expand=True)

label_email = ttk.Label(frame, text="EMAIL : ")
label_email.pack(padx=10, pady=10, fill="x", expand=True)

varEmail = tkinter.StringVar()

entry_email = ttk.Entry(frame, textvariable = varEmail)
entry_email.pack(padx=10, pady=5, fill="x", expand=True)

label_password = ttk.Label(frame, text="PASSWORD : ")
label_password.pack(padx=10, pady=10, fill="x", expand=True)

varPassword = tkinter.StringVar()

entry_password = ttk.Entry(frame, textvariable = varPassword)
entry_password.pack(padx=10, pady=5, fill="x", expand=True)

label_username = ttk.Label(frame, text="USERNAME : ")
label_username.pack(padx=10, pady=10, fill="x", expand=True)

varUsername = tkinter.StringVar()

entry_username = ttk.Entry(frame, textvariable = varUsername)
entry_username.pack(padx=10, pady=5, fill="x", expand=True)

def AksiSubmit():
    output = f"Hello, username {varUsername.get()}. Your email is {varEmail.get()} with code password {varPassword.get()}, is that right? If you sure that is already right, please click 'ok'"
    showinfo(message=output)
submit = ttk.Button(frame, text="Submit", command=AksiSubmit)
submit.pack(padx=10, pady=5, fill="x", expand=True)

show.mainloop()