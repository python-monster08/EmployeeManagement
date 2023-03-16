from django.contrib import admin
from .models import Emp, Testimonial, Feedback
# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display = ('name','working','emp_id','phone','department','address')
    list_editable =  ('working','emp_id','department')
    search_fields = ('name','emp_id')
    list_filter = ('working',)


admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial)

class FeedbackAdmin(admin.ModelAdmin):
    list_display=('email','name','feedback')

    class Meta:
        model = Feedback

admin.site.register(Feedback,FeedbackAdmin)