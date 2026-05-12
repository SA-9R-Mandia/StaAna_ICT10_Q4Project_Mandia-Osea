from pyscript import display, document

# class def attributes
class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hello I'm {self.name} from {self.section}. My favorite subject is {self.favorite_subject}."

# class mate objects
classmates = [
    Classmate("Elaine", "Ruby", "Music"),
    Classmate("Freminet", "Amethyst", "ICT"),
    Classmate("Marcus", "Black Diamond", "AP"),
    Classmate("Cayle", "Garnet", "N/A"),
    Classmate("Raffie", "Black Onyx", "Science"),
    Classmate("Ella", "Moonstone", "N/A")
]

# function add classmate
def add_clm(e):
    name = document.getElementById("c1").value
    section = document.getElementById("sect").value
    subject = document.getElementById("subj").value

    new_student = Classmate(name, section, subject)
    classmates.append(new_student)

    display(f"{name} added successfully!\n", append=True, target='output')

# display classmates
def show_clms(e):
    document.getElementById('output').innerHTML = " "

    for student in classmates:
        intro = student.introduce()
        display(intro + "\n", target='output')

