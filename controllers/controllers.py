# -*- coding: utf-8 -*-
# from odoo import http


# class MyModule2(http.Controller):
#     @http.route('/my_module_2/my_module_2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_module_2/my_module_2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_module_2.listing', {
#             'root': '/my_module_2/my_module_2',
#             'objects': http.request.env['my_module_2.my_module_2'].search([]),
#         })

#     @http.route('/my_module_2/my_module_2/objects/<model("my_module_2.my_module_2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_module_2.object', {
#             'object': obj
#         })

