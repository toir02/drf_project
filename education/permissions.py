from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderators').exists()

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
