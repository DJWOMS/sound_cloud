import base64
from typing import Optional

import requests
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed

from src.oauth.models import AuthUser
from src.oauth.services import base_auth


def get_spotify_jwt(code: str) -> Optional[str]:
    url = 'https://accounts.spotify.com/api/token'
    basic_str = f'{settings.SPOTIFY_CLIENT_ID}:{settings.SPOTIFY_SECRET}'.encode('ascii')
    basic = base64.b64encode(basic_str)
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'http://localhost:8000/spotify-callback'
    }
    headers = {
        'Authorization': f'Basic {basic.decode("ascii")}'
    }
    res = requests.post(url, data=data, headers=headers)
    if res.status_code == 200:
        r = res.json()
        return r.get('access_token')
    else:
        return None


def get_spotify_user(token: str) -> str:
    url_get_user = 'https://api.spotify.com/v1/me'
    headers = {'Authorization': f'Bearer {token}'}
    res = requests.get(url_get_user, headers=headers)
    r = res.json()
    return r.get('email')


def get_spotify_email(code: str) -> Optional[str]:
    _token = get_spotify_jwt(code)
    if _token is not None:
        return get_spotify_user(_token)
    else:
        return None


def spotify_auth(code: str):
    email = get_spotify_email(code)
    if email is not None:
        user, _ = AuthUser.objects.get_or_create(email=email)
        return base_auth.create_token(user.id)
    else:
        raise AuthenticationFailed(code=403, detail='Bad token Spotify')

