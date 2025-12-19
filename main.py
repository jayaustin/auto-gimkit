import pyautogui
import time
import random
import sys

# Configuration
screenOffsetX = -1920
screenOffsetY = 0
TOTAL_RUN_TIME_MINUTES = 57
TOTAL_RUN_TIME_SECONDS = TOTAL_RUN_TIME_MINUTES * 60

def hold_with_random_space(key_to_hold, duration):
    """Holds a key for a set duration while randomly pressing space."""
    start_time = time.time()
    
    print(f"Holding '{key_to_hold}' for {duration} seconds...")
    pyautogui.keyDown(key_to_hold)
    
    while time.time() - start_time < duration:
        # 90% chance to press space every iteration of the loop
        if random.random() < 0.9: 
            pyautogui.press('space')
        time.sleep(0.1) 
        
    pyautogui.keyUp(key_to_hold)

def answerQuestions():
    # Initial click
    pyautogui.click(x=100+screenOffsetX, y=1000+screenOffsetY, clicks=1, interval=0, button='left', duration=0)
    time.sleep(1) 
    
    # Repeat the middle clicks 20 times
    for _ in range(20):
        pyautogui.click(x=500+screenOffsetX, y=875+screenOffsetY, clicks=1, interval=0, button='left', duration=0)
        time.sleep(0.1) 
    
    # Final confirmation clicks
    pyautogui.click(x=900+screenOffsetX, y=650+screenOffsetY, clicks=2, interval=0, button='left', duration=0)

def main():
    print("--- Auto-Gimkit Started ---")
    print(f"Timer set for {TOTAL_RUN_TIME_MINUTES} minutes.")
    print("Move mouse to top-left corner of PRIMARY monitor to EMERGENCY STOP.")
    print("Starting in 5 seconds...")
    time.sleep(5)

    script_start_time = time.time() # Capture start time
    questionTimer = 1
    
    try:
        while True:
            # Check if 57 minutes have passed
            elapsed_time = time.time() - script_start_time
            if elapsed_time > TOTAL_RUN_TIME_SECONDS:
                print(f"\n{TOTAL_RUN_TIME_MINUTES} minutes reached. Exiting script safely.")
                break # Exit the while loop

            hold_with_random_space('a', 5)
            hold_with_random_space('d', 5)
            
            questionTimer -= 1
            if questionTimer == 0:
                print("Answering questions now")
                answerQuestions()
                questionTimer = 10
                print("Finished answering questions")
                
    except KeyboardInterrupt:
        print("\nAuto-Gimkit stopped manually.")
    except pyautogui.FailSafeException:
        print("\nFail-safe triggered! Mouse was moved to a corner.")
    finally:
        # Ensure keys are released even if script crashes or stops
        pyautogui.keyUp('a')
        pyautogui.keyUp('d')
        print("Script Closed.")

if __name__ == "__main__":
    main()