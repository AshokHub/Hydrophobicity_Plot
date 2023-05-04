try:
    import google.colab
    !pip install biopython
except ImportError:
    pass

import matplotlib.pyplot as plt
from io import StringIO
from Bio import SeqIO

sequence = ">sp|Q9UKY0|PRND_HUMAN Prion-like protein doppel OS=Homo sapiens GN=PRND PE=1 SV=2\nMRKHLSWWWLATVCMLLFSHLSAVQTRGIKHRIKWNRKALPSTAQITEAQVAENRPGAFIKQGRKLDIDFGAEGNRYYEANYWQFPDGIHYNGCSEANVTKEAFVTGCINATQAANQGEFQKPDNKLHQQVLWRLVQELCSLKHCEFWLERGAGLRVTMHQPVLLCLLALIWLTVK"
fas_seq = StringIO(sequence)
for record in SeqIO.parse(fas_seq, 'fasta'):
    id = record.id # Sequence ID
    seq = record.seq # Raw sequence
    n = len(seq) # Length of the sequence
fas_seq.close()
kd = { 'A': 1.8,'R':-4.5,'N':-3.5,'D':-3.5,'C': 2.5,
       'Q':-3.5,'E':-3.5,'G':-0.4,'H':-3.2,'I': 4.5,
       'L': 3.8,'K':-3.9,'M': 1.9,'F': 2.8,'P':-1.6,
       'S':-0.8,'T':-0.7,'W':-0.9,'Y':-1.3,'V': 4.2 }
x = range(1, n+1)
y = []
for res in seq:
    y.append(kd[res])
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y, 'b', lw = 0.7)
ax.set_xlim(1, n)
ax.set(xlabel = 'Residue Number', ylabel = 'Hydrophobicity', title = 'Hydrophobicity plot for ' + id)
ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.show()