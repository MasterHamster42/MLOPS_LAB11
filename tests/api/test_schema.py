import pytest
from pydantic import ValidationError
from src.sentiment_app.api.schema import PredictRequest

def test_predict_request_valid():
    payload = {"text": "Test sentence"}
    request = PredictRequest(**payload)
    assert request.text == "Test sentence"

def test_predict_request_invalid():
    with pytest.raises(ValidationError):
        PredictRequest(text=12345)