ALERTS = {
    "high_cpu_usage": {
        "payload": {
            "title": "High CPU Usage",
            "type": "metric alert",
            "query": "avg(last_5m):avg:system.cpu.user{*} by {host} > 90",
            "message": "CPU usage is over 90% on {{host.name}}.",
            "description": "CPU usage is over 90% on {{host.name}}.",
            "tags": "environment:production, team:backend",
            "priority": "P3",
            "monitor_id": "1234567890",
            "scopes": [],
        },
        "parameters": {
            "tags": [
                "environment:production,team:backend,monitor,service:api",
                "environment:staging,team:backend,monitor,service:api",
            ],
            "priority": ["P2", "P3", "P4"],
            "scopes": [
                "srv1-us1-prod",
                "srv2-us1-prod",
                "srv1-eu1-prod",
                "srv3-us1-prod",
                "srv2-eu1-prod",
                "srv1-ap1-prod",
                "srv2-ap1-prod",
                "srv1-us2-prod",
            ],
        },
        "renders": {
            "host.name": [
                "srv1-us1-prod",
                "srv2-us1-prod",
                "srv1-eu1-prod",
                "srv3-us1-prod",
                "srv2-eu1-prod",
                "srv1-ap1-prod",
                "srv2-ap1-prod",
                "srv1-us2-prod",
            ],
        },
    },
    "low_disk_space": {
        "payload": {
            "title": "Low Disk Space",
            "type": "metric alert",
            "query": "avg(last_1h):min:system.disk.free{*} by {host} < 20",
            "message": "Disk space is below 20% on {{host.name}}.",
            "description": "Disk space is below 20% on {{host.name}}.",
            "tags": "environment:production,team:database",
            "priority": 4,
            "monitor_id": "1234567891",
            "scopes": [],
        },
        "parameters": {
            "tags": [
                "environment:production,team:analytics,monitor,service:api",
                "environment:staging,team:database,monitor,service:api",
            ],
            "priority": ["P1", "P3", "P4"],
            "scopes": [
                "srv1-us1-prod",
                "srv2-us1-prod",
                "srv1-eu1-prod",
                "srv3-us1-prod",
                "srv2-eu1-prod",
                "srv1-ap1-prod",
                "srv2-ap1-prod",
                "srv1-us2-prod",
            ],
        },
        "renders": {
            "host.name": [
                "srv1-us1-prod",
                "srv2-us1-prod",
                "srv1-eu1-prod",
                "srv3-us1-prod",
                "srv2-eu1-prod",
                "srv1-ap1-prod",
                "srv2-ap1-prod",
                "srv1-us2-prod",
            ],
        },
    },
    "mq_consumer_struggling": {
        "payload": {
            "title": "MQ Consumer Is Struggling",
            "type": "metric alert",
            "query": "avg(last_1h):min:mq_processing{*} by {host} < 10",
            "message": "MQ Consumer is processing less than 10 messages per second on {{host.name}}.",
            "description": "MQ Consumer is processing less than 10 messages per second on {{host.name}}.",
            "tags": "environment:production,team:database",
            "priority": 4,
            "monitor_id": "1234567891",
            "scopes": [],
        },
        "parameters": {
            "tags": [
                "environment:production,team:analytics,monitor,service:api",
                "environment:staging,team:database,monitor,service:api",
            ],
            "priority": ["P1", "P3", "P4"],
            "scopes": ["mq-us1-prod", "mq-eu1-prod", "mq-ap1-prod", "mq-us2-prod"],
        },
        "renders": {
            "host.name": [
                "srv1-us1-prod",
                "srv2-us1-prod",
                "srv1-eu1-prod",
                "srv3-us1-prod",
                "srv2-eu1-prod",
                "srv1-ap1-prod",
                "srv2-ap1-prod",
                "srv1-us2-prod",
            ],
        },
    },
}