# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Earth Observation Data Visualisation Best Practice Guide'
org = 'EUMETSAT'
organization = f'{org} on behalf of the Copernicus Programme'
author = f'{org} and contributors'
copyright = f'2023, {author}'
version = '0.1.0'
release = version
sponsor_link = 'https://www.eumetsat.int/'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'python-youtube',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
#html_theme = 'furo'

# -- Options for EPUB output
epub_show_urls = 'footnote'
