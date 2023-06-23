from flask_definitions import *


# Idk if this works but Dev crashes and Live not...
@app.route("/<game_version>/catalog", methods=["GET"])
def catalog_get(game_version):
    print("Game Version of Catalog: " + game_version)
    get_remote_ip()
    try:
        return jsonify({
   "data":{
      "Result":[
         {
            "Id":"69055D534DF27180C4B36CAB4B651054",
            "DisplayName":"Runner_GhostWeaponHeal001_DisplayName",
            "Purchasable":True,
            "Consumable":False,
            "IsWeapon":False,
            "InitialQuantity":1,
            "DefaultCost":[
               {
                  "CurrencyId":"CurrencyC",
                  "Price":250
               }],
               "EventCostList":[
                  {
                     "Name":"",
                     "StartDate":1656011734,
                     "EndDate":1684869334,
                     "Cost":[
                        {
                           "CurrencyId":"CurrencyC",
                           "Price":250
                        }
                     ]
                  }
               ],
               "MetaData":{
                  "GameplayTags":[
                     {
                        "TagName":"Weapon.ICR"
                     }
                  ],
                  "BundleItems":[
                        ""
                  ],
                  "RewardBundleItems":[
                        ""
                  ],
                  "RequiredChallengesToComplete":[
                        ""
                  ],
                  "BundlePartOf":"",
                  "PrerequisiteItem":"",
                  "FollowingItem":"A1C4E2FB4BC74EB560F431B210C5094C",
                  "BundleDiscountPercent":10,
                  "MinPlayerLevel":1,
                  "MinCharacterLevel":1,
                  "Origin":"None"
               },
               "Faction":"Runner",
               "GameplayTagContainer":{
                  "GameplayTags":[
                     {
                        "TagName":"Weapon.ICR"
                     }
                  ],
                  "ParentTags":[
                     {
                        "TagName":"Runner.Smoke"
                     }
                  ]
               },
               "CustomizationGameplayTagByFaction":[
                  "Runner",
                  {
                     "TagName":"Class.Runner"
                  }
               ],
               "Gender":"Male"
         }
      ]
   }
})
        #return jsonify({"data":[{"categories":["character"],"id":"Dwight","metaData":{"character":"0",
        #"hiddenIfNotOwned":False,"role":"Runner"},"nonSecure":False,"purchasable":False,"unique":True}]})

    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        print(e)


@app.errorhandler(404)
def debug_404(e):
    print("##################################################################################")
    print("DEBUG 404")
    print("##################################################################################")
    print('HTTP Headers:')
    for header in request.headers:
        print(f'{header[0]}: {header[1]}')

    print('Cookies:')
    for key, value in request.cookies.items():
        print(f'{key}: {value}')

    print('Endpoint: ', request.endpoint)
    print('Path: ', request.path)
    print('Method: ', request.method)

    if request.json:
        print('JSON Payload:')
        print(request.json)

    print("##################################################################################")
    return jsonify({"status": "error", "code": 404})
