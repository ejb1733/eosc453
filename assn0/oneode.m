%%This function contains one 1st order ode solved in odeexamplemain.m
%%CALL: ydot = oneode(t,y);  define ydot = f(t,y) for each t

function ydot = oneode(t,y)

global a  b %we are bringing a defined in the main program.

ydot = a*y^b;