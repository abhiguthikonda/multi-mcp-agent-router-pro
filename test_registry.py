from agents import registry

print("Available Agents")
print("-" * 30)

for agent in registry.all():
    print(
        f"{agent.icon} {agent.name}"
    )

print()

print("Research Agent")

research = registry.get("researcher")

print(research.name)
print(research.supports_tools())