from django.http import JsonResponse


TEXT_NOT_FOUND = JsonResponse({"unique_id": "not_found"}, status=404)
LANGUAGE_NOT_FOUND = JsonResponse({"language": "not_found"}, status=404)