from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Tasks

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. 
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
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

# Checking if the index page opens
class TestViews(TestBase):
    def test_index_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This is test description', response.data)