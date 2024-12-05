"""
This module contains data validation classes used for structured outcomes generation with the LLM
for the step of generating context for work product.

Classes:
- PurposeModel
- DescriptionModel
- TermModel
- TermListModel
- DisambiguationEntryModel
- DisambiguationModel
- AbbreviationModel
- AbbreviationListModel
- ConceptsModel
- WorkProductContextModel
"""

from pydantic import BaseModel, Field

# ----------------- For Contextualization of WP ----------------- #
# ----- For Description ----- #
class PurposeModel(BaseModel):
    purpose_iso: str = Field(..., description="The purpose of the work product according to ISO 26262")
    purpose_aspice: str = Field(..., description="The purpose of the work product according to ASPICE")

class DescriptionModel(BaseModel):
    purpose: PurposeModel = Field(..., description="The purpose of the work product")
    content: str = Field(..., description="The content description of the work product")
    input: str = Field(..., description="The input data for the work product")
    uses: str = Field(..., description="The uses of the work product")

# ----- For Concepts ----- #
class TermModel (BaseModel):
    term: str = Field(..., description="The term in the glossary")
    definition: str = Field(..., description="The description of the term in the glossary")

class TermListModel (BaseModel):
    terms: list[TermModel] = Field(..., description="A list of relevant terms for a given work product")

class DisambiguationEntryModel(BaseModel):
    concept: str = Field(..., description="The concept being disambiguated")
    definition: str = Field(..., description="The definition of the concept")
    purpose: str = Field(..., description="The purpose of the concept")
    examples: list[str] = Field(..., description="Examples demonstrating the concept")
    elements: list[str] = Field(..., description="Related elements of the concept")
    example_elements: list[str] = Field(..., description="Example elements of the concept")
    terminology_iso26262: str = Field(..., description="ISO 26262-related terminology for the concept")
    terminology_aspice: str = Field(..., description="ASPICE-related terminology for the concept")

class DisambiguationModel(BaseModel):
    entries: list[DisambiguationEntryModel] = Field(..., description="A list of disambiguation entries for the work product")

class AbbreviationModel(BaseModel):
    abbreviation: str = Field(..., description="The abbreviation in the glossary")
    definition: str = Field(..., description="The definition of the abbreviation in the glossary")

class AbbreviationListModel(BaseModel):
    abbreviations: list[AbbreviationModel] = Field(..., description="A list of relevant abbreviations for a given work product")

class ConceptsModel(BaseModel):
    terminology_iso: TermListModel = Field(..., description="The ISO terminology model")
    disambiguation: DisambiguationModel = Field(..., description="The disambiguation concepts")
    abbreviations: AbbreviationListModel = Field(..., description="The abbreviation list")

class WorkProductContextModel(BaseModel):
    description: DescriptionModel = Field(..., description="The description of the work product")
    concepts: ConceptsModel = Field(..., description="The concepts related to the work product")
    