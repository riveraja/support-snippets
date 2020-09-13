#!/usr/bin/env python3

def kill_process(session, id):
  result = session.run_sql("KILL CONNECTION %d" % id)
