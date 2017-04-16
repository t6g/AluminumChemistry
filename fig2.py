from pylab import *

data = loadtxt('data/luowco2.txt')
pre1 = loadtxt('fig2/wco2ax.txt')

naoh = data[:, 0];
ph   = data[:, 1];
u    = data[:, 2];

sc = 1e3;
ph1      = pre1[:, 0];
naoh1    = pre1[:, 1]*sc;
u1       = pre1[:, 2]*sc;

xmax = 30;

plot(naoh1, u1, 'b-', naoh1, pre1[:, 7]*sc, 'r--', naoh1, pre1[:, 5]*sc, 'g-.', naoh, u, 'bo', linewidth=2)
l = legend(('Aqueous', 'Sorbed to Fe hydroxides', 'Liebigite', 'Observation'), numpoints=1, loc=2)
l.draw_frame(False)
t = l.get_texts();
setp(t, fontsize='small');
xlim([0, xmax])
ylim([0, 0.12])
ax = gca()
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize('x-small')
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize('x-small')
ylabel('U (mM)', fontsize='x-small');
xlabel('NaOH added (mM)',fontsize='x-small')

text(-4, 0.125, 'Figure 2', fontsize='medium', color='b')

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(4, 3)
savefig('fig2.pdf')
show()
