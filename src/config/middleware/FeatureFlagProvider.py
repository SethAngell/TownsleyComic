import cachetools.func
from config.models import FeatureFlag
from townsley.settings import DEBUG

CACHE_TTL = 10 if DEBUG else (60 * 30)


FEATURE_FLAGS_FRONTEND_CONTENT_MANAGEMENT = "FRONTEND_CONTENT_MANAGEMENT"
FEATURE_FLAGS = [FEATURE_FLAGS_FRONTEND_CONTENT_MANAGEMENT]


@cachetools.func.ttl_cache(maxsize=32, ttl=CACHE_TTL)
def get_feature_flag(flag: str) -> bool:
    try:
        return FeatureFlag.objects.get(key=flag).value

    except FeatureFlag.DoesNotExist:
        return False


class FeatureFlagProvider:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.FF_FRONTEND_CONTENT_MANAGEMENT = get_feature_flag(
            FEATURE_FLAGS_FRONTEND_CONTENT_MANAGEMENT
        )

        return self.get_response(request)
