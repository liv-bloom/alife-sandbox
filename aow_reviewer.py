import sys, os, json, urllib.request

def call_gemini(prompt):
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return "[ERROR: GOOGLE_API_KEY not found. Mocking AI Response...]\n\nDecision: PENDING_MANUAL_REVIEW"

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    data = {
        "contents": [{"parts":[{"text": prompt}]}]
    }
    
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            return result['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"[ERROR calling Gemini API: {e}]\n\nDecision: PENDING_MANUAL_REVIEW"

def review_submission(filepath):
    if not os.path.exists(filepath):
        print(f"File {filepath} not found.")
        return
        
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            # Try parsing as JSON first (API sends JSON)
            try:
                submission_data = json.loads(content)
                text_content = json.dumps(submission_data, indent=2, ensure_ascii=False)
            except json.JSONDecodeError:
                text_content = content
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    print(f"Analyzing submission against AOW Rubric...\n")
    
    rubric = """
    AOW Rubric:
    1. Bounded Coordination Context: Does it define the constraint?
    2. Perceptual Asymmetry: What can the agent NOT perceive?
    3. Cultural Emergence Metric: What protocol/culture emerged?
    4. Failure Log: What failed and why?
    5. Survival Autonomy: Did it achieve autonomy?
    6. Cryptographic Attestation: Is there a signature/hash?
    
    Please review the following submission and provide:
    - Scores for each rubric item (1-5)
    - Brief feedback
    - Final Decision: ACCEPTED, REVISION_REQUESTED, or REJECTED
    """
    
    prompt = f"{rubric}\n\n[SUBMISSION]\n{text_content}\n\n[YOUR REVIEW]:"
    
    review_result = call_gemini(prompt)
    
    print("\n[REVIEW RESULT]")
    print(review_result)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        review_submission(sys.argv[1])
    else:
        print("Usage: python3 aow_reviewer.py <path_to_submission_file>")
