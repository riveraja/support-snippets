#!/usr/bin/env python3
from percona.support import mdl, utils, slow, blocking

shell.register_report(
  'get_blocking_thd',
  'list',
  blocking.get_blocking_trx,
  {
     'brief': 'Show blocking thread.',
     'details': ['Needs the SELECT privilege on performance_schema.threads table.'],
     'options': [
         {
            'name': 'processlist_id',
            'brief': 'The processlist_id or blocking_thread',
            'shortcut': 'p',
            'required': 'true',
            'type': 'integer'
         }
     ],
     'argc': '0'
   }
)

shell.register_report(
  'get_waiting_trx',
  'list',
  blocking.get_waiting_trx,
  {
     'brief': 'Show waiting thread.',
     'details': ['Needs the SELECT privilege on information_schema and performance_schema tables.'],
     'argc': '0'
  }
)

shell.register_report(
  'get_blocking_trx',
  'list',
  blocking.get_blocking_trx,
  {
     'brief': 'Show blocking transaction.',
     'details': ['Needs the SELECT privileges on the performance_schema.events_statements_current table.'],
     'options': [
         {
            'name': 'thread_id',
            'brief': 'Single transaction.',
            'shortcut': 't',
            'required': 'true',
            'type': 'integer'
         },
         {
            'name': 'all',
            'brief': 'All transactions.',
            'shortcut': 'a',
            'type': 'bool'
         }
     ],
     'argc': '0'
   }
)

shell.register_report(
  'metadatalocks_list',
  'list',
  mdl.mdl_list,
  {
     'brief': 'Show transactions in Waiting for table metadata lock state.',
     'details': ['Needs the SELECT privilege on information_schema table.'],
     'argc': '0'
  }
)

shell.register_report(
  'metadatalocks_instruments',
  'list',
  mdl.check_mdl_instruments,
  {
     'brief': 'Check if performance_schema setup_instruments for metadata locks are enabled.',
     'details': ['Needs the SELECT privilege on information_schema table.'],
     'argc': '0'
  }
)

shell.register_report(
  'explain2me',
  'list',
  slow.explain2me,
  {
     'brief': 'Execute explain on a query.',
     'details': ['Check execution plan of a query.'],
     'options': [
        {
          'name': 'query',
          'brief': 'Full query',
          'shortcut': 'q',
          'required': 'true',
          'type': 'string'
        },
        {
          'name': 'json',
          'brief': 'Get JSON format',
          'shortcut': 'j',
          'type': 'bool'
        }
      ],
      'argc': '0'
   }
)

if 'percona' in globals():
   global_obj = percona
else:
   global_obj = shell.create_extension_object()
   shell.register_global(
      "percona",
      global_obj,
      {"brief": "MySQL Shell extension plugin."}
   )

try:
    plugin_obj = global_obj.support
except IndexError:
    plugin_obj = shell.create_extension_object()
    shell.add_extension_object_member(
       global_obj,
       "support",
       plugin_obj,
       {"brief": "Utility object for support operations."}
    )

try:
   shell.add_extension_object_member(
       plugin_obj,
       "enable_mdl_instruments",
       mdl.enable_mdl_instruments,
       {"brief": "Enables performance_schema.setup_instruments for metadata locks.",
        "parameters": [
           {
             "name":"session",
             "type":"object",
             "class":"ClassicSession",
             "brief": "The session to be used on the operation."
           }
        ]
       }
   )
except Exception as e:
   shell.log("ERROR", "Failed to register percona.support.enable_psmdl ({0}).".format(str(e).rstrip()))

try:
   shell.add_extension_object_member(
       plugin_obj,
       "disable_mdl_instruments",
       mdl.disable_mdl_instruments,
       {"brief": "Disables performance_schema.setup_instruments for metadata locks.",
        "parameters": [
           {
             "name":"session",
             "type":"object",
             "class":"ClassicSession",
             "brief": "The session to be used on the operation."
           }
        ]
       }
   )
except Exception as e:
   shell.log("ERROR", "Failed to register percona.support.disable_psmdl ({0}).".format(str(e).rstrip()))

try:
    shell.add_extension_object_member(
       plugin_obj,
       "kill",
       utils.kill_process,
       {"brief": "Kills the process with the given ID.",
        "parameters": [
           {
             "name":"session",
             "type":"object",
             "class":"ClassicSession",
             "brief": "The session to be used on the operation."
           },
           {
             "name":"id",
             "type":"integer",
             "brief": "The ID of the process to be killed."
           }
         ]
        }
     )
except Exception as e:
    shell.log("ERROR", "Failed to register percona.support.kill ({0}).".format(str(e).rstrip()))
