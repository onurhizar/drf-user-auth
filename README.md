# Django Rest Framework - User Authentication Example 1

A playground for DRF testing and practice purposes.

---

# Changelog

## v0.0.1
* ADD new app named 'core'
* ADD rest_framework, core @ server/settings.py
* ADD TestView @ core/views.py for testing
* ADD urls.py @ core with 'test/' route for testing
* ADD include core.urls @ server/urls.py with 'api/' route

## v0.0.2
* ADD superuser (admin : 123456qwe*)
* ADD users (user1 and user2 : şifrembudur123) via admin page for testing
* ADD serializers.py @ core to list or register users
* ADD UsersView @ core/views.py for GET and POST methods, to list or register users
* ADD status codes for 201, 400 etc
* ADD serializer.errors to send the error messages back with status codes
* ADD api/users/ route for GET and POST methods

