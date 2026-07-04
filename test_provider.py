import asyncio

from providers.factory import get_provider


async def main():

    provider = get_provider("openrouter")

    print(provider.provider_name)

    print(hasattr(provider, "generate"))

    print(hasattr(provider, "generate_with_tools"))


asyncio.run(main())