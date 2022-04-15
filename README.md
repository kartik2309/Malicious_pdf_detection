# Malicious_pdf_detection
This project aims to detect if a pdf file is clean or malicious.

You can generate malicious PDF Files from clean PDF Files to form your dataset using the project: https://github.com/jonaslejon/malicious-pdf. __This is a project by - jonaslejon (Jonas Lejon), maggick (maggick), tonyarris (Tony Harris). For issues regarding generation of Malicious PDF Files, please contact them or raise an issue on their repository.__
 
Create two directories `maliciouspdf` and `cleanpdf` and keep your malicious and clean PDF files accordingly.

* `command_exec.py` will iterate through each and every file in the folders viz `maliciouspdf` and `cleanpdf`.

* `feature_extraction.py` help in feature extraction of each pdf file based on its file structure. It uses pdfid.py script, which is an opensource file and part of peepdf.

* `classifier.py` implements the Random Forest Classifier and trains it with the data `pdfdataset_n.csv`. We also split the data into 30% for testing purpose. Accuracy is observed to be around 99%.

We have already extracted the necessary features from these files and formed a dataset as `pdfdataset.csv` and `pdfdataset_n.csv` is min-max normalized version of it.

Please raise a PR if you have improvements for the project.
