from ursina import *
import random
import os

# Initialize Ursina
app = Ursina()

# 🎵 Load High Score Sound (Only Needed One)
if os.path.exists('highscore.wav'):
    highscore_sound = Audio('highscore.wav', autoplay=False)
else:
    highscore_sound = None

# 📂 Function to load high score
def load_high_score():
    try:
        with open("score.txt", "r") as file:
            content = file.read().strip()
            return int(content) if content.isdigit() else 0
    except (FileNotFoundError, ValueError):
        return 0

# 📂 Function to save high score
def save_high_score(score):
    with open("score.txt", "w") as file:
        file.write(str(score))

# 📂 Function to reset high score
def reset_high_score():
    save_high_score(0)
    high_score_text.text = "🏆 High Score: 0"
    print("🔄 High score reset successfully!")

# 🎮 Game Logic
def play_game():
    global high_score_text, score_texts
    total_score = 0
    high_score = load_high_score()

    # Clear previous scores
    for text in score_texts:
        destroy(text)
    score_texts.clear()

    # 📊 Score Display Positioning (Prevent Overlapping)
    y_offset = 0.2  # Start below high score

    for i in range(1, 7):
        luck_score = random.randint(-1, 6)

        # 🏏 Wicket Logic
        if luck_score == -1:
            text = Text(text=f"⚡ Ball {i}: WICKET! Total: {total_score}", 
                        scale=1.2, y=y_offset, color=color.red)
            score_texts.append(text)
            break
        
        total_score += luck_score

        # 🏆 Color for Boundaries
        text_color = color.yellow if luck_score in [4, 6] else color.white
        
        # 📝 Display Scores with Proper Spacing
        text = Text(text=f"🏏 Ball {i}: Scored {luck_score}, Total: {total_score}", 
                    scale=1.2, y=y_offset, color=text_color)
        score_texts.append(text)
        y_offset -= 0.08  # Move text down for the next ball (Fixing overlap)

    # 🔥 Update High Score if Beaten
    if total_score > high_score:
        save_high_score(total_score)
        high_score_text.text = f"🏆 High Score: {total_score}"
        if highscore_sound:
            highscore_sound.play()  # 🎵 Play sound only when record is broken
        print("🎉 New High Score!")

    print(f"Final Score: {total_score}")

# 🎨 UI Setup
window.color = color.dark_gray
title = Text(text="🎲 3D Luck Game 🏏", scale=2, y=0.4, color=color.yellow)
high_score_text = Text(text=f"🏆 High Score: {load_high_score()}", scale=1.5, y=0.3, color=color.green)

# 🎮 Buttons
play_button = Button(text="🎮 Play", scale=(0.2, 0.1), y=-0.3, color=color.azure)
play_button.on_click = play_game

reset_button = Button(text="🔄 Reset High Score", scale=(0.3, 0.1), y=-0.45, color=color.red)
reset_button.on_click = reset_high_score

# 📜 Score Display List
score_texts = []

# Run Ursina App
app.run()