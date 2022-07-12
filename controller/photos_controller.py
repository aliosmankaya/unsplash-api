from services import photos_service


def photos_controller(page: int, per_page: int, order_by: str):
    df = photos_service(page=page, per_page=per_page, order_by=order_by)

    return df.to_dict("records")
