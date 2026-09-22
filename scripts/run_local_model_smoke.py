from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import time

from operator_compiler.experiments import build_conditions

TASKS = [
    ("boolean", "Evaluate: not ( True ) and ( True ). Answer only True or False.", "TEST", "Execute a defined check and compare observed and expected results.", "False"),
    ("arithmetic", "What is 17 * 23? Answer with only the integer.", "INFER", "Derive the result using explicit premises and rules.", "391"),
    ("constraint", "Return exactly the word cobalt in lowercase and nothing else.", "COMPILE", "Preserve quantifier, negation, scope, priority and authority.", "cobalt"),
]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model", required=True)
    p.add_argument("--output", required=True)
    args = p.parse_args()

    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    tok = AutoTokenizer.from_pretrained(args.model)
    model = AutoModelForCausalLM.from_pretrained(args.model, torch_dtype="auto")
    model.eval()
    rows = []
    for task_id, task, operator, contract, gold in TASKS:
        for condition in build_conditions(task, operator, contract):
            messages = [{"role": "user", "content": condition.prompt}]
            rendered = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
            inputs = tok(rendered, return_tensors="pt")
            t0 = time.time()
            with torch.no_grad():
                out = model.generate(**inputs, max_new_tokens=64, do_sample=False)
            generated = out[0][inputs["input_ids"].shape[1]:]
            text = tok.decode(generated, skip_special_tokens=True).strip()
            rows.append({
                "task_id": task_id,
                "operator": operator,
                "condition": condition.name,
                "model": args.model,
                "provider": "github_actions_local_transformers",
                "prompt_sha256": sha256(condition.prompt.encode()).hexdigest(),
                "response_sha256": sha256(text.encode()).hexdigest(),
                "text": text,
                "gold": gold,
                "exact": text == gold,
                "latency_seconds": round(time.time() - t0, 6),
            })
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r, sort_keys=True) + "\n" for r in rows))
    print(json.dumps({"rows": len(rows), "exact": sum(r["exact"] for r in rows), "output": str(path)}))


if __name__ == "__main__":
    main()
