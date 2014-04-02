'''
Created on Feb 19, 2014

@author: David Reading
'''
def retmax():
    retmax = 10000
    return retmax

def get_local(author):
    '''
    Checks to see if there is a local record for a given author's coauthors, so I don't have to keep contacting NCBI. Should be faster.
    '''
    import os.path
    
    authorclean = author.replace(' ','_')
    
    coll_set = set()
    
    if os.path.isfile('/Users/David/Documents/Development/shouldr/src/data/_gen/'+authorclean+'.txt'):
        filepath = '/Users/David/Documents/Development/shouldr/src/data/_gen/'+authorclean+'.txt'
        authorfile = open(filepath,'r')
        for line in authorfile:
            coll_set.add(line[0:-1])
        
    return coll_set

def cleardir():
    '''
    Clears the local directories of coauthor information to allow new data to be downloaded from NCBI.
    '''
    import os
    import shutil

    shutil.rmtree('/Users/David/Documents/Development/shouldr/src/data')
    os.makedirs('/Users/David/Documents/Development/shouldr/src/data')
    os.makedirs('/Users/David/Documents/Development/shouldr/src/data/_gen')
        
def clean(author):
    '''
    replaces spaces with underscores. Necessary for file nomenclature.
    '''
    authorclean = author.replace(' ','_')
    return authorclean

def copy_from_gen(author,coauthor):
    '''
    pull an author's file from the gen folder and places it into a parent author folder.
    '''
    
    import os
    import shutil
    
    genpath = '/Users/David/Documents/Development/shouldr/src/data'
    
    if not os.path.exists(genpath+'/'+clean(author)+'/'):
        os.makedirs(genpath+'/'+clean(author)+'/')
        shutil.copyfile(genpath+'/_gen/'+clean(coauthor)+'.txt',(genpath+'/'+clean(author)+'/'+clean(coauthor)+'.txt'))
    else:
        shutil.copyfile(genpath+'/_gen/'+clean(coauthor)+'.txt',(genpath+'/'+clean(author)+'/'+clean(coauthor)+'.txt'))
    return