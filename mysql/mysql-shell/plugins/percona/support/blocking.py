#!/usr/bin/env python3

def getWaitingTrx(session):
  query = "SELECT r.trx_id waiting_trx_id,r.trx_mysql_thread_id waiting_thread,r.trx_query waiting_query,b.trx_id blocking_trx_id,b.trx_mysql_thread_id blocking_thread,b.trx_query blocking_query FROM information_schema.innodb_lock_waits w INNER JOIN information_schema.innodb_trx b ON b.trx_id = w.blocking_trx_id INNER JOIN information_schema.innodb_trx r ON r.trx_id = w.requesting_trx_id;"

  result = session.run_sql(query)
  report = [result.get_column_names()]
  for row in result.fetch_all():
     report.append(list(row))

  return {'report': report}


def getBlockingThd(session,args,options):
  pid = options['processlist_id']
  query = ("SELECT THREAD_ID FROM performance_schema.threads WHERE PROCESSLIST_ID = %d" % pid)

  result = session.run_sql(query)
  report = [result.get_column_names()]
  for row in result.fetch_all():
     report.append(list(row))

  return {'report': report}


def getBlockingTrx(session,args,options):
  tid = options['thread_id']

  if (options.has_key('all')):
     query = ("SELECT THREAD_ID, EVENT_ID, SQL_TEXT FROM performance_schema.events_statements_history WHERE THREAD_ID = %d ORDER BY EVENT_ID" % tid)
  else:
     query = ("SELECT THREAD_ID, SQL_TEXT FROM performance_schema.events_statements_current WHERE THREAD_ID = %d" % tid)

  result = session.run_sql(query)
  report = [result.get_column_names()]
  for row in result.fetch_all():
     report.append(list(row))

  return {'report': report}

