# Import necessary modules from Jinja2
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Create a Jinja2 environment
# - FileSystemLoader("./templates/") loads templates from the current directory
# - select_autoescape() enables autoescaping for HTML/XML files (default behavior)
env = Environment(loader=FileSystemLoader("./templates/"), autoescape=select_autoescape())

# Define the path to the template file
template_path = "./template.html"

# Load the template file from the specified path
template = env.get_template(template_path)

# Define the data dictionary to pass variables into the template
data = {
    "name": "John Doe"
}

# Render the template with the provided data
rendered_template = template.render(data)

# Define the output file path
output_path = "./index.html"

# Try writing the rendered template to the output file
try:
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rendered_template)
    print(f"File created at: {output_path}")  # Success message
except FileNotFoundError:
    # Raise an error if the output file path is invalid
    raise FileNotFoundError("Error: The file does not exist.")