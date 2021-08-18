# Program name: grep.py

import os, string, json, sys

def cleaning(data):
    """
    Clean 'data' by making sure all letters are lower case, split into words and
    stripped from punctuation on both sides of the word.

    Args:
        data (string): the string which needs to be cleaned

    Returns:
        set : contains words in a file which are all lower case and stripped
        from punctuation on both sides. 
    """

    unique_words = set() # holds words without duplicates in data after cleaning

    words = data.lower().split() # make data lower case and split into words 

    for i in range(len(words)): # iterate through list
        # strip and add into set
        unique_words.add(words[i].strip(string.punctuation))
    
    return unique_words


def common_elements(lis1, lis2):
    """Find the common elements in two lists.

    Args:
        lis1 (list): one of the lists to compare
        lis2 (list): the other list to compare

    Returns:
        list : contains the elements common to both lists.
    """    

    set_1 = set(lis1) # convert lis1 to a set 
    set_2 = set(lis2) # convert lis2 to a set

    # find common elements between sets using intersection and convert to list
    common_elements_list = list(set_1.intersection(set_2))  

    return common_elements_list


def build_index(file_list, index, title_index):
    """Build a word index and a title index for all the files in a file list.

    Args:
        file_list (list): List containing file names
        index (dictionary): Index mapping words to filenames
        title_index (dictionary): Index mapping filenames to the title of the 
        article.

    Returns:
        index (dictionary): Index mapping words to filenames
        title_index (dictionary): Index mapping filenames to the title of the 
        article.
    """
    
    for file_name in file_list:
        title, content = get_content(file_name) # obtain current file contents
        title_index.update({file_name: title}) # add file title to title_index 
        unique_words = cleaning(title + content)
        for word in unique_words: 
            if word in index: # if word exists, append file_name to list
                index[word].append(file_name) 
            else: # if not, add word and create new list
                index[word] = [file_name] 
                
    return index, title_index


def get_content(file_name):
    """Return the title and contents of the file.

    Args:
        file_name (str): String containing file name

    Returns:
        title (str): String containing the file title
        content (str): String containing the remaining words in the file
    """    
    with open(file_name) as file:
        title = file.readline().strip() # get the title
        contents = file.read()          # read the rest
        return title, contents


def search(index, query):
    """Search the index for the words in the query string.

    Args:
        index (dictionary): dictionary containing word to filename mapping.
        query (string): string containing words in the query. String is lowercase.

    Returns:
        list: list of file in which all the words in the query appear.
    """   
    
    query_words = set(query.split()) # split query string into set  
    files = [] # list used to find intersection 
    
    for word in query_words: 
        if word in index: # check if word is in index
            if not files: # if empty, no need to find intersection 
                files = index[word]
            else: # find common files between two lists of file names
                files = common_elements(files, index[word])

    return files


def pretty_print(index, title_index):
    """Print the dictionaries passed as parameters

    Args:
        index (dictionary): Index mapping words to filenames
        title_index (dictionary): Index mapping filenames to the title of the article.
    """    
    print("\nIndex:")
    print(index)
    print("\nFile names and titles:")
    print(title_index)


def get_filenames(directory_name):
    """Return list of the files in the given directory.

    Args:
        directory_name (directory): Name of the directory

    Returns:
        list: list of filenames in the directory
    """    
    file_list = []

    try:
        for filename in os.listdir(directory_name):
            if filename.endswith('.txt'):
                file_list.append(os.path.join(directory_name, filename))
    except Exception:
        print("Sorry, path does not exist!")

    return file_list


def menu(index, titles):
    """Menu for the application

    Args:
        index (dictionary): Index mapping words to filenames
        title_index (dictionary): Index mapping filenames to the title of the article.
    """    
    search_query = input('Enter a search query, (empty to finish): ')    

    while search_query != '':
        filename_list = search(index, search_query)
        print("Results: ", search_query)
        if len(filename_list) == 0:
            print("No results")
        else:
            for file in filename_list:
                title = titles[file]
                print("File: ", file, "Title: ", title)
        search_query = input('Enter a search query, (empty to finish): ')


def main():
    index = {}
    titles = {} 

    args = sys.argv[1:]             

    if len(args) != 1:
        print("usage")
        return 

    files = get_filenames(args[0])

    if files:
        build_index(files, index, titles)
        menu(index, titles)


if __name__ == '__main__':
    main()