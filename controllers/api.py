# To do list
# return redirect link from the login and register
import simplejson as json

def get_listings():
  return dict(listings=[])

def login():
  if request.vars.email and request.vars.password:
    check_logged_in = auth.login_bare(request.vars.email, request.vars.password.encode('utf8'))
    if check_logged_in:
      return response.json(dict(success=True, data=URL('default', 'job_listings')))
  return response.json(dict(success=False, data=URL('default', 'login')))

def register():
  if request.vars.email:
    request.vars.password = db.auth_user.password.validate(request.vars.password.encode('utf8'))[0]
    register_user = db.auth_user.insert(**request.vars)
    if register_user:
      add_group = db.auth_membership.insert(user_id=register_user.id, group_id=2)
      return response.json(dict(success=True, data=URL('default', 'login')))
  return response.json(dict(success=False, data=URL('default', 'register')))

def handle_resume_request():
  print request.vars
  if request.vars and 'add' in request.args:
    request.vars.update(dict(user_id=auth.user_id, request_status='pending'))
    form_data = {key.replace('[]','') if '[]' in key else key: json.dumps(val) if isinstance(val, list) else val for key, val in request.vars.iteritems()}
    # extract the record for the resume_info table
    resume_info_fields = db.resume_info.fields
    resume_info_record = {key: val for key, val in form_data.iteritems() if key in resume_info_fields}
    print resume_info_record
    send_request = db.resume_info.insert(**resume_info_record)
    if send_request:
      return response.json(dict(success=True, data=send_request.id))
  return response.json(dict(success=False, data='Erro adding'))