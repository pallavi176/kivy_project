import PyPDF2, os, filetype
from log import lg


class FileFinder:
    def __init__(self,path):
        self.path=path
        lg(f"Initializing path variable: {path}")

    def validate_path(self,pt):
        """
        This method will validate a path passed to it whether the path exists or not
        """
        try:
            lg("Checking if path exists.")
            return True if os.path.exists(pt) else False
        except Exception as e:
            issue = "exception in validate_path(): with error:"+ str(e) + "\n"
            issue = issue + "-------------------------------------------------\n"
            lg(issue)
            return issue

    def file_extractor(self):
        """
        This method will list down all the files present in the current path and append to the list
        """
        try:
            file_list = []
            for root, dirs, files in os.walk(self.path):
                for f in files:
                    file_name = os.path.join(self.path, f)
                    if os.path.isfile(file_name):
                        file_list.append(file_name)
            lg(f"List list created: {file_list}")
            return file_list
        except Exception as e:
            issue = "exception in file_extractor(): with error:" + str(e) + "\n"
            issue = issue + "-------------------------------------------------\n"
            lg(issue)
            return issue

    def is_pdf(self, file_name):
        """
        This method will check if file type is of pdf or not
        """
        try:
            #return True if filetype.guess(file_name).mime == 'application/pdf' else False
            lg(f"Checking is {file_name} is of type pdf or not")
            return True if file_name.endswith('.pdf') else False
        except Exception as e:
            issue = "exception in is_pdf(): with error:" + str(e) + "\n"
            issue = issue + "-------------------------------------------------\n"
            lg(issue)
            return issue

    def pdf_file_counter(self, file_list):
        """
        This method will count the number of pdf files in the list of files
        """
        lg("counting the number of pdf files")
        try:
            if len(file_list) == 0:
                return 0
            else:
                c=0
                for n in file_list:
                    if self.is_pdf(n):
                        c += 1
                return c
        except Exception as e:
            issue = "exception in pdf_file_counter(): with error:" + str(e) + "\n"
            issue = issue + "-------------------------------------------------\n"
            lg(issue)
            return issue

    def filter_pdf(self, file_list):
        """
        This method will count filter all the pdf files names from the list of files and append to the list
        """
        try:
            filtered_list = []
            for n in file_list:
                if n:
                    if self.validate_path(n) and self.is_pdf(n):
                        filtered_list.append(n)
            lg(f"Filtering only pdf files: {filtered_list}")
            return filtered_list
        except Exception as e:
            issue = "exception in filter_pdf(): with error:" + str(e) + "\n"
            issue = issue + "-------------------------------------------------\n"
            lg(issue)
            return issue

    def pdf_merger(self, file_list):
        """
        This method will merge all the pdf files from the list of all the files
        """
        try:
            lg("Merging all pdf files")
            c = self.pdf_file_counter(file_list)
            filtered_list = self.filter_pdf(file_list)
            if c == 0:
                return f"No pdf file found in the input path: {self.path}."
            elif c == 1:
                return f"1 pdf file: {filtered_list[0]} found at the input path."
            elif c >= 2:
                file_name = 'merged.pdf'
                merged_file = os.path.join(self.path, file_name)
                merger = PyPDF2.PdfFileMerger()
                for item in filtered_list:
                    merger.append(item)
                merger.write(f'{merged_file}')
                merger.close()
                return f"All pdf files merged to: {merged_file}"
        except Exception as e:
            issue = "exception in pdf_merger(): with error:" + str(e) + "\n"
            issue = issue + "-------------------------------------------------\n"
            lg(issue)
            return issue
