from tkinter import *
from PIL import Image, ImageTk


class LoadData:
    def __init__(self):
        self.input_code = Entry(root, font="Georgia 12")
        self.input_code.place(x=320, y=60)

    def get_filename(self):
        try:
            global filename
            filename = str(self.input_code.get())
            self.load()
        except FileNotFoundError:
            self.input_code.insert(0, "Error: Not Found")

    def load(self):
            file = open(filename + "_GI.txt", "r")
            name_box.delete(0.0, END)
            name_box.insert(0.0, file.readline())
            name_box.configure(state="disabled")
            age_box.delete(0.0, END)
            age_box.insert(0.0, file.readline())
            age_box.configure(state="disabled")
            gender_box.delete(0.0, END)
            gender_box.insert(0.0, file.readline())
            gender_box.configure(state="disabled")
            last_visit_box.delete(0.0, END)
            last_visit_box.insert(0.0, file.readline())
            last_visit_box.configure(state="disabled")
            file.close()

            file = open(filename + "_ALG.txt", "r")
            allergies_box.delete(0.0, END)
            allergies_box.insert(0.0, file.read())
            allergies_box.configure(state="disabled")
            file.close()

            file = open(filename + "_DIS.txt", "r")
            diseases_conditions_box.delete(0.0, END)
            diseases_conditions_box.insert(0.0, file.read())
            diseases_conditions_box.configure(state="disabled")
            file.close()

            file = open(filename + "_MEDHIS.txt", "r")
            med_history_box.delete(0.0, END)
            med_history_box.insert(0.0, file.read())
            med_history_box.configure(state="disabled")
            file.close()

            file = open(filename + "_ADDINFO.txt", "r")
            add_comments_box.delete(0.0, END)
            add_comments_box.insert(0.0, file.read())
            add_comments_box.configure(state="disabled")
            file.close()

    def edit(self):
        name_box.configure(state="normal")
        age_box.configure(state="normal")
        gender_box.configure(state="normal")
        last_visit_box.configure(state="normal")
        allergies_box.configure(state="normal")
        diseases_conditions_box.configure(state="normal")
        med_history_box.configure(state="normal")
        add_comments_box.configure(state="normal")


class SetUp:
    def __init__(self, master):
        self.file_obj = LoadData()
        self.master = master

        load_btn = Button(master, text="Load Patient Info", command=self.file_obj.get_filename)
        load_btn.place(x=320, y=100)
        edit_btn = Button(master, text="Edit Current Patient Info", command=self.file_obj.edit)
        edit_btn.place(x=320, y=140)
        save_btn = Button(master, text="Save Current Patient Info")
        save_btn.place(x=320, y=180)
        save_as_btn = Button(master, text="Save As...")
        save_as_btn.place(x=320, y=220)

        general_info = Frame(master, relief=GROOVE, bd=5)
        general_info.place(x=650, y=50, width=550, height=200)
        general_info_heading = Label(master, font="Georgia 14 bold", text="General Information")
        general_info_heading.place(x=660, y=60)

        name_heading = Label(master, font="Georgia 12", text="Name:")
        name_heading.place(x=660, y=100)
        age_heading = Label(master, font="Georgia 12", text="Age:")
        age_heading.place(x=660, y=130)
        gender_heading = Label(master, font="Georgia 12", text="Gender:")
        gender_heading.place(x=660, y=160)
        last_visit_heading = Label(master, font="Georgia 12", text="Last Visit:")
        last_visit_heading.place(x=660, y=190)

        allergies = Frame(master, relief=GROOVE, bd=5)
        allergies.place(x=50, y=260, width=550, height=200)
        allergies_heading = Label(master, font="Georgia 14 bold", text="Allergies")
        allergies_heading.place(x=60, y=270)

        diseases_conditions = Frame(master, relief=GROOVE, bd=5)
        diseases_conditions.place(x=650, y=260, width=550, height=200)
        diseases_conditions_heading = Label(master, font="Georgia 14 bold", text="Diseases/Conditions")
        diseases_conditions_heading.place(x=660, y=270)

        med_history = Frame(master, relief=GROOVE, bd=5)
        med_history.place(x=50, y=470, width=550, height=200)
        med_history_heading = Label(master, font="Georgia 14 bold", text="Medical/Treatment History")
        med_history_heading.place(x=60, y=480)

        add_comments = Frame(master, relief=GROOVE, bd=5)
        add_comments.place(x=650, y=470, width=550, height=200)
        add_comments_heading = Label(master, font="Georgia 14 bold", text="Additional Comments")
        add_comments_heading.place(x=660, y=480)


root = Tk()
root.wm_title("Medical Database v1.0")
root.geometry("1250x800")
root.maxsize(width=1250, height=800)

run = SetUp(root)

header = Label(root, font="Georgia 20", text="Internal Database", relief=GROOVE, bd=5)
header.pack(fill=X, anchor=N)

load = Image.open("DefaultProfilePic.png")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render, relief=SUNKEN)
img.image = render
img.place(x=50, y=50)

name_box = Text(root, font="Georgia 12", width=35, height=1)
name_box.place(x=780, y=100)
age_box = Text(root, font="Georgia 12", width=35, height=1)
age_box.place(x=780, y=130)
gender_box = Text(root, font="Georgia 12", width=35, height=1)
gender_box.place(x=780, y=160)
last_visit_box = Text(root, font="Georgia 12", width=35, height=1)
last_visit_box.place(x=780, y=190)

allergies_box = Text(root, font="Georgia 12", width=50, height=7)
allergies_box.place(x=70, y=310)

diseases_conditions_box = Text(root, font="Georgia 12", width=50, height=7)
diseases_conditions_box.place(x=670, y=310)

med_history_box = Text(root, font="Georgia 12", width=50, height=7)
med_history_box.place(x=70, y=520)

add_comments_box = Text(root, font="Georgia 12", width=50, height=7)
add_comments_box.place(x=670, y=520)

root.mainloop()
