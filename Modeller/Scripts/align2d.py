from modeller import *

env = Environ()
aln = Alignment(env)
mdl = Model(env, file='1eh6', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='1eh6A', atom_files='1eh6.pdb')
aln.append(file='mgmt.ali', align_codes='MGMT')
aln.align2d(max_gap_length=50)
aln.write(file='mgmt-1eh6A.ali', alignment_format='PIR')
aln.write(file='mgmt-1eh6A.pap', alignment_format='PAP')
