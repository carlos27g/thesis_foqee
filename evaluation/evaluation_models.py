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

from typing import Literal

from pydantic import BaseModel, Field

class EvaluationModel(BaseModel):
    """
    EvaluationModel is a Pydantic model used to evaluate questions, checklists, and requirements.
    """
    score: int = Field(
        ...,
        description="A qualification between 1 and 3 (3 being the best) indicating the score for the given evaluation."
    )
    notes: str = Field(
        ...,
        description="Notes providing arguments or explanations for the given qualification."
    )

class RubricQuestionModel(EvaluationModel):
    """
    EvaluationQuestionModel is a Pydantic model used to evaluate questions 
    based on several criteria such as traceability, correctness, redundancy, 
    and applicability. Each criterion is accompanied by notes providing 
    arguments or explanations for the given qualifications.
    """
    rubric: Literal['traceability', 'correctness', 'redundancy', 'applicability'] = Field(
        ...,
        description="The rubric name indicating the evaluation criterion."
    )


class RubricChecklistModel(EvaluationModel):
    """
    EvaluationChecklistModel is a Pydantic model used to evaluate checklists
    based on two criteria: Applicability and Consistency.
    Each criterion is accompanied by notes providing arguments or explanations for the given 
    qualifications.
    """
    rubric = Literal['applicability', 'consistency'] = Field(
        ...,
        description="The rubric name indicating the evaluation criterion."
    )


class RubricRequirementModel(EvaluationModel):
    """
    EvaluationRequirementModel is a Pydantic model used to evaluate requirements
    based on the criterion of Traceablity and Completeness.
    """
    rubric = Literal['traceability', 'completeness'] = Field(
        ...,
        description="The rubric name indicating the evaluation criterion."
    )
