%%This function contains a coupled system of 2 1st order ode solved in odeexamplemain.m
%%CALL: ydot = twoodes(t,y);  define ydot = f(t,y) for each t

function ydot = twoodes(t,y)

global a  b %we are bringing a defined in the main program.

% ydot(1) = a*y(2)^b;
% ydot(2) = a*y(1)^b;

ydot = [a*y(2)^b
        -a*y(1)^b];