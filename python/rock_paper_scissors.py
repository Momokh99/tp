"""Graphical Rock Paper Scissors game with scoreboard and recent-round history."""
import random
import tkinter as tk
from tkinter import ttk
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'tie'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return 'player'
    else:
        return 'computer'

class RockPaperScissorsApp:
    """Encapsulates the Tkinter UI and game state."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("460x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f7fb")

        self.player_score = 0
        self.computer_score = 0

        self.status_var = tk.StringVar(value="Make your move to start playing!")
        self.computer_choice_var = tk.StringVar(value="Computer hasn't played yet.")
        self.player_score_var = tk.StringVar()
        self.computer_score_var = tk.StringVar()

        self._build_layout()
        self._update_scoreboard()

    def _build_layout(self) -> None:
        style = ttk.Style(self.root)
        style.configure("Main.TFrame", background="#f5f7fb")
        style.configure("Title.TLabel", font=("Helvetica", 20, "bold"), background="#f5f7fb")
        style.configure("Score.TLabel", font=("Helvetica", 16, "bold"), background="#f5f7fb")
        style.configure("Status.TLabel", font=("Helvetica", 14), background="#f5f7fb")
        style.configure("Choice.TButton", font=("Helvetica", 12), padding=12)

        main_frame = ttk.Frame(self.root, style="Main.TFrame", padding=20)
        main_frame.pack(fill="both", expand=True)

        title_label = ttk.Label(main_frame, text="Rock Paper Scissors", style="Title.TLabel")
        title_label.pack(pady=(0, 10))

        instructions = ttk.Label(
            main_frame,
            text="Choose Rock, Paper, or Scissors. First to outscore wins!",
            style="Status.TLabel"
        )
        instructions.pack(pady=(0, 15))

        scoreboard = ttk.Frame(main_frame, style="Main.TFrame")
        scoreboard.pack(fill="x", pady=(0, 15))
        player_label = ttk.Label(scoreboard, textvariable=self.player_score_var, style="Score.TLabel")
        player_label.pack(side="left", expand=True)
        computer_label = ttk.Label(scoreboard, textvariable=self.computer_score_var, style="Score.TLabel")
        computer_label.pack(side="right", expand=True)

        choice_frame = ttk.Frame(main_frame, style="Main.TFrame")
        choice_frame.pack(fill="x")
        for idx, choice in enumerate(("rock", "paper", "scissors")):
            button = ttk.Button(
                choice_frame,
                text=choice.title(),
                style="Choice.TButton",
                command=lambda c=choice: self.play_round(c)
            )
            button.grid(row=0, column=idx, padx=5, sticky="ew")
            choice_frame.columnconfigure(idx, weight=1)

        status_frame = ttk.Frame(main_frame, style="Main.TFrame")
        status_frame.pack(fill="x", pady=15)
        computer_choice_label = ttk.Label(
            status_frame,
            textvariable=self.computer_choice_var,
            style="Status.TLabel"
        )
        computer_choice_label.pack(anchor="center")
        result_label = ttk.Label(status_frame, textvariable=self.status_var, style="Status.TLabel")
        result_label.pack(anchor="center", pady=(8, 0))

        history_frame = ttk.Frame(main_frame, style="Main.TFrame")
        history_frame.pack(fill="both", expand=True, pady=(10, 0))
        history_title = ttk.Label(history_frame, text="Recent rounds:", style="Status.TLabel")
        history_title.pack(anchor="w")
        self.history_list = tk.Listbox(
            history_frame,
            height=5,
            font=("Courier", 11),
            activestyle="none",
            borderwidth=0,
            highlightthickness=1,
            highlightcolor="#c3d4ff",
            relief="solid"
        )
        self.history_list.pack(fill="both", expand=True, pady=(4, 0))

        controls = ttk.Frame(main_frame, style="Main.TFrame")
        controls.pack(fill="x", pady=(15, 0))
        reset_btn = ttk.Button(controls, text="Reset Score", command=self.reset_scores)
        reset_btn.pack(side="left", expand=True, fill="x", padx=(0, 5))
        quit_btn = ttk.Button(controls, text="Quit", command=self.quit_game)
        quit_btn.pack(side="left", expand=True, fill="x", padx=(5, 0))

    def play_round(self, player_choice: str) -> None:
        computer_choice = get_computer_choice()
        self.computer_choice_var.set(f"Computer chose {computer_choice.title()}.")

        winner = determine_winner(player_choice, computer_choice)
        if winner == 'player':
            self.player_score += 1
            self.status_var.set(f"You win this round! {player_choice.title()} beats {computer_choice.title()}.")
        elif winner == 'computer':
            self.computer_score += 1
            self.status_var.set(f"Computer wins! {computer_choice.title()} beats {player_choice.title()}.")
        else:
            self.status_var.set("It's a tie! Try again.")

        self._update_scoreboard()
        self._record_history(player_choice, computer_choice, winner)

    def reset_scores(self) -> None:
        self.player_score = 0
        self.computer_score = 0
        self.status_var.set("Scores reset. Ready when you are!")
        self.computer_choice_var.set("Computer hasn't played yet.")
        self.history_list.delete(0, tk.END)
        self._update_scoreboard()

    def quit_game(self) -> None:
        self.root.destroy()

    def _update_scoreboard(self) -> None:
        self.player_score_var.set(f"You: {self.player_score}")
        self.computer_score_var.set(f"Computer: {self.computer_score}")

    def _record_history(self, player_choice: str, computer_choice: str, winner: str) -> None:
        if winner == 'tie':
            result_text = "Tie"
        elif winner == 'player':
            result_text = "You won"
        else:
            result_text = "Computer won"
        summary = (
            f"You {player_choice.title():<9} | "
            f"Computer {computer_choice.title():<9} -> {result_text}"
        )
        self.history_list.insert(0, summary)
        if self.history_list.size() > 6:
            self.history_list.delete(tk.END)


def main() -> None:
    root = tk.Tk()
    RockPaperScissorsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
