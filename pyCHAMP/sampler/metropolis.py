import numpy as np
from pyCHAMP.sampler.sampler_base import SamplerBase
from tqdm import tqdm
import torch
import time


class Metropolis(SamplerBase):

    def __init__(self, nwalkers=1000, nstep=1000, nelec=1, ndim=3,
                 step_size=3, domain={'min': -2, 'max': 2},
                 move='all'):
        """ Metropolis HASTING SAMPLER
        Args:
            f (func) : function to sample
            nstep (int) : number of mc step
            nwalkers (int) : number of walkers
            eps (float) : size of the mc step
            boudnary (float) : boudnary of the space
        """

        SamplerBase.__init__(self, nwalkers, nstep, nelec,
                              ndim, step_size, domain, move)

    def generate(self, pdf):
        """ perform a MC sampling of the function f
        Returns:
            X (list) : position of the walkers
        """

        self.walkers.initialize(method='uniform')
        fx = pdf(self.walkers.pos)
        fx[fx == 0] = 1E-6
        ones = np.ones((self.nwalkers, 1))

        for istep in (range(self.nstep)):

            # new positions
            xn = self.walkers.move(self.step_size, method=self.move)

            # new function
            fxn = pdf(xn)
            df = fxn/(fx)

            # accept the moves
            index = self._accept(df)

            # update position/function values
            self.walkers.pos[index, :] = xn[index, :]
            fx[index] = fxn[index]
            fx[fx == 0] = 1E-6

        return self.walkers.pos

    def _accept(self, df):

        ones = np.ones(self.nwalkers)
        P = np.minimum(ones, df)
        tau = np.random.rand(self.nwalkers)
        return (P-tau >= 0).reshape(-1)


class MetropolisTorch(SamplerBase):

    def __init__(self, nwalkers=1000, nstep=1000, nelec=1, ndim=3,
                 step_size=3, domain={'min': -2, 'max': 2},
                 move='all'):
        """ Metropolis HASTING SAMPLER
        Args:
            f (func) : function to sample
            nstep (int) : number of mc step
            nwalkers (int) : number of walkers
            eps (float) : size of the mc step
            boudnary (float) : boudnary of the space
        """

        SamplerBase.__init__(self, nwalkers, nstep, nelec,
                             ndim, step_size, domain, move)

    def generate(self, pdf):
        """ perform a MC sampling of the function f
        Returns:
            X (list) : position of the walkers
        """

        self.walkers.initialize(method='uniform')
        fx = pdf(torch.tensor(self.walkers.pos).float())
        fx[fx == 0] = 1E-6

        for istep in tqdm(range(self.nstep)):

            # new positions
            Xn = torch.tensor(self.walkers.move(
                self.step_size, method=self.move)).float()

            # new function
            t0 = time.time()
            fxn = pdf(Xn)
            df = (fxn/(fx)).double()

            # accept the moves
            index = self._accept(df)

            # update position/function values
            self.walkers.pos[index, :] = Xn[index, :]
            fx[index] = fxn[index]
            fx[fx == 0] = 1E-6

        return self.walkers.pos

    def _accept(self, P):
        ones = torch.ones(self.nwalkers)
        P[P > 1] = 1.0
        tau = torch.rand(self.nwalkers).double()
        index = (P-tau >= 0).reshape(-1)
        return index.type(torch.bool)
