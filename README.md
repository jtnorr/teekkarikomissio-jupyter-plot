# Simple plot generator for multiple choice questions acquired from an Excel file

--------------------

## Description

A Jupyter notebook written by me to further analyse the results from a survey created by the board of Teekkarikomissio. The survey in question was created using Microsoft Forms, which unfortunately doesn't seem to have great tools for creating graphs or other visualisations. Even when transferring the answers to an Excel datasheet, I was unable to present the answers easily and in an adaptable form.

This Notebook has a couple of major code blocks with Markdown used between as titles. The blocks are in order as follows:

1. Importing libraries and defining functions
2. Importing the Excel file(s) and processing the data
3. Plotting individual surveys as bar charts
4. Combining all surveys into one bar chart
5. Creating a 7-zip archive of the plots created

## Installation and usage

1. Clone the repository
2. Install the required libraries using the command `pip install -r requirements.txt`
3. Change the path to the Excel file to match the locations of the files on your system (default is `./data/`)
4. Adjust the column index to match the columns in the Excel file(s)
5. Run the notebook

## Setting up translations

The translations are in a JSON file called `translations.json`. The file is located in the `data` folder and can be edited to your translation needs. The file is structured as follows:

```json
{
  "Search term": {
    "language_code1": "Translation1",
    "language_code2": "Translation2"
  },
  
  "Another search term": {
    "language_code1": "Translation1",
    "language_code2": "Translation2"
  }
}
```

## Features

- Automatically processes the data from the Excel file(s) after the initial setup
- Can scale to larger amounts of files or data
- Comparatively simple to understand the solution, so you can adapt to your particular purpose
- Saves the plots as PNG, PDF and SVG files for easy use and adaptability
- Creates a 7-zip archive of the plots for easy sharing through instant messaging or email

## License

This project is licensed under the MIT license, see the [LICENSE](LICENSE) file for more information.

## Acknowledgements

- [Teekkarikomissio](https://teekkarikomissio.fi/) for creating the survey and allowing me to use the data for this project
- [Microsoft](https://www.microsoft.com/en-us/) for creating Microsoft Forms and Excel
- [Python](https://www.python.org/) for the language used in this project
- [Jupyter](https://jupyter.org/) for creating the notebook used in this project
- [Matplotlib](https://matplotlib.org/) for creating the plots used in this project
- [SeaBorn](https://seaborn.pydata.org/) for creating the plots used in this project
- [Pandas](https://pandas.pydata.org/) for processing the data used in this project
- [Py7zr](https://py7zr.readthedocs.io/en/latest/) for creating the 7-zip archive used in this project

## Contact information

- Name: Jani Norrby
- Email: jtnorr@utu.fi
- GitHub: [jtnorr](https://github.com/jtnorr)