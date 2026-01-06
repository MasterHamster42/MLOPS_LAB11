from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BUCKET_NAME: str = "mlops-lab11-models-jakub-zhf4"

    ARTIFACTS_DIR: str = "models"
    ONNX_DIR: str = "models/onnx"

    classifier_joblib_path: str = f"{ARTIFACTS_DIR}/classifier.joblib"
    sentence_transformer_path: str = f"{ARTIFACTS_DIR}/sentence_transformer.model"

    onnx_classifier_path: str = f"{ONNX_DIR}/classifier.onnx"
    onnx_embedding_model_path: str = f"{ONNX_DIR}/embeddings.onnx"
    onnx_tokenizer_path: str = f"{ONNX_DIR}/tokenizer/tokenizer.json"

    embedding_dim: int = 384