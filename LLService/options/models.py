from django.db import models
from registrations.models import User

# TIME_INTERVAL = [
#     ('0', '0:00'),
#     ('1', '1:00'),
#     ('2', '2:00'),
#     ('3', '3:00'),
#     ('4', '4:00'),
#     ('5', '5:00'),
#     ('6', '6:00'),
#     ('7', '7:00'),
#     ('8', '8:00'),
#     ('9', '9:00'),
#     ('10', '10:00'),
#     ('11', '11:00'),
#     ('12', '12:00'),
#     ('13', '13:00'),
#     ('14', '14:00'),
#     ('15', '15:00'),
#     ('16', '16:00'),
#     ('17', '17:00'),
#     ('18', '18:00'),
#     ('19', '19:00'),
#     ('20', '20:00'),
#     ('21', '21:00'),
#     ('22', '22:00'),
#     ('23', '23:00'),
#     ('24', '24:00'),
# ]

def time_gen():
    t = []
    for i in range(25):
        t.append((f'{i}', f'{i}:00'))
    return t

class TimeInterval(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_intervals',
        on_delete=models.CASCADE,
    )
    TIME_INTERVAL = time_gen()
    time_start = models.CharField(max_length=1, choices=TIME_INTERVAL)
    time_end = models.CharField(max_length=1, choices=TIME_INTERVAL)

class RepeatAmount(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_repeats',
        on_delete=models.CASCADE,
    )
    words_per_day = models.IntegerField(
        default=10,
    )

class Status(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_word_status',
        on_delete=models.CASCADE,
    )
    status1 = models.IntegerField(default=300)
    status2 = models.IntegerField(default=900)
    status3 = models.IntegerField(default=2700)
    status4 = models.IntegerField(default=7200)
    status5 = models.IntegerField(default=18000)
    status6 = models.IntegerField(default=86400)
    status7 = models.IntegerField(default=259200)
    status8 = models.IntegerField(default=2592000)



