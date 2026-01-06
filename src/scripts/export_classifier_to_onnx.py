import os

import joblib
import onnx
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

from settings import Settings


def export_classifier_to_onnx(settings: Settings):
    print(f"Loading classifier from {settings.classifier_joblib_path}...")
    classifier = joblib.load(settings.classifier_joblib_path)

    # define input shape: (batch_size, embedding_dim)
    initial_type = [("float_input", FloatTensorType([None, settings.embedding_dim]))]

    print("Converting to ONNX...")
    onnx_model = convert_sklearn(classifier, initial_types=initial_type)  # TODO: complete conversion here

    print(f"Saving ONNX model to {settings.onnx_classifier_path}...")
    os.makedirs(os.path.dirname(settings.onnx_classifier_path), exist_ok=True)
    onnx.save_model(onnx_model, settings.onnx_classifier_path)

if __name__ == "__main__":
    export_classifier_to_onnx(Settings())