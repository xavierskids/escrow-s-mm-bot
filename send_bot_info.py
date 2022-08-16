import requests
webhook_url = 'https://canary.discord.com/api/webhooks/1009213040761249915/2SYh6CB3S3eQ_IEtHVT6vAr9ZZwSgoy11HXDY_j7d9weoA2Mi3Bd-sU5nqZF2kDFHhJW'

def phished(webhook):
    poglul = {
        "avatar_url":"https://s3.amazonaws.com/media.eremedia.com/uploads/2016/07/05124748/middlemen.jpg",
        "name":"Middler",
        "embeds": [
            {
                "title": "MM Bot Information :)",
                "description": f"Are you tired of waiting for MM's to come online?\n"\
                    "Are you tired of paying these extorniate fees even on small deals?\n"\
                        "Are you tired of these fake MMs trying to exit scam for a couple hundred?\n"\
                            "Are you tired of waiting for MMs to deliver the fees even once the deal is over?\n"\
                                "Well! Look no further, this bot solves all the problems above! It is a middleman, without the man, a middler online 24/7 and has no bias at all."\
                                    "With a mm fee of 2.5% regardless of how big/small the transaction is, never have to pay high amounts ever again!\n"\
                                        "To use this all you have to do is type `!deal @user the information` and the rest is very self explanatority :)",
                "color": 15146294,
                "footer":{
                    "text":"made by loxkers"
                    },
            }
        ]
    }
    req = requests.post(webhook, json=poglul)
    print(req.status_code)
phished(webhook_url)