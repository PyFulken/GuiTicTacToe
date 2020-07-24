from tkinter import *
from tkinter import ttk
from random import randrange

counter = 0
player1_piece = ""
player2_piece = ""
player1_victory = 0
player2_victory = 0
pieces_placed = 0
random_var = None
turn = ""
board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
board_buttons = []
button_placement_iterator = 1

root = Tk()
root.title("Fulken's TicTactoe")
root.geometry("450x450")
root.resizable(width="False", height="False")
root.iconbitmap("X.ico")

label_welcome = ttk.Label(root, text="Welcome to Fulken's TicTacToe!", justify="center", font="arial 20 bold", wrap=350)
label_welcome.place(x=90, y=13)
label_player1_name = ttk.Label(root, text="Player 1's name?", justify="center", font="arial 10 bold", wrap=350)
label_player2_name = ttk.Label(root, text="Player 2's name?", justify="center", font="arial 10 bold", wrap=350)
label_piece_roll2 = ttk.Label(root, justify="center", font="arial 10 bold")
label_piece_roll1 = ttk.Label(root, justify="center", font="arial 10 bold")
label_player_turn = ttk.Label(root, justify="center", font="arial 20 bold", wrap=350)
entry_player1_name = ttk.Entry(root, width=30, justify='center')
entry_player2_name = ttk.Entry(root, width=30, justify='center')
label_win_count = ttk.Label(root, justify="center", font="arial 10 bold", wrap=350)
button_start_play = ttk.Button(root, text="Start the game!")
button_start_play.place(relx=0.5, rely=0.5, anchor="center")
button_start_play2 = ttk.Button(root, text="Play!")
frame_game = ttk.Frame(root, height=300, width=300, relief="ridge")
button_restart = ttk.Button(root, text="Replay!")


def piece_roll2():
    global counter
    global player1_piece
    global player2_piece
    button_start_play2.config(command=tic_tac_toe_setup)
    if random_var == 0 and counter <= 80:
        if counter % 2 == 0:
            label_piece_roll2.config(text="X")
            label_piece_roll2.place(relx=0.5, rely=0.60, anchor="center")
            counter += 1
            root.after(int(counter * counter / 70), piece_roll2)
        elif counter % 2 == 1:
            label_piece_roll2.config(text="O")
            label_piece_roll2.place(relx=0.5, rely=0.60, anchor="center")
            counter += 1
            root.after(int(counter * counter / 70), piece_roll2)
    elif random_var == 1 and counter <= 80:
        if counter % 2 == 1:
            label_piece_roll2.config(text="X")
            label_piece_roll2.place(relx=0.5, rely=0.60, anchor="center")
            counter += 1
            root.after(int(counter * counter / 70), piece_roll2)
        elif counter % 2 == 0:
            label_piece_roll2.config(text="O")
            label_piece_roll2.place(relx=0.5, rely=0.60, anchor="center")
            counter += 1
            root.after(int(counter * counter / 70), piece_roll2)
    elif random_var == 0 and counter > 80:
        label_piece_roll2.config(text="-> X <-")
        label_piece_roll2.place(relx=0.5, rely=0.60, anchor="center")
        player1_piece = "X"
        player2_piece = "O"
        print(player1_piece)
        button_start_play2.place(relx=0.5, rely=0.65, anchor="center")
    elif random_var == 1 and counter > 80:
        label_piece_roll2.config(text="-> O <-")
        label_piece_roll2.place(relx=0.5, rely=0.60, anchor="center")
        player1_piece = "O"
        player2_piece = "X"
        print(player1_piece)
        button_start_play2.place(relx=0.5, rely=0.65, anchor="center")


def piece_roll1(event):
    global random_var
    label_piece_roll1.config(text=f"{player1_name_entry()}'s piece will be:")
    label_piece_roll1.place(relx=0.5, rely=0.55, anchor="center")
    entry_player2_name.config(state="disabled")
    random_var = randrange(0, 2, 1)
    piece_roll2()


def player2_name_entry(event):
    entry_player2_name.focus_set()
    label_player2_name.place(relx=0.5, rely=0.45, anchor="center")
    entry_player2_name.place(relx=0.5, rely=0.50, anchor="center")
    entry_player2_name.bind('<Return>', piece_roll1)
    entry_player1_name.config(state="disabled")
    return entry_player2_name.get()


def player1_name_entry():
    button_start_play.place_forget()
    entry_player1_name.focus_set()
    label_player1_name.place(relx=0.5, rely=0.35, anchor="center")
    entry_player1_name.place(relx=0.5, rely=0.40, anchor="center")
    entry_player1_name.bind('<Return>', player2_name_entry)
    return entry_player1_name.get()


for i in range(10):
    board_buttons.append(Button(frame_game, height=5, width=10, text=i))


def tic_tac_toe_setup():
    global random_var
    global turn
    global button_placement_iterator
    label_win_count.config(
        text=f"Victories:\n{player1_name_entry()}: {player1_victory} \t{player2_name_entry(1)}: {player2_victory}")
    label_win_count.place(relx=0.5, y=400, anchor="center")
    label_player1_name.place_forget()
    entry_player1_name.place_forget()
    label_player2_name.place_forget()
    entry_player2_name.place_forget()
    label_piece_roll2.place_forget()
    button_start_play2.place_forget()
    label_piece_roll1.place_forget()
    label_welcome.place_forget()
    random_var = randrange(0, 2, 1)
    if random_var == 0:
        label_player_turn.config(text=f"It's {player2_name_entry(1)}'s turn!")
        turn = 2
    elif random_var == 1:
        label_player_turn.config(text=f"It's {player1_name_entry()}'s turn!")
        turn = 1
        label_player1_name.place_forget()
        entry_player1_name.place_forget()
    label_player_turn.place(relx=0.5, rely=0.1, anchor="center")
    label_win_count.place(relx=0.5, y=400, anchor="center")
    frame_game.place(relx=0.5, rely=0.5, anchor="center")
    for i2 in range(0, 3):
        for j2 in range(0, 3):
            board_buttons[button_placement_iterator].grid(row=i2, column=j2, sticky=N + E + S + W)
            button_placement_iterator += 1


def restart():
    global counter
    global player1_piece
    global player2_piece
    global random_var
    global turn
    global board
    global board_buttons
    global button_placement_iterator
    global pieces_placed
    counter = 0
    random_var = None
    turn = ""
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    button_placement_iterator = 1
    pieces_placed = 0
    for deletebuttons in range(len(board_buttons)):
        board_buttons[0].destroy()
    board_buttons = []
    for restart1 in range(10):
        board_buttons.append(Button(frame_game, height=5, width=10, text=restart1))
        board_buttons[restart1].config(command=lambda x=restart1: piece_placement(x))
    label_player1_name.place_forget()
    label_player2_name.place_forget()
    label_piece_roll2.place_forget()
    label_piece_roll1.place_forget()
    label_player_turn.place_forget()
    entry_player1_name.place_forget()
    entry_player2_name.place_forget()
    frame_game.place_forget()
    button_restart.place_forget()
    label_win_count.place(relx=0.5, y=400, anchor="center")
    tic_tac_toe_setup()


def victory_check():
    global player1_victory
    global player2_victory
    if board[1] == board[2] == board[3] or board[4] == board[5] == board[6] or board[7] == board[8] == board[9] or \
            board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or board[3] == board[6] == board[9] \
            or board[1] == board[5] == board[9] or board[3] == board[5] == board[7]:
        for what in range(10):
            board_buttons[what].config(state="disabled")
        if turn % 2 != 0:
            player1_victory += 1
            label_player_turn.config(text=f"{player1_name_entry()} wins!")
            label_player_turn.place(relx=0.5, rely=0.1, anchor="center")
            label_win_count.config(
                text=f"Victories:\n{player1_name_entry()}: {player1_victory} \t{player2_name_entry(1)}: {player2_victory}")
            label_win_count.place(relx=0.5, y=400, anchor="center")
        elif turn % 2 == 0:
            player2_victory += 1
            label_player_turn.config(text=f"{player2_name_entry(1)} wins!")
            label_player_turn.place(relx=0.5, rely=0.1, anchor="center")
            label_win_count.config(
                text=f"Victories:\n{player1_name_entry()}: {player1_victory} \t{player2_name_entry(1)}: {player2_victory}")
            label_win_count.place(relx=0.5, y=400, anchor="center")
        button_restart.config(command=restart)
        button_restart.place(relx=0.5, rely=0.5, anchor="center")
        return True


def piece_placement(x):
    global turn
    global pieces_placed
    if turn % 2 != 0 and pieces_placed < 8:
        board_buttons[x].config(text=player1_piece, state="disabled")
        board[x] = player1_piece
        if victory_check():
            pass
        else:
            label_player_turn.config(text=f"It's {player2_name_entry(1)}'s turn!")
            label_player_turn.place(relx=0.5, rely=0.1, anchor="center")
            turn += 1
            pieces_placed += 1
    elif turn % 2 == 0 and pieces_placed < 8:
        board_buttons[x].config(text=player2_piece, state="disabled")
        board[x] = player2_piece
        if victory_check():
            pass
        else:
            label_player_turn.config(text=f"It's {player1_name_entry()}'s turn!")
            label_player_turn.place(relx=0.5, rely=0.1, anchor="center")
            turn += 1
            pieces_placed += 1
    elif pieces_placed == 8:
        label_player_turn.config(text="No one wins.....")
        label_player_turn.place(relx=0.5, rely=0.1, anchor="center")
        button_restart.config(command=restart)
        button_restart.place(relx=0.5, rely=0.5, anchor="center")


button_start_play.config(command=player1_name_entry)
for i3 in range(10):
    board_buttons[i3].config(command=lambda x=i3: piece_placement(x))
key_sequence = []
key_stroke = 0
konamicode = ["Up", "Up", "Down", "Down", "Left", "Right", "Left", "Right", "b", "a", "Return"]


def konami_code(event):
    global key_sequence
    global key_stroke
    key_sequence.append(event.keysym)
    print(key_sequence)
    print(len(key_sequence))
    if key_sequence == konamicode:
        print("Konami code pressed!")
        key_stroke = 0
    elif key_sequence[key_stroke] != konamicode[key_stroke]:
        key_sequence = []
        key_stroke = 0
    elif len(key_sequence) > 10:
        key_sequence = []
        key_stroke = 0
    key_stroke += 1


root.bind("<KeyPress>", konami_code)
root.mainloop()
