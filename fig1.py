from pylab import *

data = loadtxt('data/luowco2.txt')
pre0 = loadtxt('fig1/wco2b.txt')
pre1 = loadtxt('fig1/wco2bx.txt')
pre2 = loadtxt('fig1/wco2ax.txt')

naoh = data[:, 0];
ph   = data[:, 1];
u    = data[:, 2];
co   = data[:, 4];
ni   = data[:, 5];
mn   = data[:, 6];
fe   = data[:, 7];
ca   = data[:, 8];
si   = data[:, 10];
al   = data[:, 11];
mg   = data[:, 12];

sc = 1e3;
ph0      = pre0[:, 0];
naoh0    = pre0[:, 1]*sc;
al0      = pre0[:, 2]*sc;
ca0      = pre0[:, 4]*sc;
u0       = pre0[:, 5]*sc;

ph1      = pre1[:, 0];
naoh1    = pre1[:, 1]*sc;
al1      = pre1[:, 2]*sc;
ca1      = pre1[:, 4]*sc;
u1       = pre1[:, 5]*sc;

ph2      = pre2[:, 0];
naoh2    = pre2[:, 1]*sc;
al2      = pre2[:, 2]*sc;
ca2      = pre2[:, 4]*sc;
u2       = pre2[:, 5]*sc;

xmax = 30;

fig = figure()
subplots_adjust(hspace=0.001)

ax1=subplot(3, 1, 1);
ax1.plot(naoh0, ph0, 'b-.', naoh1, ph1, 'r--', naoh2, ph2, 'g-', naoh, ph, 'bo', linewidth=2.0)
text(2, 6.5, '(a)')
xlim([0, xmax])
ylim([2, 7])
yticks([2, 3, 4, 5, 6, 7])
ylabel('pH');

text(-4, 8, 'Figure 1', fontsize='x-large', color='b')

ax2=subplot(3, 1, 2);
ax2.plot(naoh0, al0, 'b-.', naoh1, al1, 'r--', naoh2, al2, 'g-', naoh, al, 'bo', linewidth=2.0)
l = legend(('Model 1 $\mathrm{K_{Na/Al}}$=0.73', 'Model 1 $\mathrm{K_{Na/Al}}$=0.30', 'Model 2 $\mathrm{K_{Na/Al}}$=0.30', 'Observation'), numpoints=1, loc=1)
l.draw_frame(False)
t = l.get_texts();
setp(t, fontsize='small');
text(2, 2.7, '(b)')
xlim([0, xmax])
ylim([0, 3])
yticks([0, 1, 2])
ylabel('Al (mM)');

ax3=subplot(3, 1, 3);
ax3.plot(naoh0, ca0, 'b-.', naoh1, ca1, 'r--', naoh2, ca2, 'g-', naoh, ca, 'bo', linewidth=2.0)
xlim([0, xmax])
ylim([0, 3])
text(2, 2.7, '(c)')
ylabel('Ca (mM)');
yticks([0, 1, 2])
xlabel('NaOH added (mM)')

xticklabels=ax1.get_xticklabels()+ax2.get_xticklabels()
setp(xticklabels, visible=False)

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(4, 6.3)
savefig('fig1.pdf')
show()
