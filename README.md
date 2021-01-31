# Jatayu Billboard Project Api's

#### You could find the OpenAPI Docs in the `{ip}:host/docs`
### steps to run server

1. run `virtualenv my_env`
2. run `source ./my_env/bin/activate`
3. run `pip install -r requiremnets.txt`
4. run `uvicorn app:app` to start server


### To activate fake server
1. got to folder `fake_api_virtusa`
2. Run `docker build .`
3. Run the Image

### To authenticate the route
1. Login using Api to get access token
2. Use that access token to authenticate the route
