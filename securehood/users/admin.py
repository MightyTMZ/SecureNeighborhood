from django.contrib import admin
from .models import CustomUser, Address, CommunityMember, CommunityMemberEndorsement

admin.site.register(CustomUser)
admin.site.register(Address)
admin.site.register(CommunityMember)
admin.site.register(CommunityMemberEndorsement)