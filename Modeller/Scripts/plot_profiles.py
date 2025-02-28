import matplotlib.pyplot as plt
import modeller

def r_enumerate(seq):
    """Enumerate a sequence in reverse order"""
    # Note that we don't use reversed() since Python 2.3 doesn't have it
    num = len(seq) - 1
    while num >= 0:
        yield num, seq[num]
        num -= 1

def get_profile(profile_file, seq):
    """Read `profile_file` into a Python array, and add gaps corresponding to
       the alignment sequence `seq`."""
    # Read all non-comment and non-blank lines from the file:
    f = open(profile_file)
    vals = []
    for line in f:
        if not line.startswith('#') and len(line) > 10:
            spl = line.split()
            vals.append(float(spl[-1]))
    # Insert gaps into the profile corresponding to those in seq:
    for n, res in r_enumerate(seq.residues):
        for gap in range(res.get_leading_gaps()):
            vals.insert(n, None)
    # Add a gap at position '0', so that we effectively count from 1:
    vals.insert(0, None)
    return vals

e = modeller.Environ()
a = modeller.Alignment(e, file='MGMT-1eh6A.ali')

template = get_profile('MGMT.profile', a['1eh6A'])
model = get_profile('MGMT.profile', a['MGMT'])

# Plot the template and model profiles in the same plot for comparison:
fig, ax = plt.subplots()
ax.set_xlabel('Alignment position')
ax.set_ylabel('DOPE per-residue score')
ax.plot(model, color='red', linewidth=2, label='Model')
ax.plot(template, color='green', linewidth=2, label='Template')
fig.legend()
fig.savefig('dope_profile.png', dpi=200)
