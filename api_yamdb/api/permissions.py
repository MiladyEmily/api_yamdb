from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Проверяет, является ли пользователь админом или суперюзером.
    """
    def has_permission(self, request, view):
        is_safe = request.method in permissions.SAFE_METHODS
        if is_safe:
            return True
        if request.user.is_anonymous:
            return False
        return user_check(request.user)


class IsUserAuthorOrModeratorOrReadOnly(permissions.BasePermission):
    """
    Проверяет, является ли пользователь автором поста или модератором.
    """

    def has_object_permission(self, request, view, obj):
        is_safe = request.method in permissions.SAFE_METHODS
        if is_safe:
            return True
        if request.user.is_anonymous:
            return False
        if request.user.role == "moderator":
            return True
        if obj.author == request.user:
            return True
        return False


class UsersMePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return True


class IsAdminOrNoPermission(permissions.BasePermission):
    """
    Проверяет, является ли пользователь админом.
    """
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.role == "admin":
            return True
        return False


class AuthorOrModeratorReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):

        return (
            request.method in permissions.SAFE_METHODS # если метод безопасный, то можно вообще всем
            or (
                request.user.is_authenticated # доступ только для аутентифицированных, про неё подробнее напишу ниже
                and (
                    obj.author==request.user # своё можно редачить автору
                    or request.user.is_superuser # или суперюзеру
                    or request.user.role=='admin' #админу тоже можно
                    or request.user.role=='moderator' # и модератору
                )
            )
        )


class AuthorAndStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or (
                request.user.is_authenticated
                and (
                    obj.author == request.user
                    or request.user.is_moderator
                    or request.user.is_admin
                )
            )
        )
        return user_check(request.user)


def user_check(user):
    if user.is_anonymous:
        return False
    is_superuser = user.is_superuser
    is_admin = user.role == 'admin'
    return is_superuser or is_admin
