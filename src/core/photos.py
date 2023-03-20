from src.core import Unsplash


class Photos(Unsplash):
    def __init__(self):
        super().__init__()
        link = "photos/?client_id="
        self.photos_url = self.url + link + self.client_id

    @staticmethod
    def photos(page: int, per_page: int, order_by: str, *args, **kwargs):
        """
        :param page: Page number to retrieve. (Optional; default: 1)
        :param per_page: Number of items per page. (Optional; default: 10)
        :param order_by:  How to sort the photos. Optional. (Valid values: latest, oldest, popular; default: latest)
        :return: `photos` parameters (dict)
        """
        params = {
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
        return data.json()
