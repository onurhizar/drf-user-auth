# Django Rest Framework - User Authentication Example 1

A playground for DRF testing and practice purposes.

---

# Routes

`/admin/`
`/api/test/`
`/api/users/`
`/api/gettoken/`
`/api/protected-test/`
`/api/setcookie-test/`

---

# TODO
* StatusMessage model 
* Relationship that model with User model (many to one)
* List status messages of a user
* Post status message with auth token

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
* ADD users (user1 and user2 : ┼čifrembudur123) via admin page for testing
* ADD serializers.py @ core to list or register users
* ADD UsersView @ core/views.py for GET and POST methods, to list or register users
* ADD status codes for 201, 400 etc
* ADD serializer.errors to send the error messages back with status codes
* ADD api/users/ route for GET and POST methods


## v0.0.3
* ADD 'rest_framework.authtoken' @ server/settings.py installed apps
* ADD customAuth.py for enhanced version of token auth with cookies support
* ADD 'REST_FRAMEWORK' dictionary with custom authenticator
* ADD obtain_auth_token from rest_framework.authtoken.views @ core/urls.py
* ADD gettoken/ route to obtain token with credentials @ core/urls.py
* INFO now you can get token and cookie via api/gettoken/ route
* TODO get Set-Cookie header from gettoken route with CustomAuthToken? [DONE @ v0.0.4]


## v0.0.4
* ADD custom auth token inherited from ObtainAuthToken class @ core/views.py
* EDIT core/urls.py with CustomAuthTokenObtainView for gettoken/ route
* INFO now server sends back the id and username as well as the token
* INFO now server adds Set-Token header to the response (It was a todo from 0.0.3)


## v0.0.5
* ADD protected route with token @ core/views.py and core/urls.py
* INFO /api/protected-test/ route for testing the auth & permissions
to test protected route with cookie via HTTPie:
`http http://127.0.0.1:8000/api/protected-test/ Cookie:"auth_token=f619b9ec3759a05a80532654103080527e19c3ca"`
or
`http http://127.0.0.1:8000/api/protected-test/ 'Authorization: Token f619b9ec3759a05a80532654103080527e19c3ca'`


## v0.0.6
* INFO corsheaders has been installed `pip install django-cors-headers`
* ADD corsheaders @ server/settings.py and configured for 8080 port


## v0.0.7
* ADD SetCookieTestView @ core/views.py for test purposes
* ADD setcookie-test/ route 
* EDIT cookie value of CustomAuthTokenObtainView with `Path=/`


