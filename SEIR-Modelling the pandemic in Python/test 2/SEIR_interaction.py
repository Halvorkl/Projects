import numpy as np
import matplotlib.pyplot as plt
from ODESolver import RungeKutta4
from SEIR import Region, ProblemSEIR, SolverSEIR

class RegionInteraction(Region):
    def __init__(self,name,S_0,E2_0, lat, long):
        self.lat=float(lat)*(np.pi/180)
        self.long=float(long)*(np.pi/180)
        super(RegionInteraction, self).__init__(name, S_0, E2_0)
    def distance(self, other):
        u=np.sin(self.lat)*np.sin(other.lat)+np.cos(self.lat)*np.cos(other.lat)*np.cos(abs(self.long-other.long))
        if u>1:
            u=1
        elif u<0:
            u=0
        q=np.arccos(u)
        self.dis=float(q*6400)
        '''valgte å bruke except'''
        return float(self.dis)
        
class ProblemInteraction(ProblemSEIR):
    def __init__(self, region, area_name, beta, r_ia = 0.1, r_e2=1.25, lmbda_1=0.33, lmbda_2=0.5, p_a=0.4,mu=0.2, k=0.01):
        super(ProblemInteraction, self).__init__(region, beta, r_ia, r_e2, lmbda_1, lmbda_2, p_a, mu)
        self.k=k
        self.area_name=area_name
    def get_population(self):
        population=0
        try:
            super(ProblemInteraction, self).get_population()
        except:
            for i in range(len(self.region)):
                population+=self.region[i].population
            return population
    def set_initial_condition(self):
        try:
              super(ProblemInteraction, self).set_initial_condition()
        except:
            self.initial_condition=[]
            for i in range(len(self.region)):
                self.initial_condition+=[self.region[i].S_0, self.region[i].E1_0, self.region[i].E2_0, self.region[i].I_0, self.region[i].Ia_0, self.region[i].R_0]
    def  __call__(self, u, t):
            n = len(self.region)
            # create a nested list:
            # SEIR_list[i] = [S_i, E1_i, E2_i, I_i, Ia_i, R_i]:
            SEIR_list = [u[i:i+6] for i in range(0, len(u), 6)]
            # Create separate lists containing E2 and Ia values:
            E2_list = [u[i] for i in range(2, len(u), 6)]
            Ia_list = [u[i] for i in range(4, len(u), 6)]
            derivative = []
            jm_list=[]
            for i in range(n):
                S, E1, E2, I, Ia, R = SEIR_list[i]
                dS = 0
                jm1=0
                jm2=0
                N=sum(SEIR_list[i])
                for j in range(n):
                    E2_other = E2_list[j]
                    Ia_other = Ia_list[j]
                    jm1+=Ia_other/sum(SEIR_list[j])*np.exp(-self.k*self.region[i].distance(self.region[j]))
                    jm2+=E2_other/sum(SEIR_list[j])*np.exp(-self.k*self.region[i].distance(self.region[j]))
                dS = -self.beta(t)*S*I/N - self.r_ia*self.beta(t)*S*jm1 - self.r_e2*self.beta(t)*S*jm2
                dE1 = -dS-self.lmbda_1*E1
                dE2 = self.lmbda_1*(1-self.p_a)*E1 - self.lmbda_2*E2
                dI  = self.lmbda_2*E2 - self.mu*I
                dIa = self.lmbda_1*self.p_a*E1 - self.mu*Ia
                dR  = self.mu*(I + Ia)
                derivative+=[dS,dE1,dE2,dI,dIa,dR]
            return derivative
    def split_solution(self, u, t):
        n = len(t)
        n_reg = len(self.region)
        self.t = t
        i=0
        self.S = np.zeros(n);self.E1 = np.zeros(n);self.E2= np.zeros(n);self.I= np.zeros(n);self.Ia= np.zeros(n);self.R= np.zeros(n);
        SEIR_list = [u[:, i:i+6] for i in range(0, n_reg*6, 6)]
        for part, SEIR in zip(self.region, SEIR_list):
            part.set_SEIR_values(SEIR, t)
            for i in range(n):
                self.S[i]+=SEIR[i][0]
                self.E1[i]+=SEIR[i][1]
                self.E2[i]+=SEIR[i][2]
                self.I[i]+=SEIR[i][3]
                self.Ia[i]+=SEIR[i][4]
                self.R[i]+=SEIR[i][5]
    def plot(self):
        plt.title(f"{self.area_name}")
        plt.xlabel("Time(Days)")
        plt.ylabel("Population")
        plt.plot(self.t,self.S, label=" susceptible")
        plt.plot(self.t,self.I, label="symptomatic")
        plt.plot(self.t,self.Ia, label="asymptomatic")
        plt.plot(self.t,self.R, label="Recovered")
                
if __name__ == '__main__':
    innlandet = RegionInteraction('Innlandet',S_0=371385, E2_0=0, lat=60.7945,long=11.0680)
    oslo = RegionInteraction('Oslo',S_0=693494,E2_0=100, lat=59.9,long=10.8)
    print(oslo.distance(innlandet))
    problem = ProblemInteraction([oslo,innlandet],'Norway_east', beta=0.4)
    print(problem.get_population())
    problem.set_initial_condition()
    print(problem.initial_condition)
    u = problem.initial_condition
    print(problem(u,0))
    solver = SolverSEIR(problem,T=150,dt=1.0)
    solver.solve()
    problem.plot()
    plt.legend()
    plt.show()
    
#kjøreeksmepel
'''
101.00809386280783
1064979
[693494, 0, 100, 0, 0, 0, 371385, 0, 0, 0, 0, 0]
[-49.99279117178061, 49.99279117178061, -50.0, 50.0, 0.0, 0.0, -9.750265859422228, 9.750265859422228, 0.0, 0.0, 0.0, 0.0]
'''