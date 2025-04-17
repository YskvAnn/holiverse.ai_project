import requests
import config  # config.py с API_TOKEN и BASE_URL

post_id = 456  # укажи ID существующего поста
url = f"{config.BASE_URL}/api/v1/posts/{post_id}/like"

headers = {
    "Authorization": f"Bearer {config.API_TOKEN}",
    "accept": "application/json"
}
response = requests.post(url, headers=headers)

# Проверяю статус
assert response.status_code == 200, f"❌ Ожидался статус 200, но получен {response.status_code}"

# Если всё ок — вывожу))
print("✅ Статус 200 — тест пройден!")
print("Response body:")
print(response.text)