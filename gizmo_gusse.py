import random
import os

def load_best_score():
    """Load the all-time best score from scores.txt, if it exists."""
    try:
        if os.path.exists("scores.txt"):
            with open("scores.txt", "r") as file:
                return int(file.read().strip())
        return float('inf')  # No score yet, use infinity as default
    except:
        return float('inf')

def save_best_score(score):
    """Save the all-time best score to scores.txt."""
    with open("scores.txt", "w") as file:
        file.write(str(score))

def number_guessing_game():
    print("Welcome to Gizmo Gusse!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Load all-time best score
    all_time_best = load_best_score()
    session_best = float('inf')  # Track best score in this session
    
    while True:
        # Generate random number
        target = random.randint(1, 100)
        attempts = 0
        
        while True:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1
                
                if guess < 1 or guess > 100:
                    print("Please guess a number between 1 and 100.")
                    continue
                
                if guess < target:
                    print("Too low! Try again.")
                elif guess > target:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You guessed the number in {attempts} attempts!")
                    # Update session best
                    session_best = min(session_best, attempts)
                    # Update all-time best
                    all_time_best = min(all_time_best, attempts)
                    save_best_score(all_time_best)
                    # Show scores
                    print(f"Session Best: {session_best} attempts")
                    print(f"All-Time Best: {all_time_best} attempts")
                    break
            except ValueError:
                print("Please enter a valid number.")
        
        # Ask to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"Thanks for playing Gizmo Gusse! Final Session Best: {session_best} attempts, All-Time Best: {all_time_best} attempts")
            break

# Start the game
number_guessing_game()