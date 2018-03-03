# -*- coding: utf-8 -*-
# Algebra Linear

height_weight_age = [70,170,40] # Polegas, Quilos e Anos
grades = [95,80,75,62] # Teste1 e Teste2...

def vector_add(v,w):
    """Soma elementos correspondentes V e W são vetores de tamanhos iguais"""
    return [v_i + w_i for v_i, w_i in zip(v,w)]

def vector_subtract(v,w):
    """Idem o de soma"""
    return  [v_i - w_i for v_i, w_i in zip(v,w)]

def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result,vector)
    # Jeito Fácil: return reduce(vector_add,vectors)
    return result
def scalar_multiply(c,v):
    """c é um numero, v um vetor"""
    return [c*v_i for v_i in v]
