from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Tasks

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. 
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

        # Will be called before every test
    def setUp(self):
        # Creating table
        db.create_all()
        # Creating task object
        demo = Tasks(description='This is test description')
        # Saving data to db
        db.session.add(demo)
        db.session.commit()

        # Will be called before every test
    def tearDown(self):
        # Closing db connection and removing all it's content
        db.session.remove()
        db.drop_all()

class TestRead(TestBase):
    def test_index(self):
        response = self.client.get(url_for('index'))
        self.assertIn(b'Run unit tests', response.data)
# Add task
    def test_add(self):
        response = self.client.get(url_for(''))

# Get a single task
    def test_read(self):
        response = self.client.get(url_for(''))

# Update the task
    def test_update(self):
        response = self.client.get(url_for(''))

# Delete the task
    def test_read(self):
        response = self.client.get(url_for(''))