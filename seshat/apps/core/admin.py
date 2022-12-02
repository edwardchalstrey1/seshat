from django.contrib import admin
from .models import Polity, Country, Section, Subsection, Citation, Reference, Variablehierarchy, SeshatComment, SeshatCommentPart, Nga, Ngapolityrel, Capital


admin.site.register(Section)
admin.site.register(Subsection)
admin.site.register(Variablehierarchy)
admin.site.register(Polity)
admin.site.register(Country)
admin.site.register(Citation)
admin.site.register(Reference)
admin.site.register(SeshatComment)
admin.site.register(SeshatCommentPart)
admin.site.register(Nga)
admin.site.register(Ngapolityrel)
admin.site.register(Capital)






# class CustomUserAdmin(UserAdmin):
#     inlines = (ProfileInline, )

#     list_display = ('username', 'email', 'first_name',
#                     'last_name', 'is_staff', 'get_location')
#     list_select_related = ('profile', )

#     def get_location(self, instance):
#         return instance.profile.location
#     get_location.short_description = 'Location'

#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             return list()
#         return super(CustomUserAdmin, self).get_inline_instances(request, obj)


# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)
