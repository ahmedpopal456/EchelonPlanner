# Register your models here.
from app.subsystem.usermanagement.professor import Professor
from app.subsystem.usermanagement.programdirector import ProgramDirector
from app.subsystem.usermanagement.student import Student


admin.site.register(Professor)
admin.site.register(ProgramDirector)
admin.site.register(Student)