% Plotting the graph of activation functions
% and its corresponding derivatives.
% Oyesh
% 04/14/2017

% Define range
range = -5:0.1:5;

% Activation functions
tanh = tansig(range);
sigmoid = logsig(range);
linear = poslin(range);

% Create subplots
funcPlot = subplot(2,1,1);
hold on;
derivPlot = subplot(2,1,2);

% Plot activation functions
plot(funcPlot, range, tanh, 'r');
plot(funcPlot, range, sigmoid, 'g');
plot(funcPlot, range, linear, 'b');
title(funcPlot, 'Activation Functions');
legend(funcPlot, 'tanh(x)','sigmoid(x)', 'linear(x)');

% Derivative part
dTanh_dN = dtansig(range, tanh);
dSigmoid_dN = dlogsig(range, sigmoid);
dLinear_dN = dposlin(range, linear);
hold on;

% Plot derivatives
plot(derivPlot, range, dTanh_dN, 'r');
plot(derivPlot, range, dSigmoid_dN, 'g');
plot(derivPlot, range, dLinear_dN, 'b');
title(derivPlot, 'Derivatives of Activation Functions');
legend(derivPlot, 'tanh''(x)','sigmoid''(x)', 'linear''(x)');

hold off