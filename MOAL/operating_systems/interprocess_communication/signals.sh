#!/bin/sh

# List all signals available:
kill -l
# These map to the traditional terms: e.g. SIGTRAP = TRAP SIGABRT = ABRT etc...
# HUP INT QUIT ILL TRAP ABRT EMT FPE KILL BUS SEGV SYS PIPE ALRM TERM URG STOP TSTP CONT CHLD TTIN TTOU IO XCPU XFSZ VTALRM PROF WINCH INFO USR1 USR2
# Create a process that will continue running, just some random thing...
while read line
do
    echo "You typed: $line\n"
done
# Usage:
# `sh signals.sh`
# Check for the process id
# `ps ax | ag 'signals.sh'`
# `81265 s001  S+     0:00.00 ag signals.sh`
# Take the pid for the running process and use a signal to alter it.
# E.g.
kill -1 81265
kill -2 81265
kill -3 81265
kill -4 81265
# etc...
