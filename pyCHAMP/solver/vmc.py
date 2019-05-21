from functools import partial
from pyCHAMP.solver.solver_base import SolverBase


class VMC(SolverBase):

    def __init__(self, wf=None, sampler=None, optimizer=None):
        SolverBase.__init__(self, wf, sampler, optimizer)

    def sample(self, param):
        partial_pdf = partial(self.wf.pdf, param)
        pos = self.sampler.generate(partial_pdf)
        return pos
