import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import AdaptiveSemanticChunkingRouterClient

def main():
    client = AdaptiveSemanticChunkingRouterClient(target_chunk_words=45, overlap_words=10)
    res = client.chunk_document_semantically()
    print("=== Adaptive Semantic Chunking Router Output ===")
    print(f"Sentences: {res['total_sentences_processed']} -> Generated Chunks: {res['generated_chunks_count']}")
    print("\nSemantic Chunk Blocks:")
    for c in res['semantic_chunks']:
        print(f"  [{c['chunk_id']}] ({c['word_count']} words): {c['text'][:65]}...")

if __name__ == '__main__':
    main()
