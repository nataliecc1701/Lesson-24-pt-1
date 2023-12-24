from unittest import TestCase

from app import app
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False
app.config['TESTING'] = True

db.drop_all
db.create_all

class RouteTestCase(TestCase):
    def setUp(self):
        with app.app_context():
            User.query.delete()
            
            user = User(first_name="Test", last_name="Entry")
            db.session.add(user)
            db.session.commit()
            self.user_id = user.id
        
    def tearDown(self):
        with app.app_context():
            db.session.rollback()
    
    def test_index_route(self):
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Test Entry', html)
    
    def test_user_details(self):
        with app.test_client() as client:
            resp = client.get(f"/users/{self.user_id}")
            html = resp.get_data(as_text = True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Test Entry</h1>', html)
            
    def test_add_form(self):
        with app.test_client() as client:
            resp = client.get("/users/new")
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Add User</h1>', html)
            
    def test_edit_form(self):
        with app.test_client() as client:
            resp = client.get(f"/users/{self.user_id}/edit")
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Update Profile for Test Entry</h1>', html)