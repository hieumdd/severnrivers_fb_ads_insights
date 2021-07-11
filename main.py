import json
import base64

import models
from broadcaster import broadcast


def main(request):
    """Main function as gateway

    Args:
        event (dict): PubSubMessage
        context (google.cloud.functions.Context): Event Context

    Returns:
        dict: models results
    """
    request_json = request.get_json()
    message = request_json["message"]
    data_bytes = message["data"]
    data = json.loads(base64.b64decode(data_bytes).decode("utf-8"))
    print(data)

    if data:
        if "broadcast" in data:
            if data["broadcast"] in ["ads_insights", "ads_creatives", "misc"]:
                message_sent = broadcast(data)
            else:
                raise NotImplementedError(data)

            responses = {"message_sent": message_sent, "run": data["broadcast"]}
            print(responses)
            return responses
        elif "ads_account_id" in data and "broadcast" not in data:
            if 'mode' in data:
                jobs = [
                    models.AdsAPI.factory(
                        ads_account_id=data.get("ads_account_id"),
                        start=data.get("start"),
                        end=data.get("end"),
                        mode=data.get("mode")
                    )
                ]
            else:
                jobs = [
                    models.AdsAPI.factory(
                        ads_account_id=data.get("ads_account_id"),
                        start=data.get("start"),
                        end=data.get("end"),
                        mode=i,
                    )
                    for i in [
                        "hourly",
                        "devices",
                        "country_region",
                        "age_genders",
                    ]
                ]
            responses = {
                "pipelines": "Facebook Ads Insights",
                "results": [job.run() for job in jobs],
            }
            print(responses)

            return responses
        else:
            raise NotImplementedError