from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from models import Search, Photos, Random
from controller import search_controller, photos_controller, random_controller

app = FastAPI(description="Unsplash API")

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/search")
def get_search(search=Depends(Search)):
    try:
        res = search_controller(
            query=search.query,
            page=search.page,
            per_page=search.per_page,
            order_by=search.order_by
        )
        return JSONResponse(
            status_code=200, content=res
        )

    except Exception as e:
        return JSONResponse(
            status_code=500, content=e
        )


@app.get("/photos")
def get_photos(photos=Depends(Photos)):
    try:
        res = photos_controller(page=photos.page, per_page=photos.per_page, order_by=photos.order_by)
        return JSONResponse(
            status_code=200, content=res
        )

    except Exception as e:
        return JSONResponse(
            status_code=500, content=e
        )


@app.get("/random")
def get_random(random=Depends(Random)):
    try:
        res = random_controller(query=random.query, count=random.count)
        return JSONResponse(
            status_code=200, content=res
        )

    except Exception as e:
        return JSONResponse(
            status_code=500, content=e
        )
