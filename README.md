# Malicious_pdf_detection
This project aims to detect if a pdf file is clean or malicious.

Obtain the real dataset here
    - Malcicious PDF Files: https://drive.google.com/open?id=1be7tulUDkVraAr43wMHCu-SR8FhmZb4w 
    - Clean PDF Files: https://drive.google.com/open?id=18Hw9ch6lNUnHunlTZXC2bOl8def0KKxO

command_exec.py will iterate through each and every file in the folders viz 'maliciouspdf' and 'cleanpdf', which can be obtained in the link above.

feature_extraction.py help in feature extraction of each pdf file based on its file structure. It uses pdfid.py script, which is an opensource file and part of peepdf.

classifier.py implements the Random Forest Classifier and trains it with the data pdfdataset_n.csv. We also split the data into 30% for testing purpose. Accuracy is observed to be around 99%.

We have already extracted the necessary features from these files and formed a dataset as pdfdataset.csv and pdfdataset_n.csv is min-max normalized version of it.
