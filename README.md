# Pannakaawat: Ilocano to English Translator

Pannakaawat (meaning "Understanding" in Ilocano) is a rule-based machine translation system designed to translate simple Ilocano sentences into English. It utilizes a Context-Free Grammar (CFG) and a dictionary-based lexicon to parse and restructure sentences from the Verb-Initial structure common in Ilocano to the Subject-Initial structure of English.

**Note:** This project is currently under active development and requires further improvement in grammar coverage, lexicon expansion, and translation accuracy.

## Project Structure

The project follows an iterative development versioning structure. The latest stable version is **Version 5**.

### Version 5 Components

- **translator.py** - The main entry point. Handles tokenization, part-of-speech tagging, and coordinates the translation process using the grammar and lexicon.
- **grammar.py** - Defines the Context-Free Grammar rules for Ilocano using NLTK.
- **lexicon.py** - Manages the dictionary database, handling retrieval of English translations and Part-of-Speech tags.
- **ilocano_lexicon.json** - The database storing word mappings between Ilocano and English.

## Installation and Requirements

This project requires Python and the Natural Language Toolkit (NLTK).

### Installation Steps

1. Clone the repository
2. Install dependencies:
```bash
pip install nltk
```
3. Download required NLTK data (required for tokenization):
```python
import nltk
nltk.download('punkt')
```

## Usage

To run the translator, execute the `translator.py` script from the `version5` directory:
```bash
cd version5
python translator.py
```

## Contributing

Contributions are welcome. Please ensure that any changes to the lexicon maintain valid JSON formatting and that new grammar rules are tested against existing sentences.

