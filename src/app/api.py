from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from src.models import Search, Photos, Random
from src.services import search_service, photos_service, random_service

app = FastAPI(description="Unsplash API")

origins = ["*"]

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
        res = search_service(
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
        res = photos_service(page=photos.page, per_page=photos.per_page, order_by=photos.order_by)
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
        res = random_service(query=random.query, count=random.count)
        return JSONResponse(
            status_code=200, content=res
        )

    except Exception as e:
        return JSONResponse(
            status_code=500, content=e
        )
