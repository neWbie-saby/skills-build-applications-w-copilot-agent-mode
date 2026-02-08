from djongo import models

class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=50, unique=True)
    members = models.ManyToManyField('User', related_name='team_memberships')
    class Meta:
        db_table = 'teams'

class User(models.Model):
    _id = models.ObjectIdField()
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    is_superhero = models.BooleanField(default=False)
    class Meta:
        db_table = 'users'

class Activity(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()
    class Meta:
        db_table = 'activities'

class Leaderboard(models.Model):
    team = models.CharField(max_length=50)
    points = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=50)
    class Meta:
        db_table = 'workouts'
