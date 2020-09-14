#### MySQL Shell Plugins

Developed starting with MySQL Shell 8.0.19 Community version, should with with equivalent Percona MySQL Shell binary as well.

List all plugins:
```
\h percona.support
NAME
      support - Utility object for support operations.

SYNTAX
      percona.support

DESCRIPTION
      Utility object for support operations.

FUNCTIONS
      disable_mdl_instruments(session)
            Disables performance_schema.setup_instruments for metadata locks.

      enable_mdl_instruments(session)
            Enables performance_schema.setup_instruments for metadata locks.

      help([member])
            Provides help about this object and it's members

      kill(session, id)
            Kills the process with the given ID.
```

List shell reports:
```
\h shell.reports
NAME
      reports - Gives access to built-in and user-defined reports.

SYNTAX
      shell.reports

DESCRIPTION
      The 'reports' object provides access to built-in reports.

      All user-defined reports registered using the shell.registerReport()
      method are also available here.

      The reports are provided as methods of this object, with names
      corresponding to the names of the available reports.

      All methods have the same signature: Dict report(Session session, List
      argv, Dict options), where:

      - session - Session object used by the report to obtain the data.
      - argv (optional) - Array of strings representing additional arguments.
      - options (optional) - Dictionary with values for various report-specific
        options.

      Each report returns a dictionary with the following keys:

      - report (required) - List of JSON objects containing the report. The
        number and types of items in this list depend on type of the report.

      For more information on a report use: shell.reports.help('report_name').

FUNCTIONS
      explain2me(session, argv, options)
            Execute explain on a query.

      get_blocking_thd(session, argv, options)
            Show blocking thread.

      get_blocking_trx(session, argv, options)
            Show blocking transaction.

      get_waiting_trx(session)
            Show waiting thread.

      help([member])
            Provides help about this object and it's members

      metadatalocks_instruments(session)
            Check if performance_schema setup_instruments for metadata locks
            are enabled.

      metadatalocks_list(session)
            Show transactions in Waiting for table metadata lock state.

      query(session, argv)
            Executes the SQL statement given as arguments.

      threads(session[, argv][, options])
            Lists threads that belong to the user who owns the current session.

      thread(session[, argv][, options])
            Provides various information regarding the specified thread.
```

Sample output:
<img width="964" src="https://github.com/riveraja/support-snippets/blob/master/mysql/mysql-shell/plugins/percona/support/images/mysqlshellpluginsample.png" alt="sample image">

