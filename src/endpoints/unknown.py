from flask_definitions import *


# Do NOT change Result to ANYTHING or Add anything before it. Game will crash. Doesnt mean it 100% works tho XD
@app.route("/<game_version>/catalog", methods=["GET"])
def catalog_get(game_version):
    print("Game Version of Catalog: " + game_version)
    get_remote_ip()
    try:
        return jsonify({
      "Result":[
         {
            "Id":"0638DA474500E76780093DB64058A4AA",
            "DisplayName":"Scavenger_SMOKE_Outfit_STR001_Bloodbeige_NAME",
            "Purchasable":True,
            "Consumable":False,
            "IsWeapon":False,
            "InitialQuantity":1,
            "DefaultCost":[
               {
                  "CurrencyId":"CurrencyC",
                  "Price":250
               }],
               "MetaData":{
                  "GameplayTags":[
                     {
                        "TagName":"Customization.RN.Character.UpperBody"
                     },
                      {"TagName":"Customization.RN.Character.Head"},
                      {"TagName":"Customization.RN.Character.LowerBody"},
                      {"TagName":"Customization.RN.Character.Vambrace"}
                  ],
                  "BundleItems":[
                      "0EA4B7BD456E322EE1F0E1BD6D92F269",
                      "CCF1842E45E387C4E171C1AEDF179526",
                      "198B6E704CFC05EC0CA62599B2403926",
                      "B10CB7224F4BDF11444119B22D1AB381"
                  ],
                  "RewardBundleItems":[
                        "0EA4B7BD456E322EE1F0E1BD6D92F269",
                        "CCF1842E45E387C4E171C1AEDF179526",
                        "198B6E704CFC05EC0CA62599B2403926",
                        "B10CB7224F4BDF11444119B22D1AB381"
                  ],
                  "BundleDiscountPercent":10,
                  "MinPlayerLevel":1,
                  "MinCharacterLevel":1,
                  "Origin":"None"
               },
               "Faction":"Runner",
               "GameplayTagContainer":{
                  "GameplayTags":[
                     {
                        "TagName":"Customization.RN.FullSet"
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
         },
          {
              "Id": "A1C4E2FB4BC74EB560F431B210C5094C",
              "DisplayName": "RN_Weapon_Heal_002",
              "Purchasable": True,
              "Consumable": False,
              "IsWeapon": True,
              "InitialQuantity": 1,
              "DefaultCost": [
                  {
                      "CurrencyId": "CurrencyC",
                      "Price": 10
                  }],
              "MetaData": {
                  "GameplayTags": [
                      {
                          "TagName": "Weapon.ICR"
                      }
                  ],
                  "RequiredChallengesToComplete": [
                      "4D6510D3474A414BE76C95A42D09024C"
                  ],
                  "PrerequisiteItem": "69055D534DF27180C4B36CAB4B651054",
                  "FollowingItem": "89AD14A848DE42DC2A5CAB94BB25FCF9",
                  "MinPlayerLevel": 1,
                  "MinCharacterLevel": 1,
                  "Origin": "None"
              },
              "Faction": "Runner",
              "GameplayTagContainer": {
                  "GameplayTags": [
                      {
                          "TagName": "Weapon.ICR"
                      }
                  ],
                  "ParentTags": [
                      {
                          "TagName": "Weapon.ICR"
                      }
                  ]
              },
              "CustomizationGameplayTagByFaction": [
                  "Runner",
                  {
                      "TagName": "Weapon.ICR"
                  }
              ],
              "Gender": "None"
          },
          {
              "Id": "69055D534DF27180C4B36CAB4B651054",
              "DisplayName": "Runner_GhostWeaponHeal001_DisplayName",
              "Purchasable": True,
              "Consumable": False,
              "IsWeapon": True,
              "InitialQuantity": 1,
              "DefaultCost": [
                  {
                      "CurrencyId": "CurrencyC",
                      "Price": 249
                  }],
              "MetaData": {
                  "GameplayTags": [
                      {
                          "TagName": "Weapon.ICR"
                      }
                  ],
                  "MinPlayerLevel": 1,
                  "MinCharacterLevel": 1,
                  "Origin": "None"
              },
              "Faction": "Runner",
              "FollowingItem": "A1C4E2FB4BC74EB560F431B210C5094C",
              "GameplayTagContainer": {
                  "GameplayTags": [
                      {
                          "TagName": "Weapon.ICR"
                      }
                  ],
                  "ParentTags": [
                      {
                          "TagName": "Weapon.ICR"
                      }
                  ]
              },
              "CustomizationGameplayTagByFaction": [
                  "Runner",
                  {
                      "TagName": "Weapon.ICR"
                  }
              ],
              "Gender": "None"
          },
          {
              "Id": "755D4DFE40DA1512B01E3D8CFF3C8D4D",
              "DisplayName": "Runner_Sawbone_DisplayName",
              "Purchasable": True,
              "Consumable": False,
              "IsWeapon": False,
              "InitialQuantity": 1,
              "DefaultCost": [
                  {
                      "CurrencyId": "CurrencyA",
                      "Price": 10
                  }],
              "MetaData": {
                  "GameplayTags": [
                      {
                          "TagName": "Class.Runner"
                      }
                  ],
                  "BundleDiscountPercent": 10,
                  "MinPlayerLevel": 1,
                  "MinCharacterLevel": 1,
                  "Origin": "None"
              },
              "Faction": "Runner",
              "GameplayTagContainer": {
                  "GameplayTags": [
                      {
                          "TagName": "Class.Runner"
                      }
                  ],
                  "ParentTags": [
                      {
                          "TagName": "Entity.Runner"
                      }
                  ]
              },
              "CustomizationGameplayTagByFaction": [
                  "Runner",
                  {
                      "TagName": "Runner.Sawbones"
                  }
              ],
              "Gender": "Female"
          }
      ]
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
