class food_item:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self. fat = fat
def calculate_daily_nutrition(food_list):
    total_cal = 0
    total_pro = 0
    total_carbs = 0
    total_fat = 0

    for m in food_list:
        total_cal += m.calories
        total_pro += m.protein
        total_carbs += m.carbs
        total_fat += m.fat
    print(" Total nutrition of 24 hours ")
    print(f"total calories：{total_cal} kcal")
    print(f"total proteins：{total_pro:.1f} g")
    print(f"total carbs：{total_carbs:.1f} g")
    print(f"total fat：{total_fat:.1f} g")

    if total_cal > 2500 or total_fat > 90:
        print("\n Warning: You have consumed more than 2500 calories or 90g fat.") 

if __name__ =="__main__":
    Apple = food_item("Apple", 60, 0.3, 15, 0.5)
    Rice = food_item("Rice", 130, 2.7, 28, 0.3)
    Beef = food_item("Beef", 250, 26, 0, 15)
    daily_food = [Apple, Rice, Beef, Rice, Beef, Beef, Beef, Beef, Beef, Beef, Beef, Beef]
    calculate_daily_nutrition(daily_food)
   