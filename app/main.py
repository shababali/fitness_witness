import json

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# cross-origin resource sharing between for frontend svelte
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
async def root():
    # # get food data
    with open("foods.json") as f:
        data = json.load(f)
    return data


@app.post("/")
# TODO: fix the handling here...
async def root(post):
    print(post)
    pass