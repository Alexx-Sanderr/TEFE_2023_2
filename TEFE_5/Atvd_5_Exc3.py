import numpy as np
import scipy 
import matplotlib.pyplot as plt
import argparse 

def main():
    if arg.item == 1:
        item_a()

def item_a():
    print( '\nitem a)\n')
    Ns,prob, Ntot = test(10000,100,0.5, 65, False)
    
    print('O número de conjuntos em que cara foi maior ou igual que coroa é: %d'%Ntot)
    
    fig, ax = plt.subplots()
    fig.suptitle('Histograma dos lançamentos de moeda', size =12)
    ax.grid()
    ax.set_xlabel('Prob de Ns maior igual que nE', size = 10)
    ax.set_ylabel('Número de ocorrências', size = 10)
    ax.hist(Ns, np.arange(0,100+1),color='r', alpha=0.3, ec='k', label = 'lançamentos')
    fig.legend()
    fig.show()
    fig.savefig('Exercicio3-a1.svg')
    
    print('\n O p-valor estimado é: %.5f'%prob)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Atividade Assíncrona 5 - Alex Sander')
    parser.add_argument('-i', '--item', type = int, metavar = '', choices = [1], help = 'Escolha entre: 1 - item a')
    parser.add_argument('-L', action = 'store_true', help = 'Imprime no formato certo para passar pro LaTeX')
    arg = parser.parse_args()

    def test(m, N, pvalor, nE):
        np.random.seed(12558940)
        Ns = np.sum(np.random.rand(m, N)< pvalor, axis=1)
        prob = scipy.stats.binom(N,pvalor).sf(nE-1)
        Ntot = np.sum(Ns >= nE)
        return Ns, prob, Ntot
    main()