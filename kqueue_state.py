#!/usr/bin/python

import lldb

def kqueue_state(debugger, command, result, internal_dict):
    if  not command:
        print >>result, "Please input file descriptor!"
        return 
    lldb_command = "p/x (struct kqueue*)((*p->p_fd->fd_ofiles + %s)->f_fglob->fg_data)->kq_state"%command
    debugger.HandleCommand(lldb_command)
    # print >>result, "Breakpoint set on kqueue on the condition of procrss id is %s"%command

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand("command script add kqueue_state -f kqueue_state.kqueue_state")
    print "The \"kqueue_state\" python command has been installed and is ready for use"

