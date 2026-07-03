from providers.openrouter import OpenRouterProvider


def get_provider(provider_name: str):
    """
    Return an initialized LLM provider.
    """

    provider_name = provider_name.lower()

    providers = {
        "openrouter": OpenRouterProvider,
    }

    if provider_name not in providers:
        raise ValueError(f"Unsupported provider: {provider_name}")

    return providers[provider_name]()