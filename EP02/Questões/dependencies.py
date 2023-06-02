import networkx as nx

# Author: Vinícius José Soares Barbosa 

    
def dependencies(ddc, c):
    if ddc is None or c is None or c not in ddc: # Validações básicas
        return None

    if not(nx.is_directed(ddc)):
        return None
    
    direct_deps = list(ddc.neighbors(c)) # Dependências diretas
    
    indirect_deps = set() # Dependências indiretas
    
    for dep in direct_deps:
        indirect_deps.update(nx.descendants(ddc, dep))
    
    indirect_deps -= set(direct_deps) # Remover dependências diretas
    indirect_deps -= {c} # Remover o próprio vértice
    
    return direct_deps, list(indirect_deps)
