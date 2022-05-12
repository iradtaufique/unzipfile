# importing Zipfile function from zipfile
from zipfile import ZipFile


# accessing or reading your file as zip_fle
with ZipFile('your_zipped_file.zip', 'r') as zip_file:

    # and now here we extact our file.
    zip_file.extractall()