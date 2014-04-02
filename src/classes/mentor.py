'''
Created on Feb 19, 2014

@author: David Reading
'''

class mentor(object):
    '''
    classdocs
    '''
    
    
    def __init__ (self,Name,Proteges):
        '''
        Constructor
        '''
        self.name = Name
        self.proteges = Proteges
        
    def __str__(self):
        '''
        Returns the string representation of a mentor and his proteges
        '''
        return "Mentor(%Name, %Proteges)"