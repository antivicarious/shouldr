'''
Created on Feb 19, 2014

@author: David Reading
'''

class paper(object):
    '''
    classdocs
    '''
    
    
    def __init__ (self,Title,LastAuthor,PubDate,AuthorList):
        '''
        Constructor
        '''
        self.title = Title
        self.lastauthor = LastAuthor
        self.pubdate = PubDate
        self.authorlist = AuthorList
        
    def __str__(self):
        ''' 
        Returns the string representation of a paper class in the form chosen
        '''
        return "Paper(%Title, %LastAuthor, %PubDate, %AuthorList)"