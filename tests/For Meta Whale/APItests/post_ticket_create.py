import requests
import config
import json

url = f"{config.BASE_URL}/api/v1/ticket/create"

headers = {
    "Authorization": f"Bearer {config.API_TOKEN}",
    "accept": "application/json",
    "Content-Type": "application/json"
}

payload = {
    "custom_topic": "Моя тема из автотеста",
    "incident_date": "2025-04-14",
    "message": "Автотест: создание тикета",
    "email": "qa_test@example.com",
    "files": []
}

response = requests.post(url, headers=headers, json=payload)
print("➡️ Status code:", response.status_code)
print("➡️ Response:", response.text)

assert response.status_code == 200, (
    f"❌ Ожидался статус 201, но получен {response.status_code}\n"
    f"Ответ сервера: {response.text}"
)

ticket_id = response.json()["data"]["id"]
print(f"✅ Тикет создан! ID: {ticket_id}")

# Сохраняем ID в файл
with open("ticket_id.txt", "w") as file:
    file.write(str(ticket_id))
