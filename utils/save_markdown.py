"""
This script contains a function to generate a Markdown document from a ChecklistModel 
instance and save it as a file.

Functions:
    save_checklist_to_markdown(checklist_model: ChecklistModel)
"""
import os

from llm_services.models_checklist import ChecklistModel
from llm_services.models_context import WorkProductContextModel

def save_checklist_to_markdown(checklist_model: ChecklistModel, work_product: str):
    """
    Generates a Markdown document from a ChecklistModel instance and saves it as a file.
    """
    # Replace spaces with underscores and remove problematic characters for filenames
    safe_work_product = "".join(
        c if c.isalnum() or c in (' ', '_') else '_'
        for c in work_product
    )
    filename = f"{safe_work_product.replace(' ', '_')}_checklist.md"

    markdown_lines = [f"# {work_product}\n"]

    for idx, item in enumerate(checklist_model.checklist_items, start=1):
        markdown_lines.append(f"## Item {idx}: {item.title}\n")
        markdown_lines.append("**Questions:**\n")

        # Iterate over each question in the description list
        for question_idx, question in enumerate(item.description, start=1):
            markdown_lines.append(f"{question_idx}. {question}")

        markdown_lines.append("\n**IDs:**\n")
        for id_ in item.ids:
            markdown_lines.append(f"- {id_}")
        markdown_lines.append("\n")  # Add an empty line for better formatting

    markdown_content = "\n".join(markdown_lines)

    # Determine the current working directory
    path_folder = os.path.abspath(os.getcwd())
    markdowns_dir = os.path.join(path_folder, 'markdowns', 'markdowns_checklists')

    # Create the 'markdowns' directory if it doesn't exist
    os.makedirs(markdowns_dir, exist_ok=True)

    # Define the full file path
    file_path = os.path.join(markdowns_dir, filename)

    with open(file_path, 'w', encoding='utf-8') as md_file:
        md_file.write(markdown_content)

    print(f"Markdown file '{filename}' has been created.")


def save_context_to_markdown(context: WorkProductContextModel, workproduct):
    """
    Generate and save a Markdown file based on the content of a WorkProductContextModel.

    Args:
        context (WorkProductContextModel): The context object to save as Markdown.
        filename (str): The filename for the saved Markdown file.
    """
    # Initialize Markdown content
    md_content = []

    # Add Description section
    md_content.append("# Work Product Description")
    md_content.append("## Purpose")
    md_content.append("### Purpose in ISO26262")
    md_content.append(f"{context.description.purpose.purpose_iso}")
    md_content.append("### Purpose in Automotive SPICE")
    md_content.append(f"{context.description.purpose.purpose_aspice}")
    md_content.append("## Content")
    md_content.append(f"{context.description.content}")
    md_content.append("## Input")
    md_content.append(f"{context.description.input}")
    md_content.append("## Uses")
    md_content.append(f"{context.description.uses}")
    md_content.append("")

    # Add Concepts section
    md_content.append("# Concepts")

    # Add Terminology ISO section
    md_content.append("## Terminology (ISO)")
    for term in context.concepts.terminology_iso.terms:
        md_content.append(f"- **{term.term}:** {term.definition}")
    md_content.append("")

    # Add Abbreviations section
    md_content.append("## Abbreviations")
    for abbr in context.concepts.abbreviations.abbreviations:
        md_content.append(f"- **{abbr.abbreviation}:** {abbr.definition}")
    md_content.append("")

    # Add Disambiguation section
    md_content.append("## Disambiguation")
    for entry in context.concepts.disambiguation.entries:
        md_content.append(f"**{entry.concept}**")
        md_content.append(f"- **Definition:** {entry.definition}")
        md_content.append(f"- **Purpose:** {entry.purpose}")
        if entry.examples:
            md_content.append(f"- **Examples:** {', '.join(entry.examples)}")
        if entry.elements:
            md_content.append(f"- **Elements:** {', '.join(entry.elements)}")
        if entry.example_elements:
            md_content.append(f"- **Example Elements:** {', '.join(entry.example_elements)}")
        if entry.terminology_iso26262:
            md_content.append(f"- **Terminology (ISO 26262):** {entry.terminology_iso26262}")
        if entry.terminology_aspice:
            md_content.append(f"- **Terminology (ASPICE):** {entry.terminology_aspice}")
        md_content.append("")

    # Replace spaces with underscores and remove problematic characters for filenames
    safe_work_product = "".join(c if c.isalnum() or c in (' ', '_') else '_' for c in workproduct)
    filename = f"{safe_work_product.replace(' ', '_')}_context.md"

    # Determine the parent directory of the current working directory
    parent_dir = os.path.abspath(os.path.join(os.getcwd()))
    markdowns_dir = os.path.join(parent_dir, 'markdowns', 'markdowns_contexts')

    # Create the 'markdowns' directory if it doesn't exist
    os.makedirs(markdowns_dir, exist_ok=True)

    # Define the full file path
    file_path = os.path.join(markdowns_dir, filename)

    with open(file_path, 'w', encoding='utf-8') as md_file:
        md_file.write("\n".join(md_content))  # Join the content list into a single string

    print(f"Markdown file '{filename}' has been created.")

