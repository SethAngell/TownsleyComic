import os

def get_feature_version() -> str:
    return os.getenv('SEMANTIC_VERSION', 'v0.0.0')

class SemanticVersionProvider:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.SEMVER = get_feature_version()

        return self.get_response(request)
