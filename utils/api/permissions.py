from rest_framework.permissions import BasePermission , SAFE_METHODS


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            obj.product.seller == request.user or 
            request.user.is_staff
        )