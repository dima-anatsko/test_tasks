import aiohttp

import pandas as pd
from pydantic import BaseModel
from typing import List, Dict


WILDBERRIES_URL = "https://card.wb.ru/cards/detail?nm=%s"


class Product(BaseModel):
    article: int
    brand: str
    title: str

    def __init__(self, **kwargs):
        kwargs["article"] = kwargs["data"]["products"][0]["id"]
        kwargs["brand"] = kwargs["data"]["products"][0]["brand"]
        kwargs["title"] = kwargs["data"]["products"][0]["name"]
        super().__init__(**kwargs)


def get_articles_from_file(file_obj) -> List:
    df = pd.read_excel(file_obj)
    return df.iloc[:, 0].tolist()


async def get_data_from_wildberries(articles: List[int]) -> Dict | List[Dict]:
    data = []
    async with aiohttp.ClientSession() as session:
        for article in articles:
            async with session.get(WILDBERRIES_URL % article) as resp:
                article_data = await resp.json(content_type='text/plain')
                try:
                    data.append(Product.parse_obj(article_data).dict())
                except (TypeError, KeyError):
                    continue
    return data[0] if len(data) == 1 else data
