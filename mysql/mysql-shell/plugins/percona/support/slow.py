#!/usr/bin/env python3

def explain2me(session, args, options):
   simple_explain = "EXPLAIN EXTENDED "
   json_explain = "EXPLAIN FORMAT=json "

   full_query = options['query']

   if (options.has_key('json')):
      my_explain = json_explain + full_query
   else:
      my_explain = simple_explain + full_query

   result = session.run_sql(my_explain)
   report = [result.get_column_names()]
   for row in result.fetch_all():
      report.append(list(row))

   return {'report': report}
