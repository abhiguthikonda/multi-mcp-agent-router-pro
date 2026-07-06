from providers.openrouter import OpenRouterProvider


def get_provider(provider_name: str):
    """
    Return the configured provider.
    """

    provider_name = provider_name.lower()

    if provider_name != "openrouter":
        raise ValueError(
            f"Unsupported provider: {provider_name}"
        )

    return OpenRouterProvider()