# Oauthentication-and-JWTtokens-UsingFastApi
Full Process of Doing Authentication Process by hashing password  then Generating Token for API which is later retested again and again in Postman

Oauthentication-and-JWTtokens-UsingFastApi

# Description:
The provided code implements an authentication and token generation system using FastAPI, PostgreSQL, and JSON Web Tokens (JWT). 
Here's a description of the main components and their functionalities:
1.#𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲 𝗖𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻
The code establishes a connection to a PostgreSQL database using the psycopg2 library. 
It sets up a cursor object to execute SQL queries.

2.𝗨𝘀𝗲𝗿 𝗠𝗼𝗱𝗲𝗹
The user class is defined using the BaseModel from Pydantic. 
It represents the structure of a user, including the email and password fields.

3.𝗨𝘀𝗲𝗿 𝗖𝗿𝗲𝗮𝘁𝗶𝗼𝗻
The /createuser endpoint allows creating a new user. 
The provided email and password are hashed using the hashing1 module.
The hashed password and a randomly generated user ID are stored in the PostgreSQL database.

4.𝗨𝘀𝗲𝗿 𝗟𝗼𝗴𝗶𝗻
The /loginnow endpoint verifies the user's credentials by comparing the
provided password with the stored hashed password. If the password is correct, a success message is returned.

5.𝗧𝗼𝗸𝗲𝗻 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗼𝗻
The /token endpoint uses the OAuth2 password flow to generate an access token.
It expects the username (email) and password in the request body. 
If the credentials are valid, an access token is created using the Oauthandtoken1 module. The access token is returned as the response.

6.𝗧𝗼𝗸𝗲𝗻 𝗩𝗲𝗿𝗶𝗳𝗶𝗰𝗮𝘁𝗶𝗼𝗻
 The code includes commented-out functions (verify_access_token and get_current_user) that 
demonstrate the process of verifying an access token and retrieving the current user based on the token.
These functions utilize the jose library and can be used as dependencies for protected routes that require authentication.

7.𝗛𝗮𝘀𝗵𝗶𝗻𝗴 𝗣𝗮𝘀𝘀𝘄𝗼𝗿𝗱𝘀
The hashing function in the hashing1 module is used to hash user passwords using the passlib library with the bcrypt hashing scheme.

8.𝗩𝗲𝗿𝗶𝗳𝘆𝗶𝗻𝗴 𝗣𝗮𝘀𝘀𝘄𝗼𝗿𝗱𝘀
 The verify function in the hashing1 module compares a plain password with a hashed password to verify their match.
9. 𝗧𝗼𝗸𝗲𝗻 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗼𝗻 𝗗𝗲𝘁𝗮𝗶𝗹𝘀
The code includes a secret key (SECRET_KEY), algorithm (ALGORITHM), and expiration time (ACCESS_TOKEN_EXPIRE_MINUTES) for
JWT-based token generation. However, the token generation logic is commented out, and only the token endpoint is exposed for simplicity.𝗧𝗼𝗸𝗲𝗻 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗼𝗻 𝗗𝗲𝘁𝗮𝗶𝗹𝘀


𝗨𝘀𝗮𝗴𝗲
𝗖𝗿𝗲𝗮𝘁𝗲 𝗨𝘀𝗲𝗿
Endpoint: /createuser
{
  "email": "example@example.com",
  "password": "password123"
}

Response:
{
  "message": "User Created"
}
𝗟𝗼𝗴𝗶𝗻
Endpoint:/loginnow
Method: POST

Request Body:
{
  "email": "example@example.com",
  "password": "password123"
}


file:///home/sami/Desktop/Python/Screenshot.png


𝟮𝟬 𝗰𝗼𝗺𝗺𝗼𝗻 𝗲𝗿𝗿𝗼𝗿𝘀 𝘁𝗼 𝗯𝗲 𝗮𝘄𝗮𝗿𝗲 𝗼𝗳 𝘄𝗵𝗲𝗻 𝘂𝘀𝗶𝗻𝗴 𝗝𝗪𝗧 𝗮𝗻𝗱 𝗮𝘂𝘁𝗵𝗲𝗻𝘁𝗶𝗰𝗮𝘁𝗶𝗼𝗻 𝗶𝗻 𝗙𝗮𝘀𝘁𝗔𝗣𝗜

1. Weak Secret Key
2. 





