import csv


class CSVReader():
    """
    Implementation of a simple CSV reader. Contains a read method which operates on the filename which
    the reader is instantiated with. This reader is tailored to read the resources/element_weights.csv
    to create a dictionary, which is stored in the data member.
    """
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = None

    def read(self):
        """
        Read a .csv file, create a dictionary of data, and store the data within the CSVData.data variable

        :return: None
        """
        if not self.data:
            with open(self.file_name, 'rb') as f:
                reader = csv.reader(f, delimiter=',', quotechar='"')
                self.data = {row[0]: float(row[1]) for row in reader}