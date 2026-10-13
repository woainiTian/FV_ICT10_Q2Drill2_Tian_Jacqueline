from pyscript import document, display

def add_member(e):
    first = document.getElementById("firstname").value
    last = document.getElementById("lastname").value
    
    grade7 = {
    "Ellie Goulding",
    "Kitchie Nadal",
    "Colbie Callait" }

    grade8 = {
    "Lizzy McAlpine", 
    "Gracie Abrams", 
    "Emmy Rossum" }

    grade9 = {
    "Avril Lavigne", 
    "Donna Lewis", 
    "Phoebe Bridgers" }

    grade10 = {
    "Leith Ross", 
    "Luisa Marion", 
    "Faye Webster" }


    full_name = first + " " + last 
        #combines the first name and last name user inputs

    pre = (grade7 | grade8 | grade9 | grade10)
    pre.add(full_name)
    
    
    display(", ".join(pre), target='result')
