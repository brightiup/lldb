#!/usr/bin/python

import lldb


def bkqueue(debugger, command, result, internal_dict):
    if not command:
        print >>result, "Please input process id!"
        return
    lldb_command = "br s -n kqueue -c '*(uint32_t*)((char*)p + 0x10)==%s'" % command
    debugger.HandleCommand(lldb_command)
    print >>result, "Breakpoint set on kqueue on the condition of procrss id is %s" % command


def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand("command script add bkqueue -f bkqueue.bkqueue")
    print "The \"bkqueue\" python command has been installed and is ready for use"
