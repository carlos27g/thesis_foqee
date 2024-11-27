import os
from llm_services.base_models import ChecklistItem, ChecklistModel 

messages = []

def add_message(role, content, basemodel=None):
    """Add a message to the messages list with classification."""
    if basemodel:
        classification = classify_basemodel(basemodel)
        file_name = f"messages_{classification}.txt"
    else:
        file_name = "messages_unclassified.txt"

    # Save message with role and content
    messages.append(f"{role}: {content}\n")
    if role == "SYSTEM":
        messages.append("# -------------------------------------------------- #\n")
    
    save_messages(file_name)

def classify_basemodel(basemodel):
    """Classify the base model into a specific functionality."""
    if issubclass(basemodel, (ChecklistItem, ChecklistModel)):
        return "checklist_generation"
    else:
        return "unclassified" 

def save_messages(file_name):
    """Save the messages to a text file classified by functionality."""
    if messages:
        current_path = os.getcwd()
        relative_path = "messages"
        output_folder = os.path.join(current_path, relative_path)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        output_path = os.path.join(output_folder, file_name)
        with open(output_path, 'w') as f:
            for message in messages:
                f.write(message + "\n")

