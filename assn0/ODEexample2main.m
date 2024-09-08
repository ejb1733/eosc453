%Notes on the numerical solution of DEs

%Example 2: Two coupled odes ;  Initial Value Problem (IVP); 
%This script illustrates the basic numerical integration 
%of a problem involving coupled growth and decay
%A solution is marched forward in time from an initial condition defined at time t = 0.
%As with the single ODE example, 
%a critical issue in problems like this is the choice of time step: the step must be
%sufficiently small to resolve the structure of the solution Y(t).
%A CASE structure is used so that different choices of time step might be
%investigated easily. Please compare the results.
%Is the "best" choice of time step always the smallet one possible?  How
%might you define "best" in a practical sense?

clear all
close all


%decay constant
lambda = 0.75;

%Initial Y
yo = 1;

%initial time
to = 0;

%max integration time
tmax = 10;

%Recursion relation for radioactive decay: y_n+1 = y_n - lambda*y_n*deltat


%Initial condition
y(1) = yo;
yy(1) = yo;
t(1) = to;


%Investigate influence of time step on solution

for j=1:1:5
    switch j
case 1
    dt=1
    steps = round(tmax/dt);
    

    for i = 1:steps
        y(i+1) = y(i) + lambda*dt*yy(i);
        yy(i+1) = yy(i) - lambda*dt*y(i);
        t(i+1) = t(i)+dt;
    end
    
    col='r'
    
case 2
    dt=0.5
    steps = round(tmax/dt);
    

    for i = 1:steps
        y(i+1) = y(i) + lambda*dt*yy(i);
        yy(i+1) = yy(i) - lambda*dt*y(i);
        t(i+1) = t(i)+dt;
        t(i+1) = t(i)+dt;
    end
    
    col='b'

case 3
    dt=0.1
    steps = round(tmax/dt);
    

    for i = 1:steps
        y(i+1) = y(i) + lambda*dt*yy(i);
        yy(i+1) = yy(i) - lambda*dt*y(i);
        t(i+1) = t(i)+dt;
        t(i+1) = t(i)+dt;
    end
    
    col='m'

case 4
    dt=0.01
    steps = round(tmax/dt);
    

    for i = 1:steps
        y(i+1) = y(i) + lambda*dt*yy(i);
        yy(i+1) = yy(i) - lambda*dt*y(i);
        t(i+1) = t(i)+dt;
    end
    
    col='k'
    

case 5
    dt=0.001
    steps = round(tmax/dt);
    

    for i = 1:steps
        y(i+1) = y(i) + lambda*dt*yy(i);
        yy(i+1) = yy(i) - lambda*dt*y(i);
        t(i+1) = t(i)+dt;
    end
    
    col='g --'
    end

steps
figure(2)
plot(t,y,col)
hold on    
end
    



