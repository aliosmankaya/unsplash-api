from services import random_service


def random_controller(query: str, count: int):
    df = random_service(query=query, count=count)

    return df.to_dict("records")
