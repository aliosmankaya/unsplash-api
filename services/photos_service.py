from classes import Photos


def photos_service(page: int, per_page: int, order_by: str):
    obj = Photos()
    params = obj.photos(page=page, per_page=per_page, order_by=order_by)
    response = obj.request(url=obj.photos_url, params=params)
    json_data = obj.json_data(response)
    formatted_data = obj.json_formatter(data=json_data)
    df = obj.df_formatter(data=formatted_data)
    return df
