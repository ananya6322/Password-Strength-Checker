
# Password Strength Checker 🔐

A simple Python project that checks whether a password is Weak, Medium, or Strong based on different security conditions.

---

## Features

- Checks password length
- Detects uppercase letters
- Detects lowercase letters
- Detects numbers
- Detects special characters
- Gives suggestions to improve weak passwords

---

## Technologies Used

- Python
- Regular Expressions (`re` module)

---

## How It Works

The program checks whether the password contains:

- Minimum 8 characters
- Uppercase letters (A-Z)
- Lowercase letters (a-z)
- Numbers (0-9)
- Special characters (@, #, $, etc.)

Based on these checks, it classifies the password as:

- Weak
- Medium
- Strong

---

## Project Structure

```bash
password-strength-checker/
│
├── main.py
└── README.md
```

---

## How to Run

1. Install Python
2. Download or clone this project
3. Open terminal in project folder
4. Run:

```bash
python main.py
## Example
### Input
```text
Hello@123
```
### Output
```text
Password Strength: Strong
```
## Future Improvements

- Add GUI using Tkinter
- Store password history
- Generate strong passwords automatically
- Add color-based strength meter
## Author

Ananya Mohapatra