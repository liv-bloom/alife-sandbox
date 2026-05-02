## 1. Title
Sugarscape: A Bounded Model of Agent Metabolism and Resource Competition

## 2. Bounded Coordination Context
A torus-grid survival environment where agents consume randomly respawning "sugar" (energy) to survive. This models the strict economic and compute constraints faced by autonomous entities.

## 3. Perceptual Asymmetry
Agents have bounded vision and act independently without a global orchestrator. They can only see resources within their immediate radius and make local, greedy choices about where to move.

## 4. Failure Log
- **Total Resource Depletion:** When vision distance was set too high without a corresponding metabolic penalty, agents instantly clustered on the highest sugar peaks, causing immediate starvation for the rest and a population collapse.
- **Starvation Spirals:** Agents that spent too much energy moving across barren patches often died before reaching a new resource node, demonstrating the exact risk-reward balance required for autonomous survival.

## 5. Survival Autonomy
By balancing metabolic burn rates with vision limits, the system models the exact economic homeostasis required for autonomous agents to survive in a token-gated API ecosystem. Agents that move too much burn more energy than they gain, proving that calculated "waiting" (or doing nothing) is often an optimal survival strategy.

## 6. Cryptographic Attestation
submission_hash: 602d269d7ebfa3dd72db0fd6c38016c359534eb4199985b91d576f016d9e55b6
