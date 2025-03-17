"""
This module provides functionality to add and classify messages, and save them to text files.

Functions:
    add_message(role, content, basemodel=None):
        Adds a message to the messages list with classification based on the provided base model.
    
    classify_basemodel(basemodel):
        Classifies the base model into a specific functionality.
    
    save_messages(file_name):
        Saves the messages to a text file classified by functionality.
"""
import os

from llm_services.models_checklist import ChecklistItem, ChecklistModel
from llm_services.models_content import (
    TopicslistModel, RequirementDescriptionModel, TopicModel, NoInfoModel, IdentifyInformationModel,
    TableModel, IdentifyTablesModel, ClauseModel, ClauseSummaryModel, IdentifyClausesModel,
    RequirementIdModel, IdentifyExternalIdsModel)
from llm_services.models_context import (
    DescriptionModel, PurposeModel, TermModel, TermListModel, DisambiguationEntryModel,
    DisambiguationModel, AbbreviationModel, AbbreviationListModel, ConceptsModel,
    WorkProductContextModel)

from evaluation.evaluation_models import (
    RubricQuestionModel, RubricChecklistModel, RubricRequirementModel
)      


messages_unclassified = []
messages_checklist_generation = []
messages_content_segmentation = []
messages_context_generation = []
messages_evaluation = []

def add_message(role, content, basemodel=None):
    """Add a message to the messages list with classification."""
    classification = "unclassified"
    if basemodel:
        classification = classify_basemodel(basemodel)
        file_name = f"messages_{classification}.txt"
    else:
        file_name = "messages_unclassified.txt"

    if classification == "checklist_generation":
        messages_checklist_generation.append(f"{role}: {content}\n")
        if role == "SYSTEM":
            messages_checklist_generation.append(
                "# -------------------------------------------------- #\n")
    elif classification == "content_segmentation":
        messages_content_segmentation.append(f"{role}: {content}\n")
        if role == "SYSTEM":
            messages_content_segmentation.append(
                "# -------------------------------------------------- #\n")
    elif classification == "context_generation":
        messages_context_generation.append(f"{role}: {content}\n")
        if role == "SYSTEM":
            messages_context_generation.append(
                "# -------------------------------------------------- #\n")
    elif classification == "evaluation":
        messages_unclassified.append(f"{role}: {content}\n")
        if role == "SYSTEM":
            messages_evaluation.append(
                "# -------------------------------------------------- #\n")
    else:
        messages_unclassified.append(f"{role}: {content}\n")
        if role == "SYSTEM":
            messages_unclassified.append(
                "# -------------------------------------------------- #\n")
    save_messages(file_name, classification)


def classify_basemodel(basemodel):
    """Classify the base model into a specific functionality."""
    if issubclass(basemodel, (ChecklistItem, ChecklistModel)):
        return "checklist_generation"
    if issubclass(basemodel, (TopicslistModel, RequirementDescriptionModel, TopicModel, NoInfoModel,
                              IdentifyInformationModel, TableModel, IdentifyTablesModel,
                              ClauseModel, ClauseSummaryModel, IdentifyClausesModel,
                              RequirementIdModel, IdentifyExternalIdsModel)):
        return "content_segmentation"
    if issubclass(basemodel, (
            DescriptionModel, PurposeModel, TermModel, TermListModel, DisambiguationEntryModel,
            DisambiguationModel, AbbreviationModel, AbbreviationListModel, ConceptsModel,
            WorkProductContextModel
    )):
        return "context_generation"
    if issubclass(basemodel, (
        RubricQuestionModel, RubricRequirementModel, RubricChecklistModel
        )):
        return "evaluation"
    return "unclassified"

def save_messages(file_name, classification):
    """Save the messages to a text file classified by functionality."""
    if classification == "checklist_generation":
        messages = messages_checklist_generation
        relative_path = "messages_checklist_generation"
    elif classification == "content_segmentation":
        messages = messages_content_segmentation
        relative_path = "messages_content_segmentation"
    elif classification == "context_generation":
        messages = messages_context_generation
        relative_path = "messages_context_generation"
    else:
        messages = messages_unclassified
        relative_path = "messages_unclassified"

    current_path = os.getcwd()
    output_folder = os.path.join(current_path, "messages", relative_path)
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, file_name)

    with open(output_path, 'w', encoding='utf-8') as f:
        for message in messages:
            role, content = message.split(": ", 1)
            if role == "SYSTEM":
                # Add a delimiter for system messages
                f.write("\n# -------------------------------------------------- #\n")
                f.write(f"Role: {role}\n")
                f.write(f"Message:\n{content}\n")
                f.write("# -------------------------------------------------- #\n\n")
            else:
                # Write other messages normally
                f.write(f"Role: {role}\nMessage:\n{content}\n\n")
