# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PrIOR'
copyright = '2022, Kenneth Babu Opap'
author = 'Kenneth Babu Opap'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# import recommonmark
# from recommonmark.transform import AutoStructify
# from recommonmark.parser import CommonMarkParser
# source_parsers - {
#    '.md': CommonMarkParser
# }

# import sphinx_bootstrap_theme


# def setup(app):
#     app.add_config_value('recommonmark_config', {
#             'enable_math': True,
#             'enable_eval_rst': True,
#             'enable_auto_doc_ref': True,
#             'auto_code_block': True,
#             }, True)
#     app.add_transform(AutoStructify)

extensions = [
    "myst_parser",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autodoc",
    
    # 'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.githubpages',
    # 'sphinx_markdown_tables'
    
    ]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# source_suffix - ['.rst', '.md']
