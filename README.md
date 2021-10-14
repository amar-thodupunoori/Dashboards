# Profiles REST api 
1. INSTALL FLASK 
```sh
    pip install flask
```
2. INSTALL PSYCOPG2
```sh
    pip install psycopg2
```
3. INSTALL POSTMAN (for testing)
4. INSTALL POSTGRESQL
5. Open editor (visual studio code)
6. Go to Profiles 
7. Run the code present in the file HE.py
8. Copy the link provided
9. Open postman and goto localhost:5000/profiles and use Get method to view the list
```sh
    localhost:5000/profiles
```
10. To add more to the list change the method to Post and provide Name, DOB and Status

11. To edit the list change the method to Put and provide the Name and modified Status

12. To delete a user from the list change the method to Delete and provided Name

13. To view the list of the profiles whose status is paused goto localhost:5000/profiles/paused
```sh
   localhost:5000/profiles/paused
```


