import tkinter as tk
from tkinter import messagebox
import webbrowser as wb
import random
import string
import time


main_window = tk.Tk()
main_window.geometry("1400x720")
main_window.title("ENIGMA")
main_window.iconbitmap("enigma.ico")
main_window.config(background='#ccccff')
main_window.maxsize(1400,720)







canvas = tk.Canvas(main_window, width=1400, height=720, bg="black")
canvas.pack(fill="both", expand=True)


label = tk.Label(main_window, text="WELCOME TO ENIGMA", font=("Andalus", 60), foreground="#6013ad", bg="black")
label.place(relx=0.5, rely=0.14, anchor="center")  


letters = []  

def create_letter():
    letter = random.choice(string.ascii_letters)  
    font_size = random.randint(20, 60)  
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))  
    angle = random.randint(0, 360)  

    
    side = random.choice(["left", "right", "top", "bottom"]) 
    if side == "left":
        x = -50  
        y = random.randint(0, 720)  
    elif side == "right":
        x = 1450  
        y = random.randint(0, 720)  
    elif side == "top":
        x = random.randint(0, 1400)  
        y = -50  
    elif side == "bottom":
        x = random.randint(0, 1400)
        y = 770  

   
    target_x = random.randint(100, 1300)  
    target_y = random.randint(100, 620)  

    
    letter_id = canvas.create_text(x, y, text=letter, font=("Arial", font_size), fill=color, angle=angle)

    
    letters.append({
        "id": letter_id,
        "x": x,
        "y": y,
        "target_x": target_x,
        "target_y": target_y,
        "speed_x": (target_x - x) / 100,  
        "speed_y": (target_y - y) / 100,  
    })


def animate_letters(start_time):
    current_time = time.time()
    
    
    for letter in letters:
        if abs(letter["x"] - letter["target_x"]) > 1: 
            letter["x"] += letter["speed_x"]
        if abs(letter["y"] - letter["target_y"]) > 1: 
            letter["y"] += letter["speed_y"]

        
        canvas.coords(letter["id"], letter["x"], letter["y"])

   
    for letter in letters[:]:
        if abs(letter["x"] - letter["target_x"]) <= 1 and abs(letter["y"] - letter["target_y"]) <= 1:
            letters.remove(letter)  

  
    if len(letters) < 100:  
        create_letter()

  
    if current_time - start_time < 5: 
       
        canvas.after(20, animate_letters, start_time)


start_time = time.time() 
animate_letters(start_time)
author = tk.Label(main_window, text="Made by: Oussama EL ATTAOUI", font=('Cambria', 15), foreground='white',bg='#000000')
author.place(rely=0.9, relx=0.5,anchor='center')
linkdin = tk.Button(main_window, text="www.linkedin.com/in/oussama-el-attaoui-072a12335", font=('Cambria', 15), foreground='white',bg='black',cursor='hand2',
                    command=lambda: wb.open("https://www.linkedin.com/in/oussama-el-attaoui-072a12335"), relief='flat', activeforeground='black', activebackground='black',highlightthickness=3
                ,border=0,borderwidth=0)
linkdin.place(rely=0.95, relx=0.5,anchor='center')

#____________________________ENCRYPTION WINDOW_______________________________________________________________________________________


def open_encryption():




    #__________________________ROTORS_________________________________
    R = {
        1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
        11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's',
        20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
    }
    R1={1: 14, 2: 5, 3: 22, 4: 19, 5: 3, 6: 26, 7: 8, 8: 17, 9: 11, 10: 2,
        11: 20, 12: 16, 13: 7, 14: 25, 15: 12, 16: 9, 17: 23, 18: 4, 19: 18,
        20: 6, 21: 21, 22: 10, 23: 15, 24: 13, 25: 24, 26: 1}


    R2 = {1: 1, 2: 14, 3: 5, 4: 22, 5: 19, 6: 3, 7: 26, 8: 8, 9: 17, 10: 11,
        11: 2, 12: 20, 13: 16, 14: 7, 15: 25, 16: 12, 17: 9, 18: 23, 19: 4,
        20: 18, 21: 6, 22: 21, 23: 10, 24: 15, 25: 13, 26: 24}


    R3 = {1: 24, 2: 1, 3: 14, 4: 5, 5: 22, 6: 19, 7: 3, 8: 26, 9: 8, 10: 17,
        11: 11, 12: 2, 13: 20, 14: 16, 15: 7, 16: 25, 17: 12, 18: 9, 19: 23,
        20: 4, 21: 18, 22: 6, 23: 21, 24: 10, 25: 15, 26: 13}


    #__________________________Helper Functions_______________________
    def settings_get(settings):
        flag1 = True
        flag2 = True
        if settings == ['','','']:
            tk.messagebox.showinfo("Settings can't be empty", "Please enter your settings")
            return
        else :
            for x in settings:
                if not x.isdigit():
                    flag1 = False  
                    tk.messagebox.showinfo("Invalid format","Settings should be in d.d.d form only,where d is a number between 1-26")
                    return
        if len(settings) < 3 or len(settings) > 9:
            flag2 = False
            tk.messagebox.showinfo("Settings should be exactly 3 digits")
        flag = flag1 and flag2       
        if flag:
            if '0' not in settings:
                return settings
            else:
                tk.messagebox.showinfo("ZeRoError","Your settings can't include 0, only digits between 1-26 are allowed. Try again.")
                return None          

    def cycler(settings):
        if settings != None :
            x = int(settings[0])-1
            y = int(settings[1])-1
            z = int(settings[2])-1
            R1_set = { (x + i) % 26 + 1: R1[(x + i) % 26 + 1] for i in range(26)}
            R2_set = { (y + i) % 26 + 1: R2[(y + i) % 26 + 1] for i in range(26)}
            R3_set = { (z + i) % 26 + 1: R3[(z + i) % 26 + 1] for i in range(26)}
            return R1_set, R2_set, R3_set

    def get_key_by_value(dictionary, value):
        for key, val in dictionary.items():
            if val == value:
                return key

    def reflector(key, settings):
        s = []
        for u in settings:
            s.append(int(u))
        key = (key + sum(s)) % 26 + 1
        return key


    def enigma(c, R1_set, R2_set, R3_set, settings):
        L1 = list(R1_set)
        L2 = list(R2_set)
        L3 = list(R3_set)

        key = get_key_by_value(R,c)

        temp= L1[key-1]

        key= R1_set[temp]

        temp= L2[key-1]

        key = R2_set[temp]

        temp= L3[key-1]

        key = reflector(temp, settings)

        temp = R3_set[key]
        key = get_key_by_value(R2_set,temp)
        temp = get_key_by_value(R1_set,key)
        c = R[temp]
        return c




    def replacer(c):
        global linked_pairs
        p = c.upper()
        if c.isupper() :
            for pair in linked_pairs:
                if p in pair :
                    return pair[pair.index(p)-1]
        if c.islower():
            for pair in linked_pairs :
                if p in pair :
                    return pair[pair.index(p)-1].lower()
        return c

    def encrypter():
        settings =[set_entry0.get() , set_entry1.get() , set_entry2.get()]
        settings = settings_get(settings)
        txt = textbox.get('1.0', 'end')
        R1_set, R2_set, R3_set = cycler(settings)
        l = list(txt)
        n = len(l)
        for i in range(n):
            l[i]=replacer(l[i])
            if l[i].isalpha():
                f = l[i].islower()
                l[i]=l[i].lower()
                enc_cara = enigma(l[i], R1_set, R2_set, R3_set, settings)
                if f :
                    l[i] = enc_cara
                else :
                    l[i] = enc_cara.upper()
                x = i + 1
                R1_set, R2_set, R3_set = cycler([x, (x//10)+1, (x//100)+1])    
        l = ''.join(l)
        textboxenc.config(state='normal')
        textboxenc.delete('1.0', 'end')
        textboxenc.insert('1.0', l)
        textboxenc.config(state='disabled')


    #_______________________GUI Setup____________________
    root = tk.Tk()
    root.title("E N I G M A")
    root.attributes('-fullscreen', True)
    root.iconbitmap('enigma.ico')
    root.config(background='#ccccff')
    root.geometry("1900x1020")

    label = tk.Label(root, text="E N I G M A", font=('Andalus', 80), foreground='#6013ad',bg='#ccccff')
    label.place(relx=0.354, rely=0.05)

    def exit_fullscreen(event=None):
        root.attributes('-fullscreen', False)

    def close_app(event=None):
        root.destroy()

    root.bind('<Escape>', exit_fullscreen)
    root.bind('<Shift-Escape>', close_app)

    #_______________________Textbox____________________
    frame_textbox = tk.Frame(root,bg='#ccccff')
    frame_textbox.place(relx=0.005, rely=0.25, relheight=0.8, relwidth=0.49)

    textbox = tk.Text(frame_textbox,bg='#ccccff', width=49, height=10, font=('Cambria', 26))
    textbox.place(relx=0, rely=0.05)

    def Clear():
        textbox.delete('1.0', 'end')


    clear_button = tk.Button(frame_textbox, text="X", font=('Cambria', 10), width=2, height=1, command=Clear,bg='#4b0082',foreground='#ffffff',cursor='hand2',activebackground='#ccccff',activeforeground='#4b0082')
    clear_button.place(relx=0.965, rely=0.012)



    label1 = tk.Label(frame_textbox, text="Text to be encrypted:", font=('Cambria', 18),bg='#ccccff')
    label1.place(x=0.01, y=0)

    label_set = tk.Label(frame_textbox, text="Enter your settings:", font=('Cambria', 18),bg='#ccccff')
    label_set.place(relx=0.54, rely=0)

    set_entry0 = tk.Entry(frame_textbox, font=('Cambria', 16),bg='#ccccff')
    set_entry0.place(relx=0.77, rely=0.008, width=30)
    set_entry1 = tk.Entry(frame_textbox, font=('Cambria', 16),bg='#ccccff')
    set_entry1.place(relx=0.82, rely=0.008, width=30)
    set_entry2 = tk.Entry(frame_textbox, font=('Cambria', 16),bg='#ccccff')
    set_entry2.place(relx=0.87, rely=0.008, width=30)
    label_pt0 = tk.Label(frame_textbox, text="-", font=('Cambria Black', 18),bg='#ccccff')
    label_pt0.place(relx=0.8045, rely=0.0052)
    label_pt1 = tk.Label(frame_textbox, text="-", font=('Cambria Black', 18),bg='#ccccff')
    label_pt1.place(relx=0.8545, rely=0.0052)


    frame_txtenc = tk.Frame(root,bg='#ccccff')
    frame_txtenc.place(relx=0.505, rely=0.25, relheight=0.8, relwidth=0.49)

    textboxenc = tk.Text(frame_txtenc, width=49, height=10, font=('Cambria', 26),bg='#ccccff')
    textboxenc.place(relx=0, rely=0.05)
    textboxenc.config(state='disabled')

    def copy_text():
        text = textboxenc.get("1.0", tk.END)  
        root.clipboard_clear()  
        root.clipboard_append(text)       
        root.update()    

    copy_button = tk.Button(frame_txtenc, text="COPY Code 📋", font=('Cambria', 10), width=10, height=1, command=copy_text,bg='#4b0082',foreground='#ffffff',cursor='hand2',activebackground='#ccccff',activeforeground='#4b0082')
    copy_button.place(relx=0.9, rely=0.01)


    label2 = tk.Label(frame_txtenc, text="Encrypted text:", font=('Cambria', 18),bg='#ccccff')
    label2.place(x=0.01, y=0)

    #_______________________Buttons Frame____________________
    frame_buttons = tk.Frame(frame_txtenc,bg='#ccccff')
    frame_buttons.place(relx=0.11, rely=0.58, height=125, width=846)

    fram_border = tk.Frame(frame_buttons, bg='black')
    fram_border.place(relx=0, rely=0, relwidth=0.8899, relheight=0.8899)


    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    global selected_letters
    selected_letters = []
    buttons = []
    colors = [
        "#FF0000",  # Red
        "#00FF00",  # Bright Green
        "#0000FF",  # Blue
        "#FFFF00",  # Yellow
        "#FF00FF",  # Magenta
        "#00FFFF",  # Cyan
        "#FFA500",  # Orange
        "#800080",  # Purple
        "#008000",  # Dark Green
        "#FFC0CB",  # Pink
        "#A52A2A",  # Brown
        "#000080",  # Navy
        "#C0C0C0",  # Silver
    ]
    global color_index
    global linked_pairs
    color_index = 0
    linked_pairs = []



    def finder_linked(c):
        global linked_pairs
        for pair in linked_pairs:
            if c in pair and len(linked_pairs)<13:
                return True
            elif c in pair and len(linked_pairs)==13:
                return False
        return False



    def selector(l):
        global selected_letters
        if finder_linked(buttons[l]["text"]) == False and len(linked_pairs) < 13:
            selected_letters.append(buttons[l])
            buttons[l].config(foreground='red')
        elif finder_linked(buttons[l]["text"]) == False and len(linked_pairs) == 13:
            reset_btns()
        if len(selected_letters) == 2:
            if selected_letters[0] != selected_letters[1]:
                linker()
                selected_letters = []
            else:
                selected_letters.pop()


    def reset_btns():
        global color_index, linked_pairs, selected_letters
        for button in buttons:
            button.config(foreground='#ffffff', bg='#11011c')
        color_index = 0
        selected_letters=[] 
        linked_pairs=[]



    def linker():
        global linked_pairs, color_index, selected_letters
        btn1, btn2 = selected_letters
        if color_index < len(colors):
            color = colors[color_index]
            btn1.config(foreground=color)
            btn2.config(foreground=color)
            linked_pairs.append((btn1["text"], btn2["text"]))
            color_index += 1

    def reset():
        global selected_letters, color_index , linked_pairs
        for button in buttons:
            button.config(foreground='#ffffff', bg='#11011c')
        textboxenc.config(state='normal')
        textboxenc.delete('1.0', 'end')
        textboxenc.config(state='disabled')
        textbox.delete('1.0', 'end')
        set_entry0.delete(0, 'end')
        set_entry1.delete(0, 'end')
        set_entry2.delete(0, 'end')
        selected_letters = []
        linked_pairs = []
        color_index = 0

    #_______________________Buttons____________________
    for i in range(len(letters)):
        button = tk.Button(frame_buttons, text=letters[i], font=('Cambria Bold', 16), width=3, height=1, command=lambda l=i: selector(l),background='#11011c', foreground='#ffffff',cursor='spider'
                           ,activebackground='#11011c',activeforeground='#C79FEF',border=3)
        button.grid(row=i//13, column=i%13, padx=5, pady=5)
        buttons.append(button)

    reset_button = tk.Button(frame_textbox, text="RESET ⭮", font=('Cambria Bold', 16), foreground='red', width=10, height=2, command=reset,background='#11011c',cursor='pirate'
                             ,activebackground='#11011c',activeforeground='#C79FEF',border=3)
    reset_button.place(relx=0.65, rely=0.615)

    #_________________enc button_________________________
    enc_button = tk.Button(frame_textbox, text="ENCRYPT 🔒", font=('cambria', 25), width=18, height=2, command=encrypter,
                        background='#11011c', foreground='#ffffff',cursor='hand2',activebackground='#11011c',activeforeground='#C79FEF',border=3,highlightthickness=2)
    enc_button.place(relx=0.292, rely=0.6)

    def enc_shortcut(event):
        if event.state == 12 and event.keysym == 'Return':
            encrypter()


    root.bind('<Return>', enc_shortcut)

    author = tk.Label(root, text="Made by: Oussama EL ATTAOUI", font=('Cambria', 15), foreground='#c48bfc',bg='#ccccff')
    author.place(rely=0.9, relx=0.5,anchor='center')

    linkdin = tk.Button(root, text="www.linkedin.com/in/oussama-el-attaoui-072a12335", font=('Cambria', 15), foreground='#c48bfc',bg='#ccccff',cursor='hand2',
    command=lambda: wb.open("https://www.linkedin.com/in/oussama-el-attaoui-072a12335"), relief='flat', activeforeground='#c48bfc', activebackground='#ccccff',highlightthickness=0
    ,border=0,borderwidth=0)
    linkdin.place(rely=0.95, relx=0.5,anchor='center')

    full_exit = tk.Button(root, text="↪🚪", font=('Andalus', 20), width=4, height=1, foreground="#6013ad",bg='#ccccff',activeforeground='#c48bfc', activebackground='#ccccff',highlightthickness=0
    ,border=0,borderwidth=0,cursor='right_side',padx=20,pady=10,bd=0,command=close_app)
    full_exit.place(relx=0.952,y=0.02)

    root.mainloop()
    return reset







#____________________________DECRYPTION WINDOW_______________________________________________________________________________________

def open_decryption():



    #__________________________ROTORS_________________________________
    R = {
        1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
        11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's',
        20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
    }
    R1={1: 14, 2: 5, 3: 22, 4: 19, 5: 3, 6: 26, 7: 8, 8: 17, 9: 11, 10: 2,
        11: 20, 12: 16, 13: 7, 14: 25, 15: 12, 16: 9, 17: 23, 18: 4, 19: 18,
        20: 6, 21: 21, 22: 10, 23: 15, 24: 13, 25: 24, 26: 1}


    R2 = {1: 1, 2: 14, 3: 5, 4: 22, 5: 19, 6: 3, 7: 26, 8: 8, 9: 17, 10: 11,
        11: 2, 12: 20, 13: 16, 14: 7, 15: 25, 16: 12, 17: 9, 18: 23, 19: 4,
        20: 18, 21: 6, 22: 21, 23: 10, 24: 15, 25: 13, 26: 24}


    R3 = {1: 24, 2: 1, 3: 14, 4: 5, 5: 22, 6: 19, 7: 3, 8: 26, 9: 8, 10: 17,
        11: 11, 12: 2, 13: 20, 14: 16, 15: 7, 16: 25, 17: 12, 18: 9, 19: 23,
        20: 4, 21: 18, 22: 6, 23: 21, 24: 10, 25: 15, 26: 13}


    #__________________________Helper Functions_______________________
    def settings_get(settings):
        flag1 = True
        flag2 = True
        if settings == ['','','']:
            tk.messagebox.showinfo("Settings can't be empty", "Please enter your settings")
            return
        else :
            for x in settings:
                if not x.isdigit():
                    flag1 = False  
                    tk.messagebox.showinfo("Invalid format","Settings should be in d.d.d form only,where d is a number between 1-26")
                    return
        if len(settings) < 3 or len(settings) > 9:
            flag2 = False
            tk.messagebox.showinfo("Settings should be exactly 3 digits")
        flag = flag1 and flag2       
        if flag:
            if '0' not in settings:
                return settings
            else:
                tk.messagebox.showinfo("ZeRoError","Your settings can't include 0, only digits between 1-26 are allowed. Try again.")
                return None          

    def cycler(settings):
        if settings != None :
            x = int(settings[0])-1
            y = int(settings[1])-1
            z = int(settings[2])-1
            R1_set = { (x + i) % 26 + 1: R1[(x + i) % 26 + 1] for i in range(26)}
            R2_set = { (y + i) % 26 + 1: R2[(y + i) % 26 + 1] for i in range(26)}
            R3_set = { (z + i) % 26 + 1: R3[(z + i) % 26 + 1] for i in range(26)}
            return R1_set, R2_set, R3_set


    def get_key_by_value(dictionary, value):
        for key, val in dictionary.items():
            if val == value:
                return key

    def reflector_inv(key, settings):
        s = []
        for u in settings:
            s.append(int(u))
        key = (key -2 - sum(s))%26 +1
        if key < 0 :
            key = key + 26
        else :
            return key

    def enigma_inverse(c, R1_set, R2_set, R3_set, settings):
        L1 = list(R1_set)
        L2 = list(R2_set)
        L3 = list(R3_set)
        key = get_key_by_value(R,c)
        temp= R1_set[key]
        key= R2_set[temp]
        temp= get_key_by_value(R3_set,key)
        key = reflector_inv(temp, settings)
        temp= L3.index(key)+1
        key = get_key_by_value(R2_set,temp)
        temp = L2.index(key)+1
        key = get_key_by_value(R1_set,temp)
        temp = L1.index(key)+1
        c = R[temp]
        return c




    def replacer(c):
        global linked_pairs
        p = c.upper()
        if c.isupper() :
            for pair in linked_pairs:
                if p in pair :
                    return pair[pair.index(p)-1]
        if c.islower():
            for pair in linked_pairs :
                if p in pair :
                    return pair[pair.index(p)-1].lower()
        return c

    def dycrypter():
        settings =[set_entry0.get() , set_entry1.get() , set_entry2.get()]
        settings = settings_get(settings)
        txt = textbox.get('1.0', 'end')
        R1_set, R2_set, R3_set = cycler(settings)
        l = list(txt)
        n = len(l)
        for i in range(n):

            if l[i].isalpha():
                f = l[i].islower()
                l[i]=l[i].lower()
                enc_cara = enigma_inverse(l[i], R1_set, R2_set, R3_set, settings)
                if f :
                    l[i] = enc_cara
                else :
                    l[i] = enc_cara.upper()
                x = i + 1
                l[i]=replacer(l[i])
                R1_set, R2_set, R3_set = cycler([x, (x//10)+1, (x//100)+1])    
        l = ''.join(l)
        textboxenc.config(state='normal')
        textboxenc.delete('1.0', 'end')
        textboxenc.insert('1.0', l)
        textboxenc.config(state='disabled')


    #_______________________GUI Setup____________________
    root = tk.Tk()
    root.title("E N I G M A")
    root.attributes('-fullscreen', True)
    root.iconbitmap('enigma.ico')
    root.config(background='#ccccff')

    label = tk.Label(root, text="E N I G M A", font=('Andalus', 80), foreground='#6013ad',bg='#ccccff')
    label.place(relx=0.354, rely=0.05)

    def exit_fullscreen(event=None):
        root.attributes('-fullscreen', False)

    def close_app(event=None):
        root.destroy()

    root.bind('<Escape>', exit_fullscreen)
    root.bind('<Shift-Escape>', close_app)

    #_______________________Textbox____________________
    frame_textbox = tk.Frame(root,bg='#ccccff')
    frame_textbox.place(relx=0.005, rely=0.25, relheight=0.8, relwidth=0.49)

    textbox = tk.Text(frame_textbox,bg='#ccccff', width=49, height=10, font=('Cambria', 26))
    textbox.place(relx=0, rely=0.05)

    def Clear():
        textbox.delete('1.0', 'end')


    clear_button = tk.Button(frame_textbox, text="X", font=('Cambria', 10), width=2, height=1, command=Clear,bg='#4b0082',foreground='#ffffff',cursor='hand2',activebackground='#ccccff',activeforeground='#4b0082')
    clear_button.place(relx=0.965, rely=0.012)



    label1 = tk.Label(frame_textbox, text="Text to be encrypted:", font=('Cambria', 18),bg='#ccccff')
    label1.place(x=0.01, y=0)

    label_set = tk.Label(frame_textbox, text="Enter your settings:", font=('Cambria', 18),bg='#ccccff')
    label_set.place(relx=0.54, rely=0)

    set_entry0 = tk.Entry(frame_textbox, font=('Cambria', 16),bg='#ccccff')
    set_entry0.place(relx=0.77, rely=0.008, width=30)
    set_entry1 = tk.Entry(frame_textbox, font=('Cambria', 16),bg='#ccccff')
    set_entry1.place(relx=0.82, rely=0.008, width=30)
    set_entry2 = tk.Entry(frame_textbox, font=('Cambria', 16),bg='#ccccff')
    set_entry2.place(relx=0.87, rely=0.008, width=30)
    label_pt0 = tk.Label(frame_textbox, text="-", font=('Cambria Black', 18),bg='#ccccff')
    label_pt0.place(relx=0.8045, rely=0.0052)
    label_pt1 = tk.Label(frame_textbox, text="-", font=('Cambria Black', 18),bg='#ccccff')
    label_pt1.place(relx=0.8545, rely=0.0052)


    frame_txtenc = tk.Frame(root,bg='#ccccff')
    frame_txtenc.place(relx=0.505, rely=0.25, relheight=0.8, relwidth=0.49)

    textboxenc = tk.Text(frame_txtenc, width=49, height=10, font=('Cambria', 26),bg='#ccccff')
    textboxenc.place(relx=0, rely=0.05)
    textboxenc.config(state='disabled')

    def copy_text():
        text = textboxenc.get("1.0", tk.END)  
        root.clipboard_clear()  
        root.clipboard_append(text)       
        root.update()    

    copy_button = tk.Button(frame_txtenc, text="COPY Code 📋", font=('Cambria', 10), width=10, height=1, command=copy_text,bg='#4b0082',foreground='#ffffff',cursor='hand2',activebackground='#ccccff',activeforeground='#4b0082')
    copy_button.place(relx=0.9, rely=0.01)


    label2 = tk.Label(frame_txtenc, text="Encrypted text:", font=('Cambria', 18),bg='#ccccff')
    label2.place(x=0.01, y=0)

    #_______________________Buttons Frame____________________
    frame_buttons = tk.Frame(frame_txtenc,bg='#ccccff')
    frame_buttons.place(relx=0.11, rely=0.58, height=125, width=846)

    fram_border = tk.Frame(frame_buttons, bg='black')
    fram_border.place(relx=0, rely=0, relwidth=0.8899, relheight=0.8899)


    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    global selected_letters
    selected_letters = []
    buttons = []
    colors = [
        "#FF0000",  # Red
        "#00FF00",  # Bright Green
        "#0000FF",  # Blue
        "#FFFF00",  # Yellow
        "#FF00FF",  # Magenta
        "#00FFFF",  # Cyan
        "#FFA500",  # Orange
        "#800080",  # Purple
        "#008000",  # Dark Green
        "#FFC0CB",  # Pink
        "#A52A2A",  # Brown
        "#000080",  # Navy
        "#C0C0C0",  # Silver
    ]
    
    global color_index
    global linked_pairs
    
    color_index = 0
    linked_pairs = []

    def finder_linked(c):
        global linked_pairs
        for pair in linked_pairs:
            if c in pair and len(linked_pairs)<13:
                return True
            elif c in pair and len(linked_pairs)==13:
                return False
        return False



    def selector(l):
        global selected_letters
        if finder_linked(buttons[l]["text"]) == False and len(linked_pairs) < 13:
            selected_letters.append(buttons[l])
            buttons[l].config(foreground='red')
        elif finder_linked(buttons[l]["text"]) == False and len(linked_pairs) == 13:
            reset_btns()
        if len(selected_letters) == 2:
            if selected_letters[0] != selected_letters[1]:
                linker()
                selected_letters = []
            else:
                selected_letters.pop()


    def reset_btns():
        global color_index, linked_pairs, selected_letters
        for button in buttons:
            button.config(foreground='#ffffff', bg='#11011c')
        color_index = 0
        selected_letters=[] 
        linked_pairs=[]



    def linker():
        global linked_pairs, color_index, selected_letters
        btn1, btn2 = selected_letters
        if color_index < len(colors):
            color = colors[color_index]
            btn1.config(foreground=color)
            btn2.config(foreground=color)
            linked_pairs.append((btn1["text"], btn2["text"]))
            color_index += 1

    def reset_dec():
        global selected_letters, color_index , linked_pairs
        for button in buttons:
            button.config(foreground='#ffffff', bg='#11011c')
        textboxenc.config(state='normal')
        textboxenc.delete('1.0', 'end')
        textboxenc.config(state='disabled')
        textbox.delete('1.0', 'end')
        set_entry0.delete(0, 'end')
        set_entry1.delete(0, 'end')
        set_entry2.delete(0, 'end')
        selected_letters = []
        linked_pairs = []
        color_index = 0

    #_______________________Buttons____________________
    for i in range(len(letters)):
        button = tk.Button(frame_buttons, text=letters[i], font=('Cambria Bold', 16), width=3, height=1, command=lambda l=i: selector(l),background='#11011c', foreground='#ffffff',cursor='spider'
                           ,activebackground='#11011c',activeforeground='#C79FEF',border=3)
        button.grid(row=i//13, column=i%13, padx=5, pady=5)
        buttons.append(button)

    reset_button = tk.Button(frame_textbox, text="RESET ⭮", font=('Cambria Bold', 16), foreground='red', width=10, height=2, command=reset_dec,background='#11011c',cursor='pirate'
                             ,activebackground='#11011c',activeforeground='red',border=3)
    reset_button.place(relx=0.65, rely=0.615)




    #_______________________Encrypt Button____________________
    dyc_button = tk.Button(frame_textbox, text="DYCRYPT 🔑", font=('cambria', 25), width=18, height=2, command=dycrypter,
                        background='#11011c', foreground='#ffffff',cursor='hand2',activebackground='#11011c',activeforeground='#4b0082',border=3,highlightthickness=2)
    dyc_button.place(relx=0.292, rely=0.6)

    def enc_shortcut(event):
        if event.state == 12 and event.keysym == 'Return':
            dycrypter()


    root.bind('<Return>', enc_shortcut)

    author = tk.Label(root, text="Made by: Oussama EL ATTAOUI", font=('Cambria', 15), foreground='#c48bfc',bg='#ccccff')
    author.place(rely=0.9, relx=0.5,anchor='center')

    linkdin = tk.Button(root, text="www.linkedin.com/in/oussama-el-attaoui-072a12335", font=('Cambria', 15), foreground='#c48bfc',bg='#ccccff',cursor='hand2',
    command=lambda: wb.open("https://www.linkedin.com/in/oussama-el-attaoui-072a12335"), relief='flat', activeforeground='#4b0082', activebackground='#ccccff',highlightthickness=0
    ,border=0,borderwidth=0)
    linkdin.place(rely=0.95, relx=0.5,anchor='center')


    full_exit = tk.Button(root, text="↪🚪", font=('Andalus', 20), width=4, height=1, foreground="#6013ad",bg='#ccccff',activeforeground='#c48bfc', activebackground='#ccccff',highlightthickness=0
    ,border=0,borderwidth=0,cursor='right_side',padx=20,pady=10,bd=0,command=close_app)
    full_exit.place(relx=0.952,y=0.02)

    root.mainloop()
    return reset_dec

button1 = tk.Button(main_window,text="ENCRYPTION",background='#ccccff',font=('cambria', 25), width=14, height=2, command=open_encryption,
                         bg='#000000',foreground='#ffffff',cursor='hand2',activebackground='#000000',activeforeground='#000000',relief="raised",highlightthickness=3)
button1.place(relx=0.35, rely=0.6,anchor='center')
button2 = tk.Button(main_window,text="DYCRYPTION",background='#ccccff',font=('cambria', 25), width=14, height=2, command=open_decryption,
                         bg='#000000',foreground='#ffffff',cursor='hand2',activebackground='#000000',activeforeground='#000000',relief="raised",highlightthickness=3)
button2.place(relx=0.65, rely=0.6,anchor='center')
main_window.mainloop()