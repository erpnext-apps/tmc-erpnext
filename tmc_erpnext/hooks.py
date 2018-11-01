# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "tmc_erpnext"
app_title = "TMC ERPNext"
app_publisher = "Frappe"
app_description = "ERPNext extensions to cater customizations of TMC"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "developers@erpnext.com"
app_license = "GPL"

# Includes in <head>
# ------------------

fixtures = ["Custom Field"]

hide_in_installer = True

# include js, css files in header of desk.html
# app_include_css = "/assets/tmc_erpnext/css/tmc_erpnext.css"
# app_include_js = "/assets/tmc_erpnext/js/tmc_erpnext.js"

# include js, css files in header of web template
# web_include_css = "/assets/tmc_erpnext/css/tmc_erpnext.css"
# web_include_js = "/assets/tmc_erpnext/js/tmc_erpnext.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "tmc_erpnext.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "tmc_erpnext.install.before_install"
# after_install = "tmc_erpnext.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tmc_erpnext.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"tmc_erpnext.tasks.all"
# 	],
# 	"daily": [
# 		"tmc_erpnext.tasks.daily"
# 	],
# 	"hourly": [
# 		"tmc_erpnext.tasks.hourly"
# 	],
# 	"weekly": [
# 		"tmc_erpnext.tasks.weekly"
# 	]
# 	"monthly": [
# 		"tmc_erpnext.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "tmc_erpnext.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "tmc_erpnext.event.get_events"
# }

