# [sadielbartholomew.github.io](https://sadielbartholomew.github.io/)

Full URL: ``https://sadielbartholomew.github.io/``


## The personal website of Sadie Louise Bartholomew

Designed & created by Sadie Louise Bartholomew, 2020+.


### Infrastructure


### Technologies & languages

* [GitHub pages](https://pages.github.com/);
* HTML;
* CSS;
* [YAML](https://yaml.org/);
* [Jinja(2)](https://jinja.palletsprojects.com/en/2.11.x/intro/);
* [EnlighterJS](https://enlighterjs.org/).


#### Repository organisation

* The content structure is defined in HTML templates under ``templates/``.
  These are Jinja2 templates for HTML i.e. pure HTML templates except from
  lower-level elements in the document object model which are often Jinja2
  expressions, functions or variables for which pre-defined content will be
  injected to give final, pure, HTML files defining the user-facing site.

* The site design, i.e. the design mapping to the HTML templates, is stored
  under ``css/``.

* The content is located as follows:
  * written content is stored in YAML files directly under ``content/``;
  * media is stored in an organised heirarchical structure under ``img/``.


#### Build process

The command, executed from the root respoitory directory:

```console
$ python rebuild-site.py
```

will rebuild the website to pick up on any changes made in the ``templates/``,
``content/``, ``img/`` & ``css/`` directories to produce the final, user-facing
HTML files which are written directly to the root repository directory.

The command calls the Python script ``rebuild-site.py`` which:
  1. maps the content files to template files;
  2. processes the template files;
  3. uses Jinja2 to inject the YAML key-values from each content file into
     the corresponding key elements in the HTML templates;
  4. Writes the populated HTML to the root repository directory.


Changes to the code should be built into the final pages via the ``rebuild``
command & then the full state of the repository committed to the ``master``
branch. The changes will then (possibly after a short-ish delay for GitHub to
process them) display at the site domain, ``sadielbartholomew.github.io``,
as a GitHub pages website.
