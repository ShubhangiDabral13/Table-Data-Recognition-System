"""
__author__: Shubhangi_Dabral(@SHubhangiDabral13)
A Python module for API to extract tabular data from images and scanned PDFs.
"""

#Import important modules
"""
-->PIL :it support opening, manipulating, and saving many different image file formats.
-->os :OS module in python provides functions for interacting with the operating system.
-->pandas : Here pandas is used to convert list to dataframe.

"""

from PIL import Image
import os
import pandas as pd
from modules import et_sess,usage


print(usage)
"""
Usage will print 3 values
credits: Total number credits attached to the API Key

queued : Number of triggered jobs that are still processing in the queue

used : Number of credits already used
"""

#folder where images are stored
images = os.listdir("../images")
print(images)

#Traversing through each images
for image in images:

    #Extracting data from image
    table_data = et_sess.process_file(filepath="../images/"+image, output_format="df")

    #Converting the text extracted from images to dataframe.
    for i in range(len(table_data)):
        df = pd.DataFrame(table_data[i])
        df.rename(columns=df.iloc[0],inplace = True)
        df.drop(df.index[0], inplace = True)

        #Saving the dataframe in csv format in the output-csv-file folder.
        df.to_csv(r"../output-csv-file/image"+image[0]+"output"+str(i)+".csv")

print("all images have been converted to csv file")
