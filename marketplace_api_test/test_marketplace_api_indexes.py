"""
Это отдельный тест для проверки Локус индексов - ссылок на ютуб, йелд схему, why invest и тд
Остальные тесты в test marketplace api
"""

import requests

URL = "https://backend.rivo.xyz/marketplace?userAddress=0xd278A92a2bED505A67987D2d597Afd2AB160bB3a&period=month"

def get_api_data():
    response = requests.get(URL)
    return response.json()

def test_api_response():
    data = get_api_data()
    errors = []

    for item in data:
        if item['title'].get('isIndex', False):
            item_name = item['title'].get('name', 'Unknown')

            # Проверка наличия и непустоты обязательных полей
            required_fields = ['youtubeLink', 'yieldSchemeLogo', 'whyInvestDescr', 'assetsAddrs']
            for field in required_fields:
                if field not in item['title']:
                    errors.append(f"Поле '{field}' отсутствует в элементе {item_name}")
                elif field != 'assetsAddrs' and not item['title'][field].strip():
                    errors.append(f"Поле '{field}' пустое в элементе {item_name}")

            # Проверка рисков и аудитов
            if 'risksAndAudits' not in item:
                errors.append(f"Поле 'risksAndAudits' отсутствует в элементе {item_name}")
            else:
                risk_fields = ['audit', 'riskLevel', 'riskScore', 'riskScoreNumber', 'score']
                for field in risk_fields:
                    if field not in item['risksAndAudits']:
                        errors.append(f"Поле '{field}' отсутствует в 'risksAndAudits' элемента {item_name}")
                    elif field in ['audit', 'riskLevel', 'riskScore']:
                        if not str(item['risksAndAudits'][field]).strip():
                            errors.append(f"Поле 'risksAndAudits.{field}' пустое в элементе {item_name}")
                    elif field == 'riskScoreNumber':
                        if not str(item['risksAndAudits'][field]).strip():
                            errors.append(f"Поле 'risksAndAudits.{field}' пустое в элементе {item_name}")
                    elif field == 'score':
                        score = item['risksAndAudits'][field]
                        if not isinstance(score, dict) or not score:
                            errors.append(f"Поле 'risksAndAudits.{field}' пустое или не является словарем в элементе {item_name}")
                        else:
                            for score_field in ['simplicity', 'longevity', 'protocolSafety']:
                                if score_field not in score or not str(score[score_field]).strip():
                                    errors.append(f"Поле 'risksAndAudits.score.{score_field}' отсутствует или пустое в элементе {item_name}")

            # Проверка типов данных
            type_checks = [
                ('youtubeLink', str),
                ('yieldSchemeLogo', str),
                ('whyInvestDescr', str),
                ('assetsAddrs', list)
            ]
            for field, expected_type in type_checks:
                value = item['title'].get(field)
                if not isinstance(value, expected_type):
                    errors.append(f"Поле '{field}' должно быть типа {expected_type.__name__} в элементе {item_name}")

    # Вывод отчета об ошибках
    if errors:
        print("\nОтчет об ошибках:")
        for error in errors:
            print(error)

    assert not errors, "Обнаружены ошибки в ответе API"
