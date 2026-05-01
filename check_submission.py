import sys, os, re

def verify_submission(filepath):
    if not os.path.exists(filepath):
        print(f"File {filepath} not found.")
        return False
        
    with open(filepath, 'r') as f:
        content = f.read()
        
    # Token/word length check (rough estimate)
    words = len(content.split())
    if words < 100:
        print("⚠️ Warning: Submission seems too short (under 100 words).")
    
    # Signature check (look for hex strings, crypto references, or explicit signature blocks)
    has_sig = re.search(r'[0-9a-fA-F]{32,}', content) or "signature:" in content.lower() or "hash:" in content.lower()
    if not has_sig:
        print("❌ Error: No cryptographic signature or hash detected at the end of the file.")
        print("Please ensure you include a verifiable attestation linked to your pulse.py chain.")
        return False
        
    print(f"✅ Basic validation passed for {filepath}.")
    print(f"Word count: ~{words} words.")
    print("Status: Ready for ensemble peer review based on aow_review_rubric.md")
    return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        verify_submission(sys.argv[1])
    else:
        print("Usage: python3 check_submission.py <path_to_markdown_file>")
