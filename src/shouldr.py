# -*- coding: utf-8 -*-
'''
Created on Feb 20, 2014

@author: David
'''


if __name__ == '__main__':
    pass

#import general modules

#import specialized modules

#import local modules - as needed
from functions.ncbi_tools import get_coauthors
from functions.compare_tools import compare_authors
from functions.local_tools import cleardir

author1 = 'HALLAM STEVEN'
author2 = 'CROWE SEAN'

cleardir()
compare_authors(author1,author2)
