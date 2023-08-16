# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Earth Observation Data Visualisation Good Practice Guide'
org = 'EUMETSAT'
organization = f'{org} on behalf of the Copernicus Programme'
author = f'{org} and contributors'
copyright = f'CC BY 4.0 (2023)'
version = '0.1.4'
release = version

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.youtube',
    'linuxdoc.rstFlatTable'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'furo'

# -- Options for EPUB output
epub_show_urls = 'footnote'
