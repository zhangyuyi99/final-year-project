% 'start python...' opens a terminal running the script, so matlab commands
% can be run simultaneously

% 'python...' runs the script in matlab & prints to the command line:
% matlab waits for it to finish before proceeding

variable1 = 50; % distance to move up in mm
variable2 = 100; % distance to move down in mm

command = 'start python PythonEnd2.py ' + string(variable1)...
        + ' ' + string(variable2);
system(command);

% If a terminal has been opened, the process can be stopped early:
% system('taskkill /F /IM "python.exe" /T');
% (renaming "python.exe" to the default window name of the terminal)