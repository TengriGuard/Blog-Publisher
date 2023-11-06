# blog_publisher.py
import markdown
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

def main():
    for md_file in os.listdir('markdown_posts'):
        if md_file.endswith('.md'):
            with open(f'markdown_posts/{md_file}', 'r') as f:
                content = f.read()
                html_content = markdown.markdown(content)

            template = env.get_template('blog_template.html')
            output_from_parsed_template = template.render(content=html_content)

            # to save the results
            with open(f"output/{md_file.replace('.md', '.html')}", "w") as f:
                f.write(output_from_parsed_template)

if __name__ == "__main__":
    main()
