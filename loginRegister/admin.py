from django.contrib import admin
# from loginRegister.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
# class ProfileAdmin(admin.ModelAdmin):
#     list_display=('user','status',)
#     list_display = ('user.username', 'email', 'is_superuser','is_staff','is_active', 'status',)
#     list_filter = ("status",)
#     search_fields = ['title', 'content']
#     prepopulated_fields = {'slug': ('title',)}
# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'Profile'
#     fk_name = 'user'
# class CustomUserAdmin(UserAdmin):
#     inlines = (ProfileInline, )
#     # list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'status')
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff',)
#     # list_select_related = ('profile', )
#     # def status(self,instance):
#     #     if instance.profile.status:
#     #         return "Active"
#     #     else:
#     #         return "Blocked"

#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             return list()
#         return super(CustomUserAdmin, self).get_inline_instances(request, obj)


# admin.site.register(UserAdmin)
# admin.site.register(User, UserAdmin)