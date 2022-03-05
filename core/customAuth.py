from rest_framework.authentication import TokenAuthentication

authTokenName = "auth_token"

class TokenAuthWithCookiesSupport(TokenAuthentication):

    # extend the TokenAuthentication class to support cookie based auth as well
    def authenticate(self, request):
        # check if 'auth_token' in the request.COOKIES
        if authTokenName in request.COOKIES and \
            'HTTP_AUTHORIZATION' not in request.META:

            return self.authenticate_credentials(
                request.COOKIES.get(authTokenName)
            )

        else: return super().authenticate(request) # else continue with request header token auth
