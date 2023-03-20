from src.core.search import Search


def search_service(query: str, page: int, per_page: int, order_by: str):
    obj = Search()
    params = obj.search(query=query, page=page, per_page=per_page, order_by=order_by)
    response = obj.request(url=obj.search_url, params=params)
    json_data = obj.json_data(data=response)
    formatted_data = obj.json_formatter(data=json_data)
    df = obj.df_formatter(data=formatted_data)
    return df
