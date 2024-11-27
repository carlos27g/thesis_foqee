import os

from llm_services.base_models import ChecklistModel

def save_checklist_to_markdown(checklist_model: ChecklistModel):
    """
    Generates a Markdown document from a ChecklistModel instance and saves it as a file.

    :param checklist: An instance of ChecklistModel containing the checklist data.
    """
    # Replace spaces with underscores and remove problematic characters for filenames
    safe_work_product = "".join(c if c.isalnum() or c in (' ', '_') else '_' for c in checklist_model.work_product)
    filename = f"{safe_work_product.replace(' ', '_')}_checklist.md"

    markdown_lines = [f"# {checklist_model.work_product}\n"]

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