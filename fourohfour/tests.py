"""Tests for the fourohfour app."""

from unittest import TestCase, mock
import string
import random
from wsgi import create_web_app
from http import HTTPStatus as status


class TestFourOhFour(TestCase):
    """Four oh four abounds."""

    def setUp(self):
        """We have an app and a client."""
        self.app = create_web_app()
        self.client = self.app.test_client()

    def test_returns_404(self):
        """The fourohfour app returns 404."""
        with self.app.app_context():
            response = self.client.get('/')

        self.assertEqual(response.status_code, status.NOT_FOUND,
                         "The root endpoint returns 400")

    def test_returns_404_on_post(self):
        """The fourohfour app returns 404 when you POST."""
        with self.app.app_context():
            response = self.client.post('/')

        self.assertEqual(response.status_code, status.NOT_FOUND,
                         "The root endpoint returns 400")

    def test_returns_404_on_head(self):
        """The fourohfour app returns 404 when you HEAD."""
        with self.app.app_context():
            response = self.client.head('/')

        self.assertEqual(response.status_code, status.NOT_FOUND,
                         "The root endpoint returns 400")

    def test_it_really_returns_404(self):
        """The fourohfour app returns 404 no matter what, really."""
        def random_path():
            path = ''.join(random.choices(string.ascii_uppercase + '/', k=20))
            return '/' + path

        for i in range(50):
            with self.app.app_context():
                response = self.client.get(random_path())

            self.assertEqual(response.status_code,
                             status.NOT_FOUND,
                             "404 all day long")


class TestHealthCheck(TestCase):
    """Test the health check endpoint."""

    def setUp(self):
        """We have an app and a client."""
        self.app = create_web_app()
        self.client = self.app.test_client()

    def test_returns_200(self):
        """The health check endpoint returns 200."""
        with self.app.app_context():
            response = self.client.get('/healthz')

        self.assertEqual(response.status_code, status.OK,
                         "The health check endpoint returns 200")
