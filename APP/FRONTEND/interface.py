# APP/FRONTEND/interface.py
import tkinter as tk

# 🌟 UPDATED IMPORT: Using capitalized BACKEND to match your folder name!
from BACKEND.logic import calculate_tip

def on_click_calculate(event=None):
    user_bill = bill_entry.get()
    user_tip = tip_entry.get()
    
    tip_result = calculate_tip(user_bill, user_tip)
    
    if tip_result == "Invalid Input":
        result_label.config(text="Numbers only, please!", fg="#FF5252")
    else:
        result_label.config(text=f"Tip Amount: ${tip_result:.2f}", fg="#DFFF00")

# --- UI Layout (Cyber-Yellow Color Palette & Window) ---
BG_MAIN = "#1E1E24"      
BG_CARD = "#2A2A35"      
TEXT_LIGHT = "#F5F6FA"   
ACCENT_YELLOW = "#FFD200" 
INPUT_BG = "#353545"     

root = tk.Tk()
root.title("Vibrant Tip Calculator")
root.geometry("340x320")
root.config(bg=BG_MAIN) 

title_label = tk.Label(root, text="TIP CALCULATOR", font=("Helvetica Neue", 14, "bold"), bg=BG_MAIN, fg=ACCENT_YELLOW)
title_label.pack(pady=(20, 10))

input_frame = tk.Frame(root, bg=BG_CARD, padx=15, pady=15, bd=0)
input_frame.pack(padx=20, fill="x")

bill_label = tk.Label(input_frame, text="Total Bill ($)", font=("Arial", 10, "bold"), bg=BG_CARD, fg=TEXT_LIGHT)
bill_label.pack(anchor="w")
bill_entry = tk.Entry(input_frame, font=("Arial", 11), bg=INPUT_BG, fg="white", insertbackground="white", bd=0, relief="flat")
bill_entry.pack(fill="x", pady=(5, 10), ipady=4) 

tip_label = tk.Label(input_frame, text="Tip Percentage (%)", font=("Arial", 10, "bold"), bg=BG_CARD, fg=TEXT_LIGHT)
tip_label.pack(anchor="w")
tip_entry = tk.Entry(input_frame, font=("Arial", 11), bg=INPUT_BG, fg="white", insertbackground="white", bd=0, relief="flat")
tip_entry.insert(0, "15")
tip_entry.pack(fill="x", pady=(5, 0), ipady=4)

calculate_button = tk.Button(
    root, text="CALCULATE", command=on_click_calculate,
    font=("Helvetica Neue", 11, "bold"), bg=ACCENT_YELLOW, fg="#1E1E24",
    activebackground="#D4AF37", activeforeground="#1E1E24", bd=0, cursor="hand2" 
)
calculate_button.pack(fill="x", padx=20, pady=15, ipady=6)

result_label = tk.Label(root, text="Tip Amount: $0.00", font=("Helvetica Neue", 13, "bold"), bg=BG_MAIN, fg=TEXT_LIGHT)
result_label.pack(pady=10)

root.bind('<Return>', on_click_calculate)

root.mainloop()