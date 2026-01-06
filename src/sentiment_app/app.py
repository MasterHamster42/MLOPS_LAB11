from fastapi import FastAPI
from mangum import Mangum

from src.sentiment_app.api.schema import PredictResponse, PredictRequest

from src.scripts.settings import Settings
from src.sentiment_app.inference import load_classier, predict_sentiment, load_embedding_model, load_tokenizer

settings = Settings()


classier_model = load_classier(settings)
embedding_model = load_embedding_model(settings)
tokenizer = load_tokenizer(settings)

app = FastAPI()


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    sentiment = predict_sentiment(text=request.text, classier_model=classier_model, tokenizer=tokenizer, embedding_model=embedding_model)
    return PredictResponse(prediction=sentiment)


@app.get("/health")
def health_check():
    return {"status": "ok"}


handler = Mangum(app)