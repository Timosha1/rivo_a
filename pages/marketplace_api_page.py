import requests

class MarketplaceApiPage:
    URL = "https://backend.rivo.xyz/marketplace?userAddress=0xd278A92a2bED505A67987D2d597Afd2AB160bB3a&period=month"

    def get_api_data(self):

        # Отправляет GET-запрос к API и возвращает dict данные в формате JSON.
        # Исключения: Raises requests.exceptions.RequestException если статус код ответа не 200.
        response = requests.get(self.URL)
        response.raise_for_status()  # Проверка на успешность запроса
        return response.json()

    def check_required_fields(self, item, required_fields, item_name, errors):

        # Проверяет наличие обязательных полей и их непустоту.
        for field in required_fields:
            if field not in item['title']:
                errors.append(f"Поле '{field}' отсутствует в элементе {item_name}")
            elif field != 'assetsAddrs' and not item['title'][field].strip():
                errors.append(f"Поле '{field}' пустое в элементе {item_name}")

    def check_risks_and_audits(self, item, item_name, errors):

        # Проверяет наличие полей, связанных с рисками и аудитами, и их непустоту.
        if 'risksAndAudits' not in item:
            errors.append(f"Поле 'risksAndAudits' отсутствует в элементе {item_name}")
        else:
            risk_fields = ['audit', 'riskLevel', 'riskScore', 'riskScoreNumber', 'score']
            for field in risk_fields:
                if field not in item['risksAndAudits']:
                    errors.append(f"Поле '{field}' отсутствует в 'risksAndAudits' элемента {item_name}")
                elif field in ['audit', 'riskLevel', 'riskScore'] and not str(item['risksAndAudits'][field]).strip():
                    errors.append(f"Поле 'risksAndAudits.{field}' пустое в элементе {item_name}")
                elif field == 'riskScoreNumber' and not str(item['risksAndAudits'][field]).strip():
                    errors.append(f"Поле 'risksAndAudits.{field}' пустое в элементе {item_name}")
                elif field == 'score':
                    score = item['risksAndAudits'][field]
                    if not isinstance(score, dict) or not score:
                        errors.append(f"Поле 'risksAndAudits.{field}' пустое или не является словарем в элементе {item_name}")
                    else:
                        for score_field in ['simplicity', 'longevity', 'protocolSafety']:
                            if score_field not in score or not str(score[score_field]).strip():
                                errors.append(f"Поле 'risksAndAudits.score.{score_field}' отсутствует или пустое в элементе {item_name}")

    def check_data_types(self, item, type_checks, item_name, errors):

        #Проверяет типы данных полей в элементе.
        for field, expected_type in type_checks:
            value = item['title'].get(field)
            if not isinstance(value, expected_type):
                errors.append(f"Поле '{field}' должно быть типа {expected_type.__name__} в элементе {item_name}")
