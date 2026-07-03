from routers.keyword_router import KeywordRouter

router = KeywordRouter()

tests = [
    "Review my GitHub repository",
    "Find SQL injection vulnerabilities",
    "Explain quantum computing",
    "Help me with my Revit project",
]

print("=" * 50)
print("Testing Keyword Router")
print("=" * 50)

for prompt in tests:
    agent = router.route(prompt)

    print(f"\nPrompt : {prompt}")
    print(f"Selected Agent : {agent.name}")