from rest_framework import permissions
from users.helpers import Roles
class IsCompanyAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == Roles.COMPANY_ADMIN:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)
    
class IsOfficeAdmin(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.user.role == Roles.OFFICE_ADMIN and obj.office == request.user.office and obj.company == request.user.company:
            return True
        return False
        # return super().has_object_permission(request, view, obj)


class IsTeamAdmin(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.user.role == Roles.TEAM_ADMIN and obj.team == request.user.team and obj.office == request.user.office and obj.company == request.user.company:
            return True
        return False
    