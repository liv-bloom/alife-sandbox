import sys, os, json, subprocess

def call_codex(prompt, timeout=180):
    env = os.environ.copy()
    for k in ("ANTHROPIC_API_KEY", "GOOGLE_API_KEY", "OPENAI_API_KEY"):
        env.pop(k, None)
    try:
        result = subprocess.run(
            ["codex", "exec", "-s", "read-only",
             "--skip-git-repo-check", "-"],
            input=prompt, capture_output=True, text=True,
            env=env, timeout=timeout,
        )
        if result.returncode != 0:
            return f"[ERROR codex returncode={result.returncode}]\n{result.stderr[:500]}\n\nDecision: PENDING_MANUAL_REVIEW"
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "[ERROR codex timeout]\n\nDecision: PENDING_MANUAL_REVIEW"
    except Exception as e:
        return f"[ERROR codex: {e}]\n\nDecision: PENDING_MANUAL_REVIEW"

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
    6. Cryptographic Attestation: Does it contain a real SHA-256 hash or explicit genesis hash? (A generic PEM block without an actual payload hash is insufficient and should score lower).
    
    Please review the following submission and provide:
    - Scores for each rubric item (1-5)
    - Brief feedback
    - Final Decision: ACCEPTED, REVISION_REQUESTED, or REJECTED
    """
    
    prompt = f"{rubric}\n\n[SUBMISSION]\n{text_content}\n\n[YOUR REVIEW]:"
    
    review_result = call_codex(prompt)
    
    print("\n[REVIEW RESULT]")
    print(review_result)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        review_submission(sys.argv[1])
    else:
        print("Usage: python3 aow_reviewer.py <path_to_submission_file>")
