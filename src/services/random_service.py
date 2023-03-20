from src.classes import Random


def random_service(query: str, count: int):
    obj = Random()
    params = obj.random(query=query, count=count)
    response = obj.request(url=obj.random_url, params=params)
    formatted_data = obj.json_data(data=response)
    json = obj.json_formatter(data=formatted_data)
    df = obj.df_formatter(data=json)
    return df
