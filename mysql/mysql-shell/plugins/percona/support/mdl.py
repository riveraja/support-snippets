#!/usr/bin/env python3

def enable_mdl_instruments(session):
  result = session.run_sql("UPDATE performance_schema.setup_instruments SET ENABLED = 'YES', TIMED = 'YES' WHERE NAME = 'wait/lock/metadata/sql/mdl';")
  dict = []
  dict = check_mdl_instruments(session)
  for name, enabled, timed in dict['report']:
     print ("{:<30} {:<10} {:<10}".format(name,enabled,timed))

def disable_mdl_instruments(session):
  result = session.run_sql("UPDATE performance_schema.setup_instruments SET ENABLED = 'NO', TIMED = 'NO' WHERE NAME = 'wait/lock/metadata/sql/mdl';")
  dict = []
  dict = check_mdl_instruments(session)
  for name, enabled, timed in dict['report']:
     print ("{:<30} {:<10} {:<10}".format(name,enabled,timed))

def check_mdl_instruments(session):
  query = "SELECT * FROM performance_schema.setup_instruments WHERE NAME = 'wait/lock/metadata/sql/mdl';"

  result = session.run_sql(query)
  report = [result.get_column_names()]
  for row in result.fetch_all():
     report.append(list(row))

  return {'report': report}

def mdl_list(session):
  query = "SELECT id, user, host, db, time, state, info FROM information_schema.processlist WHERE state LIKE '%metadata lock' ORDER BY time"

  result = session.run_sql(query)
  report = [result.get_column_names()]
  for row in result.fetch_all():
     report.append(list(row))

  return {'report': report}
