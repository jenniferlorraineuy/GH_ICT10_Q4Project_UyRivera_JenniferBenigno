from pyscript import display, document


class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hi! I'm {self.name}. I belong to {self.section}, and my favorite subject is {self.favorite_subject}."

classmates = [
    Classmate('Anakin Batac', 'Sapphire', 'English'),
    Classmate('Sittie Macabago', 'Sapphire', 'English'),
    Classmate('Selena Galvez', 'Sapphire', 'Math'),
    Classmate('Ishan Shrestha', 'Sapphire', 'Social Studies'),
    Classmate('Seth Ngo', 'Sapphire', 'Math'),
    Classmate('Vito De Guzman', 'Sapphire', 'Social Studies'),
]

def show_list(e):
    output = document.getElementById("output")
    output.innerHTML = ""
    for cm in classmates:
        card = document.createElement("div")
        card.className = "classmate-card"
        card.innerHTML = cm.introduce()
        output.appendChild(card)

def add_classmate(e):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("favorite_subject").value

    if name == "" or section == "" or subject == "":
        document.getElementById("output").innerHTML = "<p> Fill all fields. </p>"
        return

    new_classmate = Classmate(name, section, subject)
    classmates.append(new_classmate)

    document.getElementById("name").value = ""
    document.getElementById("section").value = ""
    document.getElementById("favorite_subject").value = ""

    show_list(None)
