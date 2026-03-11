# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Void Crew Modding Documentation'
copyright = '2026, Hutlihut Games'
author = 'Hutlihut Games'
release = '0.1.0'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

myst_heading_anchors = 3

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_baseurl = "https://hutlihutgames.github.io/void_crew_modding_documentation/"
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_css_files = [
    "css/voidcrew.css",
]

html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": -1,
    "sticky_navigation": True,
    "includehidden": True,
    "titles_only": False,
}