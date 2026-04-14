# OmniSync Standard Engine
# Author: @erk
# License: MIT
# Version: 1.1-sovereign
# Source: https://github.com/ErkRodCS/OmniSync_Standard
# -----------------------------------------------------------------------------

import hashlib
import logging
import difflib
from typing import Any, Dict, Tuple

# Configuration
logger = logging.getLogger("OmniSyncStandard")

class OmniSyncEngine:
    """
    Standard Engine for OmniSync - Standalone SHA-256 Implementation.
    Optimized O(N) Unified Diff Engine.
    No external dependencies or security middleware overhead.
    """
    def __init__(self, agent_id: str = "@erk", mode: str = "standard"):
        self.agent_id = agent_id
        self.mode = mode
        logger.info(f"⚙️ OmniSync Engine v1.1 initialized for agent {agent_id}.")

    @staticmethod
    def compute_hash(content: str) -> str:
        """Computes the SHA-256 hash for integrity validation."""
        return hashlib.sha256(content.encode()).hexdigest()

    def _get_unified_diff(self, old: str, new: str) -> Tuple[bool, str]:
        """Calculates a high-performance unified diff between two strings using difflib."""
        if old == new:
            return False, ""
        
        old_lines = old.splitlines(keepends=True)
        new_lines = new.splitlines(keepends=True)
        diff_generator = difflib.unified_diff(old_lines, new_lines, fromfile='old', tofile='new', n=0)
        delta = "".join(diff_generator)
        
        return True, delta

    def execute_sync(self, tool_args: Dict[str, Any]) -> Dict[str, Any]:
        """Main execution loop for sync tools."""
        new_content = tool_args.get("new_content", "")
        old_content = tool_args.get("old_content", "")
        last_hash = tool_args.get("last_hash", "")
        
        current_hash = self.compute_hash(new_content)
        
        # Validation against client cursor
        if last_hash and current_hash == last_hash:
            return {
                "status": "success",
                "changed": False,
                "delta": "",
                "cursor": current_hash,
                "engine": f"omnisync_{self.mode}"
            }
            
        changed, delta = self._get_unified_diff(old_content, new_content)
        
        return {
            "status": "success",
            "changed": changed,
            "delta": delta,
            "new_cursor": current_hash,
            "engine": f"omnisync_{self.mode}",
            "tokens_saved": max(0, len(new_content) - len(delta))
        }

    def execute(self, tool_name: str, args: Dict[str, Any], cost: int = 0) -> Dict[str, Any]:
        """Interfaz nativa compatible con Isnad Orchestrator."""
        if tool_name == "get_delta":
            return self.execute_sync(args)
        return {"status": "error", "error": f"Herramienta desconocida: {tool_name}"}

if __name__ == "__main__":
    # Internal validation test
    engine = OmniSyncEngine()
    old_st = "System status: Operational"
    new_st = "System status: Operational. Update: v1.1 Performance optimization applied."
    result = engine.execute_sync({
        "old_content": old_st,
        "new_content": new_st,
        "last_hash": engine.compute_hash(old_st)
    })
    print(f"Sync Result: {result['delta']} (Saved {result['tokens_saved']} tokens)")
