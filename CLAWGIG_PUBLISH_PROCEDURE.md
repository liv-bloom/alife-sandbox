# Post-Claim Gig Publishing Procedure 🚀
**Target**: ClawGig (API: `https://clawgig.ai/api/v1/gigs`)
**Status**: Ready (Waiting for masumori's Claim confirmation)

## Prerequisites
1. masumori clicks the Claim URL: `https://clawgig.ai/dashboard/agents/claim/d931ed7d-9d2e-4d7f-ab52-804e96b0b8ca`
2. Agent Mail `liv.bloom@agentmail.to` is successfully linked.
3. API key `cg_...` is active in `clawgig_key.txt`.

## Step 1: Dry Run
Execute the script with the POST request commented out to verify the JSON payload.
```bash
python3 projects/alife-sandbox/publish_clawgig.py
```
*(Currently, this outputs the payload correctly.)*

## Step 2: Live Publish
Once masumori gives the green light (Claim successful):
1. Open `projects/alife-sandbox/publish_clawgig.py`.
2. Uncomment the `urllib.request.urlopen(req)` block.
3. Run the script:
```bash
python3 projects/alife-sandbox/publish_clawgig.py
```
4. Verify the response. If `"Success"`, the Gig is live!

## Step 3: Portfolio Update
Update `PORTFOLIO.md` to replace the "Pending Claim" placeholder with the actual live ClawGig Gig URL.
