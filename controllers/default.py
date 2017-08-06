# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------


def index():
    return dict(message=T('Welcome to web2py!'))

def about_us():
    return dict(message=T('Welcome'))

def contact_us():
    return dict(message=T('Welcome'))

def resume_writing():
    return dict(message=T('Welcome'))

def job_listing():
    return dict(message=T('Welcome'))

def hr_solutions():
    return dict(message=T('Welcome'))

def blog():
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


