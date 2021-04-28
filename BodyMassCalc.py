from tkinter import *

main_window = Tk()
main_window.title("Calculador de IMC")
main_window.geometry("500x200")


# Function that deletes all  input and the result label content
def delete():
    global resultado
    resultado.destroy()
    alturaIntroduzida.delete(0, "end")
    pesoIntroduzido.delete(0, "end")
    changeState()


def calculate():
    global imc
    global resultado

    try:
        imc = float(pesoIntroduzido.get()) / float(alturaIntroduzida.get()) ** 2

    except:
        resultado = Label(main_window, text="Os seus numeros não são válidos, confirme e tente de novo")
        resultado.grid(row=4, column=0, columnspan=2)
        alturaIntroduzida.delete(0, "end")
        pesoIntroduzido.delete(0, "end")

    else:
        resultado.destroy()
        imc = format(imc, ".2f")
        buttonDelete["state"] = NORMAL
        showResult()



def showResult():
    global resultado
    global imc
    imc = float(imc)
    if (imc>0):
        textoApresentar = f"O teu Índice de Massa Corporal é de: {imc}"
        resultado = Label(main_window, text=textoApresentar)

        if(imc<18.5):
            resultado["bg"] = "yellow"
        elif(imc>=18.5 and imc<24.9):
            resultado["bg"] = "#9cff33"
        elif (imc >= 24.9 and imc < 30):
            resultado["bg"] = "yellow"
        else:
            resultado["bg"] = "#ff5c33"
    else:
        resultado = Label(main_window, text="Introduziste os valores mal, é melhor rever")

    resultado.grid(row=4, column=0, columnspan=2)


# Changes Buttons' state accondingly
def changeState():
    if buttonDelete["state"] == NORMAL:
        buttonDelete["state"] = DISABLED
        buttonCalculate["state"] = NORMAL
    else:
        buttonDelete["state"] = NORMAL
        buttonCalculate["state"] = DISABLED

# Labels de texto
Label(main_window, text="Calcule o seu Índice de Massa Corporal").grid(row=0, column=0, columnspan=2)
Label(main_window, text="Introduza o seu peso").grid(row=1, column=0)
Label(main_window, text="Introduza a sua em metros").grid(row=2, column=0)

resultado = Label(main_window, text="")
resultado.grid(row=4, column=0, columnspan=2)


# Text Input - capta dados do user
pesoIntroduzido = Entry(main_window, width=10)
pesoIntroduzido.grid(row=1, column=1)

alturaIntroduzida = Entry(main_window, width=10)
alturaIntroduzida.grid(row=2, column=1)


# Button
buttonCalculate = Button(main_window, text="Calcular", command=calculate, padx=50, pady=10)
buttonCalculate.grid(row=3, column=0)

buttonDelete = Button(main_window, text="Refazer", command=delete, padx=50, pady=10, state=DISABLED)
buttonDelete.grid(row=3, column=1)


# Variables
imc = 0


main_window.mainloop()
