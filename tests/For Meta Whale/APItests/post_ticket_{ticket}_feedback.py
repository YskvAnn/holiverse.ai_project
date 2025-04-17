import requests
import config
import json

# Чтение ID тикета из файла
with open("ticket_id.txt", "r") as file:
    ticket = int(file.read().strip())  # Читаем ID тикета

# Формируем URL для отправки запроса
url = f"{config.BASE_URL}/api/v1/ticket/{ticket}/feedback"

headers = {
    "Authorization": f"Bearer {config.API_TOKEN}",
    "accept": "application/json",
    "Content-Type": "application/json"  # Важное поле для POST-запросов с JSON
}

# Тело запроса
body = {
    "feedback": "QA test Automation",
    "rank": 5
}

# Отправляем POST-запрос с телом JSON
response = requests.post(url, headers=headers, json=body)

# Проверяем статус ответа
assert response.status_code == 200, (
    f"❌ Ожидался статус 200, но получен {response.status_code}\n"
    f"Ответ сервера: {response.text}"
)

# Если все ок — выводим успешное сообщение
print("✅ Статус 200 — тест пройден!")
print("Response body:")
print(response.text)
