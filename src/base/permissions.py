from rest_framework import permissions


class IsAuthor(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
