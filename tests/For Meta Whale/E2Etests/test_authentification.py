import requests

def test_auth_and_get_token():
    url = "https://api.meta-whale.com/api/v1/users/auth/verify"

    payload = {
        "address": "0x7Fee0d55A00B248c5f2305b3207Ac1FBb8F41FFd",
        "message": "Sign this message to confirm you own this wallet address. This action will not cost any gas fees.\n\nNonce: vN2EOK6lUVX0bmHp",
        "signature": "0x1d9d5bb6369d588af4c1f64e6098ab5529eacf4617347798b0e0d15d4b9c3ae42449fcd86d7c73f07cd4adc899e4f806138dc598c7874eac3e00c3988bcb1fd41b"
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == 200, f"Ошибка: {response.status_code}, тело: {response.text}"

    data = response.json()
    assert "token" in data, f"Ответ не содержит токен: {data}"

    token = data["token"]
    print("Токен успешно получен:\n", token)

    return token


if __name__ == "__main__":
    token = test_auth_and_get_token()
    print("Токен записан в переменную 'token':", token)
