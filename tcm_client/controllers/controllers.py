# -*- coding: utf-8 -*-
# from odoo import http


# class TcmClient(http.Controller):
#     @http.route('/tcm_client/tcm_client', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tcm_client/tcm_client/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tcm_client.listing', {
#             'root': '/tcm_client/tcm_client',
#             'objects': http.request.env['tcm_client.tcm_client'].search([]),
#         })

#     @http.route('/tcm_client/tcm_client/objects/<model("tcm_client.tcm_client"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tcm_client.object', {
#             'object': obj
#         })

