%{
    Script to plot RELU
    Oyashi
    04/15/2017
%}

limit = 0.01;               % step size
range = 3;                  % range
X = -range:limit:range;     % domain
f = max(0, X);              % ReLU function
Y = diff(f)/limit;          % first derivative
plot(X,f,'b', X(:,1:length(Y)),Y,'r')   %graph plot
legend('f(x)', 'f''(x)')                % legend
title('ReLU and its derivate')          % title