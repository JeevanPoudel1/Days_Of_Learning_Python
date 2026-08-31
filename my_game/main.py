# Option 1: Importing the whole module using dot notation
from graphics import screen

# Option 2: Importing a specific function directly
from graphics.UI import draw_button

def play_game():
    print("🎮 Game logic is running...")
    return "Level 1 Complete"

def main():
    # Call the function from the screen module
    screen.clear_canvas()
    
    # Run our game logic
    result = play_game()
    print(f"Status: {result}")
    
    # Call the specific function we imported from the UI module
    draw_button()

if __name__ == '__main__':
    main()
