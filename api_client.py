import requests
import logging

logger = logging.getLogger(__name__)

def send_news_to_api(news: dict, api_url: str):
    try:
        response = requests.post(
            f"{api_url}/news",
            json=news,
            timeout=10
        )

        if response.status_code == 201:
            logger.info(f"Notícia enviada com sucesso: {news['title']}")

        elif response.status_code == 409:
            logger.warning(f"Notícia duplicada: {news['url']}")

        else:
            logger.error(
                f"Erro API {response.status_code}: {response.text}"
            )

    except requests.RequestException as e:
        logger.exception("Erro ao conectar na API")