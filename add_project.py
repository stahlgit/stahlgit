import re
import os
from datetime import datetime

# Configuration
FILE_NAME = "projects.md"
ANCHOR_TEXT = "[Back to main README](README.md)"

def get_user_input():
    print("--- Add New Project Entry ---")
    name = input("Project Name: ").strip()
    
    print("\nDescription (Press Enter twice to finish):")
    description_lines = []
    while True:
        line = input()
        if not line:
            break
        description_lines.append(line)
    description = "\n".join(description_lines)
    
    tech = input("\nTechnologies (e.g. Python, Docker): ").strip()
    
    return name, description, tech

def format_entry(name, description, tech):
    # This matches the specific HTML/Markdown mix from your file
    return f"""---

<details>
<summary><span style="font-size:1.5em;"><b>{name}</b></span></summary>

&#32;

{description}

**Tech:** {tech}

</details>

"""

def update_file(name, description, tech):
    if not os.path.exists(FILE_NAME):
        print(f"Error: {FILE_NAME} not found!")
        return

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        content = f.read()

    now = datetime.now()
    date_str = f"{now.day}.{now.month}.{now.year}"
    
    content, count = re.subn(
        r"\*last updated: .*?\*", 
        f"*last updated: {date_str}*", 
        content
    )
    
    if count == 0:
        print("Warning: Could not find 'last updated' line to update.")
    else:
        print(f"Updated date to: {date_str}")

    if ANCHOR_TEXT in content:
        new_block = format_entry(name, description, tech)
        
        parts = content.split(ANCHOR_TEXT)
        
        new_content = parts[0].rstrip() + "\n\n" + new_block + ANCHOR_TEXT + parts[1]
        
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            f.write(new_content)
            
        print(f"Successfully added project: '{name}'")
    else:
        print(f"Error: Could not find anchor text '{ANCHOR_TEXT}'.")

if __name__ == "__main__":
    try:
        p_name, p_desc, p_tech = get_user_input()
        if p_name and p_desc:
            update_file(p_name, p_desc, p_tech)
        else:
            print("Operation cancelled: Missing name or description.")
    except KeyboardInterrupt:
        print("\nExiting...")