from tkinter import *
from dbInteraction import DBInteraction


class SearchWindow:
    def __init__(self):
        self.db_conn = DBInteraction()

        self.root = Tk()
        self.root.wm_title("Search Database")
        self.root.geometry("650x400")

        self.search_label = Label(self.root, font="Georgia 14 bold", text="Search:")
        self.search_label.pack()

        self.search_box = Entry(self.root, font="Georgia 14")
        self.search_box['width'] = 20
        self.search_box.pack()

        self.search_btn = Button(self.root, text="Search", command=self.search_db)
        self.search_btn.pack()

        spacer = Label(self.root, text="\n\n", font="Georgia 5")
        spacer.pack()

        id_label = Label(self.root, text="ID", font="Georgia 14 bold")
        id_label.place(x=65, y=80)
        name_label = Label(self.root, text="Name", font="Georgia 14 bold")
        name_label.place(x=220, y=80)
        age_label = Label(self.root, text="Age", font="Georgia 14 bold")
        age_label.place(x=390, y=80)
        gender_label = Label(self.root, text="Gender", font="Georgia 14 bold")
        gender_label.place(x=525, y=80)

        self.references = []
        self.root.mainloop()

        self.db_conn.shutdown()

    def search_db(self):
        # ============== DELETING THE OLD RESULTS ==============
        for widget in self.references:
            widget.pack_forget()

        # ================= GETTING NEW RESULTS ================
        name = str(self.search_box.get())
        db_results = (self.db_conn.search_data(name))

        for i in db_results:
            temp = Label(self.root,
                         text=str(
                            str(i[0]) + "\t\t" + str(i[1]) + "\t"
                            "\t" + str(i[2]) + "\t\t" + str(i[3])
                            ),
                         font="Georgia 12"
                         )
            temp.pack()
            self.references.append(temp)

# run = SearchWindow()
