from pylab import *

data = loadtxt('data/scdata.txt')
pre1 = loadtxt('fig4/sc1.outlet.txt')
pre2 = loadtxt('fig4/sc1b.outlet.txt')
pre0 = loadtxt('fig4/sc3.outlet.txt')

xmax = 60;
xtic = [0, 10, 20, 30, 40, 50, 60];


naoh = data[:, 1]*1.59683;
tt = naoh;
ph   = data[:, 2];
u    = data[:, 3];
al   = data[:, 4];
mg   = data[:, 5];
si   = data[:, 6];
ca   = data[:, 7];
co   = data[:, 8];
ni   = data[:, 9];
mn   = data[:, 10];
cl   = data[:, 11];
no3  = data[:, 12];
so4  = data[:, 13];

scnaoh = 53.18/31/86400
sc = 1000;
tp0      = pre0[:,  1]*scnaoh;
ph0      = pre0[:,  2];
al0      = pre0[:,  3] * sc;
so40     = pre0[:,  4] * sc;
ca0      = pre0[:,  5] * sc;
mg0      = pre0[:,  6] * sc;
mn0      = pre0[:,  7] * sc;
co0      = pre0[:,  8] * sc;
ni0      = pre0[:,  9] * sc;
u0       = pre0[:, 10] * sc;
si0      = pre0[:, 11] * sc;
no30     = pre0[:, 12] * sc;
hco30    = pre0[:, 13] * sc;
na0      = pre0[:, 14] * sc;

tp1      = pre1[:,  1]*scnaoh;
ph1      = pre1[:,  2];
al1      = pre1[:,  3] * sc;
so41     = pre1[:,  4] * sc;
ca1      = pre1[:,  5] * sc;
mg1      = pre1[:,  6] * sc;
mn1      = pre1[:,  7] * sc;
co1      = pre1[:,  8] * sc;
ni1      = pre1[:,  9] * sc;
u1       = pre1[:, 10] * sc;
si1      = pre1[:, 11] * sc;
no31     = pre1[:, 12] * sc;
hco31    = pre1[:, 13] * sc;
na1      = pre1[:, 14] * sc;

tp2      = pre2[:,  1]*scnaoh;
ph2      = pre2[:,  2];
al2      = pre2[:,  3] * sc;
so42     = pre2[:,  4] * sc;
ca2      = pre2[:,  5] * sc;
mg2      = pre2[:,  6] * sc;
mn2      = pre2[:,  7] * sc;
co2      = pre2[:,  8] * sc;
ni2      = pre2[:,  9] * sc;
u2       = pre2[:, 10] * sc;
si2      = pre2[:, 11] * sc;
no32     = pre2[:, 12] * sc;
hco32    = pre2[:, 13] * sc;
na2      = pre2[:, 14] * sc;

fig = figure()
subplots_adjust(hspace=0.001)

ax1=subplot(4, 1, 1);
ax1.plot(tp0, ph0, 'b-.', tp1, ph1, 'r--', tp2, ph2, 'g-', tt, ph, 'bo', linewidth=2);
xlim([0, xmax])
ylim([2, 7])
ylabel('pH')
text(5, 6.5, '(a)')
yticks([2, 3, 4, 5, 6, 7])

text(-5, 8, 'Figure 4', fontsize='x-large', color='b')

ax2 = subplot(4, 1, 2);
ax2.plot(tp1, al1, 'r--', tp2, al2, 'g-', tp0, al0, 'b-.', tt, al, 'bo', linewidth=2);
l = legend(('Model 1,log K$\mathrm{_{sp}}$=22.7', 'Model 1,log K$\mathrm{_{sp}}$=18.7', 'Model 2', 'Observation'), numpoints=1, loc=1, labelspacing=0.1)
l.draw_frame(False)
t = l.get_texts();
setp(t, fontsize='medium');
xlim([0, xmax])
ylim([0, 10.0])
xticks(xtic);
text(5, 9, '(b)')
ylabel('Al (mM)')
yticks([0, 2, 4, 6, 8])

ax3=subplot(4, 1, 3);
ax3.plot(tp0, ca0, 'b-.', tp1, ca1, 'r--', tp2, ca2, 'g-', tt, ca, 'bo', linewidth=2);
xlim([0, xmax])
ylim([0, 10.0])
xticks(xtic);
text(5, 9, '(c)')
ylabel('Ca (mM)')
#xlabel('NaOH added (mmol)')
yticks([0, 2, 4, 6, 8])

ax4 = subplot(4, 1, 4);
ax4.plot(tt, u, 'bo', tp0, u0, '-.', tp1, u1, 'r--', tp2, u2, 'g-', linewidth=2);
xlim([0, xmax])
ylim([0, 0.2])
xticks(xtic);
text(5, 0.18, '(d)')
xlabel('NaOH added (mmol)')
ylabel('U (mM)')
#for tick in ax4.yaxis.get_major_ticks():
#	tick.label.set_fontsize('x-small')
ylabel('U (mM)')#, fontsize='small');
yticks([0.0, 0.1])

xticklabels=ax1.get_xticklabels()+ax2.get_xticklabels()+ax3.get_xticklabels()
setp(xticklabels, visible=False)

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(4, 8.4)
savefig('fig4.pdf')
show()
