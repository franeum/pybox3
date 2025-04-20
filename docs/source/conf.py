# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "pybox"
copyright = "2025, Francesco Bianchi"
author = "Francesco Bianchi"
release = "3"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "sphinx.ext.viewcode"]

templates_path = ["_templates"]
exclude_patterns = []

autodoc_mock_imports = [
    "board",
    "src",
    "adafruit_pixel_framebuf",
    "usb_midi",
    "digitalio",
    "keypad",
    "neopixel",
    "analogio",
    "adafruit_midi",
    "simpleio",
    "rotaryio",
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"

html_logo = "_static/logo.png"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

html_theme_options = {
    "light_css_variables": {
        "color-background-primary": "#ffffff",  # quasi nero
        "color-brand-primary": "#ff00f7",  # rosa neon
        "color-brand-content": "#ff00f7",  # azzurro neon
        "color-sidebar-background": "#ffffff",
        "color-sidebar-link-text": "#00f0ff",
        "color-sidebar-link-text--top-level": "#ff00f7",
    },
    "dark_css_variables": {
        "color-background-primary": "#ffffff",
        "color-brand-primary": "#ff00f7",
        "color-brand-content": "#00f0ff",
        "color-sidebar-background": "#ffffff",
        "color-sidebar-link-text": "#00f0ff",
        "color-sidebar-link-text--top-level": "#ff00f7",
    },
}


import os
import sys

sys.path.insert(0, os.path.abspath("../../src"))
