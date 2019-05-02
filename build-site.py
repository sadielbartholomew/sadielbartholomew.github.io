import os
from jinja2 import Environment, PackageLoader
from markdown2 import markdown

# Define the HTML templates which are processed by Jinja2
jinja2_env = Environment(loader=PackageLoader('build-site', 'templates'))
page_template = jinja2_env.get_template('page-template.html')

# Process the markdown content keys and values
pages = {}  # stores the markdown pages defining the content
for page in os.listdir('content'):
    file_path = os.path.join('content', page)
    with open(file_path, 'r') as file:
        pages[page] = markdown(file.read(), extras=['metadata'])

# Render each post and write it to output/<lower case name>.html
for page in pages:
    page_metadata = pages[page].metadata
    data = {'content': pages[page]}
    for metadata_key in page_metadata:
        data[metadata_key] = page_metadata[metadata_key]

    page_html_content = page_template.render(post=page_metadata)

    page_file_path = './{filename}.html'.format(
        filename=page.rsplit(".", 1)[0])

    os.makedirs(os.path.dirname(page_file_path), exist_ok=True)
    with open(page_file_path, 'w') as file:
        file.write(page_html_content)
