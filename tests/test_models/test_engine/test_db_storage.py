#!/usr/bin/python3
"""Tests for the DBStorage engine class"""


import MySQLdb
import os
import unittest


class TestDBStorage (unittest.TestCase):
    """Tests for the DBStorage class"""

    @classmethod
    def setUpClass(cls):
        """Set up environment variables and store common objects"""

        import models
        import models.base_model
        import models.engine.db_storage
        cls.Base = models.base_model.Base
        cls.DBStorage = models.engine.db_storage.DBStorage
        cls.models = models
        cls.connection = MySQLdb.connect(
            user='hbnb_test',
            passwd='hbnb_test_pwd',
            host='localhost',
            db='hbnb_test_db'
        )
        cls.connection.autocommit(True)
        cls.cursor = cls.connection.cursor()
        cls.tables = set()
        for model in cls.models.classes.values():
            if hasattr(model, '__tablename__'):
                cls.tables.add(model.__tablename__)

    def setUp(self):
        """Skip tests if not using databases"""

        if os.getenv('HBNB_TYPE_STORAGE', '') != 'db':
            self.skipTest('not using databases')

    def tearDown(self):
        """Clear database after each test"""

        self.models.storage.save()
        self.models.storage = self.DBStorage()
        self.models.storage.reload()

    def test_createTables(self):
        """Reloading storage should create model metadata if needed"""

        with self.subTest(msg='no tables'):
            tables = set(self.tables)
            self.cursor.execute('SET FOREIGN_KEY_CHECKS = 0')
            for table in tables:
                self.cursor.execute('DROP TABLE `' + table + '`')
            self.cursor.execute('SET FOREIGN_KEY_CHECKS = 1')
            self.models.storage.reload()
            self.cursor.execute('SHOW TABLES')
            query = set(record[0] for record in self.cursor.fetchall())
            self.assertEqual(len(tables - query), 0)

        with self.subTest(msg='one missing table'):
            self.cursor.execute('DROP TABLE `reviews`')
            self.models.storage.reload()
            self.cursor.execute('SHOW TABLES')
            query = (record[0] for record in self.cursor.fetchall())
            self.assertIn('reviews', query)

    def test_getInstances(self):
        """Engine should be able to load instances from the database"""

        with self.subTest(msg='one table'):
            state = self.models.classes['State'](name='Texas')
            self.models.storage.new(state)
            state = self.models.classes['State'](name='Wyoming')
            self.models.storage.new(state)
            self.models.storage.save()
            objects = self.models.storage.all(self.models.classes['State'])
            self.cursor.execute('SELECT `id`, `name` FROM `states`')
            query = self.cursor.fetchall()
            self.assertEqual(len(query), len(objects))
            objects = tuple((obj.id, obj.name) for obj in objects.values())
            self.assertEqual(set(objects), set(query))

        with self.subTest(msg='all tables'):
            state = self.models.classes['State'](name='Texas')
            self.models.storage.new(state)
            city = self.models.classes['City'](name='Dallas', state=state)
            self.models.storage.new(city)
            user = self.models.classes['User'](
                email='postmaster@example.com',
                password='password123'
            )
            self.models.storage.new(user)
            amenity = self.models.classes['Amenity'](name='Wi-Fi')
            place = self.models.classes['Place'](
                name='Souped-Up Shipping Container',
                number_rooms=1,
                number_bathrooms=0,
                max_guest=1,
                price_by_night=20,
                city=city,
                user=user,
                amenities=[amenity]
            )
            amenity.place_amenities = [place]
            self.models.storage.new(amenity)
            self.models.storage.new(place)
            review = self.models.classes['Review'](
                text='bad',
                place=place,
                user=user
            )
            self.models.storage.new(review)
            self.models.storage.save()
            objects = self.models.storage.all()
            classes = (
                (name, cls.__tablename__)
                for name, cls in self.models.classes.items()
                if hasattr(cls, '__tablename__')
            )
            for cls, table in classes:
                self.cursor.execute('SELECT `id` FROM `' + table + '`')
                record = self.cursor.fetchone()
                self.assertIn(cls + '.' + record[0], objects)

    def test_queriesDeferred(self):
        """Database should be unchanged until storage.save is called"""

        with self.subTest(msg='insert and delete deferred'):
            state = self.models.classes['State'](name='Texas')
            self.models.storage.new(state)
            city = self.models.classes['City'](name='Dallas', state=state)
            self.models.storage.new(city)
            user = self.models.classes['User'](
                email='postmaster@example.com',
                password='password123'
            )
            self.models.storage.new(user)
            amenity = self.models.classes['Amenity'](name='Wi-Fi')
            place = self.models.classes['Place'](
                name='Souped-Up Shipping Container',
                number_rooms=1,
                number_bathrooms=0,
                max_guest=1,
                price_by_night=20,
                city=city,
                user=user,
                amenities=[amenity]
            )
            amenity.place_amenities = [place]
            self.models.storage.new(amenity)
            self.models.storage.new(place)
            review = self.models.classes['Review'](
                text='bad',
                place=place,
                user=user
            )
            self.models.storage.new(review)
            for table in self.tables:
                self.cursor.execute('SELECT count(*) FROM `' + table + '`')
                self.assertEqual(self.cursor.fetchone()[0], 0)
            self.models.storage.save()
            for table in self.tables:
                self.cursor.execute('SELECT count(*) FROM `' + table + '`')
                self.assertEqual(self.cursor.fetchone()[0], 1)
            self.models.storage.delete(review)
            self.models.storage.delete(amenity)
            self.models.storage.delete(place)
            self.models.storage.delete(user)
            self.models.storage.delete(city)
            self.models.storage.delete(state)
            for table in self.tables:
                self.cursor.execute('SELECT count(*) FROM `' + table + '`')
                self.assertEqual(self.cursor.fetchone()[0], 1)
            self.models.storage.save()
            for table in self.tables:
                self.cursor.execute('SELECT count(*) FROM `' + table + '`')
                self.assertEqual(self.cursor.fetchone()[0], 0)

        with self.subTest('update deferred'):
            state = self.models.classes['State'](name='Texas')
            self.models.storage.new(state)
            self.models.storage.save()
            state.name = 'New York'
            self.cursor.execute('SELECT `name` FROM `states`')
            self.assertEqual(self.cursor.fetchone()[0], 'Texas')
