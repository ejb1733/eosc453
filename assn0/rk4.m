%   RK4.M   Use 4th order Runge Kutta Method for Numerical Solution of IVPs
%
%The inputs to the function are:
%      fxy = string variable with the name of the function file containing f(x,y)
%      xo,xf = initial and final values of the independent variable (scalars)
%      yo = initial value of dependent variable at xo (column vector)
%      N = number of intervals to use between xo and xf
%
%   The outputs to the function are:
%      X = vector containing values of the independent variable
%      Y = the estimated dependent variable at each value of the independent variable
%       --> this variable is a vector if only one equation is solved
%       --> it is a matrix [y1(x) y2(x) ... ] for multiple equations 
%
%

      function [X,Y] = rk4(fxy,xo,xf,yo,N)
%
%   compute step size and size of output variables
      if N < 2   N = 2;   end  % set minimum number for N
      h = (xf-xo)/N;           % step size
      X = zeros(N+1,1);        % initialize independent variable
      M = max(size(yo));       % number of equations (number of columns of Y matrix)
      Y = zeros(N+1,M);        % initialize dependent variables
%
%   set initial conditions
      x = xo;   X(1) = x;   y = yo;   Y(1,:) = y';
%
%   begin computational loop
      for i = 1:N
        k1 = h*feval(fxy,x,y);           % evaluate function
        k2 = h*feval(fxy,x+h/2,y+k1/2);   
        k3 = h*feval(fxy,x+h/2,y+k2/2);   
        k4 = h*feval(fxy,x+h,y+k3);   
        y = y + (k1+2*k2+2*k3+k4)/6;     % increment dependent variable
        x = x + h;                       % increment independent variable
        X(i+1) = x;                      % store current x in X vector
        Y(i+1,:) = y';                   % store current y in Y matrix
      end
%
%   end of function
%