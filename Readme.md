To execute the server run the following command:

`uvicorn Main:app --reload`

---

> [!WARNING]
> ### Database connection data
> 
> You must create a `.env` file, if you don't have it, with the database connection data in order to be able connect to the database.
> 
> The structure should be like:
> 
> ```
> DB_HOST='your_database_host'
> DB_USER='your_database_user'
> DB_PASSWORD='your_secure_password'
> ```