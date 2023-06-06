from tkinter import *

# window

window = Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=250)

# functions





# labels

label_weight = Label(text="Enter your body weight(kg).")
label_height = Label(text="Enter your height(m).")
label_weight.place(x=150 - 185/2, y=60)
label_result = Label()
#label_weight.winfo_width() is 185

#label_height.winfo_width() is 150

# Entries

label_height.place(x=150 - 150 / 2,y=110)
entry_weight = Entry(width=20)

entry_weight.focus()

entry_height = Entry(width=20)
entry_weight.place(x=150 - 166 / 2,y=85)
#entry_weight.winfo_width is 166

entry_height.place(x=150 - 166 / 2,y=135)
# button
def BMI_calculate():
    BMI_status = ""
    user_weight = None
    user_height = None
    result_label = Label()
    try:

        user_weight = float(entry_weight.get())
        user_height = float(entry_height.get())
        BMI_value = float(user_weight) / float(user_height) ** 2
        if BMI_value <= 18.4:
            BMI_status = "Underweight"
        elif BMI_value >= 18.5 and BMI_value <= 24.9:
            BMI_status = "Normal"
        elif BMI_value >= 25 and BMI_value <= 39.9:
            BMI_status = "Overweight"
        else:
            BMI_status = "Obese"
        result_label.config(text=f"Your BMI value is {'%.2f' % BMI_value}, {BMI_status}")
        result_label.place(x=53 - len(BMI_status) , y=200)
    except:
        if type(entry_weight.get()) == str or type(entry_height.get()) == str:
            BMI_status = "Enter a valid number!"
        else:

            BMI_status = "Enter both weight and height!"
        result_label.config(text=BMI_status)
        print(type(entry_height.get()))
        print(entry_height.get())
        print(bool(entry_height.get() == str))

        result_label.place(x=150 - len(BMI_status)*3, y=200)


calculate_button = Button(text="Calculate", command=BMI_calculate)
calculate_button.place(x=150 - 44.5, y=165)



mainloop()
