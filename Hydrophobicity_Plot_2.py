import matplotlib.pyplot as plt
seq = "MRKHLSWWWLATVCMLLFSHLSAVQTRGIKHRIKWNRKALPSTAQITEAQVAENRPGAFIKQGRKLDIDFGAEGNRYYEANYWQFPDGIHYNGCSEANVTKEAFVTGCINATQAANQGEFQKPDNKLHQQVLWRLVQELCSLKHCEFWLERGAGLRVTMHQPVLLCLLALIWLTVK"
kd = { 'A': 1.8,'R':-4.5,'N':-3.5,'D':-3.5,'C': 2.5,
       'Q':-3.5,'E':-3.5,'G':-0.4,'H':-3.2,'I': 4.5,
       'L': 3.8,'K':-3.9,'M': 1.9,'F': 2.8,'P':-1.6,
       'S':-0.8,'T':-0.7,'W':-0.9,'Y':-1.3,'V': 4.2 }
n = len(seq)
x = range(1, n+1)
y = []
for res in seq:
    y.append(kd[res])
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y, 'b', lw = 0.7)
ax.set_xlim(1, n)
ax.set(xlabel = 'Residue Number', ylabel = 'Hydrophobicity', title = 'Hydrophobicity Plot')
ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.show()