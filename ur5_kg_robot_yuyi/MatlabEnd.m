% I'm calling python via a system command from matlab. Here I'm only
% passing 12 variables, so give them as arguments: if I needed
% more (or if I needed feedback from the ur5 as it runs),
% I'd save them into a file which the script reads

% 'start python...' opens a terminal running the script, so matlab commands
% can be run simultaneously

% 'python...' runs the script in matlab & prints to the command line:
% matlab waits for it to finish before proceeding

command = 'start python PythonEnd.py '+ string(mxamp)...
        + ' ' + string(mxfreq) + ' ' + string(mxphase)...
        + ' ' + string(myamp) + ' ' + string(myfreq)...
        + ' ' + string(myphase) + ' ' + string(mzamp)...
        + ' ' + string(mzfreq) + ' ' + string(mdepth)...
        + ' ' + string(manglex) + ' ' + string(mangley)...
        + ' ' + string(duration);
system(command);

% If a terminal has been opened, the process can be stopped early:
system('taskkill /F /IM "python.exe" /T');
% (renaming "python.exe" to the default window name of the terminal)