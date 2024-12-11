"""
This module provides utility functions to save and load Pydantic models using pickle.

Functions:
- save_models(file_name: str, model: BaseModel) -> None:

- load_models(file_name: str, base_model: BaseModel) -> BaseModel:
"""

import os
import json

import pickle
from pydantic import BaseModel

def save_models(file_name: str, model: BaseModel) -> None:
    """
    Saves the context models to a pickle file in a 'models_saved' folder.

    Args:
    - file_name (str): Name of the file to save the model as (without extension).
    - model (BaseModel): Pydantic model instance to save.
    """
    folder_name = "models_saved"
    os.makedirs(folder_name, exist_ok=True)

    file_path = os.path.join(folder_name, f"{file_name}.pkl")

    with open(file_path, "wb") as file:
        pickle.dump(model.model_dump(), file)

    print(f"Model saved successfully to {file_path}")


def load_models(file_name: str, base_model: BaseModel) -> BaseModel:
    """
    Loads the context models from a pickle file in a 'models_saved' folder.

    Args:
    - file_name (str): Name of the file to load the model from (without extension).

    Returns:
    - model (BaseModel): Pydantic model instance loaded from the file.
    """
    folder_name = "models_saved"
    file_path = os.path.join(folder_name, f"{file_name}.pkl")

    if not os.path.exists(file_path):
        print(f"No model found at {file_path}")
        return None

    with open(file_path, "rb") as file:
        model_dict = pickle.load(file)

    model_json = json.dumps(model_dict)
    model = base_model.model_validate_json(model_json)
    print(f"Model loaded successfully from {file_path}")

    return model
