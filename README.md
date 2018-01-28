
start  

	honcho start -f local (use gunicorn)

____  

Frest
=====
<img src="https://raw.githubusercontent.com/h4wldev/frest/master/frest.png" height="150">

[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/h4wldev/Frest/blob/master/LICENSE)

Frest is the frame of the restful api server created with [pallets/flask](https://github.com/pallets/flask).

## GOAL
Basic restful api server including login, sign up, sign out, modify account, writing, and etc..

## Getting Started
Just modify [`app/config`](https://github.com/h4wldev/Frest/blob/master/app/config.py) and `python app.py runserver` use it.

## FEATURE
__API__
- `GET /api/v@/` Return environment, versions
- `POST /api/v@/auth` Login
- `POST /api/v@/logout` Sign out
- `GET /api/v@/users` Get users with token and params: page(Default: 0), limit(Default: 10)
- `POST /api/v@/users` Sign Up
- `GET /api/v@/users/<prefix(me or user_id)>` Return user information
- `PUT /api/v@/users/<prefix(me or user_id)>` Modify user information
- `DELETE /api/v@/users/<prefix(me or user_id)>` Delete user
- `GET /api/v@/token?type=extension&token=<token>` Token expire time extension 
- `GET /api/v@/users/<prefix(me or user_id)>/login_histories` Return Login histories with token and params: page(Default: 0), limit(Default: 10)

__FUNCTION__
- Auto route loading `app/routes`
- Decorating return values `app/modules/frest/api`
- You can expire token with function `app/models/user_token_model` token_expire_all, token_expire_with_token

## APIDOC

How to see apidoc
~~~
//install
npm install apidoc -g

//run
apidoc -i ./ -o ./apidoc

//in directory ./apidoc, apidoc will be generated
~~~

