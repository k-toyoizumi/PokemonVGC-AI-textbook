"""Independently check textbook toy calculations and matrix-game solutions."""
import math
import numpy as np
from scipy.optimize import linprog
# Bayes update and two joint-action branching steps.
assert math.isclose(.8*.3/(.8*.3+.2*.7),12/19)
assert 64*64==4096 and 4096**2==16777216
A=np.array([[-1.,2.],[1.,-2.]])
# Row strategy x: minimize -v subject to each pure opponent's payoff >= v.
row=linprog([0,0,-1],A_ub=np.column_stack([-A.T,np.ones(2)]),b_ub=[0,0],A_eq=[[1,1,0]],b_eq=[1],bounds=[(0,None),(0,None),(None,None)],method='highs')
# Column strategy y: minimize w subject to every pure row payoff <= w.
col=linprog([0,0,1],A_ub=np.column_stack([A,-np.ones(2)]),b_ub=[0,0],A_eq=[[1,1,0]],b_eq=[1],bounds=[(0,None),(0,None),(None,None)],method='highs')
assert row.success and col.success
assert np.allclose(row.x,[.5,.5,0]) and np.allclose(col.x,[2/3,1/3,0])
assert np.max(np.min(A,axis=1))==-1
assert np.allclose(A@np.array([.2,.8]),[1.4,-1.4])
assert np.allclose(A@np.array([.8,.2]),[-.4,.4])
assert math.isclose(.8*.9+.2*.1,.74) and math.isclose(.8*.55+.2*.45,.53)
a=.60+.5*math.sqrt(math.log(100)/25);b=.50+.5*math.sqrt(math.log(100)/4)
assert round(a,3)==.815 and round(b,3)==1.036
hidden=np.array([[1,0],[0,1]])
assert np.max(np.array([.5,.5])@hidden)==.5
assert np.mean(np.max(hidden,axis=1))==1
print('PASS: Bayes, branching, matrix equilibrium by linear programs, response values, UCT scores, hidden-information example')


assert math.isclose(-math.log(.8),.2231435513142097)
assert math.isclose(.98**50,.36416968008711675)
assert math.isclose(.25*.8+.75*.4,.5)
assert math.isclose(.1+.9*.7-.5,.23)
assert math.isclose(.2+.9*.8*(-.1),.128)
def clipped(r,a,e=.2):return min(r*a,max(1-e,min(1+e,r))*a)
assert np.allclose([clipped(1.5,2),clipped(.5,-2),clipped(.5,2),clipped(1.5,-2)],[2.4,-1.6,1,-3])
print('PASS: BC loss, sequential agreement, value, TD, GAE and both signs of PPO clipping')
