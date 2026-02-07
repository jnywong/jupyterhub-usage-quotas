# JupyterHub Usage Quotas

This library implements enforcement of compute usage quotas for Jupyter servers at server startup-time to manage resource consumption across shared infrastructure managed by [Zero to JupyterHub with Kubernetes](https://z2jh.jupyter.org/en/stable/) deployments.

## Features

- Metric based accounting for compute usage with Prometheus
- Flexible and declarative usage policies, such as quota sizes and quota time windows
- Server startup-time enforcement

## Installation

📦 Packaged helm charts for this project can be found at [https://2i2c.org/jupyterhub-usage-quotas/](https://2i2c.org/jupyterhub-usage-quotas/) 📦

This project is designed to be compatible with Zero to JupyterHub distributions, making it easy to deploy in the cloud with Kubernetes.

Add this project as a subchart of the z2jh `Chart.yaml` file with

```yaml
dependencies:
  - name: jupyterhub-usage-quotas
    version: "<version-number>"
    repository: "https://2i2c.org/jupyterhub-usage-quotas/"
    condition: jupyterhub-usage-quotas.enabled
```

In the values file, enable the usage quotas chart for your Kubernetes cluster:

```yaml
jupyterhub-usage-quotas:
  enabled: true
```

## Documentation

Documentation can be found at [https://jupyterhub-usage-quotas.readthedocs.io/en/latest/](https://jupyterhub-usage-quotas.readthedocs.io/en/latest/)

## Contributing

See the guidance in [CONTRIBUTING](CONTRIBUTING.md)

## License

This project is licensed under the [BSD 3-Clause License](LICENSE.md).
