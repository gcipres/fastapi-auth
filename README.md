# fastapi-auth
Project to authentication with python use fastapi and run with docker and mysql like a database.

## Steps to run

For run this app execute the `docker-compose up` command in the root of project and the app and database containers will be created.

Next you will enter to the follow url to check the API documentation `http://127.0.0.0:8000/docs`

You need first excecute the next request:
```
Request: POST | /auth/signup
Body: {
  "email": "<your email here>",
  "name": "<your name here>
}
```


*** The password will be generate automatically, you need show logs to check password generated, because this app was designed to send a random password by email (This app don't send emails, is for this reason that password is print in logs, only is a test app) ***

For access you need excecute the follow request:
```
Request: POST | auth/signin
Form: {
  username: "<your email here>"
  password: "<your password here>"
}
```

After excecute the before petition, you can see a jwt in the response.

Now you can excecute `GET | /auth/profile` to validate a user authenticated (make sure put a jwt data in your header petition like Bearer)
