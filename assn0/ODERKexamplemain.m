%%This script and the accompanying functions is designed to help you learn
%%about the numerical solution of initial value problems (ODEs) using the
%%MATLAB solver ODE45, which employs the 4th order Runge Kutta method.
%%The algorithm is as follows:
%% 1) Define Equation(s) to be solved. This will be a 1st order ODE or system of ODEs. 
%% 2) Define or input appropriate control parameters (such as the length of time for
%% the integration and the tolerance for convergence).
%% 3) Define the vector of initial conditions-- a value(s) of the function at time = 0
%% 4) Call the ODE solver
%% 5) Plot your results

%% Note that typing 'help <function>' at the command line is very usefl!


%%clear memory and figures
clear all
%close all

%%A global variable can be passed to all called functions; 'a' and 'b' are
%%constants in the ODE in the function 'oneode,m': dy/dt = -a*y^b  
%%NOTE: if b = 1 then this ode is linear and the analytical solution can be
%%obtained by separation of variables (this is raddioactive decay): y(t) =exp(-at) 
%% Try playing around with 'b' and see what happens!

global a b

%%a constant
a = -1;
b = 1.5;            %%The larger b is the more nonlinear the equations to be solved are
                    %%In the coupled ode example the nonlinear coupling has
                    %%a large effect-- Increase or decrease b from 1 with
                    %%small steps (< than 1) and explore the behavior; You
                    %%may have to increase the number of time steps below
                    %%to achieve resolution.

%%Define time interval for integration

time_min = 0;
time_max = 10;

%%Define a linearly-spaced vector with n points.
n = 1000;
timespan = linspace(time_min,time_max,n);
timespan=-timespan

%%Initial condition for a single ode defined in the function 'oneode.m'
yo = 100;

%%Column vector of initial conditions defined in the function 'twoodes.m'
yyo = [100
       100];


%%Solve one ODE contained in the function oneode.m.  
%%INPUTS: (function handle for 'oneode', timespan, initial condition)
%%OUTPUTS: [t,y]

[t,y] = ode45(@oneode,timespan,yo);


%%Solve two coupled ODEs contained in the function twoodes.m.  
%%INPUTS: (function handle for 'twoodes', timespan, VECTOR ofinitial condition)
%%OUTPUTS: [t,y]
%%Note you may want to comment this out when working with one ode

[tt,yy] = ode45(@twoodes,timespan,yyo);



%%Plot resutls
figure(20)
plot(t,y)
xlabel('time')
ylabel('y')

%%Plot resutls
%%Note you may want to comment this out when working with one ode
figure(30)
plot(tt,yy(:,1),'r',tt,yy(:,2),'b')
hold on
%plot(tt,yy(:,1)+yy(:,2),'k')
xlabel('time')
ylabel('y: Red is y1; blue is y2;sum is black')

