import time

def typing_speed_test():
    prompt_text = "The quick brown fox jumps over the lazy dog."
    
    input("Press Enter to start typing...")
    
    start_time = time.time()
    user_input = input(prompt_text + "\n")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    words_per_minute = len(user_input.split()) / (elapsed_time / 60)
    
    print(f"You typed at a speed of {words_per_minute:.2f} words per minute.")

if __name__ == "__main__":
    typing_speed_test()
