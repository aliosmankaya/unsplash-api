from services import search_service


def search_controller(query: str, page: int, per_page: int, order_by: str):
    df = search_service(query=query, page=page, per_page=per_page, order_by=order_by)

    return df.to_dict("records")
