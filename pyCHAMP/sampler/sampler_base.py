
from pyCHAMP.sampler.walkers import WALKERS


class SAMPLER_BASE:

    def __init__(self, nwalkers=1000, nstep=1000, nelec=1, ndim=3,
                 step_size=3, domain={'min': -2, 'max': 2},
                 move='all'):

        self.nwalkers = nwalkers
        self.nstep = nstep
        self.step_size = step_size
        self.domain = domain
        self.move = move
        self.nelec = nelec
        self.ndim = ndim

        self.walkers = WALKERS(nwalkers, nelec, ndim, domain)

    def set_ndim(self, ndim):
        self.ndim = ndim

    def set_initial_guess(self, guess):
        self.initial_guess = guess

    def generate(self):
        raise NotImplementedError()
