"""
This module contains data validation classes used for structured outcomes generation with the LLM
for the final step of generating the checklists. 

Classes:
- ChecklistItem
- ChecklistModel
"""

from pydantic import BaseModel, Field

class ChecklistItem(BaseModel):
    """
    Represents an individual checklist item, including IDs, title, and associated questions.
    """
    ids: list[str] = Field(
        ...,
        description="A list of the complete IDs used to create the checklist item")
    title: str = Field(..., description="The title of the checklist item")
    description: list[str] = Field(..., description="A list of questions for the checklist item")


class ChecklistModel(BaseModel):
    """
    Represents a structured checklist for a given work product, including associated checklist 
    items.
    """
    work_product: str = Field(
        ...,
        description="The work product for which the checklist is generated")
    checklist_items: list[ChecklistItem] = Field(
        ...,
        description="A list of checklist items for a requirement")
