import requests
import unittest

class TestPageStatus(unittest.TestCase):
    def test_multiple_pages_status_200(self):
        urls = [
            "https://b.metaforce.app/about",
            "https://b.metaforce.app/",
            "https://b.metaforce.app/news-portal/",
            "https://meta-whale.com/news-portal/en/post/453",
            "https://b.metaforce.app/TS",
            "https://w-dex.ai/swap"
        ]

        for url in urls:
            with self.subTest(url=url):
                try:
                    response = requests.get(url, timeout=2)
                    self.assertEqual(response.status_code, 200, f"Ожидался статус 200, но получен {response.status_code} на {url}")
                except requests.exceptions.RequestException as e:
                    self.fail(f"Ошибка при открытии страницы {url}: {e}")

if __name__ == "__main__":
    unittest.main()
