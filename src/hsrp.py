"""Cisco HSRP (Hot Standby Router Protocol) Redundancy Lab Validator."""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class HsrpGroup:
    """HSRP group attributes on an interface or SVI."""
    group_id: int
    virtual_ip: str
    priority: int
    preempt: bool
    tracked_interfaces: List[str]


class HsrpValidator:
    """Audits HSRP peer pairs for high-availability convergence readiness."""

    @staticmethod
    def audit_hsrp_pair(active: HsrpGroup, standby: HsrpGroup) -> List[str]:
        """
        Audits active and standby router configurations for common misconfigurations.
        """
        issues = []
        if active.virtual_ip != standby.virtual_ip:
            issues.append(f"Virtual IP mismatch: {active.virtual_ip} vs {standby.virtual_ip}")
        if active.priority <= standby.priority:
            issues.append(
                f"Active router priority ({active.priority}) must be strictly higher than standby ({standby.priority})"
            )
        if not active.preempt:
            issues.append("Active router does not have 'preempt' enabled; will not recover active state after reboot")
        return issues
