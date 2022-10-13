#!/usr/bin/python
import sqlite3

from registration import Registration


class Database:
    def __init__(self, filename: str):
        self.filename = filename

    def __connect_to_db(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.filename)
        return conn

    def create_registration_table(self):
        try:
            conn = self.__connect_to_db()
            conn.execute(
                "CREATE TABLE IF NOT EXISTS registration(registration_id INTEGER PRIMARY KEY NOT NULL, date_1 DATE NOT NULL, date_2 DATE NOT NULL, who TEXT NOT NULL, what TEXT NOT NULL)")
            conn.commit()
            print("registration table created successfully")
        except:
            print("registration table creation failed - Maybe table")
        finally:
            conn.close()

    def insert_registration(self, registration: Registration):
        inserted_registration = {}
        try:
            conn = self.__connect_to_db()
            cur = conn.cursor()
            cur.execute("INSERT INTO registration (date_1, date_2, who, what) values (?, ?, ?, ?)",
                        (registration['date_1'], registration['date_2'], registration['who'], registration['what']))

            conn.commit()
            inserted_registration = self.get_registration_by_id(cur.lastrowid)
        except:
            conn.rollback()

        finally:
            conn.close()

        return inserted_registration

    def get_registrations(self):
        registrations = []
        try:
            conn = self.__connect_to_db()
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT * FROM registration")
            rows = cur.fetchall()
            print(rows)

            # convert row objects to dictionary
            for i in rows:
                registration = {}
                registration["registration_id"] = i["registration_id"]
                registration["date_1"] = i["date_1"]
                registration["date_2"] = i["date_2"]
                registration["who"] = i["who"]
                registration["what"] = i["what"]
                registrations.append(registration)

        except:
            registrations = []

        return registrations

    def get_registration_by_id(self, registration_id: int):
        registration = {}
        try:
            conn = self.__connect_to_db()
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT * FROM registration WHERE registration_id = ?",
                        (registration_id,))
            row = cur.fetchone()

            # convert row object to dictionary
            registration["registration_id"] = row["registration_id"]
            registration["date_1"] = row["date_1"]
            registration["date_2"] = row["date_2"]
            registration["who"] = row["who"]
            registration["what"] = row["what"]
        except:
            registration = {}

        return registration

    def get_registartions_by_name(self, name: str):
        registrations = []
        try:
            conn = self.__connect_to_db()
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT * FROM registration WHERE who = ?",
                        (name,))
            rows = cur.fetchall()
            print(rows)

            for i in rows:
                registration = {}
                registration["registration_id"] = i["registration_id"]
                registration["date_1"] = i["date_1"]
                registration["date_2"] = i["date_2"]
                registration["who"] = i["who"]
                registration["what"] = i["what"]
                registrations.append(registration)

            print("dupa")
            print(registrations)
        except:
            registrations = []

        return registrations

    def update_registration(self, registration, registartion_id):
        updated_registration = {}
        try:

            conn = self.__connect_to_db()
            cur = conn.cursor()

            cur.execute("UPDATE registration SET date_1 = ?, date_2 = ?, who = ?, what = ? WHERE registration_id = ?",
                        (registration['date_1'], registration['date_2'], registration['who'], registration['what'], registartion_id))

            conn.commit()

            updated_registration = self.get_registration_by_id(
                registartion_id)
            # print(updated_registration)

        except:
            conn.rollback()
            updated_registration = {}
        finally:
            conn.close()

        return updated_registration

    def delete_registration(self, registration_id: int):
        message = {}
        try:
            conn = self.__connect_to_db()
            conn.execute("DELETE from registration WHERE registration_id = ?",
                         (registration_id,))
            conn.commit()
            message["status"] = "registration deleted successfully"
        except:
            conn.rollback()
            message["status"] = "Cannot delete registration"
        finally:
            conn.close()

        return message

    def delete_all(self):
        message = {}
        try:
            conn = self.__connect_to_db()
            conn.execute("DELETE FROM registration")
            conn.commit()
            message["status"] = "all records deleted successfully"
        except:
            conn.rollback()
            message["status"] = "Cannot delete all records"
        finally:
            conn.close()

        return message
