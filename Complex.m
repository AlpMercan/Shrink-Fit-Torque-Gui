clc
clear 

% Define the material and geometric properties for both the outer (o) and inner (i) components
E_0 = 210*10^9; % Young's modulus for the outer component in Pascals
E_i = 210*10^9; % Young's modulus for the inner component in Pascals
v_0 = 0.3; % Poisson's ratio for the outer component
v_i = 0.3; % Poisson's ratio for the inner component
d_0 = 0.005; % Outer diameter of the outer component in meters
% d_i = 0.0045; % Inner diameter of the inner component in meters
d_i=0;
% The average diameter where the pressure is being calculated could be 
% the mean of the outer and inner diameters. You might need to adjust this.
% d = (d_0 - d_i)/2 ; 
d=0.0045;

% Interference in meters (difference between the outer diameter of the inner part
% and the inner diameter of the outer part)
inter = 0.0001; 
sag= (d/E_0)*((d_0^2+d^2)/(d_0^2-d^2)+v_0);
sol= (d/E_i)*((d_i^2+d^2)/(d^2-d_i^2)-v_i);
P=inter/(sag+sol);


% Friction coefficient
u = 0.3; 
radius = d / 2; 

L = 2.7*10^-2; 
A = 2 * pi * radius * L; 

N = P * A; 
T = u * N * radius; 

% Display the result
disp(['The calculated torque due to friction is ', num2str(T), ' Nm']);
