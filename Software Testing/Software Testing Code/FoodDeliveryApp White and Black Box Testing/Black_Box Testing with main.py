import pyautogui
import time
import subprocess
# Launch the app (example: python main.py)
subprocess.Popen(["python", "main.py"])
time.sleep(3) # wait for GUI to appear
# Find the "Register" button by coordinates (adjust coordinates as needed)
# pyautogui.click(x=100, y=200)
time.sleep(2)
# Type email
pyautogui.typewrite("Test_user@example.com", interval=0.1)
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.press("tab")
# Type password
pyautogui.typewrite("ValidPass123@", interval=0.1)
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.press("tab")
# Confirm password
pyautogui.typewrite("ValidPass123@", interval=0.1)
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.press("tab")
# Wait for confirmation
time.sleep(1)
pyautogui.press("space")
time.sleep(1)
# Take a screenshot to verify success message
pyautogui.screenshot("registration_result.png")
# Manually check the screenshot or use OCR for verification