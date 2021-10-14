from flask import Flask
from flask_restful import Resource, Api, reqparse
import psycopg2

app = Flask(__name__)
api = Api(app)



class Profiles(Resource):
    def __init__(self):
        self.conn=psycopg2.connect(database='amar', user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        self.cur=self.conn.cursor()
        self.tablename = 'profiles' 

    def get(self):
        self.cur.execute(f"select * from {self.tablename}")
        data=self.cur.fetchall()
        return {'profiles': data} , 200  # return data and 200 OK
    
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('Name', required=True)  # add args
        parser.add_argument('DOB', required=True)
        parser.add_argument('Status', default='Active')
        args = parser.parse_args()  # parse arguments to dictionary
        # add data entry
        self.cur.execute(f"insert into {self.tablename} values ('{args['Name']}','{args['DOB']}','{args['Status']}')")
        self.conn.commit()
        self.cur.execute(f"select * from {self.tablename} where Name='{args['Name']}' and DOB='{args['DOB']}'")
        data=self.cur.fetchall()
        return {'data': data}, 200  # return data with 200 OK'''

    def put(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('Name', required=True)
        parser.add_argument('Status', default='Active')  # add args
        args = parser.parse_args()  # parse arguments to dictionary
        self.cur.execute(f"select Name from {self.tablename}")
        c=self.cur.fetchall()
        flat_list = [item for sublist in c for item in sublist]
        if args['Name'] in flat_list:
            # update data entry matching given Name
            self.cur.execute(f'update {self.tablename} set Status = \'%s\' where name = \'%s\''%(args['Status'],args['Name']))
            self.conn.commit()
            data = self.cur.execute(f"select * from {self.tablename} where Name='{args['Name']}'")
            data=self.cur.fetchall()
            return {'data': data}, 200 #return data and 200 OK

        else:
            # otherwise the Name does not exist
            return {
                'message': f"'{args['Name']}' user not found."
            }, 404

    def delete(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('Name', required=True)  # add userId arg
        args = parser.parse_args()  # parse arguments to dictionary
        self.cur.execute("SELECT Name FROM profiles")
        c=self.cur.fetchall()
        flat_list = [item for sublist in c for item in sublist]        
        if args['Name'] in flat_list:
            # remove data entry matching given Name
            self.cur.execute(f"delete from {self.tablename} where Name='{args['Name']}'")
            self.conn.commit()
            return {"message":"success"}
        else:
            # otherwise we return 404 because userId does not exist
            return {
                'message': f"'{args['Name']}' user not found."
            }, 404
class Paused(Resource):
    def __init__(self):
        self.conn=psycopg2.connect(database='amar', user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        self.cur=self.conn.cursor()
        self.tablename = 'profiles'
    def get(self):
        self.cur.execute(f"select * from {self.tablename} where Status='Paused'")
        data=self.cur.fetchall()
        return {'Paused Profiles': data} , 200 # return data and 200 OK'''
  
api.add_resource(Profiles, '/profiles')  # add endpoint
api.add_resource(Paused, '/profiles/paused')  # add endpoint

if __name__ == '__main__':
    app.run()  # run our Flask app