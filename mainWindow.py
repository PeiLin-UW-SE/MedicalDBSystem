from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from dbInteraction import DBInteraction
from searchDB import SearchWindow

db = DBInteraction()
db.create_tables()
f = open('stored_p_id.txt', 'r')
stored_p_id = int(f.read())
current_p_id = -1
img_new = None

# ===================================================================================================
# =================================== MESSAGE BOX FUNCTIONALITIES ===================================
# ===================================================================================================


def clear_all():
    name_box.delete(0.0, END)
    age_box.delete(0.0, END)
    gender_box.delete(0.0, END)
    last_visit_box.delete(0.0, END)
    allergies_box.delete(0.0, END)
    diseases_conditions_box.delete(0.0, END)
    med_history_box.delete(0.0, END)
    add_comments_box.delete(0.0, END)
    patient_box.delete(0, END)


def enable_all():
    name_box.configure(state="normal", background="white")
    age_box.configure(state="normal", background="white")
    gender_box.configure(state="normal", background="white")
    last_visit_box.configure(state="normal", background="white")
    allergies_box.configure(state="normal", background="white")
    diseases_conditions_box.configure(state="normal", background="white")
    med_history_box.configure(state="normal", background="white")
    add_comments_box.configure(state="normal", background="white")


def disable_all():
    name_box.configure(state="disabled", background="alice blue")
    age_box.configure(state="disabled", background="alice blue")
    gender_box.configure(state="disabled", background="alice blue")
    last_visit_box.configure(state="disabled", background="alice blue")
    allergies_box.configure(state="disabled", background="alice blue")
    diseases_conditions_box.configure(state="disabled", background="alice blue")
    med_history_box.configure(state="disabled", background="alice blue")
    add_comments_box.configure(state="disabled", background="alice blue")

# ===================================================================================================
# ============================= INITIALIZATION OF BASIC WINDOW ELEMENTS =============================
# ===================================================================================================


def new():
    new_patient = str(name_box.get(0.0, END))
    global stored_p_id

    if new_patient != "" and new_patient != "\n":
        db.insert_data(
            int(stored_p_id),
            str(name_box.get(0.0, END)).strip("\n"),
            str(age_box.get(0.0, END)).strip("\n"),
            str(gender_box.get(0.0, END)).strip("\n"),
            str(last_visit_box.get(0.0, END)).strip("\n"),
            str(allergies_box.get(0.0, END)).strip("\n"),
            str(diseases_conditions_box.get(0.0, END)).strip("\n"),
            str(med_history_box.get(0.0, END)).strip("\n"),
            str(add_comments_box.get(0.0, END)).strip("\n")
        )
        stored_p_id += 1

        global f
        f.close()
        f = open('stored_p_id.txt', 'w')
        f.write(str(stored_p_id))
        f.close()
        f = open('stored_p_id.txt', 'r')

        messagebox.showinfo(title="Confirmation", message="New Patient Successfully Added")
        clear_all()
    else:
        messagebox.showinfo(title="System Error", message="Error: Addition Unsuccessful")


def get_entry():
    temp_p_id = patient_box.get()
    try:
        temp_p_id = int(temp_p_id)
    except ValueError:
        patient_box.delete(0, END)
        patient_box.insert(0, "Invalid Input")
        return -1
    return int(temp_p_id)


def load():
    global stored_p_id
    query = get_entry()

    if 0 < query < stored_p_id:
        db.load_data(query)
        enable_all()
        clear_all()

        global current_p_id
        current_p_id = query

        name_box.insert(0.0, str(db.name))
        age_box.insert(0.0, int(db.age))
        gender_box.insert(0.0, str(db.gender))
        last_visit_box.insert(0.0, str(db.lastVisit))
        allergies_box.insert(0.0, str(db.allergies))
        diseases_conditions_box.insert(0.0, str(db.diseases))
        med_history_box.insert(0.0, str(db.history))
        add_comments_box.insert(0.0, str(db.comments))

        disable_all()

        global img_new
        load_new = Image.open("DefaultProfilePic.png")
        try:
            load_new = Image.open(str(current_p_id) + ".png")
        except FileNotFoundError:
            pass
        finally:
            render_new = ImageTk.PhotoImage(load_new)
            img_new = Label(root, image=render_new, relief=SUNKEN)
            img_new.image = render_new
            img_new.place(x=50, y=50)
    else:
        patient_box.delete(0, END)
        patient_box.insert(0, "Invalid Input")


def update():
    global current_p_id
    db.update_data(
        int(current_p_id),
        str(name_box.get(0.0, END)).strip("\n"),
        str(age_box.get(0.0, END)).strip("\n"),
        str(gender_box.get(0.0, END)).strip("\n"),
        str(last_visit_box.get(0.0, END)).strip("\n"),
        str(allergies_box.get(0.0, END)).strip("\n"),
        str(diseases_conditions_box.get(0.0, END)).strip("\n"),
        str(med_history_box.get(0.0, END)).strip("\n"),
        str(add_comments_box.get(0.0, END)).strip("\n")
    )
    if current_p_id != -1:
        messagebox.showinfo(title="Confirmation", message="Patient Information\nSuccessfully Updated")
    else:
        messagebox.showinfo(title="System Error", message="Error: Update Unsuccessful")
    disable_all()


def reset():
    global current_p_id
    current_p_id = -1
    enable_all()
    clear_all()

    global img_new
    img_new.pack_forget()
    load_again_img = Image.open("DefaultProfilePic.png")
    render_again = ImageTk.PhotoImage(load_again_img)
    img_again = Label(root, image=render_again, relief=SUNKEN)
    img_again.image = render_again
    img_again.place(x=50, y=50)


def search():
    SearchWindow()

# ===================================================================================================
# ============================= INITIALIZATION OF BASIC WINDOW ELEMENTS =============================
# ===================================================================================================

root = Tk()
root.wm_title("Medical Database v2.0")
root.geometry("1250x800")
root.maxsize(width=1250, height=800)

header = Label(root, font="Georgia 20", text="Internal Medical Database", relief=GROOVE, bd=5)
header.pack(fill=X, anchor=N)

load_img = Image.open("DefaultProfilePic.png")
render = ImageTk.PhotoImage(load_img)
img = Label(root, image=render, relief=SUNKEN)
img.image = render
img.place(x=50, y=50)

# ===================================================================================================
# =============================== GENERAL PATIENT INFORMATION WINDOWS ===============================
# ===================================================================================================

general_info = Frame(root, relief=GROOVE, bd=5)
general_info.place(x=650, y=50, width=550, height=200)
general_info_heading = Label(root, font="Georgia 14 bold", text="General Information")
general_info_heading.place(x=660, y=60)

name_heading = Label(root, font="Georgia 12", text="Name:")
name_heading.place(x=660, y=100)
name_box = Text(root, font="Georgia 12", width=35, height=1)
name_box.place(x=780, y=100)

age_heading = Label(root, font="Georgia 12", text="Age:")
age_heading.place(x=660, y=130)
age_box = Text(root, font="Georgia 12", width=35, height=1)
age_box.place(x=780, y=130)

gender_heading = Label(root, font="Georgia 12", text="Gender:")
gender_heading.place(x=660, y=160)
gender_box = Text(root, font="Georgia 12", width=35, height=1)
gender_box.place(x=780, y=160)

last_visit_heading = Label(root, font="Georgia 12", text="Last Visit:")
last_visit_heading.place(x=660, y=190)
last_visit_box = Text(root, font="Georgia 12", width=35, height=1)
last_visit_box.place(x=780, y=190)

# ===================================================================================================
# ================================== PROGRAM FUNCTIONALITY WIDGETS ==================================
# ===================================================================================================

id_label = Label(root, font="Georgia 14 bold", text="Patient ID")
id_label.place(x=320, y=50)

patient_box = Entry(root, font="Georgia 14")
patient_box.place(x=320, y=85)

new_btn = Button(root, text="New", command=new)
new_img = PhotoImage(file=r"Button Icons\new.png")
new_btn.config(image=new_img)
new_btn.place(x=335, y=120)

load_btn = Button(root, text="Load", command=load)
load_img = PhotoImage(file=r"Button Icons\load.png")
load_btn.config(image=load_img)
load_btn.place(x=415, y=120)

edit_btn = Button(root, text="Edit", command=enable_all)
edit_img = PhotoImage(file=r"Button Icons\edit.png")
edit_btn.config(image=edit_img)
edit_btn.place(x=495, y=120)

save_btn = Button(root, text="Update", command=update)
save_img = PhotoImage(file=r"Button Icons\save.png")
save_btn.config(image=save_img)
save_btn.place(x=335, y=190)

reset_btn = Button(root, text="Reset/Clear", command=reset)
reset_img = PhotoImage(file=r"Button Icons\clear.png")
reset_btn.config(image=reset_img)
reset_btn.place(x=415, y=190)

search_btn = Button(root, text="Search", command=search)
search_img = PhotoImage(file=r"Button Icons\search.png")
search_btn.config(image=search_img)
search_btn.place(x=495, y=190)

# ===================================================================================================
# =============================== SPECIFIC PATIENT INFORMATION WINDOWS ==============================
# ===================================================================================================

allergies = Frame(root, relief=GROOVE, bd=5)
allergies.place(x=50, y=260, width=550, height=200)
allergies_heading = Label(root, font="Georgia 14 bold", text="Allergies")
allergies_heading.place(x=60, y=270)
allergies_box = Text(root, font="Georgia 12", width=50, height=7)
allergies_box.place(x=70, y=310)

diseases_conditions = Frame(root, relief=GROOVE, bd=5)
diseases_conditions.place(x=650, y=260, width=550, height=200)
diseases_conditions_heading = Label(root, font="Georgia 14 bold", text="Diseases/Conditions")
diseases_conditions_heading.place(x=660, y=270)
diseases_conditions_box = Text(root, font="Georgia 12", width=50, height=7)
diseases_conditions_box.place(x=670, y=310)

med_history = Frame(root, relief=GROOVE, bd=5)
med_history.place(x=50, y=470, width=550, height=200)
med_history_heading = Label(root, font="Georgia 14 bold", text="Medical/Treatment History")
med_history_heading.place(x=60, y=480)
med_history_box = Text(root, font="Georgia 12", width=50, height=7)
med_history_box.place(x=70, y=520)

add_comments = Frame(root, relief=GROOVE, bd=5)
add_comments.place(x=650, y=470, width=550, height=200)
add_comments_heading = Label(root, font="Georgia 14 bold", text="Additional Comments")
add_comments_heading.place(x=660, y=480)
add_comments_box = Text(root, font="Georgia 12", width=50, height=7)
add_comments_box.place(x=670, y=520)

# ===================================================================================================
# ================================= CLOSING ALL CONNECTIONS AND FILES ===============================
# ===================================================================================================

root.mainloop()
db.shutdown()
f.close()
