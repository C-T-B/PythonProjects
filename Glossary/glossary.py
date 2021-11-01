from tkinter import *
#key down function
def click():
    entered_text=textentry.get() #Collects data from input box
    output.delete(0.0, END)
    try:
        definition = my_compdictionary[entered_text]
    except:
        definition = "Sorry there is no word like that please try again"
    output.insert(END, definition)

window = Tk()
window.title("A simple glossary")
window.configure(background="black")

### My Photo
me = PhotoImage(file="me.gif")
Label(window, image=me, bg="black") .grid(row=0, column=0, sticky=W)

#Function Label
Label (window, text="Enter word for definition:", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)
Label (window, text="\nDefinition:", bg="black", fg="white", font="none 12 bold") .grid(row=4, column=0, sticky=W)

#text entry
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)

#Submit Button
Button(window, text="SUBMIT", width=6, command=click) .grid(row=3, column=0, sticky=W)

#Exit button
def close_window():
    window.destroy()
    exit()
Button(window, text="EXIT", width=14, command=close_window) .grid(row=7, column =0, sticky=W)


#Output
output =Text(window, width=48,height=6, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=1, sticky=W)

#Create dictionary
my_compdictionary = {
    'algorithm': 'Step by step instructions to complete a task', 'bug': 'piece of code that causes a program to fail'
    }


window.mainloop()