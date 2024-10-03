# проверка наличия основных полей (archiveDescription и archiveStrategyRecommendation),
# в ответе запроса marketplace для архивных стратегий/индексов


import requests

marketplace_api_url = \
    "https://backend.rivo.xyz/marketplace?userAddress=0xd278A92a2bED505A67987D2d597Afd2AB160bB3a&period=month"


def test_marketplace_data():
    response = requests.get(marketplace_api_url)
    errors = []

    assert response.status_code == 200, f"Marketplace request error: {response.status_code}"
    data = response.json()

    # Проверка, что данные являются списком
    if not isinstance(data, list):
        errors.append("Marketplace response data is not a list")

    required_fields = [
        "archiveDescription", "archiveStrategyRecommendation"
    ]

    for index, item in enumerate(data):
        title = item.get("title", {})

        # Игнорируем все элементы где isArchived false
        is_archived = title.get("isArchived")
        if not is_archived:
            continue

        # Исключаем объексты которые еще в разработке
        ignored_names = ['Mantle Index']
        if title.get('name') in ignored_names:
            continue

        # Проверка, что все поля из списка required_fields присутствуют и не пусты в объекте title
        for field in required_fields:
            # существует ли ключ field ("archiveDescription", "archiveStrategyRecommendation") в объекте title
            if field not in title:
                errors.append(f"Item {index}: Missing field '{field}' in {title.get('name', 'Unknown')}")
            else:
                # проверка, что значение поля ("archiveDescription", "archiveStrategyRecommendation") не пустое
                if not title[field]:
                    errors.append(f"Item {index}: Field '{field}' is empty in {title.get('name', 'Unknown')}")

    # Если есть ошибки, вывести их
    if errors:
        for error in errors:
            print(error)
        assert False, "Errors found in test"


