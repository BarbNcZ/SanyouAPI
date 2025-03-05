To execute the server run the following command:

`uvicorn main:app --reload`

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

## Folder structure explanation

[Click here](Folders_Structure.md) to read more about the folder structure

## `requirements.txt` file explanation

[Click here](Requirements_File.md) to read more about the `requirements.txt` file