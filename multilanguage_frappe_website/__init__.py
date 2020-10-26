# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe


__version__ = '0.0.1'


def dfp_guess_language(lang_list=None) -> str:
	"""Set `frappe.local.lang` from url language segment: `/xx/...`"""
	from .hooks import multilanguage_app_site_hosts as multilanguage_site
	from .hooks import translated_languages_for_website as languages
	if frappe.local.site in multilanguage_site and languages:
		# If language passed in url like: `url?_lang=xx`
		if frappe.local.form_dict._lang and frappe.local.form_dict._lang in languages:
			lang = frappe.local.form_dict._lang
		else:
			path = frappe.local.request.path
			# Default language first in list
			lang = languages[0]
			# /xx || /xx/path 
			if (len(path) == 3 or (len(path) > 3 and path[3:4] == "/")) and path[1:3] in languages:
				lang = path[1:3]
		# frappe.form_dict._lang = lang
		frappe.lang = frappe.local.lang = lang
		return lang
	return frappe_guess_language(lang_list)

import frappe.website.render
from frappe.translate import guess_language as frappe_guess_language
frappe.translate.guess_language = dfp_guess_language
frappe.website.render.guess_language = dfp_guess_language


def dfp_load_lang(lang, apps=None):
	"""Checks `en` too"""
	from .hooks import multilanguage_app_site_hosts as multilanguage_site
	from .hooks import translated_languages_for_website as languages
	if frappe.local.site in multilanguage_site and languages:
		import os
		from frappe.translate import get_translation_dict_from_file
		out = frappe.cache().hget("lang_full_dict", lang, shared=True)
		if not out:
			out = {}
			for app in (apps or frappe.get_all_apps(True)):
				path = os.path.join(frappe.get_pymodule_path(app), "translations", lang + ".csv")
				out.update(get_translation_dict_from_file(path, lang, app) or {})
			frappe.cache().hset("lang_full_dict", lang, out, shared=True)
		return out or {}
	return frappe_load_lang(lang, apps)

from frappe.translate import load_lang as frappe_load_lang
frappe.translate.load_lang = dfp_load_lang


def context_extend(context):
	import frappe

	languages = frappe.get_hooks("translated_languages_for_website")

	context["lang"] = frappe.local.lang
	context["url_lang"] = "" if frappe.local.lang == languages[0] else "/{0}".format(frappe.local.lang)

	path = frappe.local.request.path

	# Below context not needed for JS/CSS
	if not path.endswith((".js", ".css")):

		path_without_language = path
		if path == "/":
			path_without_language = ""
		elif len(path) >= 3 and path[1:3] in languages:
			path_without_language = path[3:]

		context["languages_meta"] = []
		for language in languages:
			# Main language: "x-default"
			if language == languages[0]:
				meta_url = "{0}".format(path_without_language)
			else:
				meta_url = "/{0}{1}".format(language, path_without_language)
			context["languages_meta"].append({
				"code": language,
				"hreflang": "x-default" if language == languages[0] else language,
				"url": frappe.utils.get_url(meta_url),
				"is_home": not path_without_language,
			})

		if not "context" in frappe.local.response:
			frappe.local.response.context = {}

	return context


def dfp_add_preload_headers(response):
	"""Allow externals links preloading"""
	frappe_add_preload_headers(response)
	response.headers["Link"] = response.headers["Link"].replace("/http", "http")

from frappe.website.render import add_preload_headers as frappe_add_preload_headers
frappe.website.render.add_preload_headers = dfp_add_preload_headers
