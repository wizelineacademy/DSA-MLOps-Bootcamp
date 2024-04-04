import pickle
import re
from pathlib import Path

__version__ = "1.0.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/trained_model-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)

with open(f"{BASE_DIR}/language_dec-{__version__}.pkl", "rb") as f:
    decoder = pickle.load(f)


def predict_pipeline(text):
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', " ", text)
    text = re.sub(r"[[]]", " ", text)
    text = text.lower()
    pred = model.predict([text])
    return decoder[pred[0]]
