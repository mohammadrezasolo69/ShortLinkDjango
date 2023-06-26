from rest_framework import permissions


class IsUser(permissions.BasePermission):
    """
    This class checks whether the logged in user is the same as
    the user who created the link
    """

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return bool(
                request.user.is_authenticated and
                (obj.user == request.user)
            )
