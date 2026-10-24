import json, sys
from client import AdaptiveSemanticChunkingRouterClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "semantic-chunking-router", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "chunk_document_semantically", "description": "Partitions unstructured documents into coherence-bounded RAG semantic chunks."}]}}
    elif method == "tools/call":
        client = AdaptiveSemanticChunkingRouterClient()
        res = client.chunk_document_semantically()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = AdaptiveSemanticChunkingRouterClient()
        print(json.dumps(client.chunk_document_semantically(), indent=2))
