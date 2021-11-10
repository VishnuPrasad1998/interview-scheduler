from rest_framework.response import Response
from rest_framework import status

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return Response({"detail": "You are not authorized to view this endpoint"}, status=status.HTTP_403_FORBIDDEN)
		return wrapper_func
	return decorator

