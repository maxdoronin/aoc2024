import datetime
import urllib
from flask import abort

class Solver:
    def __init__(self, request, year, day, input=None):
        self.request = request
        self.input = list()
        if self.request is None: # __init__ is called from test
            self.input = input
            return
        if self.request.method == "GET":
            session = self.request.cookies.get("session", None)
            if (session != None):
                url=urllib.request.Request(f"https://adventofcode.com/{year}/day/{day}/input")
                url.add_header ("Cookie", f"session={session}")
                lines = urllib.request.urlopen(url).readlines()
                try:
                    self.input = list(l.decode("utf-8").rstrip("\n") for l in lines)
                except urllib.error.HTTPError as e:     
                    print (e.reason)
                    abort (400)
            else:
                abort (400, "GET: Need AOC session cookie to get the input file.")
        elif self.request.method == "POST":
                abort (400, "POST: Not implemented.")

    def process(self):
        res = ""
        if self.input != None:
            res += self.timed_run(self.first_problem)
            res += self.timed_run(self.second_problem)
        else:
            abort (400, "Got no input")
        return (res)
    
    def timed_run(self, f: callable):
        start = datetime.datetime.now()
        result = f()
        end = datetime.datetime.now()
        return (f"{f.__qualname__}: {start} + {end - start}\n{result}\n")

    def first_problem(self):
        return ("first_problem is not implemented")

    def second_problem(self):
        return ("second_problem is not implemented")