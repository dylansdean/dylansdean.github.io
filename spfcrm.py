# app.py

from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

class Contact:
    def __init__(self, id, name, email, status):
        self.id = id
        self.name = name
        self.email = email
        self.status = status


class CRM:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_contacts_table()

    # ... same as previous code ...


crm = CRM("crm.db")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_contact', methods=['POST'])
def add_contact():
    name = request.form['name']
    email = request.form['email']
    status = request.form['status']
    contact_id = crm.add_contact(name, email, status)
    return f"Contact added with ID: {contact_id}"


@app.route('/find_contact', methods=['POST'])
def find_contact():
    contact_id = request.form['contact_id']
    contact = crm.find_contact(contact_id)
    if contact:
        return f"ID: {contact.id}, Name: {contact.name}, Email: {contact.email}, Status: {contact.status}"
    else:
        return "Contact not found"


@app.route('/update_contact', methods=['POST'])
def update_contact():
    contact_id = request.form['contact_id']
