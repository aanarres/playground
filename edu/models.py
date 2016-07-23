from django.db import models

# edu minimalist models: School, Classroom, Student

class School(models.Model):
    def __str__(self):
        return 'School %d' % self.id

class Classroom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    
    def __str__(self):
        return 'Classroom %d from school %d' % (self.id, self.school_id)

class Student(models.Model):
    classroom = models.ForeignKey(Classroom)

    def __str__(self):
        return 'Student %d in classroom %d' % (self.id, self.classroom_id)
