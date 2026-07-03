from services.memory import MemoryManager

memory = MemoryManager()

memory.add_message(
    "researcher",
    "user",
    "Explain quantum computing."
)

memory.add_message(
    "researcher",
    "assistant",
    "Quantum computing uses qubits..."
)

memory.add_message(
    "code_reviewer",
    "user",
    "Review my Python project."
)

print("=" * 40)
print("Research History")
print("=" * 40)

for message in memory.get_history("researcher"):
    print(message)

print()

print("=" * 40)
print("Code Reviewer History")
print("=" * 40)

for message in memory.get_history("code_reviewer"):
    print(message)