# -*- coding: utf-8 -*-
"""
Created on Fri Jul  4 15:13:45 2025

@author: tizia

Description: 
    this function allow to create an extension of the classic Kronecker Delta:
    δ(i_1 + i_2 + ... + i_S = i_1 + i_2 + ... + i_T), where i is an array-like 
    with integer component from "inf" up to "sup", i.e. if inf = -2 and sup = 3
    the array looks like i=(-2,-1,0,1,2,3). The subscript are indication of
    dummy variables: instead og using i,j,k, and so on, we use i_1 + i_2,...
    to define indeces.  
    
Example: let's consider 3 indeces i_1, i_2, and i_3 within a range between 
        -128 and and 128 and a elta of the kind δ(i_1 + i_2 - i_3).
        To call the function you enter as arguments (-128,128,2,1). The output 
        is a 3-dimensional tensor of 257 lenght in each direction.
"""

import numpy as np
import operator 

pi = np.pi

def delta(inf, sup ,S,T):
    '''
    Parameters
    ----------
    inf : integer.
        Inferior limit of the array-range.
    sup : integer.
        Superior limit of the array-range.        
    S : integer.
        A value expressing the number of positive sign.
    T : integer from 1 to 5
        A value expressing the number of ngative sign.
        
        M = S+T is the number of variables involved in the linear combination.
        
        Note:
        - By Commutative property of linear algebra t The combination is structured
        in such a way that you first have in order all the positive contributions
        and then the negatives, e.g. if n=5 and resonace_type=3 gives a 
        combination with 3 '+' and two '-':
        +o1 +o2 +o3 -o4 -o5, where o_i represent the i-th object.
        - the first element of the combination is always positive;
        - The '+' number is = to S - 1
        - while '-' = to T
        
    Returns
    -------
    A M-dim hyper-matrice made of 0 and 1 generalizing the classical Kronacker-delta,
    which takes more than two arguments.

    '''  
    # Class of resonance
    M = S + T
    if M > 6 or M < 3:
        return print('WARNING: This resonance class is not allowed! Please choose S and T in such a way that their sum do not exceed 6')
    else:    
 
        list_op = [operator.add if m<S else operator.sub for m in range(1,M)]    
        
        sup = sup + 1
        N = np.abs(sup) + np.abs(inf) 
        tensor_k = np.zeros([N]*M)
        
        if M == 3:
            for i1 in range(inf,sup):                 
                 for i2 in range(inf,sup):         
                     for i3 in range(inf,sup):
                        list_o = [i1,i2,i3]
                        
                        for m in range(M-1):
                            if m ==0:
                                op = list_op[0](list_o[0],list_o[1])
                            else:
                                op = list_op[m](op,list_o[m+1])                                      
                        if op%N == 0:
                            tensor_k[i1][i2][i3] = 1    
        elif M == 4:
    
            for i1 in range(inf,sup):                 
                 for i2 in range(inf,sup):         
                     for i3 in range(inf,sup):
                        for i4 in range(inf,sup):    
                            list_o = [i1,i2,i3,i4]
    
                            for m in range(M-1):
                                if m ==0:
                                    op = list_op[0](list_o[0],list_o[1])
                                else:
                                    op = list_op[m](op,list_o[m+1])  
                              
                            if op%N == 0:
                                tensor_k[i1][i2][i3][i4] = 1  
        elif M == 5:
    
            for i1 in range(inf,sup):                 
                 for i2 in range(inf,sup):         
                     for i3 in range(inf,sup):
                        for i4 in range(inf,sup):       
                            for i5 in range(inf,sup):    
                                list_o = [i1,i2,i3,i4,i5]
        
                                for m in range(M-1):
                                    if m ==0:
                                        op = list_op[0](list_o[0],list_o[1])
                                    else:
                                        op = list_op[m](op,list_o[m+1])  
                                  
                                if op%N == 0:
                                    tensor_k[i1][i2][i3][i4][i5] = 1   
        elif M == 6:
    
            for i1 in range(inf,sup):                 
                 for i2 in range(inf,sup):         
                     for i3 in range(inf,sup):
                        for i4 in range(inf,sup):       
                            for i5 in range(inf,sup):    
                                for i6 in range(inf,sup):    
                                    list_o = [i1,i2,i3,i4,i5,i6]
            
                                    for m in range(M-1):
                                        if m ==0:
                                            op = list_op[0](list_o[0],list_o[1])
                                        else:
                                            op = list_op[m](op,list_o[m+1])  
                                      
                                    if op%N == 0:
                                        tensor_k[i1][i2][i3][i4][i5][i6] = 1   
                                    
    return tensor_k
