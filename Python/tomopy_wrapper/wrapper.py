from __future__ import (absolute_import, division, print_function)
from tigre.geometry import TIGREParameters
import numpy as np
import tomopy
import copy
from matplotlib import pyplot as plt
import tigre
from _Ax import Ax

# TODO: modify 'center' so that it actually does something.

def tigre_w(tomo,  theta, recon, center=None, **kwargs):
    default_opts = {'blocksize': 20,
                    'lmbda': 1,
                    'lmbda_red': 0.99,
                    'OrderStrategy': None,
                    'Quameasopts': None,
                    'init': None,
                    'verbose': True,
                    'noneg': True,
                    'computel2': False,
                    'geo': {}
                    }

    opts = default_opts
    opts.update(kwargs['options'])

    niter = opts['num_iter']
    m_opt = opts['method']

    # generate tigre geometry

    geo=tigre.geo(recon.shape,geo=opts['geo'])
    
    if m_opt is 'OS_SART':
        res = tigre.OS_SART(tomo, geo, theta, niter,
                            blocksize=opts['blocksize'],
                            lmbda=opts['lmbda'],
                            lmbda_red=opts['lmbda_red'],
                            OrderStrategy=opts['OrderStrategy'],
                            Quameasopts=opts['Quameasopts'],
                            init=opts['init'],
                            verbose=opts['verbose'],
                            computel2=opts['computel2'])

        return res
    if m_opt is 'SART':
        res = tigre.SART(tomo, geo, theta, niter,
                         lmbda=opts['lmbda'],
                         lmbda_red=opts['lmbda_red'],
                         OrderStrategy=opts['OrderStrategy'],
                         Quameasopts=opts['Quameasopts'],
                         init=opts['init'],
                         verbose=opts['verbose'],
                         computel2=opts['computel2'])
        return res
    if m_opt is 'SIRT':
        res = tigre.SIRT(tomo, geo, theta, niter,
                         lmbda=opts['lmbda'],
                         lmbda_red=opts['lmbda_red'],
                         OrderStrategy=opts['OrderStrategy'],
                         Quameasopts=opts['Quameasopts'],
                         init=opts['init'],
                         verbose=opts['verbose'],
                         computel2=opts['computel2'])
    if m_opt is 'SART_TV':
        res = tigre.SART_TV(tomo, geo, theta, niter,
                             lmbda=opts['lmbda'],
                             lmbda_red=opts['lmbda_red'],
                             OrderStrategy=opts['OrderStrategy'],
                             Quameasopts=opts['Quameasopts'],
                             init=opts['init'],
                             verbose=opts['verbose'],
                             computel2=opts['computel2'])
        return res
    if m_opt is 'FDK':
        res = tigre.FDK(tomo, geo, theta)
        return res
    if m_opt not in ['SIRT', 'SART', 'OS_SART', 'FDK','SART_TV']:
        raise ValueError('Algorithm for TIGRE not recognised')


obj = tomopy.shepp3d((64, 64, 64))
ang = np.linspace(0, 2 * np.pi, 100, dtype=np.float32)
geo = tigre.geo((64,64,64),geo={'nDetector':[94,64]})
sim = tomopy.project(obj,ang).transpose(1,2,0)
sim2 = Ax(obj,geo,ang,'ray-voxel')
print(geo)
print (sim.shape)
print(sim2.shape)
# rec = tigre_w(sim2, ang, obj, options={'method': 'SART', 'num_iter': 10, 'blocksize': 20,'geo':{'filter':'shepp_logan',
#                                                                                                'nDetector':[94,64],
#                                                                                                'mode':'parallel'}})
rec1 = tigre_w(sim, ang, obj, options={'method': 'SART_TV', 'num_iter': 10, 'blocksize': 20,'geo':{'filter':'shepp_logan',
                                                                                               'nDetector':[94,64],
                                                                                               'mode':'parallel'}})
tigre.plotImg(rec1)



