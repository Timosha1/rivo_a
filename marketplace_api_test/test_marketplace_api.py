# проверка наличия основных полей (required_fields и другие) в ответе запроса marketplace
# архивные стратегии игнорируются

import requests

url = "https://backend.rivo.xyz/marketplace?userAddress=0xd278A92a2bED505A67987D2d597Afd2AB160bB3a&period=month"


def test_marketplace_data():
    response = requests.get(url)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    data = response.json()
    assert isinstance(data, list), "Response data is not a list"

    required_fields = [
        "name", "header", "cardDescription", "asset", "protocol", "ticker",
        "address", "chainName", "logo", "protocolLogo", "protocolName",
        "typeStrategy", "volatility", "typeStrategyDetails", "volatilityDetails",
        "rewardCollection", "yieldSource"
    ]

    for index, item in enumerate(data):
        title = item.get("title", {})

        # Игнорируем все элементы где isArchived true
        is_archived = title.get("isArchived")
        if is_archived:
            continue

        # Проверка, что title является словарем и не пустой
        assert isinstance(title, dict), f"Item {index} has 'title' that is not a dictionary: {title}"
        assert title, f"Item {index} has 'title' that is an empty dictionary"

        # Проверка required_fields в title
        for field in required_fields:
            assert field in title, f"Item {index}: Missing field '{field}' in 'title': {title}"
            assert title[field], f"Item {index}: Field '{field}' is empty in 'title': {title}"

        # Проверка tags
        tags = title.get("tags", [])
        assert isinstance(tags, list), f"Item {index}: 'tags' is not a list or is missing in 'title': {title}"
        assert tags, f"Item {index}: 'tags' list is empty in 'title': {title}"

        # Проверка links
        links = title.get("links", {})
        assert isinstance(links, dict), f"Item {index}: 'links' is not a dictionary or is missing in 'title': {title}"

        required_links = ["websites", "twitter", "discord"]
        assert isinstance(required_links, list), f"Item {index}: 'required_links' is not a list"

        for link in required_links:
            assert link in links, f"Item {index}: '{link}' is missing in 'links': {links}"
            assert isinstance(links[link], list), f"Item {index}: '{link}' is not a list in 'links': {links}"
            assert links[link], f"Item {index}: '{link}' list is empty in 'links': {links}"

        # Проверка swapProviders
        swap_providers = title.get("swapProviders", [])
        assert isinstance(swap_providers,
                          list), f"Item {index}: 'swapProviders' is not a list or is missing in 'title': {title}"
        assert swap_providers, f"Item {index}: 'Swap providers' list is empty in 'title': {title}"

        # Проверка списка mainTags
        main_tags = title.get("mainTags", [])
        assert isinstance(main_tags, list), f"Item {index}: 'mainTags' is not a list or is missing in 'title': {title}"
        assert main_tags, f"Item {index}: 'Main_tags' list is empty in 'title': {title}"