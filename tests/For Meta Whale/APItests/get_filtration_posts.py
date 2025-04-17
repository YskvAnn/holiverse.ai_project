import requests
import config  # config.py с API_TOKEN и BASE_URL

url = f"{config.BASE_URL}/api/v1/filtration/posts"

headers = {
    "Authorization": f"Bearer {config.API_TOKEN}",
    "accept": "application/json"
}

# Запрос без query-параметров
# Отправляю запрос
response = requests.get(url, headers=headers)

# Проверяю статус
assert response.status_code == 200, f"❌ Ожидался статус 200, но получен {response.status_code}"

# Если всё ок — вывожу))
print("✅ Статус 200 — тест пройден!")
print("Response body:")
print(response.text)