mttkinter
=========

A thread-safe version of tkinter

Adapted from the Python-2-only module of the same name by Allen
B. Taylor (a dot b dot taylor at gmail dot com), available at
[the Tkinter wiki](http://tkinter.unpythonic.net/wiki/mtTkinter).

Although tkinter is technically thread-safe (assuming Tk is built with --enable-threads), practically speaking there are still problems when used in multithreaded Python applications. The problems stem from the fact that the `_tkinter` module attempts to gain control of the main thread via a polling technique when processing calls from other threads. If it succeeds, all is well. If it fails (i.e., after a timeout), the application receives an exception with the message: `RuntimeError: main thread is not in main loop`. There is no way to tell when this might happen, so calling Tk routines from multiple threads seems to be problematic at best.

The `mttkinter` module solves this problem by modifying some `tkinter` module definitions (in memory). The modified code intercepts out-of-thread `tkinter` calls and marshals them through a queue which is read by an 'after' event running periodically in the main loop. This is similar to the technique used in many other platforms (e.g., .NET's `InvokeRequired`/`Invoke` mechanism). The technique used in `mttkinter` is exception-safe as well, marshaling exceptions through a response queue back to the caller's thread.

Note that, because it modifies the original `tkinter` module in
memory, other modules that use `tkinter` (e.g., `Pmw`) reap the
benefits automagically as long as `mttkinter` is imported at some
point before additional threads are created.

Typical usage:
===

    import mttkinter as tkinter

or

    from mttkinter import *
