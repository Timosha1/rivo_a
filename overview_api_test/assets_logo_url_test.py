import requests
import pytest

def test_check_logoURI():
    url = "https://backend.rivo.xyz/assets/v2"
    response = requests.get(url)

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    data = response.json()

    # Список для хранения значений "symbol" с пустыми или null "logoURI"
    empty_logo_url = []

    # Убедимся, что ключ "data" присутствует и это список
    assert "data" in data, "Key 'data' not found in the response"
    assert isinstance(data['data'], list), "'data' is not a list"

    # Проверяем каждый элемент списка "data"
    for index, item in enumerate(data['data']):
        symbol = item.get('symbol')
        chainName = item.get('chainName')
        logoURI = item.get('logoURI')

        # Если logoURI пустой или null, добавляем "symbol" в список missedurl
        if not logoURI:
            empty_logo_url.append((symbol, chainName))  # Сохраняем кортеж (index, symbol, chainName)

    # Проверяем, что список не пустой, если есть пропущенные URL логотипов
    assert len(empty_logo_url) == 0, f"Missing logoURIs for symbols: {empty_logo_url}"

    # Выводим индексы, символы и chainName без логотипов, если есть
    print("Symbol and chainName with missing logoURIs:")
    for symbol, chainName in empty_logo_url:
        print(f"Symbol: {symbol}, ChainName: {chainName}")

