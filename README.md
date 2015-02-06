GeoPDF_to_GeoTIFF
=================

#####   IMPORTANT   ######   
You must have GDAL and Python installed on your computer for this to work.

Instructions ---->   Drop both the .bat and the .py file into the folder that contains the GeoPDFs that you wish to convert. Open a command prompt within the folder, and type "cutline.bat".  This will run the .bat file which will iterated through each .pdf in the folder and run the .py file against it. The .py file will use the .pdf file as an argument and clip it with the neatline and convert it to a GeoTIFF. 

You can then reproject the GeoTiff to NAD 83 if desired using the reproject.bat file. You will need to first create a folder called "NAD83" in the directory that the bat file will copy the new file to.

*If any of the PDF filenames contain whitespaces, use the remove_whitespaces.bat file to replace the whitespaces with underscores before running the cutline.bat file. 
