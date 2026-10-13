# KBA - KAUN BANEGA CROREPATI

# 1. 7 Sawal (Jisse Prize Levels se match karein)
Questions = [
    "1. Bharat ki rajdhani (Capital) kya hai?",
    "2. Computer ka dimaag (Brain) kise kehte hain?",
    "3. Cricket World Cup me ek over me kitni balls hoti hain?",
    "4. Bharat ka Rashtriya Pashu (National Animal) kaun sa hai?",
    "5. ISRO ka mukhyalaya (Headquarters) kahan hai?",
    "6. Bharat ke pehle Rashtrapati (President) kaun the?",
    "7. Bharat ke kis rajya ko 'Land of Five Rivers' kaha jata hai?",
]

# 2. Options List
Options = [
    ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
    ["A. Keyboard", "B. Monitor", "C. CPU", "D. Mouse"],
    ["A. 4", "B. 5", "C. 6", "D. 8"],
    ["A. Sher (Lion)", "B. Bagh (Tiger)", "C. Hathi", "D. Cheetah"],
    ["A. Bengaluru", "B. Mumbai", "C. Delhi", "D. Chennai"],
    [
        "A. Dr. APJ Abdul Kalam",
        "B. Dr. Rajendra Prasad",
        "C. Pandit Nehru",
        "D. Sardar Patel",
    ],
    ["A. Haryana", "B. Punjab", "C. Rajasthan", "D. Gujarat"],
]

# 3. Capital Letters me Sahi Answers (match karne ke liye)
Answers = ["B", "C", "C", "B", "A", "B", "B"]

# 4. 7 Sawalon ke liye 7 Prize Levels
prize_levels = [
    "Rs. 10,000",
    "Rs. 1,00,000",
    "Rs. 10,00,000 (10 Lakh)",
    "Rs. 50,00,000 (50 Lakh)",
    "Rs. 1,00,00,000 (1 Crore)",
    "Rs. 3,00,00,000 (3 Crore)",
    "Rs. 7,00,00,000 (7 CRORE!)",
]

total_money = "RS 0"

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("Welcome to Kaun Banega Crorepati!")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("Total Questions:", len(Questions))
print()

# Loop shuru
for i in range(len(Questions)):
  # Sawal Print Karo
  print(f"Question {i+1} ({prize_levels[i]} ke liye):")
  print(Questions[i])

  # Saare Options ek-ek karke print karo
  for option in Options[i]:
    print(option)

  # Options PRINT HONE KE BAAD User se Answer maango (Loop ke bahar)
  user_answer = input("\nChoose your option (a, b, c, d): ").upper()

  # Check karo Jawab Sahi hai ya Galat
  if user_answer == Answers[i]:
    total_money = prize_levels[i]
    print(f"🎉 SAHI JAWAB! Aapne jeet liye hain: {total_money}\n")
    print("-" * 40)
  else:
    print(
        f"\n❌ GALAT JAWAB! Afsos, aapka safar yahi samapt hota hai."
        f" Correct answer is {Answers[i]}.\n"
    )
    break  # Game khatam

print("================================================")
print(f"🏆 GAME OVER! Aap ghar le ja rahe hain: {total_money}")
print("================================================")