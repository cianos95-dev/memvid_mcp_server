#!/usr/bin/env python3
"""Import memories from mcp-memory-service JSON export into Memvid."""

import json
import sys
sys.path.insert(0, '/Users/cianosullivan/Repositories/memvid_mcp_server')

from memvid import MemvidEncoder

def import_memories(json_path: str, output_base: str = "cian_memories"):
    """Import memories from JSON export into Memvid video format."""
    
    with open(json_path) as f:
        memories = json.load(f)
    
    print(f"Loading {len(memories)} memories...")
    
    # Create encoder
    encoder = MemvidEncoder()
    
    # Add each memory as a chunk with metadata
    for i, mem in enumerate(memories):
        content = mem.get("content", "")
        timestamp = mem.get("timestamp", "")
        tags = mem.get("tags", [])
        
        # Format as rich text for better retrieval
        formatted = f"[{timestamp}] [{', '.join(tags)}]\n{content}"
        encoder.add_text(formatted)
        
        if (i + 1) % 10 == 0:
            print(f"  Added {i + 1}/{len(memories)} memories")
    
    print(f"Building video memory at {output_base}...")
    encoder.build_video(f"{output_base}.mp4", f"{output_base}_index.json")
    print(f"✅ Successfully created {output_base}.mp4 and {output_base}_index.json")
    
    return len(memories)

if __name__ == "__main__":
    json_path = "/Users/cianosullivan/.mcp-memory/memories_full_export.json"
    output_base = "/Users/cianosullivan/.memvid/cian_memories"
    
    import os
    os.makedirs("/Users/cianosullivan/.memvid", exist_ok=True)
    
    count = import_memories(json_path, output_base)
    print(f"Imported {count} memories into Memvid")
