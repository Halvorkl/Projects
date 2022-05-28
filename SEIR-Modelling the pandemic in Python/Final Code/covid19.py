from SEIR_interaction import ProblemInteraction, SolverSEIR, RegionInteraction
import matplotlib.pyplot as plt
import numpy as np
from datetime import date


def read_region(filename):
    infile = open(filename, "r")
    words = []
    for line in infile:
        words += line.split(";")
    lsi = [0]*int(len(words)/6)
    for i in range(len(words)):
        words[i] = words[i].replace("\t", "")
        words[i] = words[i].replace("\n", "")
    for j in range(0, len(words), 6):
        # name=words[j+1]
        name = RegionInteraction(
            f'{words[j+1]}', words[2+j], words[3+j], words[4+j], words[5+j])
        lsi[int(j/6)] = name
    return lsi


def covid19_Norway(beta, filename, num_days, dt):
    counties = read_region(filename)
    problem = ProblemInteraction(counties, "Norge", beta)
    for i in range(len(problem.initial_condition)):
        problem.initial_condition[i] = int(problem.initial_condition[i])
    problem.set_initial_condition()
    problem(problem.initial_condition, 0)
    solver = SolverSEIR(problem, num_days, dt)
    solver.solve()
    # return counties
    plt.figure(figsize=(9, 12))  # set figsize
    problem.plot()
    for i in range(len(counties)):
        plt.subplot(4, 3, i+1)
        problem.region[i].plot()
    plt.subplots_adjust(hspace=0.75, wspace=0.5)
    plt.subplot(4, 3, 12)
    problem.plot()
    plt.legend()
    plt.show()
    return problem

'''
test = read_region("fylker.txt")
covid = covid19_Norway(0.4, "fylker.txt", 150, 1)
print(max(covid.I[0:35])*0.2*0.05)
'''
# denne linjen tar maks antall smittede in perioden 0-35 dager og finner ut hvor mange som trenger respiratorer på dette tidspunktet
# om vi ser på de første 35 dagene ser vi at ca. 414 trengte respratorer
# I og med at beta endrer seg etter 30 dager, er etter 35 dager ett ganske bra estemat på smitten tidligere i pandemien
# nummeret smittede er høyest mellom 60-70 dager på landsbasis i følge denne modellen

# beta er utregnet på forhånd ved en løkke og formelen beta[i]=R[i]/(Norge.r_e2/Norge.lmbda_2+Norge.r_ia/Norge.mu+1/Norge.mu)


def beta(t):
    beta = [0.4, 0.0625, 0.0875, 0.0875, 0.15,
            0.125, 0.125, 0.1625, 0.1625]
    dato = [date(2020, 2, 15), date(2020, 3, 14), date(2020, 4, 19), date(2020, 5, 10), date(2020, 6, 30), date(
        2020, 7, 31), date(2020, 8, 31), date(2020, 9, 30), date(2020, 10, 25), date(2020, 11, 4)]
    time = [0]*len(dato)
    time[0] = (dato[1]-dato[0]).days
    for i in range(1, len(time)-1):
        time[i] = (dato[i+1]-dato[i]).days-1
    days=0
    for j in range(len(dato)):
        days+=time[j]
        if t<=days:
            return beta[j]
        elif t>520:
            return 0.29
    else:
        return 0.125

days=(date(2021,11,16)-date(2020,2,15)).days
Norge =covid19_Norway(beta,"fylker.txt",640,1)

print(Norge.R[640]+Norge.I[640], " smittede")#finner antall smittede med modellen
print(Norge.I[640], "syke")
#om vi ser på fhi sine sider ser vi at smitten har økt eksponensielt siden mai
#derfor etter litt prøving og feiling vaøgte jeg å sitte beta=0.29 rundt august i år
#om vi sette beta=0.4, altså R=3.2 vil antall smittede øke eksponensielt
'''
234286.69801513472 smittede 
18332.14087657428 syke
'''

#grafene stemmer ikke helt 100% med fhi sine men er noenlunde like
#stemmer veldig bra der antallet smittede er ganske likt fhi sine tall og antall syke er nesten identisk til nye tilfeller de siste 2 ukene