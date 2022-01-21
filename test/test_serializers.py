from django.test import TestCase
from you_tube_rest.models import *
from you_tube_rest.serializers import *
from django.contrib.auth.models import User


class TestVideoSerializer(TestCase):
    def setUp(self):
        self.actor = Video.objects.create( name='Wonder woman',  video_location='https://www.youtube.com/watch?v=sfM7_JLk-84',
        viewers=415625874 , creation_time_video = "1984-04-30", gender='P')
    def test_data(self):
        data =VideoSerializer(self.actor).data
        self.assertIsNotNone(data)
        assert data['id'] is not None
        assert data['name'] == 'Wonder woman'
        self.assertEqual(data['gender'], 'P')
        assert data['creation_time_video'] == "1984-04-30"
        assert data['viewers'] == 415625874
        assert data['video_location'] == 'https://www.youtube.com/watch?v=sfM7_JLk-84'
        
class TestCommentValidation(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Shuxratmusayev', password='1234admin')
        self.video = Video.objects.create( name='Wonder woman',  video_location='https://www.youtube.com/watch?v=sfM7_JLk-84',
        viewers=415625874 , creation_time_video = "1984-04-30", gender='P')
    def test_is_valid(self):
        data = { 
            'id': 1,
            'video':self.video,
            'userprofile':self.user,
            "description":'Elparvar haqiqatni gapriadigan okamiz'     
                }
        ser = CommentSerializer(data=data)
        self.assertFalse(ser.is_valid())
        
        
        


class TestPlayListValidation(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Shuxratmusayev', password='1234admin')
        self.video = Video.objects.create( name='Wonder woman',  video_location='https://www.youtube.com/watch?v=sfM7_JLk-84',
        viewers=415625874 , creation_time_video = "1984-04-30", gender='P')
    def test_is_valid(self):
        data = { 
            'id': 1,
            'title':'Elparvar top videolar',
            'video':self.video,
            'user':self.user,
            'creation_time_playlist':'1984-04-30'   
                }
        ser = PlaylistSerilaizer(data=data)
        self.assertFalse(ser.is_valid())