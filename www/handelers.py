#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Gu Xianxiong'

class BaseHandler(tornado.web.RequestHandler):

    def get_login_url(self):
        return u"/login"

    def get_current_user(self):
        user_json = self.get_secure_cookie("user")
        if user_json:
            return tornado.escape.json_decode(user_json)
        else:
            return None

class LoginHandler(BaseHandler):

    def get(self):
        self.render("login.html", next=self.get_argument("next","/"))

    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        # The authenticate method should match a username and password
        # to a username and password hash in the database users table.
        # Implementation left as an exercise for the reader.
        auth = self.db.authenticate(username, password)
        if auth:
            self.set_current_user(username)
            self.redirect(self.get_argument("next", u"/"))
        else:
            error_msg = u"?error=" + tornado.escape.url_escape("Login incorrect.")
            self.redirect(u"/login" + error_msg)

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie("user", tornado.escape.json_encode(user))
        else:
            self.clear_cookie("user")

class LogoutHandler(BaseHandler):

    def get(self):
        self.clear_cookie("user")
        self.redirect(u"/login)


class BaseHandler(tornado.web.RequestHandler):

            def get_login_url(self):
                return u"/login"

            def get_current_user(self):
                user_json = self.get_secure_cookie("user")
                if user_json:
                    return tornado.escape.json_decode(user_json)
                else:
                    return None

        class LoginHandler(BaseHandler):

            def get(self):
                self.render("login.html", next=self.get_argument("next", "/"), message=self.get_argument("error", ""))

            def post(self):
                email = self.get_argument("email", "")
                password = self.get_argument("password", "")

                user = self.application.syncdb['users'].find_one({'user': email})

                if user and user['password'] and bcrypt.hashpw(password, user['password']) == user['password']:
                    self.set_current_user(email)
                    self.redirect("hello")
                else:
                    error_msg = u"?error=" + tornado.escape.url_escape("Login incorrect.")
                    self.redirect(u"/login" + error_msg)

            def set_current_user(self, user):
                print
                "setting " + user
                if user:
                    self.set_secure_cookie("user", tornado.escape.json_encode(user))
                else:
                    self.clear_cookie("user")

        class RegisterHandler(LoginHandler):

            def get(self):
                self.render("register.html", next=self.get_argument("next", "/"))

            def post(self):
                email = self.get_argument("email", "")

                already_taken = self.application.syncdb['users'].find_one({'user': email})
                if already_taken:
                    error_msg = u"?error=" + tornado.escape.url_escape("Login name already taken")
                    self.redirect(u"/login" + error_msg)

                password = self.get_argument("password", "")
                hashed_pass = bcrypt.hashpw(password, bcrypt.gensalt(8))

                user = {}
                user['user'] = email
                user['password'] = hashed_pass

                auth = self.application.syncdb['users'].save(user)
                self.set_current_user(email)

                self.redirect("hello")
