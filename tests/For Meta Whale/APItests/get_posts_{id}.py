import requests
import config  # config.py с API_TOKEN и BASE_URL

post_id = 456  # явно задаём ID поста
url = f"{config.BASE_URL}/api/v1/posts/{post_id}"

headers = {
    "Authorization": f"Bearer {config.API_TOKEN}",
    "accept": "application/json"
}

# Запрос без query-параметров
response = requests.get(url, headers=headers)

# Проверка ответа
assert response.status_code == 200, (
    f"❌ GET /posts/{post_id}: ожидался статус 200, но получен {response.status_code}\n"
    f"Ответ сервера: {response.text}"
)

print(f"✅ GET /posts/{post_id}: статус 200 — тест пройден!")
print("Response body:")
print(response.text)
