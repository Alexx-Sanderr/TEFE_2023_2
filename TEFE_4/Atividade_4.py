# Created by Alexx-Sanderr - Statistical Data Treatment in Experimental Physics 
 
import argparse 
import glob
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import os
from pathlib import Path
from scipy.optimize import fmin

def main():
    
    if arg.item == 1:
        item_a()
    elif arg.item == 2:
        item_b()
    elif arg.item == 3:
        item_c()

# Itens:
def item_a():
    for i in range(len(data)):
        dat = np.loadtxt(data[i])
        dat_t, dat_h, dat_s = dat[:,0].astype(float), dat[:,1].astype(float), dat[:,2].astype(float)    #leitura dos arquivos por variável
        if i == 0:
            h_0, tau = 14, 120                             #Estimativas observacionais a partir da figura
            cerve = Path(data[i]).stem
        elif i == 1:
            h_0, tau = 14, 160                             #Estimativas observacionais a partir da figura
            cerve = Path(data[i]).stem
        elif i ==  2:
            h_0, tau = 17, 280                             #Estimativas observacionais a partir da figura
            cerve = Path(data[i]).stem                         

        chi = np.sum(((dat_h - h_0*np.exp(-dat_t/tau))/dat_s)**2)
        print('chi^2 = ' + str(chi) + ' para ' + str(cerve.split('_')[1]))


def item_b():
    '''
    Determinação dos parâmetros h_0 e tau, a partir de ajuste via MMQ. 
    '''

    print('\nitem - b)')	                                                                        #* \label{lin:item - b-ini} *)
    #Aqui aplicaremos o método de MMQ para ajustar os parâmetros citados.
    dat = np.loadtxt(data[arg.cerveja-1])                                                           # leitura dos dados da cerveja selecionada
    dat_t, dat_h, dat_s = dat[:,0].astype(float), dat[:,1].astype(float), dat[:,2].astype(float)    #leitura dos arquivos por variável
    
    cerve = Path(data[arg.cerveja-1]).stem
    print('A cerveja selecionada foi:' + str(cerve.split('_')[1]))


    print('\nitem - b_1)\n')                                                                          #* \label{lin:item - b_1-ini} *)

    yi = np.log(np.asarray(dat_h))                                                                  # y = ln(h)
    sig_yi_2 = np.asarray(dat_s/dat_h)**2                                                           # sy² = (sh/h)²
    g_1 = np.ones_like(dat_t)
    G = np.asarray([g_1, -1*dat_t])
    D = np.zeros((len(G), 1))
    M = np.zeros((len(G),len(G)))
 
    for i in range(len(G)):
        D[i,0] =  np.sum(yi*G[i]/sig_yi_2)
        for j in range(len(G)):
            M[i,j] = np.sum(G[i]*G[j]/sig_yi_2)

    M_1 =  np.linalg.inv(M)
    A = M_1 @ D 
    sA = np.sqrt( np.diag(M_1) ).reshape( (-1,1) )
    print(A)
    print('Os valores dos parâmetros são:\n a = %.5f(%.5f)\n b = %.5f(%.5f)' %(A[0], sA[0], A[1], sA[1]))
    print('A matrix de covariância é dada por:\n %s'%M_1)                                           #* \label{lin:item - b_1-fim} *)

    print('\nitem - b_2)\n')                                                                        #* \label{lin:item - b_2-ini} *)

    h_0 = np.exp(A[0])
    tau = 1/A[1]
    sig_h0 = np.sqrt((h_0*sA[0])**2)
    sig_tau = np.sqrt(((-1/(A[1]**2))*sA[1])**2)
    print('Os valores dos parâmetros são:\n h_0 = %.5f(%.5f) cm\n tau = %.5f(%.5f) s' %(h_0, sig_h0, tau, sig_tau)) #* \label{lin:item - b_2-fim} *)

    print('\nitem - b_3)\n')                                                                        #* \label{lin:item - b_3-ini} *)

    f = lambda x: h_0*np.exp(-x/tau)
    t = np.linspace(0,400)
    Q = (dat_h - f(dat_t))/dat_s

    # Plot do ajuste e dos resíduos
    fig = plt.figure(constrained_layout = True)
    spec = plt.GridSpec(ncols = 4, nrows = 3, figure = fig)
    ax1 = fig.add_subplot(spec[0:2, :])
    ax2 = fig.add_subplot(spec[2,:])
    fig.suptitle(' Ajuste da função $h = h_0\cdot e^{\dfrac{-t}{T}}$ para ' + str(cerve.split('_')[1]), fontsize = '14')
    fig.supxlabel('tempo (s)', fontsize = '12')
    fig.supylabel('altura (cm)', fontsize= '12')
    plt.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
    ax1.grid()
    ax1.scatter(dat_t, dat_h, color = 'red', alpha = 0.3, ec = 'k', label =  'Dados')
    ax1.plot(t, f(t),color = 'k', linestyle =  '--', alpha = 0.6, label =  'Ajuste')
    ax1.errorbar(x =dat_t, y=dat_h, yerr = dat_s, fmt =  '.r', alpha = 0.3, capsize=2, barsabove=True)
    ax1.legend()
    ax2.grid()
    ax2.axhline(y=0, color = 'k', linestyle = '--', alpha = 0.4 )
    ax2.scatter(dat_t, Q, color = 'red', alpha = 0.3, ec = 'k')
    plt.savefig(str(arg.path)+'/Exercicio2_item_b_3_' + str(cerve.split('_')[1]) + '.svg')
    plt.show()
    print('verifique no diretório a existencia de um .sgv')                                         #* \label{lin:item - b_3-fim} *)

    print('\nitem - b_4)\n')                                                                        #* \label{lin:item - b_4-ini} *)

    chi = np.sum(((dat_h - h_0*np.exp(-dat_t/tau))/dat_s)**2)
    print('Chi^2 = %.5f'%(chi))                                                                     #* \label{lin:item - b_4-fim} *)


def item_c():

    cerve = Path(data[arg.cerveja-1]).stem
    print('A cerveja selecionada foi:%' + str(cerve.split('_')[1]))

    dat = np.loadtxt(data[arg.cerveja-1])                                                           # leitura dos dados da cerveja selecionada
    dat_t, dat_h, dat_s = dat[:,0].astype(float), dat[:,1].astype(float), dat[:,2].astype(float)    #leitura dos arquivos por variável

    f_h = lambda A: A[0]*np.exp(-dat_t/A[1])
    f_q = lambda A: np.sum(((dat_h - f_h(A))/dat_s)**2)
    Ac = [max(dat_h), 150]
    A = fmin(f_q, Ac)
    print('O valor dos parâmetros são:\nh_0 = %.5f cm\ntau = %.5f s'%(A[0], A[1])) 

    chi = np.sum(((dat_h - A[0]*np.exp(-dat_t/A[1]))/dat_s)**2)
    print('Chi^2 = %.5f'%(chi))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = 'Atividade Assíncrona 4 - Alex Sander')
    parser.add_argument('-p', '--path', type = Path, default = Path(__file__).absolute().parent / "data", metavar = '', help = 'Caminho para os arquivos')
    parser.add_argument('-i', '--item', type = int, metavar = '', choices = [1,2,3], help = 'Escolha entre: 1 - item a, 2 - item b e 3 - item c')
    parser.add_argument('-c', '--cerveja', type = int, metavar = '', choices = [1, 2, 3], help = 'Escolha entre: 1 = Augustiner, 2 = Budweiser e 3 = Erdinger ' )
    parser.add_argument('-L', action = 'store_true', help = 'Imprime no formato certo para passar pro LaTeX')
    
    arg = parser.parse_args()
    data = sorted(filter(os.path.isfile, glob.glob(str(arg.path)+'/*.txt')))   
    main()
