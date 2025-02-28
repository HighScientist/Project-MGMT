from modeller import *
from modeller.scripts import complete_pdb

log.verbose()    # Request verbose output
env = Environ()
env.libs.topology.read(file='$(LIB)/top_heav.lib') # read topology
env.libs.parameters.read(file='$(LIB)/par.lib') # read parameters

# Read model file
mdl = complete_pdb(env, 'MGMT.B99990003.pdb')

# Assess with DOPE:S
s = Selection(mdl)   # all atom selection
s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='MGMT.profile',
              normalize_profile=True, smoothing_window=15)
