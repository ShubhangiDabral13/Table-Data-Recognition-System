"""
__author__: Shubhangi_Dabral(@SHubhangiDabral13)
A Python module for API to extract tabular data from images and scanned PDFs.
"""

# Importing ExtractTable 
from ExtractTable import ExtractTable
#Inplace of Enter-Your-key Enter the api-key that will be send to your respective email id.
api_key = 'Enter-Your-key'
et_sess = ExtractTable(api_key)
usage = et_sess.check_usage()
