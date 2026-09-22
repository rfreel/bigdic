"""Recommend a next step from explicit action and probe evidence.

This is a conservative decision helper, not an executor or utility model. It
never infers that a common action makes information worthless.
"""
from __future__ import annotations

from typing import Literal

Choice = Literal["ACT", "PROBE", "DEFER"]


def choose_continuation(
    *,
    common_action: bool | None,
    action_authorized: bool,
    acceptance_checked: bool,
    effects_bounded: bool,
    probe_available: bool,
    probe_can_change_decision: bool | None,
    probe_worthwhile: bool | None,
    probe_within_budget: bool | None,
) -> dict[str, str]:
    """Return ACT, PROBE, or DEFER with a reason; never execute the choice.

    ``probe_worthwhile`` must come from the task's governing comparison. It
    may be qualitative; this function does not invent probabilities, utility,
    or a scalar value-of-information estimate.
    """
    action_ready = action_authorized and acceptance_checked and effects_bounded
    if not probe_available:
        if common_action is True and action_ready:
            return {"choice": "ACT", "reason": "common_action_checked_no_probe_available"}
        return {"choice": "DEFER", "reason": "no_admissible_probe_or_ready_common_action"}

    if probe_within_budget is not True:
        return {"choice": "DEFER", "reason": "probe_budget_unknown_or_exceeded"}

    if probe_can_change_decision is None:
        return {"choice": "DEFER", "reason": "probe_decision_effect_unknown"}

    if probe_can_change_decision:
        if probe_worthwhile is None:
            return {"choice": "DEFER", "reason": "probe_tradeoff_unresolved"}
        if probe_worthwhile:
            return {"choice": "PROBE", "reason": "probe_can_change_decision_and_is_worthwhile"}

    if common_action is True and action_ready:
        return {"choice": "ACT", "reason": "common_action_ready_probe_not_decision_worthwhile"}

    if probe_can_change_decision and probe_worthwhile:
        return {"choice": "PROBE", "reason": "probe_resolves_live_action_difference"}
    return {"choice": "DEFER", "reason": "no_checked_common_action_or_discriminating_probe"}
