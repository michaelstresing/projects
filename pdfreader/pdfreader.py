import PyPDF2


def get_text():

    """
    Takes a PDF and runs PyPDF2 - pulls text into a list.
    :param document:
    :return: list of strings of each word in the document
    """

    pdfFileObj = open('example.pdf', 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # getting the number of pages in pdf file
    length = pdfReader.numPages

    # setting the empty list for words
    document_text = []

    page_number = 0
    # looping through each page and extracting the text into a list
    while page_number <= length:
        pageObj = pdfReader.getPage(page_number)
        pagetext = pageObj.extractText()  # extracting text from page
        document_text.append(pagetext.split)
        page_number += 1

    # closing the pdf file object
    pdfFileObj.close()

    return document_text


print(get_text())
