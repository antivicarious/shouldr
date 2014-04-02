'''
Created on Feb 19, 2014

@author: David Reading
'''

def get_coauthors(author):
    '''
    gets an author and returns all their coauthors.
    '''
     
    #import modules
    from Bio import Entrez
    Entrez.email = "readingd@me.com"
    from functions.local_tools import get_local
    from functions.local_tools import retmax
    import os
    import sys
    
    coll_set = set()
    
    #Check to see whether search is necessary
    authorclean = author.replace(' ','_')
    if os.path.isfile('/Users/David/Documents/Development/shouldr/src/data/_gen/'+authorclean+'.txt'):
        print
        print 'local records were found for '+author
        coll_set = get_local(author)
    else:
        #Search PubMed for a given author, return a maximum of 10000 results
        #print 'contacting PubMed...'
        print
        handle = Entrez.esearch(db="pubmed", retmax=retmax(), term=author+" [AU]")
        results = Entrez.read(handle)
        IDs = results['IdList']
        print str(len(IDs))+' paper IDs found for '+author+'...'
        #print
        handle.close()
        
        lastperc = 0
        
        for x in range(len(IDs)):
            handle = Entrez.esummary(db="pubmed", id=IDs[x])
            record = Entrez.read(handle)
            #Title = (record[0]['Title']).encode('utf-8')
            percent = int((50/float(len(IDs)))*float(x+1))
            sys.stdout.write((percent-lastperc)*'|'),
            lastperc = percent
            #print 'parsing '+author+' ID '+str(x+1)+' of '+str(len(IDs))+' ... ('+Title[0:30]+')'
            #PubDate = (record[0]['PubDate']).encode('utf-8')
            #print PubDate
            AuthorList = (record[0]['AuthorList'])
            AuthorList = [z.encode('utf-8') for z in AuthorList]
            #print AuthorList
            for n in AuthorList:
                n = n.upper()
                coll_set.add(n)
            #LastAuthor = (AuthorList[-1]).encode('utf-8')
            #print LastAuthor
            handle.close()
        
        #print
        #print 'finished parsing papers.'
        #print
        #print 'writing authors to text file...'
        authorclean = author.replace(' ','_')
        filepath = '/Users/David/Documents/Development/shouldr/src/data/_gen/'+authorclean+'.txt'
        authorfile = open(filepath,'w')
        for i in coll_set:
            authorfile.write(i + '\n')
            
        authorfile.close()
        #print 'authors written to text file.'
        #print
        
    return coll_set
