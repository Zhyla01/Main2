# (Завдання_1)

class Recipe:
    def __init__(self, name, ingredients, text, time):
        self.name = name
        self.ingredients = ingredients
        self.text = text
        self.time = time

    def __str__(self):
        return self.name

    def __contains__(self, item):
        return item in self.ingredients

    def __gt__(self, other):
        return self.time > other.time

    def display_info(self):
        print(f"Назва: {self.name}")
        print(f"Інгредієнти: {', '.join(self.ingredients)}")
        print(f"Рецепт: {self.text}")
        print(f"Час приготування: {self.time} хвилин")


recipes = [
    Recipe("Піца", ["борошно", "вода", "дріжджі", "томат", "сир"],
           "Готуємо тісто, додаємо інгредієнти та запікаємо", 30),
    Recipe("Салат", ["томат", "огірок", "зелень", "олія"],
           "Нарізаємо овочі, додаємо зелень та поливаємо олією", 10),
    Recipe("Суп", ["вода", "картопля", "морква", "м'ясо"],
           "Варимо всі інгредієнти до готовності", 45)
]

print("Рецепти, які містять інгредієнт 'томата':")
for recipe in recipes:
    if "томат" in recipe:
        print(recipe)

quickest_recipe = min(recipes, key=lambda r: r.time)
print("\nРецепт з найменшим часом приготування:")
quickest_recipe.display_info()