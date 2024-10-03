"""
Это отдельный тест для проверки Локус индексов - ссылок на ютуб, йелд схему, why invest и тд
Остальные тесты в test marketplace api
"""

from pages.marketplace_api_page import MarketplaceApiPage

def test_api_response():
    api_page = MarketplaceApiPage()
    data = api_page.get_api_data()
    errors = []

    ignored_names = ['Mantle Index']

    for item in data:
        title = item.get('title')

        # Пропускаем объекты, которые находятся в разработке
        if title.get('name') in ignored_names:
            continue

        # Пропускаем не индексы
        if title.get('isIndex', False):
            item_name = title.get('name', 'Unknown')

            # Проверка наличия и непустоты обязательных полей
            required_fields = ['youtubeLink', 'yieldSchemeLogo', 'whyInvestDescr', 'assetsAddrs']
            api_page.check_required_fields(item, required_fields, item_name, errors)

            # Проверка рисков и аудитов
            api_page.check_risks_and_audits(item, item_name, errors)

            # Проверка типов данных
            type_checks = [
                ('youtubeLink', str),
                ('yieldSchemeLogo', str),
                ('whyInvestDescr', str),
                ('assetsAddrs', list)
            ]
            api_page.check_data_types(item, type_checks, item_name, errors)

    # Вывод отчета об ошибках
    if errors:
        print("\nОтчет об ошибках:")
        for error in errors:
            print(error)

    assert not errors, "Обнаружены ошибки в ответе API"




