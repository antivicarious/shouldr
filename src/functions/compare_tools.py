'''
Created on Feb 20, 2014

@author: David
'''
def compare_authors(author1,author2):
    #import general modules
    
    #import specialized modules
    
    #import local modules - as needed.
    from functions.ncbi_tools import get_coauthors
    from functions.local_tools import copy_from_gen
    
    #check to see whether two authors have published together
    author1_coauthors = get_coauthors(author1)
    #print author2
    #print author1_coauthors
    author2_coauthors = get_coauthors(author2)
    #print author1
    #print author2_coauthors
    
    
    if author1 in author2_coauthors or author2 in author1_coauthors:
        print
        print author1 + ' has published with ' + author2
        exit()
    else:
        print
        print author1 + ' has not published with ' + author2
        print
        raw_input('Press Enter to move to 1 degree of separation. Each new degree of separation requires an exponential amount more computing power.')
        author1_dictionary = {}
        author2_dictionary = {}
        for c in author1_coauthors:
            author1_dictionary[c] = get_coauthors(c)
            copy_from_gen(author1,c)
        for d in author2_coauthors:
            author2_dictionary[d] = get_coauthors(d)
            copy_from_gen(author2,d)
        
        for key,value in author1_dictionary.iteritems():
            if author2 == value:
                print author1 + ' has published with ' + author2 + 'via '+key
                exit()
            else:
                continue
        for key,value in author2_dictionary.iteritems():
            if author1 == value:
                print author1 + ' has published with ' + author2 + 'via '+key
                exit()
            else:
                continue
        print
        print author1 + ' has not published with ' + author2 + ' at 1 degree of separation.'
        print
        raw_input('Press Enter to move to 2 degrees of separation. Each new degree of separation requires an exponential amount more computing power. Computing at this level will likely take hours or days.')
        print
        print 'Just kidding, I totally have no idea how to do this yet.'