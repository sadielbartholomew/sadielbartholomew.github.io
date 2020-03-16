import os
from jinja2 import Environment, PackageLoader
from markdown2 import markdown

# Define the HTML templates which are processed by Jinja2
jinja2_env = Environment(loader=PackageLoader('rebuild-site', 'templates'))
root_homepage_template = jinja2_env.get_template('index.html')
creative_homepage_template = jinja2_env.get_template('subindex-creative.html')
technical_homepage_template = jinja2_env.get_template(
    'subindex-technical.html')

# Define which template shoudl be applied which each content set
content_to_template_mapping = {
    'index.md': root_homepage_template,
}
for page in os.listdir('content'):
    if page.startswith('creative-sub'):
        content_to_template_mapping[page] = creative_homepage_template
    elif page.startswith('technical-sub'):
        content_to_template_mapping[page] = technical_homepage_template

for content_set, template in content_to_template_mapping.items():
    # Process the markdown content keys and values
    file_path = os.path.join('content', content_set)
    with open(file_path, 'r') as file:
        page = markdown(file.read(), extras=['metadata'])

    # Render each post to '<md file name>.html' under top-level repo dir
    data = {'content': page}
    data.update(page.metadata)
    page_html = template.render(thispage=data)

    print(data, page_html) ### debug
    page_file_path = './{}.html'.format(content_set.rsplit(".", 1)[0])
    os.makedirs(os.path.dirname(page_file_path), exist_ok=True)
    with open(page_file_path, 'w') as file:
        file.write(page_html)
