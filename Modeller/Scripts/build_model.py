from modeller import *
from modeller.automodel import *
#from modeller import soap_protein_od
env.io.hetatm = True
env = Environ()
a = AutoModel(env, alnfile='mgmt-1eh6A.ali',
              knowns='1eh6A', sequence='MGMT',
              assess_methods=(assess.DOPE,
                              #soap_protein_od.Scorer(),
                              assess.GA341))
a.starting_model = 1
a.ending_model = 5
a.make()