
# import fields from django.db.models
from django.db.models import fields
# import serializers from rest_framework
from rest_framework import serializers
# import Views from app.views
from you_tube_rest.views import *
# import models from app.models
from you_tube_rest.models import *
from django.test import TestCase, Client



class Video_TestViewlists(TestCase): # POST /post
    def setUp(self) -> None:
        """Set up the video viewlists. """
        self.cl = Client() 
        
    def test_post_an_actor(self):
        new = { "id" : 5,
            "name" : "shuhrat musayev elparvar urshib ketdi janjal", 
            "video_location" : "https://www.youtube.com/watch?v=lw9fG-7ePrs",
            "viewers" : 83558,
            "creation_time_video" : "2021-11-22",
            "userprofile" : "islomjon",
            "gender" : "P"
            }
        a = self.cl.post('/videolist/', data=new)
        response = self.cl.get('/videolist/')
        self.assertEqual(response.status_code, 200)
        assert new is not None
        assert new["id"] is not None
        assert new["name"] == "shuhrat musayev elparvar urshib ketdi janjal"
        assert new["video_location"] == "https://www.youtube.com/watch?v=lw9fG-7ePrs"
        assert new["viewers"] == 83558
        assert new["creation_time_video"] == "2021-11-22"
        assert new["userprofile"] == "islomjon"
        assert new["gender"] == "P"
        
class TestCommentViewList(TestCase):
    def setUp(self) -> None:
        """ Set up comment view lists. """
        self.cl = Client()
        
    def test_all_comments(self):
        """ Test all comments """
        comment = self.cl.get("/commentlist/").data
        self.assertEqual(len(comment), 0)
        assert len(comment) == 0
        
class Playlist_TestViewlists(TestCase): # POST /post
    def setUp(self) -> None:
        """Set up the video viewlists. """
        self.cl = Client() 
        
    def test_play_an_playlist(self):
        new = { "id" : 5,
            "title" : "shuhrat musayev elparvar urshib ketdi janjal", 
            "user" : "islomjon",
            "creation_time_playlist" : "2021-11-22",
            "video" : "https://www.youtube.com/watch?v=lw9fG-7ePrs",
            }
        a = self.cl.post('/playlist/', data=new)
        response = self.cl.get('/playlist/')
        self.assertEqual(response.status_code, 200)
        assert new is not None
        assert new["id"] is not None
        assert new["title"] == "shuhrat musayev elparvar urshib ketdi janjal"
        assert new["user"] == "islomjon"
        assert new["creation_time_playlist"] == "2021-11-22"
        assert new["video"] == "https://www.youtube.com/watch?v=lw9fG-7ePrs"
        
