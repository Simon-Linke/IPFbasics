import numpy as np

def IPF(g,p,g0):
    # calculates the IPF a single time

    # g is array with previous n system state
    # p is array of IPF modelling paramters \alpha and \beta_k
    # g0 is inital value, wich is used, when IPF is diverging
    g1=np.array(g)
    g1[g1!=g1]=g0 #replace nan values by g0

    su=0

    for i in range(1,len(p)):
        su=su+p[i]*np.exp(g1[0]-g1[i])

    arg=(g1[0]-su)/p[0]

    if arg<0:
        return np.append([np.nan],g[:-1])
    else:
        gt=g1[0]-np.log(arg)

        return np.append([gt],g[:-1])
    
def IPF_ser(it,p,g0):
    # calculates the IPF multiple iterations

    # it numner of iterations of calculating the IPF
    # p is array of IPF modelling paramters \alpha and \beta_k
    # g0 is inital value, wich is used, when IPF is diverging
    g=np.ones(len(p))*g0

    G=np.zeros(it)

    for i in range(it):
        g=IPF(g,p,g0)
        G[i]=g[0]

    return(G)

def IPF_chAlpha(it,p,al,g0):
    # calculates the IPF multiple iterations while linearly changing alpha

    # it numner of iterations of calculating the IPF
    # p is array of IPF modelling paramters alpha (at start) and \beta_k
    # al alpha after all iterations
    # g0 is inital value, wich is used, when IPF is diverging

    alp=np.linspace(p[0], al, it)
    g=np.ones(len(p))*g0

    G=np.zeros(it)

    for i in range(it):
        g=IPF(g,np.append(alp[i],p[1:]),g0)
        G[i]=g[0]
    return(G)

def ampMod(A,c,han=True):
    #weights the Amplitude of a single Periode with the factor c, if han=true the Amplitude is also weighted by a hanning-window
    A=np.array(A)
    if han:
        A=A*np.hanning(len(A))

    return A*c