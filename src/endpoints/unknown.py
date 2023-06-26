from flask_definitions import *


# Do NOT change Result to ANYTHING or Add anything before it. Game will crash. Doesnt mean it 100% works tho XD
@app.route("/<game_version>/catalog", methods=["GET"])
def catalog_get(game_version):
    print("Game Version of Catalog: " + game_version)
    get_remote_ip()
    try:
        return jsonify({
            "Result": [
                {
         "Id":"0EA4B7BD456E322EE1F0E1BD6D92F269",
         "DisplayName":"Scavenger_SMOKE_Head_STR001_Bloodbeige_NAME",
         "Purchasable":True,
         "Consumable":False,
         "IsWeapon":False,
         "InitialQuantity":1,
         "DefaultCost":[
            {
               "CurrencyId":"CurrencyC",
               "Price":10
            }
         ],
         "MetaData":{
            "GameplayTags":[
               {
                  "TagName":"Customization.RN.Character.Head"
               }
            ],
            "MinPlayerLevel":1,
            "MinCharacterLevel":1,
            "Origin":"None"
         },
         "Faction":"Runner",
         "GameplayTagContainer":{
            "GameplayTags":[
               {
                  "TagName":"Customization.RN.Character.Head"
               }
            ],
            "ParentTags":[
               {
                  "TagName":"Runner.Smoke"
               }
            ]
         }
      },
      {
         "Id":"CCF1842E-45E387C4-E171C1AE-DF179526",
         "DisplayName":"Scavenger_SMOKE_UpperBody_STR001_Bloodbeige_NAME",
         "Purchasable":True,
         "Consumable":False,
         "IsWeapon":False,
         "InitialQuantity":1,
         "DefaultCost":[
            {
               "CurrencyId":"CurrencyC",
               "Price":10
            }
         ],
         "MetaData":{
            "GameplayTags":[
               {
                  "TagName":"Customization.RN.Character.UpperBody"
               }
            ],
            "MinPlayerLevel":1,
            "MinCharacterLevel":1,
            "Origin":"None"
         },
         "Faction":"Runner",
         "GameplayTagContainer":{
            "GameplayTags":[
               {
                  "TagName":"Customization.RN.Character.UpperBody"
               }
            ],
            "ParentTags":[
               {
                  "TagName":"Runner.Smoke"
               }
            ]
         }
      },
      {
         "Id":"198B6E704CFC05EC0CA62599B2403926",
         "DisplayName":"Scavenger_SMOKE_LowerBody_STR001_Bloodbeige_NAME",
         "Purchasable":True,
         "Consumable":False,
         "IsWeapon":False,
         "InitialQuantity":1,
         "DefaultCost":[
            {
               "CurrencyId":"CurrencyC",
               "Price":10
            }
         ],
         "MetaData":{
            "GameplayTags":[
               {
                  "TagName":"Customization.RN.Character.LowerBody"
               }
            ],
            "MinPlayerLevel":1,
            "MinCharacterLevel":1,
            "Origin":"None"
         },
         "Faction":"Runner",
         "GameplayTagContainer":{
            "GameplayTags":[
               {
                  "TagName":"Customization.RN.Character.LowerBody"
               }
            ],
            "ParentTags":[
               {
                  "TagName":"Runner.Smoke"
               }
            ]
         }
      },
                {
                    "Id": "400E708541EA5FC40D2D73BB4FDFD106",
                    "DisplayName": "Scavenger_SMOKE_Outfit_STR001_Lightcoat_NAME",
                    "Purchasable": True,
                    "Consumable": False,
                    "IsWeapon": False,
                    "InitialQuantity": 1,
                    "DefaultCost": [
                        {
                            "CurrencyId": "CurrencyC",
                            "Price": 250
                        }
                    ],
                    "MetaData": {
                        "GameplayTags": [
                            {
                                "TagName": "Customization.RN.FullSet"
                            },
                            {
                                "TagName": "Customization.RN.Character.UpperBody"
                            },
                            {
                                "TagName": "Customization.RN.Character.Head"
                            },
                            {
                                "TagName": "Customization.RN.Character.LowerBody"
                            },
                            {
                                "TagName": "Customization.RN.Character.Vambrace"
                            }
                        ],
                        "BundleItems": [
                            "99752C6E4F54F9D7A4FFF3AA9A50B3E6",
                            "45D82E4044C3319F3AA388B366083718",
                            "D77F839F48462E2D610EADA98C084E48",
                            "E3C6E6BC4B224BF0EF414BB72A0EA7F4"
                        ],
                        "RewardBundleItems": [
                            "99752C6E4F54F9D7A4FFF3AA9A50B3E6",
                            "45D82E4044C3319F3AA388B366083718",
                            "D77F839F48462E2D610EADA98C084E48",
                            "E3C6E6BC4B224BF0EF414BB72A0EA7F4"
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
                                "TagName": "Customization.RN.FullSet"
                            }
                        ],
                        "ParentTags": [
                            {
                                "TagName": "Runner.Smoke"
                            }
                        ]
                    }
                },
                {
                    "Id": "D89AA4884C54121C007FC3B613A8DDE8",
                    "DisplayName": "Scavenger_SMOKE_Outfit_STR001_Winter01_NAME",
                    "Purchasable": True,
                    "Consumable": False,
                    "IsWeapon": False,
                    "InitialQuantity": 1,
                    "DefaultCost": [
                        {
                            "CurrencyId": "CurrencyC",
                            "Price": 250
                        }
                    ],
                    "MetaData": {
                        "GameplayTags": [
                            {
                                "TagName": "Customization.RN.FullSet"
                            },
                            {
                                "TagName": "Customization.RN.Character.UpperBody"
                            },
                            {
                                "TagName": "Customization.RN.Character.Head"
                            },
                            {
                                "TagName": "Customization.RN.Character.LowerBody"
                            },
                            {
                                "TagName": "Customization.RN.Character.Vambrace"
                            }
                        ],
                        "BundleItems": [
                            "70A248D340C77F1E552282AB8D73EADA",
                            "ACE0A0304A74F795A6466192FCBC7CBC",
                            "4C0728944310CD3252C500B2B39BD34F",
                            "248D60AC47F987E895AD65B722D8912B"
                        ],
                        "RewardBundleItems": [
                            "70A248D340C77F1E552282AB8D73EADA",
                            "ACE0A0304A74F795A6466192FCBC7CBC",
                            "4C0728944310CD3252C500B2B39BD34F",
                            "248D60AC47F987E895AD65B722D8912B"
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
                                "TagName": "Customization.RN.FullSet"
                            }
                        ],
                        "ParentTags": [
                            {
                                "TagName": "Runner.Smoke"
                            }
                        ]
                    }
                },
                {
                    "Id": "0638DA474500E76780093DB64058A4AA",
                    "DisplayName": "Scavenger_SMOKE_Outfit_STR001_Bloodbeige_NAME",
                    "Purchasable": True,
                    "Consumable": False,
                    "IsWeapon": False,
                    "InitialQuantity": 1,
                    "DefaultCost": [
                        {
                            "CurrencyId": "CurrencyC",
                            "Price": 250
                        }
                    ],
                    "MetaData": {
                        "GameplayTags": [
                            {
                                "TagName": "Customization.RN.FullSet"
                            },
                            {
                                "TagName": "Customization.RN.Character.UpperBody"
                            },
                            {
                                "TagName": "Customization.RN.Character.Head"
                            },
                            {
                                "TagName": "Customization.RN.Character.LowerBody"
                            },
                            {
                                "TagName": "Customization.RN.Character.Vambrace"
                            }
                        ],
                        "BundleItems": [
                            "0EA4B7BD456E322EE1F0E1BD6D92F269",
                            "CCF1842E45E387C4E171C1AEDF179526",
                            "198B6E704CFC05EC0CA62599B2403926",
                            "B10CB7224F4BDF11444119B22D1AB381"
                        ],
                        "RewardBundleItems": [
                            "0EA4B7BD456E322EE1F0E1BD6D92F269",
                            "CCF1842E45E387C4E171C1AEDF179526",
                            "198B6E704CFC05EC0CA62599B2403926",
                            "B10CB7224F4BDF11444119B22D1AB381"
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
                                "TagName": "Customization.RN.FullSet"
                            }
                        ],
                        "ParentTags": [
                            {
                                "TagName": "Runner.Smoke"
                            }
                        ]
                    }
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
                        }
                    ],
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
                    }
                },
                {
                    "Id": "A1C4E2FB4BC74EB560F431B210C5094C",
                    "DisplayName": "RN_Weapon_Heal_002",
                    "Purchasable": True,
                    "Consumable": False,
                    "IsWeapon": False,
                    "InitialQuantity": 1,
                    "DefaultCost": [
                        {
                            "CurrencyId": "CurrencyC",
                            "Price": 10
                        }
                    ],
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
                    }
                },
                {
                    "Id": "89AD14A848DE42DC2A5CAB94BB25FCF9",
                    "DisplayName": "RN_Weapon_Heal_003",
                    "Purchasable": True,
                    "Consumable": False,
                    "IsWeapon": False,
                    "InitialQuantity": 1,
                    "DefaultCost": [
                        {
                            "CurrencyId": "CurrencyC",
                            "Price": 460
                        }
                    ],
                    "MetaData": {
                        "GameplayTags": [
                            {
                                "TagName": "Weapon.ICR"
                            }
                        ],
                        "RequiredChallengesToComplete": [
                            "4D6510D3474A414BE76C95A42D09024C"
                        ],
                        "PrerequisiteItem": "A1C4E2FB4BC74EB560F431B210C5094C",
                        "FollowingItem": "895471FA4A8A74AB2FEE16BF35FC9D04",
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
                    }
                },
                {
                    "Id": "895471FA4A8A74AB2FEE16BF35FC9D04",
                    "DisplayName": "RN_Weapon_Heal_004",
                    "Purchasable": True,
                    "Consumable": False,
                    "IsWeapon": False,
                    "InitialQuantity": 1,
                    "DefaultCost": [
                        {
                            "CurrencyId": "CurrencyC",
                            "Price": 460
                        }
                    ],
                    "MetaData": {
                        "GameplayTags": [
                            {
                                "TagName": "Weapon.ICR"
                            }
                        ],
                        "RequiredChallengesToComplete": [
                            "4D6510D3474A414BE76C95A42D09024C"
                        ],
                        "PrerequisiteItem": "89AD14A848DE42DC2A5CAB94BB25FCF9",
                        "FollowingItem": "D7D7D07B4FB0FABDBF8C3CBE62EB6E96",
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
                    }
                },
                {
                    "Id": "D7D7D07B4FB0FABDBF8C3CBE62EB6E96",
                    "DisplayName": "RN_Weapon_Heal_005",
                    "Purchasable": True,
                    "Consumable": False,
                    "IsWeapon": False,
                    "InitialQuantity": 1,
                    "DefaultCost": [
                        {
                            "CurrencyId": "CurrencyC",
                            "Price": 460
                        }
                    ],
                    "MetaData": {
                        "GameplayTags": [
                            {
                                "TagName": "Weapon.ICR"
                            }
                        ],
                        "RequiredChallengesToComplete": [
                            "4D6510D3474A414BE76C95A42D09024C"
                        ],
                        "PrerequisiteItem": "895471FA4A8A74AB2FEE16BF35FC9D04",
                        "FollowingItem": "00170D7743531334E51EC3B955C7BF82",
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
                    }
                },
                {
                    "Id": "00170D7743531334E51EC3B955C7BF82",
                    "DisplayName": "RN_Weapon_Heal_006",
                    "Purchasable": True,
                    "Consumable": False,
                    "IsWeapon": False,
                    "InitialQuantity": 1,
                    "DefaultCost": [
                        {
                            "CurrencyId": "CurrencyC",
                            "Price": 460
                        }
                    ],
                    "MetaData": {
                        "GameplayTags": [
                            {
                                "TagName": "Weapon.ICR"
                            }
                        ],
                        "RequiredChallengesToComplete": [
                            "4D6510D3474A414BE76C95A42D09024C"
                        ],
                        "PrerequisiteItem": "D7D7D07B4FB0FABDBF8C3CBE62EB6E96",
                        "FollowingItem": "667B362746F7049D78BFC08A996D2876",
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
                    }
                },
                {
                    "Id": "667B362746F7049D78BFC08A996D2876",
                    "DisplayName": "RN_Weapon_Heal_007",
                    "Purchasable": True,
                    "Consumable": False,
                    "IsWeapon": False,
                    "InitialQuantity": 1,
                    "DefaultCost": [
                        {
                            "CurrencyId": "CurrencyC",
                            "Price": 460
                        }
                    ],
                    "MetaData": {
                        "GameplayTags": [
                            {
                                "TagName": "Weapon.ICR"
                            }
                        ],
                        "RequiredChallengesToComplete": [
                            "4D6510D3474A414BE76C95A42D09024C"
                        ],
                        "PrerequisiteItem": "00170D7743531334E51EC3B955C7BF82",
                        "FollowingItem": "8BF4B8E24F4CD5AB9DEA78851D73A0CC",
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
                    }
                },
                {
                    "Id": "8BF4B8E24F4CD5AB9DEA78851D73A0CC",
                    "DisplayName": "RN_Weapon_Heal_008",
                    "Purchasable": True,
                    "Consumable": False,
                    "IsWeapon": False,
                    "InitialQuantity": 1,
                    "DefaultCost": [
                        {
                            "CurrencyId": "CurrencyC",
                            "Price": 460
                        }
                    ],
                    "MetaData": {
                        "GameplayTags": [
                            {
                                "TagName": "Weapon.ICR"
                            }
                        ],
                        "RequiredChallengesToComplete": [
                            "4D6510D3474A414BE76C95A42D09024C"
                        ],
                        "PrerequisiteItem": "667B362746F7049D78BFC08A996D2876",
                        "FollowingItem": "A82051B5470DC62447DCB0800F756A9E",
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
                    }
                },
                {
                    "Id": "A82051B5470DC62447DCB0800F756A9E",
                    "DisplayName": "RN_Weapon_Heal_009",
                    "Purchasable": True,
                    "Consumable": False,
                    "IsWeapon": False,
                    "InitialQuantity": 1,
                    "DefaultCost": [
                        {
                            "CurrencyId": "CurrencyC",
                            "Price": 460
                        }
                    ],
                    "MetaData": {
                        "GameplayTags": [
                            {
                                "TagName": "Weapon.ICR"
                            }
                        ],
                        "RequiredChallengesToComplete": [
                            "4D6510D3474A414BE76C95A42D09024C"
                        ],
                        "PrerequisiteItem": "8BF4B8E24F4CD5AB9DEA78851D73A0CC",
                        "FollowingItem": "5CFA81324913D8C90C16E399A33B3A3A",
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
                    }
                },
                {
                    "Id": "5CFA81324913D8C90C16E399A33B3A3A",
                    "DisplayName": "RN_Weapon_Heal_010",
                    "Purchasable": True,
                    "Consumable": False,
                    "IsWeapon": False,
                    "InitialQuantity": 1,
                    "DefaultCost": [
                        {
                            "CurrencyId": "CurrencyC",
                            "Price": 460
                        }
                    ],
                    "MetaData": {
                        "GameplayTags": [
                            {
                                "TagName": "Weapon.ICR"
                            }
                        ],
                        "RequiredChallengesToComplete": [
                            "4D6510D3474A414BE76C95A42D09024C"
                        ],
                        "PrerequisiteItem": "A82051B5470DC62447DCB0800F756A9E",
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
                    }
                },
      {
         "Id":"B10CB7224F4BDF11444119B22D1AB381",
         "DisplayName":"Scavenger_SMOKE_Vambrace_STR001_Bloodbeige_NAME",
         "Purchasable":True,
         "Consumable":False,
         "IsWeapon":False,
         "InitialQuantity":1,
         "DefaultCost":[
            {
               "CurrencyId":"CurrencyC",
               "Price":10
            }
         ],
         "MetaData":{
            "GameplayTags":[
               {
                  "TagName":"Customization.RN.Character.Vambrace"
               }
            ],
            "MinPlayerLevel":1,
            "MinCharacterLevel":1,
            "Origin":"None"
         },
         "Faction":"Runner",
         "GameplayTagContainer":{
            "GameplayTags":[
               {
                  "TagName":"Customization.RN.Character.Vambrace"
               }
            ],
            "ParentTags":[
               {
                  "TagName":"Runner.Smoke"
               }
            ]
         },
          "CustomizationGameplayTagByFaction": [
              "Runner",
              {
                  "TagName": "Class.Runner"
              }
          ],
          "Gender": "Male"
      }
   ]
})

    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        print(e)


@app.errorhandler(404)
def debug_404(e):
    return jsonify({"message": "Endpoint not found"}), 404
