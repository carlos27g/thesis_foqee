"""
This module defines Pydantic models for evaluating the checklist on a question level, 
checklists level, and requirements level, based on various criteria.

Classes:
    EvaluationQuestionModel: Based on traceability, correctness, redundancy, and 
                             applicability.
    EvaluationChecklistModel: Based on applicability and consistency.
    EvaluationRequirementModel: Based on traceability and completeness.

Each model includes fields for the criteria and accompanying notes providing arguments or 
explanations for the given qualifications.
"""

from pydantic import BaseModel, Field

class EvaluationQuestionModel(BaseModel):
    """
    EvaluationQuestionModel is a Pydantic model used to evaluate questions 
    based on several criteria such as traceability, correctness, redundancy, 
    and applicability. Each criterion is accompanied by notes providing 
    arguments or explanations for the given qualifications.
    """
    traceability: int = Field(
        ...,
        description="A qualification between 1 and 3 (3 being the best) indicating if each "
        "question is traced to at least one requirement."
    )
    traceability_notes: str = Field(
        ...,
        description="Notes providing arguments or explanations for the traceability qualification."
    )
    correctness: int = Field(
        ...,
        description="A qualification between 1 and 3 (3 being the best) indicating if the question "
                    "captures at least part of the information from the requirements it traces to."
    )
    correctness_notes: str = Field(
        ...,
        description="Notes providing arguments or explanations for the correctness qualification."
    )
    redundancy: int = Field(
        ...,
        description="A qualification between 1 and 3 (3 being the best) indicating if the question "
                    "is free of criteria that are not derived from any traced requirement."
    )
    redundancy_notes: str = Field(
        ...,
        description="Notes providing arguments or explanations for the redundancy qualification."
    )
    applicability: int = Field(
        ...,
        description="A qualification between 1 and 3 (3 being the best) indicating if the question "
                    "can be answered by looking just at the work product."
    )
    applicability_notes: str = Field(
        ...,
        description="Notes providing arguments or explanations for the applicability qualification."
    )


class EvaluationChecklistModel(BaseModel):
    """
    EvaluationChecklistModel is a Pydantic model used to evaluate checklists
    based on two criteria: Applicability and Consistency.
    Each criterion is accompanied by notes providing arguments or explanations for the given 
    qualifications.
    """
    applicability: int = Field(
        ...,
        description="A qualification between 1 and 3 (3 being the best) indicating if the "
                    "checklist can be applied to the work product."
    )
    applicability_notes: str = Field(
        ...,
        description="Notes providing arguments or explanations for the applicability qualification."
    )
    consistency: int = Field(
        ...,
        description="A qualification between 1 and 3 (3 being the best) indicating if the "
                    "checklist is consistent with the requirements."
    )
    consistency_notes: str = Field(
        ...,
        description="Notes providing arguments or explanations for the consistency qualification."
    )


class EvaluationRequirementModel(BaseModel):
    """
    EvaluationRequirementModel is a Pydantic model used to evaluate requirements
    based on the criterion of Traceablity and Completeness.
    """
    traceability: int = Field(
        ...,
        description="A qualification between 1 and 3 (3 being the best) indicating if the "
                    "requirement is traced to at least one question."
    )
    traceability_notes: str = Field(
        ...,
        description="Notes providing arguments or explanations for the traceability qualification."
    )
    completeness: int = Field(
        ...,
        description="A qualification between 1 and 3 (3 being the best) indicating if the relevant "
                    "information of each requirement is captured by a checklist question it "
                    "traces to."
    )
    completeness_notes: str = Field(
        ...,
        description="Notes providing arguments or explanations for the completeness qualification."
    )
