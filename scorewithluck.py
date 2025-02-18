import random

def luckgame():
    total_score = 0
    with open ("score.txt", "r") as file:
       High_score = file.read().strip()
       if(High_score!=""):
           High_score=int(High_score)
       else:
           High_score=0
    for i in range(1,7):
     luck_score = random.randint(-1,6)
     if(luck_score == -1):
         print(f"{i} Ball:- \n\n  OHHH!!! THAT'S A WICKET")
         break
     total_score += luck_score
     print(f"{i} Ball:- \n  SCORED SCORE IS:{luck_score}")
     
    if total_score > High_score:
        with open ("score.txt", "w") as file:
            file.write(str(total_score))
        print("CONGRATULATIONS!!! You scored a new HIGH SCORE")
        return total_score
    else:
        return total_score
    
final_score = luckgame()
print(f"\n\nYOUR TOTAL SCORE IS: {final_score}")
with open ("score.txt", "r") as file:
    High_score = file.read().strip()
    print(f"CURRENT HIGH SCORE IS: {High_score}\n\n")    

reset=(input("If you want to reset the high score press 'Y' otherwise choose any key\n")).lower()
if(reset == 'y'):
    with open("score.txt","w") as file:
        file.write("")
    print("HIGH SCORE RESET SUCCESSFULLY")
else:
    print("THANK YOU FOR PLAYING. Come back soon!! and break the high score with your luck.\n")
    
