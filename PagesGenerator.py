import os, shutil
from jinja2 import Environment, FileSystemLoader


class PagesGenerator:
    def __init__(self, path_to_result, rss_entries):
        self._path_to_result = path_to_result
        self._rss_entries = rss_entries

    def generate(self):
        self._copy_static()
        self._generate_index_pages()
        self._generate_posts()

    def _copy_static(self):
        shutil.rmtree(self._path_to_result)
        shutil.copytree(os.path.abspath('./result'), self._path_to_result)

    def _generate_index_pages(self):
        template = self._get_template('list.html')
        chank_size = 5
        beginning_of_chanks = range(0, len(self._rss_entries), chank_size)
        current_page = 0
        for i in beginning_of_chanks:
            chank = self._rss_entries[i:i + chank_size]
            file_name = 'index.html' if (current_page == 0) else 'index_{}.html'.format(current_page)
            file = open(os.path.join(self._path_to_result, file_name), 'a')
            file.write(template.render(entries=chank, current_page=current_page, number_of_pages=len(beginning_of_chanks)))
            current_page += 1

    def _generate_posts(self):
        for entry in self._rss_entries:
            template = self._get_template('post.html')
            file = open(os.path.join(self._path_to_result, entry.link + ".html"), 'a')
            file.write(template.render(post=entry))

    def _get_template(self, template_name):
        file_loader = FileSystemLoader('templates')
        env = Environment(loader=file_loader)
        template = env.get_template(template_name)
        return template



