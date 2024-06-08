import unittest
from unittest.mock import patch
from io import StringIO
import pyperclip
import time
from app.monitor_pasteboard_for_kindle import monitor_clipboard

class TestMonitorClipboard(unittest.TestCase):
    def test_monitor_clipboard(self):
        # Set up the initial clipboard text
        initial_text = "Initial clipboard text"
        pyperclip.copy(initial_text)
        
        # Set up the expected cleaned text
        cleaned_text = "Cleaned clipboard text"
        
        # Patch the pyperclip.paste function to return the initial text and then the cleaned text
        with patch('pyperclip.paste', side_effect=[initial_text, cleaned_text]):
            # Redirect the standard output to a StringIO object
            captured_output = StringIO()
            import sys
            sys.stdout = captured_output
            
            # Call the monitor_clipboard function
            monitor_clipboard()
            
            # Get the output from the standard output
            output = captured_output.getvalue().strip()
            
            # Assert that the cleaned text is copied to the clipboard
            self.assertEqual(pyperclip.paste(), cleaned_text)
            
            # Assert that the output contains the cleaned text
            self.assertIn(cleaned_text, output)
            
            # Assert that the output does not contain the initial text
            self.assertNotIn(initial_text, output)
            
            # Assert that the output contains the sleep message
            self.assertIn("Sleeping", output)
            
            # Assert that the pyperclip.paste function is called twice
            self.assertEqual(pyperclip.paste.call_count, 2)
            
            # Assert that the time.sleep function is called once
            self.assertEqual(time.sleep.call_count, 1)

if __name__ == '__main__':
    unittest.main()