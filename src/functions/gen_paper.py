'''
Created on Feb 19, 2014

@author: David Reading
'''

def gen_paper(identifier,num_to_gen,author):
    '''
    Creates objects from a paper's metadata
    '''
    
    
    #import modules
    from Bio import Entrez
    Entrez.email = "readingd@me.com"
    
    from classes.paper import paper

    #Search PubMed for a given author, return a maximum of 20 results
    handle = Entrez.esearch(db="pubmed", retmax=num_to_gen, term=author+" [AU]")
    results = Entrez.read(handle)
    IDs = results['IdList']
    handle.close()
    handle = Entrez.esummary(db="pubmed", id=IDs[identifier])
    record = Entrez.read(handle)
    Title = (record[0]['Title']).encode('utf-8')
    PubDate = (record[0]['PubDate']).encode('utf-8')
    AuthorList = (record[0]['AuthorList'])
    AuthorList = [z.encode('utf-8') for z in AuthorList]
    LastAuthor = (AuthorList[-1]).encode('utf-8')
    handle.close()
    reference = paper(Title,LastAuthor,PubDate,AuthorList)
    return reference