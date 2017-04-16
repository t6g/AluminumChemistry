from pylab import *

prea  = loadtxt('figtoc/a0.txt')
prej  = loadtxt('figtoc/j0.txt')
preb0 = loadtxt('figtoc/b0.txt')
preb  = loadtxt('figtoc/b.txt')
preb1 = loadtxt('figtoc/b1.txt')
prec  = loadtxt('figtoc/c0.txt')

gw1 = loadtxt('data/GuNaOH.txt')
gw2 = loadtxt('data/GuNa2CO3.txt')
gw3 = loadtxt('data/luogw.txt')

soil1 = loadtxt('data/za.txt')
soil2 = loadtxt('data/zd.txt')
soil3 = loadtxt('data/luowoco2.txt')
soil4 = loadtxt('data/luowco2.txt')

sc = loadtxt('data/scdata.txt')
scph = sc[:, 2]
scal = sc[:, 4]

lc = loadtxt('data/lcdata.txt')
lcph = lc[:, 2]
lcal = lc[:, 6]

gwph1   = gw1[:, 0];
gwal1   = gw1[:, 6];

gwph2   = gw2[:, 0];
gwal2   = gw2[:, 6];

gwph3   = gw3[:, 1];
gwal3   = gw3[:, 4];

soilph1   = soil1[:, 1];
soilal1   = soil1[:, 4];

soilph2   = soil2[:, 1];
soilal2   = soil2[:, 4];

soilph3   = soil3[:, 1];
soilal3   = soil3[:, 11];

soilph4   = soil4[:, 1];
soilal4   = soil4[:, 11];

plot(prea[:, 0], prea[:, 2]*1e3, 'r:', prej[:, 0], prej[:, 2]*1e3, 'r-.', preb0[:, 0], preb0[:, 2]*1e3, 'g--', preb[:, 0], preb[:, 2]*1e3, 'm-', preb1[:, 0], preb1[:, 2]*1e3, 'b-.', prec[:, 0], prec[:, 2]*1e3, 'k:', scph, scal, 'g^', lcph, lcal, 'm>', gwph1, gwal1, 'bo', gwph2, gwal2, 'bs', gwph3, gwal3, 'bd', soilph1, soilal1, 'rx', soilph2, soilal2, 'r+', soilph3, soilal3, 'r*', soilph4, soilal4, 'r.',markeredgecolor='none',linewidth=2)
#l = legend(('Alunite', 'Jurbanite', 'Basal. log K$\mathrm{_{sp}}$=19.7', 'Basal. log K$\mathrm{_{sp}}$=22.7', 'Basal. log K$\mathrm{_{sp}}$=25.0', 'Al(OH)$\mathrm{_{3a}}$', 'Small column', 'Large column'), numpoints=1, loc=1)
#l.draw_frame(False)
#t = l.get_texts();
#setp(t, fontsize='x-small');
text(3.1,  2.5, 'soil', color='r', rotation=-50, size='x-small')
text(3.5, 5.0, 'small column', color='g', rotation=-75, size='x-small')
text(3.7,   6, 'large column', color='m', rotation=-75, size='x-small')
text(4.2,   6, 'groundwater', color='b', rotation=-80, size='x-small')
text(4.8,   9, 'Al(OH)$\mathrm{_{3a}}$', rotation=-80, size='small')
text(3.5, 9.2, 'Basaluminite', size='small')
text(3.4, 8.5, 'log K$\mathrm{_{sp}}$ = 19.7', color='g', rotation=-85, size='x-small')
text(3.6, 8.5, 'log K$\mathrm{_{sp}}$ = 22.7', color='m', rotation=-85, size='x-small')
text(4.1, 8.5, 'log K$\mathrm{_{sp}}$ = 25.0', color='b', rotation=-85, size='x-small')
text(3.1,  3.8, 'Jurbanite', color='r', rotation=-50, size='small')
text(3.03,  1.8, 'Alunite', color='r', rotation=-50, size='small')

xlim([3, 5.5])
ylim([0, 10])
xlabel('pH');
ylabel('Al (mM)');

text(2.8, 10.5, 'Figure TOC', fontsize='medium', color='b')

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(5.2, 4)
savefig('figtoc.pdf')
show()
