# Cisco HSRP Pair Validator

Checks a supplied active/standby HSRP pair for virtual IP, priority, preemption, and tracked-interface consistency.

## Main entry points

- `src.hsrp.HsrpGroup`
- `src.hsrp.HsrpValidator` (`audit_hsrp_pair`)

## Run the tests

```bash
python -m unittest discover -s tests -v
```

The project uses the Python standard library; no third-party package is required.

## Scope

The check uses the two HSRP records provided by the caller. It does not discover HSRP peers or confirm live forwarding state.
