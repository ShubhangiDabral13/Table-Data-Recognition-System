[![image](https://i.imgur.com/2Hihfwwg.png)](https://extracttable.com?ref=github-ET)

[![image](https://img.shields.io/pypi/v/extracttable.svg?maxAge=3600)](https://pypi.org/project/extracttable/) ![image](https://img.shields.io/github/license/ExtractTable/ExtractTable-py) ![image](https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue)
  
# Overview
[ExtractTable](https://extracttable.com) - **API to extract tabular data from images and scanned PDFs**

The motivation is to make it easy for developers to extract tabular data from images or scanned PDF files without worrying about the table area, column coordinates, rotation et al.

# Prerequisite

**API Key**: All requests to ExtractTable are authorized by an API Key. [FREE credits here](https://extracttable.com/signup/trial.html). The same API Key can also be used for conversions on the browser at [Web Pro](https://extracttable.com/pro.html).


# Installation

`pip install -U ExtractTable`


# Basic Usage
Ok, enough selling. Let the ease in coding do the talk, and the output encourages you to buy credits; put that timer on and count the LOC.


```python
from ExtractTable import ExtractTable
et_sess = ExtractTable(api_key=YOUR_API_KEY)        # Replace your VALID API Key here
print(et_sess.check_usage())        # Checks the API Key validity as well as shows associated plan usage 
table_data = et_sess.process_file(filepath=Location_of_Image_with_Tables, output_format="df")

# To process PDF, make use of pages ("1", "1,3-4", "all") params in the read_pdf function
table_data = et_sess.process_file(filepath=Location_of_PDF_with_Tables, output_format="df", pages="all")
```

## Detailed Library Usage
The tutorial available at <a href="https://colab.research.google.com/github/ExtractTable/ExtractTable-py/blob/master/example-code.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> takes you through

```Markup
1. Installation
2. Import and check version
3. Create Session & Validate API Key
    3.1 Create Session with your API Key
    3.2 Validate the Key and check the plan usage
    3.3 Check Usage Details
4. Trigger the extraction process
    4.1 Accepted Input Types
    4.2 Process an IMAGE Input
    4.3 Process a PDF Input
    4.4 Output options
    4.5 Explore session objects
5. Explore the Output
    5.1 Output Structure
    5.2 Output Details
6. Make Corrections
    6.1 Split Merged Rows
    6.2 Split Merged Columns
    6.3 Fix Decimal Format
    6.4 Fix Date Format
7. Helpful Code Snippets
    7.1 Get text data
    7.2 Table output to Excel
```

## How to run the code for your images.
* Add your images in the images folder.
* Run the python file "convert_to_csv" in src folder.
* Your output will be sorted in output-csv-file.




