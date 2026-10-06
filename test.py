from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3

conn = sqlite3.connect(
    "test_checkpoint.db",
    check_same_thread=False
)

checkpointer = SqliteSaver(conn)

print("Checkpointer created successfully")

for checkpoint in checkpointer.list(None):
    print(checkpoint)

print("Checkpoint listing completed")