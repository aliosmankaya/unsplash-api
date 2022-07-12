from classes import Unsplash


class Random(Unsplash):
    def __init__(self):
        super().__init__()
        link = "photos/random?client_id="
        self.random_url = self.url + link + self.client_id

    @staticmethod
    def random(query: str, count: int, *args, **kwargs):
        """
        :param query: Limit selection to photos matching a search term. (Optional; default: `nature`)
        :param count: The number of photos to return. (Default: 1; max: 30)
        :return: `random` parameters (dict)
        """
        params = {
            "query": query,
            "count": count
        }

        if len(args) and len(kwargs) != 0:
            for i, j in zip(kwargs["args"], kwargs["kwargs"]):
                params[j] = i

        return params

    @staticmethod
    def json_data(data):
        return data.json()
