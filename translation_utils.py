"""
translation_utils.py

This module provides utility functions for handling translations stored in JSON files.

Functions:
- load_translations(file_path): Loads translations from a specified JSON file.
- save_translations(translations, file_path): Saves translations to a specified JSON file (currently commented out).

Usage:
- Use `load_translations` to read translations from a JSON file.

Example:
    translations = load_translations('path/to/translations.json')
"""

import json
import os

def load_translations(file_path):
    """Load translations from a JSON file."""
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        print(f"Translation file not found: {file_path}")
        return {}


# def save_translations(translations, file_path):
#     """Save translations to a file_path"""
#     with open(file_path, 'w', encoding='utf-8') as f:
#         json.dump(translations, f, ensure_ascii=False, indent=2)
