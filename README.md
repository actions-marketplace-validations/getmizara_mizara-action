<p align="center">
  <a href="https://mizara.ai"><img src="assets/logo-banner.svg" width="340" alt="mizara"></a>
</p>

<p align="center"><a href="https://mizara.ai">mizara.ai</a></p>

<p align="center">
  <a href="https://github.com/getmizara/mizara-action/actions/workflows/self-test.yml"><img src="https://github.com/getmizara/mizara-action/actions/workflows/self-test.yml/badge.svg" alt="Self-test"></a>
  <a href="https://github.com/getmizara/mizara-python#cli"><img src="https://img.shields.io/pypi/v/mizara?color=3776ab&label=mizara" alt="mizara"></a>
  <a href="LICENSE.md"><img src="https://img.shields.io/badge/license-Apache%202.0-blue" alt="License"></a>
</p>

# Mizara Safety Test

GitHub Action wrapper for [`mizara test`](https://github.com/getmizara/mizara-python#cli) - runs your Mizara
policy against six common risk scenarios spanning infrastructure, external communication, and sensitive data,
and reports the result as a job summary.

## Usage

```yaml
- uses: getmizara/mizara-action@v1
  with:
    policy-path: policy.json
```

Fails the check if any scenario would be allowed through unprotected. See
[`examples/policy.json`](examples/policy.json) for a minimal policy, and
[`.github/workflows/self-test.yml`](.github/workflows/self-test.yml) for this repo running the action
against it.

## Inputs

| Input | Required | Default | Description |
| --- | --- | --- | --- |
| `policy-path` | yes | - | Path to the Mizara policy JSON file to test. |
| `mizara-version` | no | latest | Pin a specific `mizara` PyPI version instead of the latest release. |
| `python-version` | no | `3.x` | Python version to set up. |

## Outputs

| Output | Description |
| --- | --- |
| `result` | `pass` if every scenario was protected or default-denied, `fail` if any scenario would be allowed through. |

## What it checks

Each scenario is classified against your policy:

- **PROTECTED** - a rule you wrote explicitly matched and blocked it
- **DEFAULT-DENIED** - no rule matched; blocked only by the fail-closed default, not an intentional rule
- **FAIL** - the action would be allowed to proceed

See [`mizara test`](https://github.com/getmizara/mizara-python#cli) in the SDK repo for the full scenario
list and how coverage is evaluated.

## License

Apache-2.0
