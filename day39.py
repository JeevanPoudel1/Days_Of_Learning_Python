import time
import os

def clear_screen():
    # Clears the terminal screen for a clean UI look
    os.system('cls' if os.name == 'nt' else 'clear')

def run_timer(seconds):
    while seconds > 0:
        clear_screen()
        # Format seconds into Minutes:Seconds
        mins, secs = divmod(seconds, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        print("=== COUNTDOWN TIMER ===")
        print(f"\nTime Remaining: {timer_display}\n")
        print("=======================")
        time.sleep(1)
        seconds -= 1
    
    clear_screen()
    print("⏰ Time's up! ⏰")

def run_stopwatch():
    clear_screen()
    print("=== STOPWATCH ===")
    print("Press CTRL+C to stop the stopwatch.")
    input("\nPress Enter to START...")
    
    start_time = time.time()
    try:
        while True:
            clear_screen()
            elapsed_time = time.time() - start_time
            mins, secs = divmod(int(elapsed_time), 60)
            print("=== STOPWATCH ===")
            print(f"\nElapsed Time: {mins:02d}:{secs:02d}\n")
            print("=======================")
            time.sleep(1)
    except KeyboardInterrupt:
        # Catches CTRL+C so the program exits gracefully
        total_time = time.time() - start_time
        mins, secs = divmod(int(total_time), 60)
        print(f"\nStopwatch stopped! Total Time: {mins:02d}:{secs:02d}")

def main():
    while True:
        clear_screen()
        print("--- Time Management Tool ---")
        print("1. Countdown Timer")
        print("2. Stopwatch")
        print("3. Exit")
        
        choice = input("\nChoose an option (1-3): ").strip()
        
        if choice == "1":
            try:
                mins = int(input("Enter timer duration in minutes: "))
                run_timer(mins * 60)
                input("\nPress Enter to return to menu...")
            except ValueError:
                print("Please enter a valid number.")
                time.sleep(2)
        elif choice == "2":
            run_stopwatch()
            input("\nPress Enter to return to menu...")
        elif choice == "3":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()
