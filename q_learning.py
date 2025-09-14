import itertools
from random import uniform,randint
from numpy import argmax,sqrt,log10
import matplotlib.pyplot as plt

# define start and goal points ,dimension and envirment size, also check result of selcted step 
class LineMove:
    def __init__(self,dim=3,dima=5):
        self.start=tuple([0]*dim)
        self.goal=tuple([dima-1]*dim)
        self.size=dima
        self.state=self.start
    
    def reset(self):
        self.state=self.start
        return self.state

    def step(self,action):
        x=self.state
        index=int(action/2)
        dir=action%2
        list_x_index=list(x)
        if dir==0:
            list_x_index[index] =min(list_x_index[index] +1,self.size-1)
        else:
            list_x_index[index] =max(0,list_x_index[index] -1)
        
        self.state=tuple(list_x_index)
        
        if self.state == self.goal:
            return self.state,sqrt(len(self.state)*2*self.size**2),True
        else:
            return self.state,-1,False

# make an instance and initialize q dict with required keys and zero values 
move=LineMove()
q={}
for key in itertools.product(range(move.size),repeat=(len_:=len(move.state))):
    q[key]=[0]*(2*len_)



alpha=0.5 
gamma=0.9
path_=[move.start]

#  learning process and adding final path 
for eq in range(last:=move.size**len_):
    epsilon=0.3/(1+log10(eq/2+1))
    state=move.reset()
    done=False
    while not done:
        
        if uniform(0,1)<epsilon:
            action=randint(0,len_*2-1)
        else:
            action=int(argmax(q[state]))
        
        new_state,reward,done=move.step(action)
        best_next=max(q[new_state])
        q[state][action]= q[state][action]+ alpha*(reward+gamma*best_next- q[state][action])

        state= new_state

        if eq==last-1:
            path_.append(state)

# ========== show in matplotlib =======
if len_==3:
    x,y,z=zip(*path_)
    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')
    ax.plot(x,y,z,marker='o')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('3D Path of Agent')
    
elif len_==2:
    x,y=zip(*path_)
    plt.plot(x,y,marker='o')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('2D Path of Agent')


plt.show()

