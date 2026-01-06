import numpy as np
import onnxruntime as ort
from onnxruntime import InferenceSession
from tokenizers import Tokenizer

from src.scripts.settings import Settings


SENTIMENT_MAP = {
    0:'NEGATIVE',
    1:'NEUTRAL',
    2:'POSITIVE',
}

def load_classier(settings: Settings):
    return ort.InferenceSession(settings.onnx_classifier_path)

def load_embedding_model(settings: Settings):
    return ort.InferenceSession(settings.onnx_embedding_model_path)

def load_tokenizer(settings: Settings):
    return Tokenizer.from_file(settings.onnx_tokenizer_path)


def predict_sentiment(
        text: str,
        classier_model: InferenceSession,
        tokenizer: Tokenizer,
        embedding_model: InferenceSession
) -> str:
    encoded = tokenizer.encode(text)

    # prepare numpy arrays for ONNX
    input_ids = np.array([encoded.ids])
    attention_mask = np.array([encoded.attention_mask])

    # run embedding inference
    embedding_inputs = {"input_ids": input_ids, "attention_mask": attention_mask}
    embeddings = embedding_model.run(None, embedding_inputs)[0]

    # run classifier inference
    classifier_input_name = classier_model.get_inputs()[0].name
    classifier_inputs = {classifier_input_name: embeddings.astype(np.float32)}
    prediction = classier_model.run(None, classifier_inputs)[0]

    label = SENTIMENT_MAP.get(prediction[0], "unknown")

    return label
