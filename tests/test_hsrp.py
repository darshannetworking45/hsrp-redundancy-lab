import unittest
from src.hsrp import HsrpGroup, HsrpValidator

class TestHsrp(unittest.TestCase):
    def test_healthy_pair(self):
        g1 = HsrpGroup(group_id=1, virtual_ip="10.1.1.1", priority=110, preempt=True, tracked_interfaces=["Gi0/0"])
        g2 = HsrpGroup(group_id=1, virtual_ip="10.1.1.1", priority=100, preempt=False, tracked_interfaces=[])
        issues = HsrpValidator.audit_hsrp_pair(g1, g2)
        self.assertEqual(len(issues), 0)

    def test_flawed_pair(self):
        g1 = HsrpGroup(group_id=1, virtual_ip="10.1.1.1", priority=100, preempt=False, tracked_interfaces=[])
        g2 = HsrpGroup(group_id=1, virtual_ip="10.1.1.2", priority=105, preempt=True, tracked_interfaces=[])
        issues = HsrpValidator.audit_hsrp_pair(g1, g2)
        self.assertGreaterEqual(len(issues), 2)

if __name__ == "__main__":
    unittest.main()
