import tkinter as tk
import random

my_font = ("Consolas",50)
button_layout = [
   [" ", " ", " "],
   [" ", " ", " "],
   [" ", " ", " "] 
]

players = ["x", "o"]
player_on_turn = random.choice(players)

def empty_spaces():
    empty_spaces_count = 9
    for r_i, row in enumerate(button_layout):
        for c_i, button_text in enumerate(row):
            if button_layout[r_i][c_i]["text"] != " ":
                empty_spaces_count -= 1
    if empty_spaces_count == 0:
        return False
    else:
        pass

def check_winner():
    for r_i, row in enumerate(button_layout):
        if button_layout[r_i][0]["text"] == button_layout[r_i][1]["text"] == button_layout[r_i][2]["text"] != " ":
            button_layout[r_i][0].config(bg="green")
            button_layout[r_i][1].config(bg="green")
            button_layout[r_i][2].config(bg="green")
            return True
    
    for c_i, column in enumerate(button_layout):
        if button_layout[0][c_i]["text"] == button_layout[1][c_i]["text"] == button_layout[2][c_i]["text"] != " ":
            button_layout[0][c_i].config(bg="green")
            button_layout[1][c_i].config(bg="green")
            button_layout[2][c_i].config(bg="green")
            return True
    
    if button_layout[0][0]["text"] == button_layout[1][1]["text"] == button_layout[2][2]["text"] != " ":
        button_layout[0][0].config(bg="green")
        button_layout[1][1].config(bg="green")
        button_layout[2][2].config(bg="green")
        return True

    elif button_layout[0][2]["text"] == button_layout[1][1]["text"] == button_layout[2][0]["text"] != " ":
        button_layout[0][2].config(bg="green")
        button_layout[1][1].config(bg="green")
        button_layout[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:
        for r_i, row in enumerate(button_layout):
            for c_i, button_text in enumerate(row):
                button_layout[r_i][c_i].config(bg="yellow")
        return "tie"   
    else:
        return False

def next_turn(r_i, c_i):
    global player_on_turn

    if button_layout[r_i][c_i]["text"] == " " and check_winner() is False:
        if player_on_turn == players[0]:
            button_layout[r_i][c_i]["text"] = player_on_turn     
            if check_winner() is False:
                player_on_turn = players[1]
                info_label.config(text="turn "+player_on_turn)
            elif check_winner() is True:
                info_label.config(text=player_on_turn+" wins")
                player_on_turn = None
            elif check_winner() == "tie":
                info_label.config(text="tie")
                player_on_turn = None
        else:
            button_layout[r_i][c_i]["text"] = player_on_turn
            if check_winner() is False:
                player_on_turn = players[0]
                info_label.config(text="turn "+player_on_turn)
            elif check_winner() is True:
                info_label.config(text=player_on_turn+" wins")
                player_on_turn = None
            elif check_winner() == "tie":
                info_label.config(text="tie")
                player_on_turn = None
    

def create_buttons():
    for r_i, row in enumerate(button_layout):
        for c_i, button_text in enumerate(row):
            button_layout[r_i][c_i] = tk.Button(window, text=button_text, bg="white", font=my_font, command=lambda r_i=r_i, c_i=c_i: next_turn(r_i, c_i))
            button_layout[r_i][c_i].grid(row=r_i, column=c_i)

def reset():
    global player_on_turn
    for r_i, row in enumerate(button_layout):
        for c_i, button_text in enumerate(row):
            button_layout[r_i][c_i].config(text=" ", bg="white")
    
    player_on_turn = random.choice(players)
    info_label.config(text="turn "+player_on_turn)

window = tk.Tk()
window.title("PIŠKVORKY")
window.config(bg="white")
info_label = tk.Label(window, font=my_font, text="turn " + player_on_turn, bg="white")
info_label.grid(row=3, columnspan=3)
create_buttons()
tk.Button(window, text="reset", bg="red", font=my_font, command=reset).grid(row=4, columnspan=3)



window.mainloop()
print(button_layout) #tohle ukáže, že list button_layout obsahuje objekty button1-9
