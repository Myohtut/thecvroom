db.define_table('resume_info',
  Field('user_id', db.auth_user),
  Field('request_status', type='string',
    requires=IS_IN_SET(['pending', 'acknowledged', 'finish'])),
  migrate=True
)
