import random
import sys

class BlackjackGame:
    """Primitive Blackjack game with a simple command-line interface by AITMAD Python Developer."""
    def __init__(self):
        self.cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
        self.player_wins = 0
        self.computer_wins = 0
        self.draws = 0

    def deal_card(self):
        return random.choice(self.cards)

    def calculate_score(self, hand):
        score = sum(hand)

        # Handle Ace logic
        while score > 21 and 11 in hand:
            hand[hand.index(11)] = 1
            score = sum(hand)

        return score

    def display(self, player, computer, hide=True):
        print("" + "="*40)
        print("🃏  BLACKJACK 21 GAME")
        print("="*40)

        if hide:
            print(f"🤖 Computer: [{computer[0]}, ?]")
        else:
            print(f"🤖 Computer: {computer} | Score: {self.calculate_score(computer)}")

        print(f"👤 Player  : {player} | Score: {self.calculate_score(player)}")
        print("="*40)

    def show_scoreboard(self):
        print("📊 SCOREBOARD")
        print("-"*30)
        print(f"🏆 Player Wins   : {self.player_wins}")
        print(f"🤖 Computer Wins : {self.computer_wins}")
        print(f"🤝 Draws         : {self.draws}")
        print("-"*30)

    def get_player_choice(self):
        """Safe input handling."""
        while True:
            choice = input("👉 Hit (h) or Stand (s): ").strip().lower()
            if choice in ["h", "s"]:
                return choice
            print("⚠️ Invalid input! Please type 'h' or 's'.")

    def play_round(self):
        player = [self.deal_card(), self.deal_card()]
        computer = [self.deal_card(), self.deal_card()]

        while True:
            self.display(player, computer)

            player_score = self.calculate_score(player)

            if player_score > 21:
                print("💥 You busted! Computer wins.")
                self.computer_wins += 1
                return

            choice = self.get_player_choice()

            if choice == "h":
                player.append(self.deal_card())
            else:
                break

        while self.calculate_score(computer) < 17:
            computer.append(self.deal_card())

        self.display(player, computer, hide=False)

        player_score = self.calculate_score(player)
        computer_score = self.calculate_score(computer)

        if computer_score > 21 or player_score > computer_score:
            print("🎉 You win!")
            self.player_wins += 1
        elif player_score < computer_score:
            print("😢 Computer wins!")
            self.computer_wins += 1
        else:
            print("🤝 It's a draw!")
            self.draws += 1

    def start(self):
        print("🎮 Welcome to Blackjack 21!\n")

        while True:
            try:
                self.play_round()
                self.show_scoreboard()

                again = input("🔁 Play again? (y/n): ").lower()

                if again != "y":
                    print("👋 Thanks for playing!")
                    sys.exit()

            except KeyboardInterrupt:
                print("⚠️ Game interrupted. Exiting safely.")
                sys.exit()


if __name__ == "__main__":
    game = BlackjackGame()
    game.start()