import random

def luckgame():
    total_score = 0
    with open ("score.txt", "r") as file:
       High_score = file.read()
       if(High_score!=""):
           High_score=int(High_score)
       else:
           High_score=0
    for i in range(1,7):
     luck_score = random.randint(0,6)
     total_score += luck_score
     print(f"{i} Ball:- \n  SCORED SCORE IS:{luck_score}")
     
    if total_score > High_score:
        with open ("score.txt", "w") as file:
            file.write(str(total_score))
        print("CONGRATULATINS!!! You scored a new HIGH SCORE")
        return total_score
    
final_score = luckgame()
print(f"\n\nYOUR TOTAL SCORE IS: {final_score}\n\n")

    
