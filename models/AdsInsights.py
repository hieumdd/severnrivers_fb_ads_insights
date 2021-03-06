from models.models import FacebookAdsInsights


class AdsInsights(FacebookAdsInsights):
    keys = {
        "p_key": [
            "date_start",
            "date_stop",
            "account_id",
            "campaign_id",
            "adset_id",
            "ad_id",
        ],
        "incre_key": "_batched_at",
    }

    fields = [
        "date_start",
        "date_stop",
        "campaign_id",
        "adset_id",
        "ad_id",
        "campaign_name",
        "adset_name",
        "ad_name",
        "reach",
        "impressions",
        "cpc",
        "cpm",
        "frequency",
        "spend",
        "actions",
        "action_values",
        "conversions",
        "conversion_values",
        "cost_per_action_type",
        "purchase_roas",
    ]

    breakdowns = None

    schema = [
        {"name": "account_id", "type": "INTEGER"},
        {"name": "date_start", "type": "DATE"},
        {"name": "date_stop", "type": "DATE"},
        {"name": "campaign_id", "type": "INTEGER"},
        {"name": "adset_id", "type": "INTEGER"},
        {"name": "ad_id", "type": "INTEGER"},
        {"name": "campaign_name", "type": "STRING"},
        {"name": "adset_name", "type": "STRING"},
        {"name": "ad_name", "type": "STRING"},
        {"name": "reach", "type": "INTEGER"},
        {"name": "impressions", "type": "INTEGER"},
        {"name": "cpc", "type": "FLOAT"},
        {"name": "cpm", "type": "FLOAT"},
        {"name": "frequency", "type": "FLOAT"},
        {"name": "spend", "type": "FLOAT"},
        {
            "name": "actions",
            "type": "record",
            "mode": "repeated",
            "fields": [
                {"name": "action_type", "type": "STRING"},
                {"name": "value", "type": "FLOAT"},
                {"name": "_1d_click", "type": "FLOAT"},
                {"name": "_7d_click", "type": "FLOAT"},
                {"name": "_28d_click", "type": "FLOAT"},
                {"name": "_1d_view", "type": "FLOAT"},
                {"name": "_7d_view", "type": "FLOAT"},
                {"name": "_28d_view", "type": "FLOAT"},
            ],
        },
        {
            "name": "action_values",
            "type": "record",
            "mode": "repeated",
            "fields": [
                {"name": "action_type", "type": "STRING"},
                {"name": "value", "type": "FLOAT"},
                {"name": "_1d_click", "type": "FLOAT"},
                {"name": "_7d_click", "type": "FLOAT"},
                {"name": "_28d_click", "type": "FLOAT"},
                {"name": "_1d_view", "type": "FLOAT"},
                {"name": "_7d_view", "type": "FLOAT"},
                {"name": "_28d_view", "type": "FLOAT"},
            ],
        },
        {
            "name": "conversions",
            "type": "record",
            "mode": "repeated",
            "fields": [
                {"name": "action_type", "type": "STRING"},
                {"name": "value", "type": "FLOAT"},
                {"name": "_1d_click", "type": "FLOAT"},
                {"name": "_7d_click", "type": "FLOAT"},
                {"name": "_28d_click", "type": "FLOAT"},
                {"name": "_1d_view", "type": "FLOAT"},
                {"name": "_7d_view", "type": "FLOAT"},
                {"name": "_28d_view", "type": "FLOAT"},
            ],
        },
        {
            "name": "conversion_values",
            "type": "record",
            "mode": "repeated",
            "fields": [
                {"name": "action_type", "type": "STRING"},
                {"name": "value", "type": "FLOAT"},
                {"name": "_1d_click", "type": "FLOAT"},
                {"name": "_7d_click", "type": "FLOAT"},
                {"name": "_28d_click", "type": "FLOAT"},
                {"name": "_1d_view", "type": "FLOAT"},
                {"name": "_7d_view", "type": "FLOAT"},
                {"name": "_28d_view", "type": "FLOAT"},
            ],
        },
        {
            "name": "cost_per_action_type",
            "type": "record",
            "mode": "repeated",
            "fields": [
                {"name": "action_type", "type": "STRING"},
                {"name": "value", "type": "FLOAT"},
                {"name": "_1d_click", "type": "FLOAT"},
                {"name": "_7d_click", "type": "FLOAT"},
                {"name": "_28d_click", "type": "FLOAT"},
                {"name": "_1d_view", "type": "FLOAT"},
                {"name": "_7d_view", "type": "FLOAT"},
                {"name": "_28d_view", "type": "FLOAT"},
            ],
        },
        {
            "name": "purchase_roas",
            "type": "record",
            "mode": "repeated",
            "fields": [
                {"name": "action_type", "type": "STRING"},
                {"name": "value", "type": "FLOAT"},
                {"name": "_1d_click", "type": "FLOAT"},
                {"name": "_7d_click", "type": "FLOAT"},
                {"name": "_28d_click", "type": "FLOAT"},
                {"name": "_1d_view", "type": "FLOAT"},
                {"name": "_7d_view", "type": "FLOAT"},
                {"name": "_28d_view", "type": "FLOAT"},
            ],
        },
        {"name": "_batched_at", "type": "TIMESTAMP"},
    ]

    def transform(self, rows):
        return [
            {
                "account_id": row["account_id"],
                "date_start": row["date_start"],
                "date_stop": row["date_stop"],
                "campaign_id": row["campaign_id"],
                "adset_id": row["adset_id"],
                "ad_id": row["ad_id"],
                "campaign_name": row["campaign_name"],
                "adset_name": row["adset_name"],
                "ad_name": row["ad_name"],
                "reach": row["reach"],
                "impressions": row["impressions"],
                "cpc": row.get("cpc"),
                "cpm": row.get("cpm"),
                "frequency": row["frequency"],
                "spend": row["spend"],
                "actions": [
                    {
                        "action_type": action.get("action_type"),
                        "value": action.get("value"),
                        "_1d_view": action.get("1d_view"),
                        "_1d_click": action.get("1d_click"),
                        "_7d_view": action.get("7d_view"),
                        "_7d_click": action.get("7d_click"),
                        "_28d_view": action.get("28d_view"),
                        "_28d_click": action.get("28d_click"),
                    }
                    for action in row["actions"]
                ]
                if row.get("actions", [])
                else [],
                "action_values": [
                    {
                        "action_type": action.get("action_type"),
                        "value": action.get("value"),
                        "_1d_view": action.get("1d_view"),
                        "_1d_click": action.get("1d_click"),
                        "_7d_view": action.get("7d_view"),
                        "_7d_click": action.get("7d_click"),
                        "_28d_view": action.get("28d_view"),
                        "_28d_click": action.get("28d_click"),
                    }
                    for action in row["action_values"]
                ]
                if row.get("action_values", [])
                else [],
                "conversions": [
                    {
                        "action_type": action.get("action_type"),
                        "value": action.get("value"),
                        "_1d_view": action.get("1d_view"),
                        "_1d_click": action.get("1d_click"),
                        "_7d_view": action.get("7d_view"),
                        "_7d_click": action.get("7d_click"),
                        "_28d_view": action.get("28d_view"),
                        "_28d_click": action.get("28d_click"),
                    }
                    for action in row["conversions"]
                ]
                if row.get("conversions", [])
                else [],
                "conversion_values": [
                    {
                        "action_type": action.get("action_type"),
                        "value": action.get("value"),
                        "_1d_view": action.get("1d_view"),
                        "_1d_click": action.get("1d_click"),
                        "_7d_view": action.get("7d_view"),
                        "_7d_click": action.get("7d_click"),
                        "_28d_view": action.get("28d_view"),
                        "_28d_click": action.get("28d_click"),
                    }
                    for action in row["conversion_values"]
                ]
                if row.get("conversion_values", [])
                else [],
                "cost_per_action_type": [
                    {
                        "action_type": action.get("action_type"),
                        "value": action.get("value"),
                        "_1d_view": action.get("1d_view"),
                        "_1d_click": action.get("1d_click"),
                        "_7d_view": action.get("7d_view"),
                        "_7d_click": action.get("7d_click"),
                        "_28d_view": action.get("28d_view"),
                        "_28d_click": action.get("28d_click"),
                    }
                    for action in row["cost_per_action_type"]
                ]
                if row.get("cost_per_action_type", [])
                else [],
                "purchase_roas": [
                    {
                        "action_type": action.get("action_type"),
                        "value": action.get("value"),
                        "_1d_view": action.get("1d_view"),
                        "_1d_click": action.get("1d_click"),
                        "_7d_view": action.get("7d_view"),
                        "_7d_click": action.get("7d_click"),
                        "_28d_view": action.get("28d_view"),
                        "_28d_click": action.get("28d_click"),
                    }
                    for action in row["purchase_roas"]
                ]
                if row.get("purchase_roas", [])
                else [],
            }
            for row in rows
        ]
