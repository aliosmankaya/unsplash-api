from src.core import Unsplash


class Search(Unsplash):
    def __init__(self):
        super().__init__()
        link = "search/photos?client_id="
        self.search_url = self.url + link + self.client_id

    @staticmethod
    def search(query: str, page: int, per_page: int, order_by: str, *args, **kwargs):
        """
        :param query: Search terms. (Optional; default: `nature`)
        :param page: Page number to retrieve. (Optional; default: 1)
        :param per_page: Number of items per page. (Optional; default: 10)
        :param order_by: How to sort the photos. (Optional; default: relevant). Valid values are `latest` and `relevant`
        :return: `search` parameters (dict)
        """
        params = {
            "query": query,
            "page": page,
            "per_page": per_page,
            "order_by": order_by
        }

        if len(args) and len(kwargs) != 0:
            for i, j in zip(kwargs["args"], kwargs["kwargs"]):
                params[j] = i

        return params

    @staticmethod
    def json_data(data):
        return data.json()["results"]
