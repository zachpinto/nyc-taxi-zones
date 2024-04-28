# conf.py - Sphinx configuration file for generating the project documentation

import os
import sys

# General configuration
project = 'NYC Taxi Zone Visualization'
author = 'Your Team Name'
version = '1.0'
release = '1.0'

extensions = []
templates_path = ['_templates']
exclude_patterns = ['_build']

html_theme = 'alabaster'
html_static_path = ['_static']

# Options for HTML output
html_theme_options = {
    'logo': 'logo.png',
    'favicon': 'favicon.ico',
    'navigation_depth': 2,
}

sys.path.insert(0, os.path.abspath('../src'))
