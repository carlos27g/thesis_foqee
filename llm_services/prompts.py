# ----------------- System Role ----------------- #
def prompt_system_role() -> list[str]:
    prompt = (
        "You are a compliance auditor for ISO26262 and Automotive SPICE (ASPICE) in software and hardware "
        "development in an automotive company, you are advising in how to fulfill the standards necessary "
        "for developing a new system."
    )
    return prompt

# ----------------- Checklist Generation ----------------- #
def prompt_generate_checklist(workproduct, content) -> str:
    prompt = (
        f"You are tasked with generating a comprehensive checklist to support tracking and compliance of **{workproduct}** within the ISO 26262 and Automotive SPICE standard frameworks for the automotive industry.\n\n"
        f"**Objective:**\n"
        f"- Create a checklist that serves as a practical guide of actionable items and questions.\n"
        f"- Ensure that following the checklist will fulfill the standard requirements.\n"
        f"- The checklist should be clear, concise, and organized by related topics.\n"
        f"- Provide enough information for the end user to understand what needs to be done to comply with the standards without needing to read the frameworks themselves.\n\n"
        f"**Task:**\n"
        f"1. **Thoroughly analyze the provided content of requirements** related to compliance.\n"
        f"2. **For each checklist item:**\n"
        f"   - Include the **IDs** of all the requirements that are relevant to the item.\n"
        f"     - Present the IDs as a list.\n"
        f"   - Provide a **title** for the item that encapsulates the main theme.\n"
        f"   - Write a list of **specific, actionable questions** that guide the user on what needs to be addressed for compliance.\n"
        f"     - Ensure the questions are closed questions (yes or no).\n"
        f"     - Ensure the questions are clear and concise.\n\n"
        f"**Content to use for generating the Checklist:**\n"
    )
    for req_id, details in content.items():
        prompt += (
            f"- **Requirement ID:** {req_id}\n"
            f"  - **Description:** {details['Description']}\n"
        )
    return prompt