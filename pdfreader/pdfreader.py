from tika import parser
import pdb

def get_words(document):
    """
    Gets a list of words within the document, then sets them all to lowercase
    :param document:
    :return: a list of words in the PDF as all lowercase
    """

    raw = parser.from_file(document)
    docwords = raw['content'].split()
    print(docwords)

    lowercasewords = []

    for word in docwords:
        lowercasewords.append(word.lower())

    print(lowercasewords)
    return lowercasewords


def Check_for_financial_activity(list):
    """
    Checks the word list from get_words for potential issue words relating to fintech companies.
    :param list:
    :return: Flag message for fintech
    """

    flagwords = ['fca',
                 'exchange',
                 'insurance',
                 'freetrade',
                 'robinhood',
                 'securities',
                 'algorithmic trading',
                 'insure',
                 'financial',
                 'professional services',
                 'roboadvisor',
                 'fintech']

    for word in list:
        if word in flagwords:
            print('There may be financial activity present.')
        else:
            print('.')

#use sets (command that will check if something is in a list) avoiding for loops wherever possible (time efficiency)
# assertin -> assertIn('exchange_id', dir(market) 

def Check_for_sufficient_risks(list):
    """
    Checks the word list from get_words for if any words relate to R2C condition.
    :param list:
    :return: Flag message for risks
    """

    flagwords = ['risks',
                 'weaknesses',
                 'threats',
                 'swot',
                 ]

    for word in list:
        if word not in flagwords:
            print('There is unlikely any presentation of risks.')
        else:
            print('.')


def Check_for_blockchain(list):
    """
    Checks the word list from get_words for potential issue words relating to blockchain companies.
    :param list:
    :return: Flag message for blockchain
    """

    flagwords = ['dlt',
                 'etherium',
                 'blockchain',
                 'ledger',
                 'tokenization',
                 'tokens',
                 ]

    for word in list:
        if word not in flagwords:
            print('There may be blockchain related issues.')
        else:
            print('.')


def Check_for_groups(list):
    """
    Checks the word list from get_words for potential issue words relating to group structures.
    :param list:
    :return: Flag message for groups
    """

    flagwords = ['group',
                 'subsidiary',
                 'subsidiaries',
                 'topco',
                 ]

    for word in list:
        if word not in flagwords:
            print('There may be group structure related issues.')
        else:
            print('.')

Check_for_financial_activity(get_words('example.pdf'))


'''current issues + features: 

    1. structuring the program better, so that it's OOP? (A function to check, with decotrators or sub-functions which 
    modify the text dependant on the trigger words.
    
    2. Setting up the input so that it can be run on any pdf file. 
    
    3. Setting up the output so that it flags where the word was, for example as an MVP, it could output where the
    flagged word was in the list, as a percentage of the way through the document?. 
    
    4. Writing tests. 
    
    --> sys.argv[0,1 etc..]
'''

# ==================

''' Initial work was using PyPDF2 - however, accuracy and utility appears worse than tika

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
'''
