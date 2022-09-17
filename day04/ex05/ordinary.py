#!/usr/bin/env python3
import sys
import resource


def file_to_list():
    with open(sys.argv[1], 'r') as f:
        return f.readlines()


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise Exception("No file argument")
        for i in file_to_list():
            pass
        self = resource.getrusage(resource.RUSAGE_SELF)
        peak_mem = self.ru_maxrss * 1.0E-6
        user_mode_time = self.ru_utime
        system_mode_time = self.ru_stime
        print(f"Peak Memory Usage = {peak_mem:.3f} GB")
        print(f"User Mode Time + System Mode Time = {user_mode_time + system_mode_time:.2f}s")
    except FileNotFoundError as n:
        print(n)
    except Exception as e:
        print(e)
