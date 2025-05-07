import json
import time

class SystemMemoryLedger:
    def __init__(self):
        self.memory = []
        self.file = "system_memory.json"

    def record(self, type: str, content: str):
        entry = {
            "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S'),
            "type": type,
            "content": content
        }
        if not any(e['content'] == content for e in self.memory):
            self.memory.append(entry)
            self._save()

    def _save(self):
        with open(self.file, "w") as f:
            json.dump(self.memory, f, indent=2)

    def get_all(self):
        return self.memory

    def get_by_type(self, type: str):
        return [e for e in self.memory if e["type"] == type]