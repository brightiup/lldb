#!/usr/bin/python

import lldb

def kqueue(debugger, command, result, internal_dict):
    if  not command:
        print >>result, "Please input file descriptor!"
        return 
    lldb_command = "p *(struct kqueue*)((*p->p_fd->fd_ofiles + %s)->f_fglob->fg_data)"%command
    debugger.HandleCommand(lldb_command)
    # print >>result, "Breakpoint set on kqueue on the condition of procrss id is %s"%command

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand("command script add kqueue -f kqueue.kqueue")
    print "The \"kqueue\" python command has been installed and is ready for use"

