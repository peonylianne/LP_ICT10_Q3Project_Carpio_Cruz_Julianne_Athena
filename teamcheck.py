from js import document
from pyodide.ffi import create_proxy

def assign_team(event=None):
    reg = document.querySelector('input[name="reg"]:checked')
    med = document.querySelector('input[name="med"]:checked')
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value.lower()
    output = document.getElementById("output")

    if reg is None or med is None:
        output.innerHTML = "(°ロ°) Please answer all questions."
        return

    if reg.value == "yes" and med.value == "yes":

        if section == "ruby":
            team = "Red Bulldogs"
            color = "red"
        elif section == "topaz":
            team = "Yellow Tigers"
            color = "gold"
        elif section == "sapphire":
            team = "Blue Bears"
            color = "royalblue"
        else:
            team = "Green Hornets"
            color = "green"

        output.innerHTML = (
            "♪(´▽｀) Congratulations!<br>"
            f"You are part of the "
            f"<span style='color:{color};'>{team}</span>"
        )

    else:
        output.innerHTML = (
            "╰（‵□′）╯ Registration incomplete.<br>"
            "Please finish online registration and medical clearance."
        )

button = document.getElementById("signup")
button.addEventListener("click", create_proxy(assign_team))
