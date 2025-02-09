from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def index(request):
    template_name = 'calculator/index.html'
    return render(request, template_name)


def get_recipe(request, dish):
    template_name = 'calculator/index.html'
    cur_dish = DATA.get(dish, {})
    amount = int(request.GET.get("servings", 1))
    recipe = {}
    if len(cur_dish) > 0:
        for key, val in cur_dish.items():
            recipe[key] = val * amount

    return render(request, template_name, context={'recipe': recipe})
