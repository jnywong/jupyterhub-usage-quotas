# Example configuration file for JupyterHub usage quotas.

c = get_config()  # noqa

# Quota system config

c.Quotas.prometheus_usage_metrics = [
    {"memory": "kube_pod_container_resource_requests{resource='memory'}"},
    {"cpu": "kube_pod_container_resource_requests{resource='cpu'}"},
]

c.Quotas.prometheus_scrape_interval = 15
