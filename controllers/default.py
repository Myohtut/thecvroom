# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------

def admin():
  check_requests = db((db.resume_info.request_status == 'pending')&(db.resume_info.user_id == db.auth_user.id)).select().as_list()
  request_table = TABLE(
    [TR(TD('User'), TD('Status'), TD('Action'))]
    +
    [TR([TD(data['auth_user']['first_name']),
      TD(data['resume_info']['request_status']),
      TD(BUTTON('View',
        _class='btn btn-raised btn-primary',
        _onclick="$('#modal .modal-body').html('%s')" % DIV(H6(T('Name')),
          DIV('%s %s' % (data['auth_user']['first_name'], data['auth_user']['last_name'])),
          H6(T('Email')),
          DIV(data['auth_user']['email']),
          DIV(H5(T('List of Degrees'))),
          CAT([DIV(degree) for degree in eval(data['resume_info']['education_degree'])]) if data['resume_info']['education_degree'] and isinstance(eval(data['resume_info']['education_degree']), list) else data['resume_info']['education_degree'],
          DIV(H5(T('List of Certificates'))),
          CAT([DIV(certificate) for certificate in eval(data['resume_info']['certificate'])]) if data['resume_info']['certificate'] and isinstance(eval(data['resume_info']['certificate']), list) else data['resume_info']['certificate'],
          DIV(H5(T('List of Awards'))),
          CAT([DIV(award) for award in eval(data['resume_info']['award'])]) if data['resume_info']['award'] and isinstance(eval(data['resume_info']['award']), list) else data['resume_info']['award'],
          DIV(H5(T('List of Volunteering Experience'))),
          CAT([DIV(volunteer) for volunteer in eval(data['resume_info']['volunteer'])]) if data['resume_info']['volunteer'] and isinstance(eval(data['resume_info']['volunteer']), list) else data['resume_info']['volunteer'],
          DIV(H5(T('Technical Skills'))),
          DIV(data['resume_info']['technical_skills']),
          DIV(H5(T('Language Proficiency'))),
          DIV(data['resume_info']['language_proficiency'])),
        **{'_data-toggle':'modal', '_data-target':'#modal'})
      )]) for data in check_requests]
    ,_class='table')
  return dict(message=request_table)

def index():
    return dict(message=T('Welcome to web2py!'))

def about_us():
    return dict(message=T('Welcome'))

def contact_us():
    return dict(message=T('Welcome'))

def resume_writing():
    return dict(message=T('Welcome'))

def request_resume():
  return dict(message=T('Welcome'))

def job_listings():
    return dict(message=T('Welcome'))

def hr_solutions():
    return dict(message=T('Welcome'))

def blog():
    return dict(message=T('Welcome'))

def login():
    return dict(message=T('Welcome'))

def register():
    return dict(message=T('Welcome'))

def user():
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


