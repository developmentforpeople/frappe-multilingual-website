# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "multilanguage_frappe_website"
app_title = "Multilanguage Frappe Website"
app_publisher = "DFP developmentforpeople"
app_description = "Multilanguage Frappe Framework website example"
app_icon = "octicon octicon-file-directory"
app_color = "green"
app_email = "developmentforpeople@gmail.com"
app_license = "MIT"


# App name (used to override only sites with this app installed)
multilanguage_app_site_name = app_name

# Hosts/sites where this app will be enabled
multilanguage_app_site_hosts = ["mf.local", "frappe-multilingual-website.developmentforpeople.com"]

# Languages available for site
translated_languages_for_website = ["en", "es"]

# First one on list will be the default one
language_default = translated_languages_for_website[0]

# Home page
home_page = "index"

# Url 301 redirects
website_redirects = [
	# Remove duplicated pages for home:
	{ "source": "/index", "target": "/" },
	{ "source": "/index.html", "target": "/" },
	# Languages: Remove main language segment. For example,
	# if "en" is first one in "translated_languages_for_website"
	# then route "/en/example" will be redirected 301 to "/example"
	{ "source": r"/{0}".format(language_default), "target": "/" },
	{ "source": r"/{0}/(.*)".format(language_default), "target": r"/\1" },
	# Foce url language for some Frappe framework dynamic pages:
	{ "source": "/en/login", "target": "/login?_lang=en" },
	{ "source": "/es/login", "target": "/login?_lang=es" },
	{ "source": "/en/contact", "target": "/contact?_lang=en" },
	{ "source": "/es/contact", "target": "/contact?_lang=es" },
	# Foce url language for not language specific pages:
	{ "source": "/en/translations", "target": "/translations?_lang=en" },
	{ "source": "/es/translations", "target": "/translations?_lang=es" },
]

# Setup some global context variables related to languages
website_context = {
	"languages": translated_languages_for_website,
	"language_default": language_default,
	"app_site_name": app_name,
}

# Calculate active language from url first segment
update_website_context = [
	"{0}.context_extend".format(app_name),
]


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/multilanguage_frappe_website/css/multilanguage_frappe_website.css"
# app_include_js = "/assets/multilanguage_frappe_website/js/multilanguage_frappe_website.js"

# include js, css files in header of web template
web_include_css = "/assets/multilanguage_frappe_website/css/multilanguage_frappe_website.css"
# web_include_js = "/assets/multilanguage_frappe_website/js/multilanguage_frappe_website.js"

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
# get_website_user_home_page = "multilanguage_frappe_website.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "multilanguage_frappe_website.install.before_install"
# after_install = "multilanguage_frappe_website.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "multilanguage_frappe_website.notifications.get_notification_config"

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
# 		"multilanguage_frappe_website.tasks.all"
# 	],
# 	"daily": [
# 		"multilanguage_frappe_website.tasks.daily"
# 	],
# 	"hourly": [
# 		"multilanguage_frappe_website.tasks.hourly"
# 	],
# 	"weekly": [
# 		"multilanguage_frappe_website.tasks.weekly"
# 	]
# 	"monthly": [
# 		"multilanguage_frappe_website.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "multilanguage_frappe_website.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "multilanguage_frappe_website.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "multilanguage_frappe_website.task.get_dashboard_data"
# }

