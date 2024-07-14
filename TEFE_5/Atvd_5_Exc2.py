import numpy as np
import scipy 
import argparse

def main():
    if arg.item == 1:
        np.random.seed(12558940)
        item_a()
    elif arg.item == 2:
        np.random.seed(11850761)
        item_b()

def item_a():
    print('item a)\n')

    xm, sm, t, pvalor = test(1, 3,  25, 2, t2 = 4.53)
    print('O valor de x médio é: %.5f(%.5f)'%(xm,sm))
    
    print('item a.1)\n')

    print('O valor de t observado foi: %.5f'%t)

    print('item a.2)\n')

    print('O valor de p-valor encontrado foi: %.5f'%pvalor)

def item_b():
    print('item b)\n')

    xm, sm, t, pvalor = test(1, 3,  25, 2, z2 = 2)
    print('O valor de x médio é: %.5f(%.5f)'%(xm,sm))

    print('item b.1)\n')

    print('O valor de z observado foi: %.5f'%t)

    print('item b.2)\n')

    print('O valor de p-valor encontrado foi: %.5f'%pvalor)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = 'Atividade Assíncrona 5 - Alex Sander')
    parser.add_argument('-i', '--item', type = int, metavar = '', choices = [1,2], help = 'Escolha entre: 1 - item a, 2 - item b')
    parser.add_argument('-L', action = 'store_true', help = 'Imprime no formato certo para passar pro LaTeX')
    
    arg = parser.parse_args()

    def test(m, N, x_0, s_0, t2 = None, z2 = None):
        data_xm = []
        data_smtil = []
        for i in range(m):
            x_s = np.random.randn(N)*s_0 + x_0
            x_m = np.mean(x_s)
            data_xm.append(x_m)
            s_til = np.sqrt(sum(((x_s-x_m)**2)/(N-1)))
            s_mtil = s_til/np.sqrt(N)
            data_smtil.append(s_mtil)
        data_xm, data_smtil  = np.asarray(data_xm), np.asarray(data_smtil)

        if t2 is not None:
            t = (data_xm-x_0)/data_smtil
            p_valorT = 2*scipy.stats.t(df=2).sf(x=abs(t))
            return(data_xm, data_smtil, t, p_valorT)
        
        if z2 is not None:    
            z = (data_xm-x_0)/(s_0/np.sqrt(N))
            p_valorZ = 2*scipy.stats.norm.sf(x=abs(z))
            sm_z = s_0/np.sqrt(N)
            return(data_xm, sm_z,z, p_valorZ)

    main()