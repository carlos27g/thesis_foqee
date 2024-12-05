"""
This module contains data validation classes used for structured outcomes generation with the LLM
for the step of extracting the ISO26262 external knowledge retrieval.

Classes:
- DescriptionModel
- TopicModel
- TopicslistModel
- NoInfoModel
- IdentifyInformationModel
- TableModel
- IdentifyTablesModel
- ClauseModel
- ClauseSummaryModel
- IdentifyClausesModel
- RequirementIdModel
- IdentifyExternalIdsModel
"""

from typing import Literal
from pydantic import BaseModel, Field


# ------------------ Model Requirement Description ------------------ #
class DescriptionModel(BaseModel):
    """
    Represents the description of a requirement.
    """
    description: str = Field(
        ..., description="The description of the requirement.")

# ------------------ Model Topic Groups ------------------ #
class TopicModel(BaseModel):
    """
    Represents a topic for a work product.
    """
    topic: str = Field(
        ..., description="The topic for a work product.")
    ids: list[str] = Field(
        ..., description="A list of the IDs used to create the checklist item")

class TopicslistModel(BaseModel):
    """
    Represents a list of topics for a work product.
    """
    topics: list[TopicModel] = Field(
        ..., description="A list of topics for a work product.")

# ------------------ Models ISO ------------------ #
class NoInfoModel(BaseModel):
    """
    Represents the idea that when the LLM does not find a table or a clause, it returns 
    a NoneModel with the boolean set to true indicating no information found.
    """
    no_information_found: bool = Field(
        ..., description="Indicates that no information was found.")


class IdentifyInformationModel(BaseModel):
    """
    Represents information about a standard and its part number.
    """
    standard_name: Literal['ISO 26262', 'ASPICE'] = Field(
        ..., description="The name of the standard, either ISO 26262 or ASPICE.")
    part_number: int = Field(
        ..., description="The part of the standard, where the table is at.")


class TableModel(IdentifyInformationModel):
    """
    Extends IdentifyInformationModel to include table-specific information.
    """
    table_number: int = Field(
        ..., description="The number of the table in the part.")


class IdentifyTablesModel(BaseModel):
    """
    Represents a collection of table models.
    """
    tables: list[TableModel] = Field(
        ..., description="A list of table model instances.")


class ClauseModel(IdentifyInformationModel):
    """
    Extends IdentifyInformationModel to include clause-specific information.
    """
    clause_number: int = Field(
        ..., description="The number of the clause in the part.")


class ClauseSummaryModel(ClauseModel):
    """
    Extends ClauseModel to include a summary of the clause.
    """
    summary: str = Field(
        ..., description="A summary of the clause.")


class IdentifyClausesModel(BaseModel):
    """
    Represents a collection of clause models.
    """
    clauses: list[ClauseModel] = Field(
        ..., description="A list of clause model instances.")


class RequirementIdModel(ClauseModel):
    """
    Extends ClauseModel to include section and subsection-specific information.
    """
    section_number: int = Field(
        ..., description="The number of the section in the clause.")
    subsection_number: int = Field(
        ..., description="The id in the section. Default is 0.")
    subsubsection_number: int = Field(
        ..., description="The id in the subsection. Default is 0.")


class IdentifyExternalIdsModel(BaseModel):
    """
    Represents a collection of external id models.
    """
    external_ids: list[RequirementIdModel] = Field(
        ..., description="A list of external id model instances.")
