import os
from jinja2 import Environment, FileSystemLoader
import yaml
# import pprint  # debugging

# Define the HTML templates which are processed by Jinja2
jinja2_env = Environment(loader=FileSystemLoader('./templates'))
root_homepage_template = jinja2_env.get_template('index.html')
creative_homepage_template = jinja2_env.get_template('subindex-creative.html')
technical_homepage_template = jinja2_env.get_template(
    'subindex-technical.html')

# Define which template should be applied which each content set
content_to_template_mapping = {
    'index.yml': root_homepage_template,
}
for page in os.listdir('content'):  # assume all YAML files (as standard)
    if page.startswith('creative-sub'):
        content_to_template_mapping[page] = creative_homepage_template
    elif page.startswith('technical-sub'):
        content_to_template_mapping[page] = technical_homepage_template

# Populate templates with content and write to files as the rendered pages
# Process global content first:
with open(os.path.join('content', 'global.yml')) as file:
    global_content = yaml.load(file.read(), Loader=yaml.BaseLoader)
for content_set, template in content_to_template_mapping.items():
    # Process the local (page-specific) content keys and values
    file_path = os.path.join('content', content_set)
    with open(file_path, 'r') as file:
        content = yaml.load(file.read(), Loader=yaml.BaseLoader)
    # pprint.pprint(content)  # debugging

    # Render each post to '<md file name>.html' under top-level repo dir
    page_html = template.render(page=content, site_global=global_content)
    page_file_path = './{}.html'.format(content_set.rsplit(".", 1)[0])
    os.makedirs(os.path.dirname(page_file_path), exist_ok=True)
    with open(page_file_path, 'w') as file:
        file.write(page_html)
