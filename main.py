#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp2

routes = [
    webapp2.Route(r'/acl_insert', handler='acl.InsertAcl'),
    webapp2.Route(r'/acl_delete', handler='acl.DeleteAcl'),
    webapp2.Route(r'/api_acl_insert', handler='api_test.ApiInsertAcl'),
]
app = webapp2.WSGIApplication(routes=routes, debug=True))
