# Скрипт по поиску неверных рекоммендаций для архивных стратегий

import requests

url = "https://backend.rivo.xyz/marketplace"
response = requests.get(url)
data = response.json()

Archived_strategies = []
Recommendations = []

# Проходим по каждому "title" в ответе
for item in data:
    strategy_title = item.get("title", {})

    if strategy_title.get("isArchived"):  # Если "isArchived" == true
        # Ищем "name", "address" и "swapProviders", сохраняем их в переменную Archived_strategies
        name = strategy_title.get("name")
        address = strategy_title.get("address")
        swap_providers = strategy_title.get("swapProviders")

        if name and address and swap_providers:  # Проверка что все ключи существуют
            Archived_strategies.append({
                "name": name,
                "address": address,
                "swapProviders": swap_providers
            })

    # Ищем ключ "archiveStrategyRecommendation" и добавляем в Recommendations
    recommendation = strategy_title.get("archiveStrategyRecommendation")
    if recommendation:
        Recommendations.append(recommendation)

# Сравниваем данные из Recommendations с "address" в Archived_strategies
for strategy in Archived_strategies:
    assert strategy['address'] not in Recommendations, f"Wrong recommendations: {strategy['name']}"

print("All recommendations are correct.")

