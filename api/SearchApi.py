import requests


class SearchApi:
    # def __init__(self) -> None:
    base_url = "https://www.labirint.ru/"
    
    def search_item_by_id(self, product_id: int):
        path = "{labirint}/books/{id}/".format(labirint=self.base_url,
                                               id=product_id)
        print(path)
        resp = requests.get(path)

        return resp.json()