#SOURCE: http://code.activestate.com/recipes/474070-creating-a-single-instance-application/

from win32event import CreateMutex
from win32api import CloseHandle, GetLastError
from winerror import ERROR_ALREADY_EXISTS

class ApplicationAlreadyrunning(Exception):
    pass

def get_mutex():
    mutexname = "testmutex_{D0E858DF-985E-4907-B7FB-8D732C3FC3B9}"
    mutex = CreateMutex(None, False, mutexname)
    lasterror = GetLastError()
    if lasterror == ERROR_ALREADY_EXISTS:
        raise ApplicationAlreadyrunning
    return mutex

def close(mutex):
    CloseHandle(mutex)
