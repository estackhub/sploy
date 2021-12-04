from . import __version__ as app_version

app_name = "sploy"
app_title = "Sploy"
app_publisher = "gross innovate and contributors"
app_description = "making it quote"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "spryngmanaged@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sploy/css/sploy.css"
# app_include_js = "/assets/sploy/js/sploy.js"

# include js, css files in header of web template
# web_include_css = "/assets/sploy/css/sploy.css"
# web_include_js = "/assets/sploy/js/sploy.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sploy/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

before_install = "sploy.ploy.install.before_install"

# before_install = "sploy.install.before_install"
# after_install = "sploy.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sploy.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
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

on_login = 'sploy.events.auth.successful_login'

doc_events = {
  'User': {
    'validate': 'sploy.sploy.api.allot.user_limit',
    'on_update': 'sploy.sploy.api.allot.user_limit'
	},
  'Company': {
    'validate':'sploy.sploy.api.allot.company_limit',
    'on_update':'sploy.sploy.api.allot.company_limit'
	},
	'Warehouse': {
    'validate':'sploy.sploy.api.allot.warehouse_limit',
    'on_update':'sploy.sploy.api.allot.warehouse_limit'
	},
  ('Stock Entry', 'Purchase Invoice', 'Payment', 'Journal Entry'):{
	  'validate':'sploy.sploy.api.allot.db_space_limit',
	  'on_submit' :'sploy.sploy.api.allot.db_space_limit'
	  },
  'File': {
    'validate': 'sploy.sploy.api.allot.files_space_limit',
	"on_update": "sploy.sploy.api.allot.files_space_limit",
	},
  ('Attendance','Expense Claim', 'Attendance Request', 'Employee Checkin','Leave Application', 'Shift Request', 'Shift Assignment', 'Employee Onboarding','Employee Promotion','Vehicle Log', 'Driver','Vehicle'): {
	  'validate': 'sploy.sploy.api.allot.hrm_status',
	  'on_submit' :'sploy.sploy.api.allot.hrm_status' 
	  },
  ('Loan Application', 'Loan', 'Loan Disbursement', 'Loan Repayment', 'Loan Write Off'): {
	  'validate': 'sploy.sploy.api.allot.loan_status',
	  'on_submit' :'sploy.sploy.api.allot.loan_status'
	  },
	('Lead','Opportunity','Contract','Appointment','Newsletter','Campaign','Email Campaign','Social Media Post'): {
	  'validate': 'sploy.sploy.api.allot.crm_status',
	  'on_submit' :'sploy.sploy.api.allot.crm_status'
	  },
  ('Salary Component','Salary Structure','Salary Structure Assignment','Payroll Entry','Salary Slip','Additional Salary','Retention Bonus','Employee Incentive','Employee Benefit Application','Employee Benefit Claim') : {
	  'validate': 'sploy.sploy.api.allot.payroll_status',
	  'on_submit' :'sploy.sploy.api.allot.payroll_status'
  },
  ('Project', 'Task', 'Project Template', 'Project Type', 'Timesheet', 'Activity Cost', 'Activity Type') : {
	  'validate': 'sploy.sploy.api.allot.project_status',
	  'on_submit' :'sploy.sploy.api.allot.project_status'
  },
  ('Issue', 'Issue Type', 'Warranty Claim', 'Serial No', 'Service Level Agreement', 'Maintenance Schedule', 'Maintenance Visit') : {
	  'validate': 'sploy.sploy.api.allot.care_status',
	  'on_submit' :'sploy.sploy.api.allot.care_status'
  }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sploy.tasks.all"
# 	],
# 	"daily": [
# 		"sploy.tasks.daily"
# 	],
# 	"hourly": [
# 		"sploy.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sploy.tasks.weekly"
# 	]
# 	"monthly": [
# 		"sploy.tasks.monthly"
# 	]
# }

scheduler_events = {
	"daily": [
		"sploy.ploy.tasks.daily"
	]
}

# Testing
# -------

# before_tests = "sploy.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sploy.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "sploy.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"sploy.auth.validate"
# ]

