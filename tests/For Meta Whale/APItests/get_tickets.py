import requests
import config

url = f"{config.BASE_URL}/api/v1/tickets/"

headers = {
    "Authorization": f"Bearer {config.API_TOKEN}",
    "accept": "application/json"
}
params = {
    "limit": 5,
    "page": 1
}

# Отправляю запрос
response = requests.get(url, headers=headers, params=params)

# Проверяю статус
assert response.status_code == 200, f"❌ Ожидался статус 200, но получен {response.status_code}"

# Если всё ок — вывожу))
print("✅ Статус 200 — тест пройден!")
print("Response body:")
print(response.text)
