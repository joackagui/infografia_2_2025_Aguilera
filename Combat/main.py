import random
import character

class Main:
    def __init__(self):
        self.players = 0
        self.players_list = []
        self.roles_list = [character.Warrior(), 
                           character.Wizard(), 
                           character.Tank(), 
                           character.Archer()]

    def start(self):
        self.greeting()
        self.definePlayers()
        self.showRoles()
        self.characterSelection()
        self.showRules()
        self.battle()

    def greeting(self):
        print("========= Welcome to the battle arena =========\n")
        input("Press Enter to start the battle...\n")

    def definePlayers(self):
        print("========= Number of Players =========\n")
        while True:
            num = input("Insert the number of players: ")
            if num.isdigit() and int(num) >= 2:
                self.players = int(num)
                break
            else:
                print("❌ Invalid number of players. Please enter a number greater than 1.\n")
        
        

    def showRoles(self):
        print("========= Roles =========\n")
        for i, role in enumerate(self.roles_list):
            print(f"({i+1}) Role: {role.role}, Hp: {role.hp}, Damage: {role.damage}")
        input("Press Enter to continue...\n")

    def characterSelection(self):
        print("========= Player Setup =========\n")
        for i in range(self.players):
            name = input(f"\nInsert the name of player {i+1}: ").strip()
            
            while True:
                role_input = input(f"Choose role number for {name}: ").strip()
                if role_input.isdigit():
                    role_index = int(role_input) - 1
                    if 0 <= role_index < len(self.roles_list):
                        break
                print("❌ Invalid role number. Please choose a number between 1 and 4.")

            selected_role = type(self.roles_list[role_index])
            player_character = selected_role(name)
            self.players_list.append(player_character)
            print(f"✅ {name} has chosen {player_character.role}.\n")

        input("Press Enter to continue...\n")

    def showRules(self):
        print("========= Rules =========")
        print("- Select your opponent when it's your turn.")
        print("- Type 'power up' once per game to use your special ability.")
        print("- The game ends when only one character remains standing.\n")
        input("Press Enter to continue...\n")

    def battle(self):
        print("The battle begins!")

        round_num = 1
        while len(self.players_list) > 1:
            print(f"\n========= ROUND {round_num} =========")
            round_num += 1

            print("Player Status:")
            for player in self.players_list:
                print(f"- {player.name} ({player.role}) - HP: {player.hp}")
            
            input("Press Enter to continue...\n")

            random.shuffle(self.players_list)

            print("The order of this round will be: ")
            for player in self.players_list:
                print(f"- {player.name} ({player.role})")

            
            for current_player in list(self.players_list):
                if current_player.hp <= 0:
                    continue

                print(f"\nIt's {current_player.name}'s turn ({current_player.role})!")

                while True:
                    action = input("Type the name of your target or 'power up': ").strip().lower()

                    if action == "power up":
                        self.handlePowerUp(current_player)
                        break

                    target = None
                    for p in self.players_list:
                        if p.name.lower() == action and p != current_player:
                            target = p
                            break

                    if target:
                        current_player.attack(target)
                        break
                    else:
                        print("❌ Invalid target. Try again.")
            
            alive_players = []
            for p in self.players_list:
                if p.hp > 0:
                    alive_players.append(p)
            self.players_list = alive_players


        winner = self.players_list[0]
        print(f"\n🏆 {winner.name} ({winner.role}) is the last one standing!\n")
        input("Would you like to play again? (yes/no): ")
        while True:
            if input().strip().lower() == "yes":
                self.start()
                break
            elif input().strip().lower() == "no":
                print("Thanks for playing! Goodbye!")
                break
            else:
                print("❌ Invalid input. Please type 'yes' or 'no'.")

    def handlePowerUp(self, user):
        valid_targets = [p for p in self.players_list if p != user]
        print("Type the name of the player you want to apply your power up to:")

        while True:
            target_name = input("Target name: ").strip().lower()
            target = next((p for p in valid_targets if p.name.lower() == target_name), None)
            if target:
                user.powerUp(target)
                break
            print("❌ Invalid name. Try again.")

main = Main()
main.start()