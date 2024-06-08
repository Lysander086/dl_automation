import re
import pyperclip

def remove_unrelated_text(text):
    # Define the pattern to match unrelated words and characters
    pattern = r'\b(?:unrelated_word1|unrelated_word2|unrelated_character1|unrelated_character2)\b'
    
    # Remove unrelated words and characters using regular expressions
    cleaned_text = re.sub(pattern, '', text)
    
    return cleaned_text 

def monitor_clipboard():
    previous_text = ''
    
    while True:
        # Get the current text from the clipboard
        current_text = pyperclip.paste()
        
        # Check if the text has changed
        if current_text != previous_text:
            # Remove unrelated words and characters
            cleaned_text = remove_unrelated_text(current_text)
            
            # Update the clipboard with the cleaned text
            pyperclip.copy(cleaned_text)
            
            # Update the previous text
            previous_text = cleaned_text
        
        # Sleep for a short duration before checking the clipboard again
        time.sleep(0.5)

# Start monitoring the clipboard
monitor_clipboard()