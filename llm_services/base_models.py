from pydantic import BaseModel, Field

# ----------------- Checklist Generation ----------------- #
class ChecklistItem(BaseModel):
    ids: list[str] = Field(..., description="A list of the complete IDs used to create the checklist item")
    title: str = Field(..., description="The title of the checklist item")
    description: list[str] = Field(..., description="A list of questions for the checklist item")

class ChecklistModel(BaseModel):
    work_product: str = Field(..., description="The work product for which the checklist is generated")
    checklist_items: list[ChecklistItem] = Field(..., description="A list of checklist items for a requirement")