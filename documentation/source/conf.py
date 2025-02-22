# Configuration file for the Sphinx documentation builder.
#
# For a full list of options see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import os
import sys
from typing import List

# Modules to document with autodoc are in another directory. That directory is
# added to 'sys.path' here. The path is best expressed relative to the current
# directory so needs to be made absolute for use.
#
sys.path.insert(0, os.path.abspath('../../source'))

from stylist import __version__ as STYLIST_VERSION  # noqa: E402
#
# Must appear after path addition otherwise it wouldn't be found.


# -- Project information -----------------------------------------------------

project = 'Stylist'
copyright = '2024, Met Office. All rights reserved'
author = 'Stylist Developers'

# Headline version for archiving purposes.
#
version = STYLIST_VERSION.split('-', 1)[0]

# The full version, including alpha/beta/rc tags. This reflects development.
#
release = STYLIST_VERSION


# -- General configuration ---------------------------------------------------

# Sphinx extension module names are listed here. They can be extensions coming
# with Sphinx (named 'sphinx.ext.*') or your custom ones.
#
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_autodoc_typehints',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinxcontrib.plantuml'
]

# Paths to directories containing templates. Relative to this directory.
#
templates_path = ['_templates']

# Filename patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
#
# These patterns also affect 'html_static_path' and 'html_extra_path'.
#
exclude_patterns: List[str] = []


# -- Autodoc configuration ---------------------------------------------------

autodoc_default_options = {
    'members': True,
    'show-inheritance': True
}

autoclass_content = 'both'


# -- Integrated PlantUML configuration ---------------------------------------

plantuml_output_format = 'svg'

# -- Todo configuration ------------------------------------------------------

todo_include_todos = True


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages. See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/MetOffice/stylist",
            "icon": "fa-brands fa-github"
        }
    ],
    "footer_start": ["crown-copyright"],
    "footer_center": ["sphinx-version"],
    "footer_end": ["theme-version"]
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#
html_static_path = ['_static']

html_logo = '_static/stylist.png'
