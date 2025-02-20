import random

class RockPaperScissors:
    def __init__(self, total_rounds):
        self.total_rounds = total_rounds
        self.current_round = 0
        self.user_wins = 0
        self.computer_wins = 0
        self.choices = ["rock", "paper", "scissors"]
    
    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "draw"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            self.user_wins += 1
            return "user"
        else:
            self.computer_wins += 1
            return "computer"
    
    def has_winner(self):
        return self.user_wins > self.total_rounds // 2 or self.computer_wins > self.total_rounds // 2
    
    def play_game(self):
        while self.current_round < self.total_rounds:
            self.current_round += 1
            print(f"Round {self.current_round}:")
            user_choice = input("Choose rock, paper, or scissors: ").lower()
            while user_choice not in self.choices:
                print("Invalid choice, try again.")
                user_choice = input("Choose rock, paper, or scissors: ").lower()
            
            computer_choice = self.get_computer_choice()
            print(f"Computer chose: {computer_choice}")
            
            winner = self.winner(user_choice, computer_choice)
            if winner == "draw":
                print("It's a draw!")
            elif winner == "user":
                print("You win this round!")
            else:
                print("Computer wins this round!")
            
            if self.has_winner():
                break
        
        print("Game Over!")
        if self.user_wins > self.computer_wins:
            print("Congratulations! You won the game!")
        elif self.computer_wins > self.user_wins:
            print("Computer wins the game! Better luck next time.")
        else:
            print("It's a tie!")

# Example usage
total_rounds = int(input("Enter number of rounds: "))
game = RockPaperScissors(total_rounds)
game.play_game()
