import time

def print_slow(text):
    """Prints text character by character for a retro feel."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01) # Small delay for effect
    print()

def start_game():
    # --- Variables & Datatypes ---
    # Integer for health
    player_hp = 100 
    # String for player name
    player_name = "" 
    # List for inventory
    inventory = [] 
    # Boolean for game loop control
    game_running = True

    print_slow("Welcome to... DUNGEON ESCAPE!")
    print_slow("-------------------------------")
    
    while player_name == "":
        player_name = input("Enter your name, adventurer: ")
    
    print_slow(f"\nHello, {player_name}. You wake up in a dark, cold cell.")
    print_slow("The door is unlocked. You hear strange noises outside.")

    # --- Game Loop (While Loop) ---
    while game_running:
        print(f"\n[Status] HP: {player_hp} | Inventory: {inventory}")
        print("------------------------------------------------")
        print("You are in a corridor. There are two paths:")
        print("1. Go LEFT towards a flickering light.")
        print("2. Go RIGHT into the darkness.")
        print("3. Check your backpack.")
        print("4. Quit game.")
        
        # Taking Input
        choice = input("\nMake your choice (1-4): ")

        # --- Conditionals (If/Elif/Else) ---
        if choice == '1':
            print_slow("\nYou walk towards the light...")
            print_slow("It's a guard room! A goblin is sleeping on a chair.")
            
            action = input("Do you (A)ttack or (S)neak past? ").upper()
            
            if action == 'A':
                print_slow("You punch the goblin! He wakes up and bites you!")
                player_hp -= 20 # Math operation
                print_slow(f"You lost 20 HP. Current HP: {player_hp}")
                if "Goblin Ear" not in inventory:
                    print_slow("You managed to defeat him and took a trophy.")
                    inventory.append("Goblin Ear") # List operation
            elif action == 'S':
                print_slow("You sneak past quietly... Success!")
                print_slow("You found a shiny key on the table.")
                if "Gold Key" not in inventory:
                    inventory.append("Gold Key")
            else:
                print_slow("You hesitated and ran back to the corridor.")
                
        elif choice == '2':
            print_slow("\nYou step into the darkness...")
            if "Torch" in inventory:
                print_slow("Your torch lights the way! You find the exit door!")
                if "Gold Key" in inventory:
                    print_slow("You use the Gold Key to unlock the door.")
                    print_slow("FREEDOM! You have escaped the dungeon!")
                    game_running = False # End the loop
                else:
                    print_slow("The door is locked. You need a key.")
            else:
                print_slow("It's too dark! You trip and fall.")
                player_hp -= 10
                print_slow("You crawl back to the start, bruised.")
                print_slow("Maybe you can find a light source elsewhere?")
                # Hint: There is no torch in this simple version, 
                # but let's add a secret way to find one for demonstration.
                
        elif choice == '3':
            print_slow("\nYou check your backpack...")
            if len(inventory) == 0:
                print_slow("It's empty. You feel sad.")
                # Secret item finding logic for demonstration
                print_slow("Wait, you feel a hidden pocket...")
                print_slow("You found a Torch!")
                inventory.append("Torch")
            else:
                print_slow("You have:")
                for item in inventory: # For loop iterating over a list
                    print_slow(f"- {item}")
                    
        elif choice == '4':
            print_slow("You give up? Shame.")
            game_running = False # Exit condition
            
        else:
            print_slow("Invalid choice. Please type 1, 2, 3, or 4.")

        # Check for Game Over
        if player_hp <= 0:
            print_slow("\nYou have succumbed to your injuries.")
            print_slow("GAME OVER")
            game_running = False

    print_slow("\nThanks for playing Dungeon Escape!")

if __name__ == "__main__":
    start_game()
