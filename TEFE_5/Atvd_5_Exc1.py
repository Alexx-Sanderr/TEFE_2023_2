import numpy as np
import matplotlib.pyplot as plt 
import scipy
import argparse

def main():  
    if arg.item == 1:
        exc_1()
    elif arg.item == 2:
        exc_extra()

def exc_1():
    print('item b)\n')
    t, ft2, sft2 = test(10_000, 3,  50, 10, t2 = 4.53)
    t_m = sum(abs(t))/len(t)
    print('O valor de t médio é: %.5f'%t_m)

    print('\nitem b.1)\n')

    fig, ax = plt.subplots()
    fig.suptitle('Histograma dos valores de t', size=12)
    ax.grid()
    ax.set_xlabel('Valores de t', size=10)
    ax.set_ylabel('Número de ocorrências', size=10)
    ax.hist(t, bins=40,range=(-20,20),color='c', alpha=0.3, ec='k', label = 't-bins')
    fig.legend()
    fig.show()
    fig.savefig('Exercicio1-b1.svg')
    
    print('Confira o histograma (.SGV) na pasta deste arquivo')
    

    print("\nitem b.2)\n")
    print('A frequência, ft2, é de: %.5f(%.5f)'%(ft2, sft2))

    print('\nitem c)\n')

    z, fz2, sfz2 = test(10_000, 3,  50, 10, z2 = 2)
    z_m = sum(abs(z))/len(z)
    print('O valor de z médio é: %.5f'%z_m)

    print('\nitem c.1)\n')
    fig, ax = plt.subplots()
    fig.suptitle('Histograma dos valores de z', size = 12)
    ax.grid()
    ax.set_xlabel('Valores de z', size=10)
    ax.set_ylabel('Número de ocorrências', size=10)
    ax.hist(z, bins=40,color='g', alpha=0.3, ec='k', label = 't-bins')
    fig.legend()
    fig.show()
    fig.savefig('Exercicio1-c1.svg')

    print('Confira o histograma (.SGV) na pasta deste arquivo')
    

    print("\nitem c.2)\n")
    print('A frequência, fz2, é de: %.5f(%.5f)'%(fz2, sfz2))

def exc_extra():
    print('\nitem b)\n')
    t, ft2, sft2 = test(10_000, 21,  50, 10, t2 = 2.13)
    t_m = sum(abs(t))/len(t)
    print('O valor de t médio é: %.5f'%t_m)

    print('\nitem b.1)\n')

    fig, ax = plt.subplots()
    fig.suptitle('Histograma dos valores de t', size =12)
    ax.grid()
    ax.set_xlabel('Valores de t', size = 10)
    ax.set_ylabel('Número de ocorrências', size = 10)
    ax.hist(t, bins=40,range=(-20,20),color='b', alpha=0.3, ec='k', label = 't-bins')
    fig.legend()
    fig.show()
    fig.savefig('Exercicio_extra-b1.svg')

    print('Confira o histograma (.SGV) na pasta deste arquivo')
    

    print("\nitem b.2)\n")
    print('A frequência, ft2, é de: %.5f(%.5f)'%(ft2, sft2))

    print('\nitem c)\n')

    z, fz2, sfz2 = test(10_000, 21,  50, 10, z2 = 2)
    z_m = sum(abs(z))/len(z)
    print('O valor de z médio é: %.5f'%z_m)

    print('\nitem c.1)\n')


    fig, ax = plt.subplots()
    fig.suptitle('Histograma dos valores de z', size=12)
    ax.grid()
    ax.set_xlabel('Valores de z', size=10)
    ax.set_ylabel('Número de ocorrências', size=10)
    ax.hist(z, bins=40,color='r', alpha=0.3, ec='k', label = 't-bins')
    fig.legend()
    fig.show()
    fig.savefig('Exercicio_extra-c1.svg')

    print('Confira o histograma (.SGV) na pasta deste arquivo')
    

    print("\nitem c.2)\n")
    print('A frequência, fz2, é de: %.5f(%.5f)'%(fz2, sfz2))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = 'Atividade Assíncrona 5 - Alex Sander')
    parser.add_argument('-i', '--item', type = int, metavar = '', choices = [1,2], help = 'Escolha entre: 1 - exc_1, exc_extra')
    parser.add_argument('-L', action = 'store_true', help = 'Imprime no formato certo para passar pro LaTeX')
    
    arg = parser.parse_args()
    np.random.seed(12558940)

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
            nt = np.sum(abs(t) <= t2)
            ft2 = nt/m
            sft2 = np.sqrt(nt*(1-nt/m))/m
            return(t, ft2, sft2)
        
        if z2 is not None:    
            z = (data_xm-x_0)/(s_0/np.sqrt(N))
            nz = np.sum(abs(z) <= z2)
            fz2 = nz/m
            sfz2 = np.sqrt(nz*(1-nz/m))/m
            return(z, fz2, sfz2)
    main()