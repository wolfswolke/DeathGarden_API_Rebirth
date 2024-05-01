# Catalog Parser From Inventory
import random
import uuid

RunnerGroupA = {
    "data": {
        "characterId": {
            "tagName": "Runner.Sawbones"
        },
        "equipment": [
            "5C14F8C842B140E8CD6428BFC6659DD2",
            "24EADA804F62075E9BD526B3E0EE724C",
            "1774E376406ADD822F1C39A9DC4CC04B",
            "1AB1CFA743D595B05A872F8FDC6202D8"
        ],
        "equippedBonuses": [
            "109BC5904DC1272D70822EBA79CC85B1",
            "54B3EF794FCB0643C4644FA15BEF31D5"
        ],
        "equippedPerks": [
            "274EB0B34AB39E468BFA878F7E87465B",
            "D495BCB543F2D005B559C888E4BF2B3B"
        ],
        "equippedPowers": [
            "C8AF3D534973F82FADBB40BDA96F9DCD"
        ],
        "equippedWeapons": [
            "5A2DD3F6433AB83A725513B868D240CF"
        ],
        "pickedChallenges": [
            {
                "itemId": "ED14BB8240B4AE8124EDA69ECD37AB10",
                "list": [
                    {
                        "challengeId": "4F67D7064B9E706B36EEDABDBAB43AXD",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "72FF4B494F0257218238C695F072D794",
                "list": [
                    {
                        "challengeId": "EB68DD384E4BB1B012E8759F41980EF7",
                        "challengeCompletionValue": 2,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner"
                    }
                ]
            },
            {
                "itemId": "5F89822342D5E60F474080A36A7E6A5D",
                "list": [
                    {
                        "challengeId": "0BC1B3CF4FB218A9437CFABD534AD4F8",
                        "challengeCompletionValue": 270,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Heal_Runner.Challenge_Heal_Runner"
                    }
                ]
            },
            {
                "itemId": "807857C9498AEC6575932689C7733231",
                "list": [
                    {
                        "challengeId": "A7D3E8064C64AF0C80DE24B8988F731E",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner"
                    }
                ]
            },
            {
                "itemId": "0BD046FD439CDEC9DB6B138AF66B849D",
                "list": [
                    {
                        "challengeId": "F8B3276A4FF09F6366A6D19E86F21FAD",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "863513AF4D63B2AF0E70E7B670754E44",
                "list": [
                    {
                        "challengeId": "01601C514D2538D5424C83A14423BCEA",
                        "challengeCompletionValue": 14,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "5A8F3E354CBC6F8B5BD015AB89DE031A",
                "list": [
                    {
                        "challengeId": "9054DF734604F0076336789453A9EBBD",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "51CAE9D747988206193B08BAD648FF96",
                "list": [
                    {
                        "challengeId": "39E81FA4478ED4730F0717ABDFBC77C3",
                        "challengeCompletionValue": 2,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_BloodMode_Runner.Challenge_BloodMode_Runner"
                    }
                ]
            },
            {
                "itemId": "287E08D341A4C1D79E16A086E603A926",
                "list": [
                    {
                        "challengeId": "C500AB104B4D06219DB234B869289E5F",
                        "challengeCompletionValue": 45,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner"
                    }
                ]
            },
            {
                "itemId": "E8CE4B54417D9A6712B4B2927BF49376",
                "list": [
                    {
                        "challengeId": "46E60E174613D6E9E21940BEFC1DFB6F",
                        "challengeCompletionValue": 9450,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner"
                    }
                ]
            },
            {
                "itemId": "25CA213F463F21AC064611925BF357B7",
                "list": [
                    {
                        "challengeId": "032735174748799E27706CB28035567C",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "CBC263344E4D94F5AA1D3AAF46685EA8",
                "list": [
                    {
                        "challengeId": "251FEF7844BF2309631F99B1EB6EB4DD",
                        "challengeCompletionValue": 14,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates"
                    }
                ]
            },
            {
                "itemId": "832CDFB74A4C1A77BF4875BABEB31287",
                "list": [
                    {
                        "challengeId": "0DD143DC4E4AA67B60FACC984D45E31D",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "A0138AA648CE0DF4BBDB969A25C32EB2",
                "list": [
                    {
                        "challengeId": "FA68BDFD413B82B0A7B7109A55BB7127",
                        "challengeCompletionValue": 756,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner"
                    }
                ]
            },
            {
                "itemId": "F501B9E34800BEA6B29CFC87C1584669",
                "list": [
                    {
                        "challengeId": "D758EC434105075A146170B757E174B0",
                        "challengeCompletionValue": 360,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Climb_Runner.Challenge_Climb_Runner"
                    }
                ]
            },
            {
                "itemId": "D5674BD74129FD5F4C36958930CF7252",
                "list": [
                    {
                        "challengeId": "E9A1EE3844569C30E201C8847B30DF2B",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "828C25F148899221FEBD11976BD91551",
                "list": [
                    {
                        "challengeId": "DD4CCDF047F831EFCD876D9AC54DEFEA",
                        "challengeCompletionValue": 5,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "19E643BF4612E414EBE75B8EB069A15A",
                "list": [
                    {
                        "challengeId": "E66EE56F450413191BFEADB828A22D94",
                        "challengeCompletionValue": 105,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "FEE8A7004DC0DDFE1A22AC9156675E92",
                "list": [
                    {
                        "challengeId": "5A2C5CBB416C121FD0DE648271808591",
                        "challengeCompletionValue": 1200,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner"
                    }
                ]
            },
            {
                "itemId": "4FDB6DFE4E545F793CEF5780D40B84A6",
                "list": [
                    {
                        "challengeId": "AB711C4C4B383070F50016A4C2D8006F",
                        "challengeCompletionValue": 1890,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "F8E2A13648900939B5B086B2D61A6E43",
                "list": [
                    {
                        "challengeId": "624E6D924EB71A58BF6CFB827EE99D40",
                        "challengeCompletionValue": 11340,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "2729DEB04123FAF12B80D2970F6E5C98",
                "list": [
                    {
                        "challengeId": "55C1A7864DF7AB42F7EF1783E095B53C",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates"
                    }
                ]
            },
            {
                "itemId": "AD6D6B384FA0CB8D11149E8CBD2E65CD",
                "list": [
                    {
                        "challengeId": "6AD721414D3CDD85C4D42DBCAC1B5F83",
                        "challengeCompletionValue": 250,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "6BE58FB140091754841745BD81B1CD52",
                "list": [
                    {
                        "challengeId": "112847484561E72A98C392BFCC07B529",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "2D391C604941F465AA4EE7800AEF401F",
                "list": [
                    {
                        "challengeId": "57657766407BB9AF5EA38084D2A1BF31",
                        "challengeCompletionValue": 1,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner"
                    }
                ]
            },
            {
                "itemId": "B9FD9CD4489CDBCA483E96AB689B1FCE",
                "list": [
                    {
                        "challengeId": "98E66E8E4BF296519389949A1F50FAB8",
                        "challengeCompletionValue": 84,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "F732FE3845585D24E94AE39BA12D5E71",
                "list": [
                    {
                        "challengeId": "22639F234C9E4CCCECB7C6ACDD773A8E",
                        "challengeCompletionValue": 11340,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "A925877C4FA6CB2C470D11B7FF487D34",
                "list": [
                    {
                        "challengeId": "8ADE40CD4B61C349AF36BE94E1433006",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner"
                    }
                ]
            },
            {
                "itemId": "9C2F6A4F49A38054D8A3DBB3FF6DC7D6",
                "list": [
                    {
                        "challengeId": "E0C544B9402DE4896523BD905E16ED64",
                        "challengeCompletionValue": 6750,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "B8E6EB014D43FC4E7C5CEDBD530969ED",
                "list": [
                    {
                        "challengeId": "1B98F29341C2D71819B52ABDC37FCD08",
                        "challengeCompletionValue": 44100,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "AD1759374CC44614DCC46DBA60A9C670",
                "list": [
                    {
                        "challengeId": "171025E74F144CB256D0CDA3852E306F",
                        "challengeCompletionValue": 2000,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "D63DC301472FB3505E0E00BB878404C9",
                "list": [
                    {
                        "challengeId": "1F3C3C5548444F2D1DED4FAF9BCDDCFB",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "8438827D44AA0C807A8C85ABA3A9481B",
                "list": [
                    {
                        "challengeId": "72B688754657E294298BAB99D3366661",
                        "challengeCompletionValue": 27,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo"
                    }
                ]
            },
            {
                "itemId": "DF5AEE0248C6F69C140B67A038EFE2C8",
                "list": [
                    {
                        "challengeId": "179FD2EC47F7FC6E91FFB09FBD33B645",
                        "challengeCompletionValue": 4590,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "53954CDB4EB93E44EAB2EA9EF4D9C19C",
                "list": [
                    {
                        "challengeId": "176A1AEE43912906E0DB09AB27C6C420",
                        "challengeCompletionValue": 15,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "ED943B334280F225A7C2AE88B3DC48B9",
                "list": [
                    {
                        "challengeId": "AC57C1734CD39022B74670A6377B5338",
                        "challengeCompletionValue": 350,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "43916EE24C8F0395C826A2960D23AB6B",
                "list": [
                    {
                        "challengeId": "00B6FF4D4C1264D7007B73AF47605B52",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "36CE4DFC412B8FDF255791A609CCBEF4",
                "list": [
                    {
                        "challengeId": "3934DC7F4283AE4ECCF35D94DC3BD23D",
                        "challengeCompletionValue": 21,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "9B9218FB4DE925E6C729FA8162FDB505",
                "list": [
                    {
                        "challengeId": "98E33AD540CB22BB8DC7B6BEE264A789",
                        "challengeCompletionValue": 90,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "75D6E6DF48575AFB5758CAB46C9D7534",
                "list": [
                    {
                        "challengeId": "00F3159149A18ED735900C85887B51D0",
                        "challengeCompletionValue": 6800,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "2A8C0EAD44A5A393CCEE738C2E7409D9",
                "list": [
                    {
                        "challengeId": "0BB4F9F24D28C3C769E730900D2404E5",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "C133B57849D2179835EBC4AA25582CF1",
                "list": [
                    {
                        "challengeId": "BE35D2014ECAFF022CBE08ADF701B3CB",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "89AD14A848DE42DC2A5CAB94BB25FCF9",
                "list": [
                    {
                        "challengeId": "34150BD24607CE5CDCC6C49278466E3A",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "895471FA4A8A74AB2FEE16BF35FC9D04",
                "list": [
                    {
                        "challengeId": "09047C31486F9AE7F599F2A5D7D839E6",
                        "challengeCompletionValue": 756,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner"
                    }
                ]
            },
            {
                "itemId": "D7D7D07B4FB0FABDBF8C3CBE62EB6E96",
                "list": [
                    {
                        "challengeId": "5FA0EFFF4B7EA3A3DC8C87BED87C1E33",
                        "challengeCompletionValue": 3600,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "667B362746F7049D78BFC08A996D2876",
                "list": [
                    {
                        "challengeId": "0A348B4449A2F6359192FD845D49E0E0",
                        "challengeCompletionValue": 4,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "8BF4B8E24F4CD5AB9DEA78851D73A0CC",
                "list": [
                    {
                        "challengeId": "D95AEB6F400965E19E9BFD942EF4EADF",
                        "challengeCompletionValue": 6750,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "A82051B5470DC62447DCB0800F756A9E",
                "list": [
                    {
                        "challengeId": "FEBBC7804EBC5D094D0E258F06DD86F8",
                        "challengeCompletionValue": 350,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            }
        ],
        "prestigeLevel": 0
    },
    "objectId": "RunnerGroupA",
    "schemaVersion": 1,
    "version": 3
}

RunnerGroupB = {
    "data": {
        "characterId": {
            "tagName": "Runner.Ink"
        },
        "equipment": [
            "733A624F49F34D4659C084A4325D3202",
            "B782F75E4A250FBD58BED0AAA2F9B4B0",
            "2F282A504F9D04B0E3E8089CDAAC31FC",
            "540DB1914938D04F524DC9850A325B21"
        ],
        "equippedBonuses": [
            "261144CC43A9F74A60506AB0335B23B2",
            "92B767F442A89C87CC3C9CB5D279D6EA"
        ],
        "equippedPerks": [
            "48C47A4341B0E3E001F3D18537658D40",
            "366DFB0841631FE3A1F4FE9BF814CF2C"
        ],
        "equippedPowers": [
            "C8AF3D534973F82FADBB40BDA96F9DCD"
        ],
        "equippedWeapons": [
            "62AF95414827D3B29B9DFD97D54F1E95"
        ],
        "pickedChallenges": [
            {
                "itemId": "ED14BB8240B4AE8124EDA69ECD37AB10",
                "list": [
                    {
                        "challengeId": "4F67D7064B9E706B36EEDABDBAB43AFD",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "72FF4B494F0257218238C695F072D794",
                "list": [
                    {
                        "challengeId": "EB68DD384E4BB1B012E8759F41980EF7",
                        "challengeCompletionValue": 2,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner"
                    }
                ]
            },
            {
                "itemId": "5F89822342D5E60F474080A36A7E6A5D",
                "list": [
                    {
                        "challengeId": "0BC1B3CF4FB218A9437CFABD534AD4F8",
                        "challengeCompletionValue": 270,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Heal_Runner.Challenge_Heal_Runner"
                    }
                ]
            },
            {
                "itemId": "807857C9498AEC6575932689C7733231",
                "list": [
                    {
                        "challengeId": "A7D3E8064C64AF0C80DE24B8988F731E",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner"
                    }
                ]
            },
            {
                "itemId": "0BD046FD439CDEC9DB6B138AF66B849D",
                "list": [
                    {
                        "challengeId": "F8B3276A4FF09F6366A6D19E86F21FAD",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "863513AF4D63B2AF0E70E7B670754E44",
                "list": [
                    {
                        "challengeId": "01601C514D2538D5424C83A14423BCEA",
                        "challengeCompletionValue": 14,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "5A8F3E354CBC6F8B5BD015AB89DE031A",
                "list": [
                    {
                        "challengeId": "9054DF734604F0076336789453A9EBBD",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "51CAE9D747988206193B08BAD648FF96",
                "list": [
                    {
                        "challengeId": "39E81FA4478ED4730F0717ABDFBC77C3",
                        "challengeCompletionValue": 2,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_BloodMode_Runner.Challenge_BloodMode_Runner"
                    }
                ]
            },
            {
                "itemId": "287E08D341A4C1D79E16A086E603A926",
                "list": [
                    {
                        "challengeId": "C500AB104B4D06219DB234B869289E5F",
                        "challengeCompletionValue": 45,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner"
                    }
                ]
            },
            {
                "itemId": "E8CE4B54417D9A6712B4B2927BF49376",
                "list": [
                    {
                        "challengeId": "46E60E174613D6E9E21940BEFC1DFB6F",
                        "challengeCompletionValue": 9450,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner"
                    }
                ]
            },
            {
                "itemId": "25CA213F463F21AC064611925BF357B7",
                "list": [
                    {
                        "challengeId": "032735174748799E27706CB28035567C",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "CBC263344E4D94F5AA1D3AAF46685EA8",
                "list": [
                    {
                        "challengeId": "251FEF7844BF2309631F99B1EB6EB4DD",
                        "challengeCompletionValue": 14,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates"
                    }
                ]
            },
            {
                "itemId": "832CDFB74A4C1A77BF4875BABEB31287",
                "list": [
                    {
                        "challengeId": "0DD143DC4E4AA67B60FACC984D45E31D",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "A0138AA648CE0DF4BBDB969A25C32EB2",
                "list": [
                    {
                        "challengeId": "FA68BDFD413B82B0A7B7109A55BB7127",
                        "challengeCompletionValue": 756,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner"
                    }
                ]
            },
            {
                "itemId": "F501B9E34800BEA6B29CFC87C1584669",
                "list": [
                    {
                        "challengeId": "D758EC434105075A146170B757E174B0",
                        "challengeCompletionValue": 360,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Climb_Runner.Challenge_Climb_Runner"
                    }
                ]
            },
            {
                "itemId": "D5674BD74129FD5F4C36958930CF7252",
                "list": [
                    {
                        "challengeId": "E9A1EE3844569C30E201C8847B30DF2B",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "828C25F148899221FEBD11976BD91551",
                "list": [
                    {
                        "challengeId": "DD4CCDF047F831EFCD876D9AC54DEFEA",
                        "challengeCompletionValue": 5,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "19E643BF4612E414EBE75B8EB069A15A",
                "list": [
                    {
                        "challengeId": "E66EE56F450413191BFEADB828A22D94",
                        "challengeCompletionValue": 105,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "FEE8A7004DC0DDFE1A22AC9156675E92",
                "list": [
                    {
                        "challengeId": "5A2C5CBB416C121FD0DE648271808591",
                        "challengeCompletionValue": 1200,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner"
                    }
                ]
            },
            {
                "itemId": "4FDB6DFE4E545F793CEF5780D40B84A6",
                "list": [
                    {
                        "challengeId": "AB711C4C4B383070F50016A4C2D8006F",
                        "challengeCompletionValue": 1890,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "F8E2A13648900939B5B086B2D61A6E43",
                "list": [
                    {
                        "challengeId": "624E6D924EB71A58BF6CFB827EE99D40",
                        "challengeCompletionValue": 11340,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "2729DEB04123FAF12B80D2970F6E5C98",
                "list": [
                    {
                        "challengeId": "55C1A7864DF7AB42F7EF1783E095B53C",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates"
                    }
                ]
            },
            {
                "itemId": "AD6D6B384FA0CB8D11149E8CBD2E65CD",
                "list": [
                    {
                        "challengeId": "6AD721414D3CDD85C4D42DBCAC1B5F83",
                        "challengeCompletionValue": 250,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "6BE58FB140091754841745BD81B1CD52",
                "list": [
                    {
                        "challengeId": "112847484561E72A98C392BFCC07B529",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "2D391C604941F465AA4EE7800AEF401F",
                "list": [
                    {
                        "challengeId": "57657766407BB9AF5EA38084D2A1BF31",
                        "challengeCompletionValue": 1,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner"
                    }
                ]
            },
            {
                "itemId": "B9FD9CD4489CDBCA483E96AB689B1FCE",
                "list": [
                    {
                        "challengeId": "98E66E8E4BF296519389949A1F50FAB8",
                        "challengeCompletionValue": 84,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "F732FE3845585D24E94AE39BA12D5E71",
                "list": [
                    {
                        "challengeId": "22639F234C9E4CCCECB7C6ACDD773A8E",
                        "challengeCompletionValue": 11340,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "A925877C4FA6CB2C470D11B7FF487D34",
                "list": [
                    {
                        "challengeId": "8ADE40CD4B61C349AF36BE94E1433006",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner"
                    }
                ]
            },
            {
                "itemId": "9C2F6A4F49A38054D8A3DBB3FF6DC7D6",
                "list": [
                    {
                        "challengeId": "E0C544B9402DE4896523BD905E16ED64",
                        "challengeCompletionValue": 6750,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "B8E6EB014D43FC4E7C5CEDBD530969ED",
                "list": [
                    {
                        "challengeId": "1B98F29341C2D71819B52ABDC37FCD08",
                        "challengeCompletionValue": 44100,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "AD1759374CC44614DCC46DBA60A9C670",
                "list": [
                    {
                        "challengeId": "171025E74F144CB256D0CDA3852E306F",
                        "challengeCompletionValue": 2000,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "D63DC301472FB3505E0E00BB878404C9",
                "list": [
                    {
                        "challengeId": "1F3C3C5548444F2D1DED4FAF9BCDDCFB",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "8438827D44AA0C807A8C85ABA3A9481B",
                "list": [
                    {
                        "challengeId": "72B688754657E294298BAB99D3366661",
                        "challengeCompletionValue": 27,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo"
                    }
                ]
            },
            {
                "itemId": "DF5AEE0248C6F69C140B67A038EFE2C8",
                "list": [
                    {
                        "challengeId": "179FD2EC47F7FC6E91FFB09FBD33B645",
                        "challengeCompletionValue": 4590,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "53954CDB4EB93E44EAB2EA9EF4D9C19C",
                "list": [
                    {
                        "challengeId": "176A1AEE43912906E0DB09AB27C6C420",
                        "challengeCompletionValue": 15,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "ED943B334280F225A7C2AE88B3DC48B9",
                "list": [
                    {
                        "challengeId": "AC57C1734CD39022B74670A6377B5338",
                        "challengeCompletionValue": 350,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "43916EE24C8F0395C826A2960D23AB6B",
                "list": [
                    {
                        "challengeId": "00B6FF4D4C1264D7007B73AF47605B52",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "36CE4DFC412B8FDF255791A609CCBEF4",
                "list": [
                    {
                        "challengeId": "3934DC7F4283AE4ECCF35D94DC3BD23D",
                        "challengeCompletionValue": 21,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "9B9218FB4DE925E6C729FA8162FDB505",
                "list": [
                    {
                        "challengeId": "98E33AD540CB22BB8DC7B6BEE264A789",
                        "challengeCompletionValue": 90,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "75D6E6DF48575AFB5758CAB46C9D7534",
                "list": [
                    {
                        "challengeId": "00F3159149A18ED735900C85887B51D0",
                        "challengeCompletionValue": 6800,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "2A8C0EAD44A5A393CCEE738C2E7409D9",
                "list": [
                    {
                        "challengeId": "0BB4F9F24D28C3C769E730900D2404E5",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "C133B57849D2179835EBC4AA25582CF1",
                "list": [
                    {
                        "challengeId": "BE35D2014ECAFF022CBE08ADF701B3CB",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "89AD14A848DE42DC2A5CAB94BB25FCF9",
                "list": [
                    {
                        "challengeId": "34150BD24607CE5CDCC6C49278466E3A",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "895471FA4A8A74AB2FEE16BF35FC9D04",
                "list": [
                    {
                        "challengeId": "09047C31486F9AE7F599F2A5D7D839E6",
                        "challengeCompletionValue": 756,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner"
                    }
                ]
            },
            {
                "itemId": "D7D7D07B4FB0FABDBF8C3CBE62EB6E96",
                "list": [
                    {
                        "challengeId": "5FA0EFFF4B7EA3A3DC8C87BED87C1E33",
                        "challengeCompletionValue": 3600,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "667B362746F7049D78BFC08A996D2876",
                "list": [
                    {
                        "challengeId": "0A348B4449A2F6359192FD845D49E0E0",
                        "challengeCompletionValue": 4,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "8BF4B8E24F4CD5AB9DEA78851D73A0CC",
                "list": [
                    {
                        "challengeId": "D95AEB6F400965E19E9BFD942EF4EADF",
                        "challengeCompletionValue": 6750,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "A82051B5470DC62447DCB0800F756A9E",
                "list": [
                    {
                        "challengeId": "FEBBC7804EBC5D094D0E258F06DD86F8",
                        "challengeCompletionValue": 350,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            }
        ],
        "prestigeLevel": 0
    },
    "objectId": "RunnerGroupB",
    "schemaVersion": 1,
    "version": 3
}

RunnerGroupC = {
    "data": {
        "characterId": {
            "tagName": "Runner.Ghost"
        },
        "equipment": [
            "F6C3C02843F4DBA84109A0BF2D607DC2",
            "97F3953347EE8BE10A29D39E3C4F0D1E",
            "B3F3E6D84078F1DAE3C95AB5BFDEE945",
            "BE23A8F14E783C51E662DCADD9AA76FF"
        ],
        "equippedBonuses": [
            "8EFCD5CC464EBFE1B7B03A984563710A",
            "336D01F84D412B0D0D38F39311CA8D64"
        ],
        "equippedPerks": [
            "6A8FA1C845AE1D7576BD87A53F7ED4A4",
            "C7A898A44F208F9F85CE75969A98242D"
        ],
        "equippedPowers": [
            "C8AF3D534973F82FADBB40BDA96F9DCD"
        ],
        "equippedWeapons": [
            "0E262D7A47567BE03A49ABA756FC1482"
        ],
        "pickedChallenges": [
            {
                "itemId": "ED14BB8240B4AE8124EDA69ECD37AB10",
                "list": [
                    {
                        "challengeId": "4F67D7064B9E706B36EEDABDBAB43AFD",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "72FF4B494F0257218238C695F072D794",
                "list": [
                    {
                        "challengeId": "EB68DD384E4BB1B012E8759F41980EF7",
                        "challengeCompletionValue": 2,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner"
                    }
                ]
            },
            {
                "itemId": "5F89822342D5E60F474080A36A7E6A5D",
                "list": [
                    {
                        "challengeId": "0BC1B3CF4FB218A9437CFABD534AD4F8",
                        "challengeCompletionValue": 270,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Heal_Runner.Challenge_Heal_Runner"
                    }
                ]
            },
            {
                "itemId": "807857C9498AEC6575932689C7733231",
                "list": [
                    {
                        "challengeId": "A7D3E8064C64AF0C80DE24B8988F731E",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner"
                    }
                ]
            },
            {
                "itemId": "0BD046FD439CDEC9DB6B138AF66B849D",
                "list": [
                    {
                        "challengeId": "F8B3276A4FF09F6366A6D19E86F21FAD",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "863513AF4D63B2AF0E70E7B670754E44",
                "list": [
                    {
                        "challengeId": "01601C514D2538D5424C83A14423BCEA",
                        "challengeCompletionValue": 14,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "5A8F3E354CBC6F8B5BD015AB89DE031A",
                "list": [
                    {
                        "challengeId": "9054DF734604F0076336789453A9EBBD",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "51CAE9D747988206193B08BAD648FF96",
                "list": [
                    {
                        "challengeId": "39E81FA4478ED4730F0717ABDFBC77C3",
                        "challengeCompletionValue": 2,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_BloodMode_Runner.Challenge_BloodMode_Runner"
                    }
                ]
            },
            {
                "itemId": "287E08D341A4C1D79E16A086E603A926",
                "list": [
                    {
                        "challengeId": "C500AB104B4D06219DB234B869289E5F",
                        "challengeCompletionValue": 45,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner"
                    }
                ]
            },
            {
                "itemId": "E8CE4B54417D9A6712B4B2927BF49376",
                "list": [
                    {
                        "challengeId": "46E60E174613D6E9E21940BEFC1DFB6F",
                        "challengeCompletionValue": 9450,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner"
                    }
                ]
            },
            {
                "itemId": "25CA213F463F21AC064611925BF357B7",
                "list": [
                    {
                        "challengeId": "032735174748799E27706CB28035567C",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "CBC263344E4D94F5AA1D3AAF46685EA8",
                "list": [
                    {
                        "challengeId": "251FEF7844BF2309631F99B1EB6EB4DD",
                        "challengeCompletionValue": 14,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates"
                    }
                ]
            },
            {
                "itemId": "832CDFB74A4C1A77BF4875BABEB31287",
                "list": [
                    {
                        "challengeId": "0DD143DC4E4AA67B60FACC984D45E31D",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "A0138AA648CE0DF4BBDB969A25C32EB2",
                "list": [
                    {
                        "challengeId": "FA68BDFD413B82B0A7B7109A55BB7127",
                        "challengeCompletionValue": 756,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner"
                    }
                ]
            },
            {
                "itemId": "F501B9E34800BEA6B29CFC87C1584669",
                "list": [
                    {
                        "challengeId": "D758EC434105075A146170B757E174B0",
                        "challengeCompletionValue": 360,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Climb_Runner.Challenge_Climb_Runner"
                    }
                ]
            },
            {
                "itemId": "D5674BD74129FD5F4C36958930CF7252",
                "list": [
                    {
                        "challengeId": "E9A1EE3844569C30E201C8847B30DF2B",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "828C25F148899221FEBD11976BD91551",
                "list": [
                    {
                        "challengeId": "DD4CCDF047F831EFCD876D9AC54DEFEA",
                        "challengeCompletionValue": 5,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "19E643BF4612E414EBE75B8EB069A15A",
                "list": [
                    {
                        "challengeId": "E66EE56F450413191BFEADB828A22D94",
                        "challengeCompletionValue": 105,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "FEE8A7004DC0DDFE1A22AC9156675E92",
                "list": [
                    {
                        "challengeId": "5A2C5CBB416C121FD0DE648271808591",
                        "challengeCompletionValue": 1200,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner"
                    }
                ]
            },
            {
                "itemId": "4FDB6DFE4E545F793CEF5780D40B84A6",
                "list": [
                    {
                        "challengeId": "AB711C4C4B383070F50016A4C2D8006F",
                        "challengeCompletionValue": 1890,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "F8E2A13648900939B5B086B2D61A6E43",
                "list": [
                    {
                        "challengeId": "624E6D924EB71A58BF6CFB827EE99D40",
                        "challengeCompletionValue": 11340,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "2729DEB04123FAF12B80D2970F6E5C98",
                "list": [
                    {
                        "challengeId": "55C1A7864DF7AB42F7EF1783E095B53C",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates"
                    }
                ]
            },
            {
                "itemId": "AD6D6B384FA0CB8D11149E8CBD2E65CD",
                "list": [
                    {
                        "challengeId": "6AD721414D3CDD85C4D42DBCAC1B5F83",
                        "challengeCompletionValue": 250,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "6BE58FB140091754841745BD81B1CD52",
                "list": [
                    {
                        "challengeId": "112847484561E72A98C392BFCC07B529",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "2D391C604941F465AA4EE7800AEF401F",
                "list": [
                    {
                        "challengeId": "57657766407BB9AF5EA38084D2A1BF31",
                        "challengeCompletionValue": 1,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner"
                    }
                ]
            },
            {
                "itemId": "B9FD9CD4489CDBCA483E96AB689B1FCE",
                "list": [
                    {
                        "challengeId": "98E66E8E4BF296519389949A1F50FAB8",
                        "challengeCompletionValue": 84,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "F732FE3845585D24E94AE39BA12D5E71",
                "list": [
                    {
                        "challengeId": "22639F234C9E4CCCECB7C6ACDD773A8E",
                        "challengeCompletionValue": 11340,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "A925877C4FA6CB2C470D11B7FF487D34",
                "list": [
                    {
                        "challengeId": "8ADE40CD4B61C349AF36BE94E1433006",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner"
                    }
                ]
            },
            {
                "itemId": "9C2F6A4F49A38054D8A3DBB3FF6DC7D6",
                "list": [
                    {
                        "challengeId": "E0C544B9402DE4896523BD905E16ED64",
                        "challengeCompletionValue": 6750,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "B8E6EB014D43FC4E7C5CEDBD530969ED",
                "list": [
                    {
                        "challengeId": "1B98F29341C2D71819B52ABDC37FCD08",
                        "challengeCompletionValue": 44100,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "AD1759374CC44614DCC46DBA60A9C670",
                "list": [
                    {
                        "challengeId": "171025E74F144CB256D0CDA3852E306F",
                        "challengeCompletionValue": 2000,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "D63DC301472FB3505E0E00BB878404C9",
                "list": [
                    {
                        "challengeId": "1F3C3C5548444F2D1DED4FAF9BCDDCFB",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "8438827D44AA0C807A8C85ABA3A9481B",
                "list": [
                    {
                        "challengeId": "72B688754657E294298BAB99D3366661",
                        "challengeCompletionValue": 27,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo"
                    }
                ]
            },
            {
                "itemId": "DF5AEE0248C6F69C140B67A038EFE2C8",
                "list": [
                    {
                        "challengeId": "179FD2EC47F7FC6E91FFB09FBD33B645",
                        "challengeCompletionValue": 4590,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "53954CDB4EB93E44EAB2EA9EF4D9C19C",
                "list": [
                    {
                        "challengeId": "176A1AEE43912906E0DB09AB27C6C420",
                        "challengeCompletionValue": 15,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "ED943B334280F225A7C2AE88B3DC48B9",
                "list": [
                    {
                        "challengeId": "AC57C1734CD39022B74670A6377B5338",
                        "challengeCompletionValue": 350,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "43916EE24C8F0395C826A2960D23AB6B",
                "list": [
                    {
                        "challengeId": "00B6FF4D4C1264D7007B73AF47605B52",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "36CE4DFC412B8FDF255791A609CCBEF4",
                "list": [
                    {
                        "challengeId": "3934DC7F4283AE4ECCF35D94DC3BD23D",
                        "challengeCompletionValue": 21,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "9B9218FB4DE925E6C729FA8162FDB505",
                "list": [
                    {
                        "challengeId": "98E33AD540CB22BB8DC7B6BEE264A789",
                        "challengeCompletionValue": 90,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "75D6E6DF48575AFB5758CAB46C9D7534",
                "list": [
                    {
                        "challengeId": "00F3159149A18ED735900C85887B51D0",
                        "challengeCompletionValue": 6800,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "2A8C0EAD44A5A393CCEE738C2E7409D9",
                "list": [
                    {
                        "challengeId": "0BB4F9F24D28C3C769E730900D2404E5",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "C133B57849D2179835EBC4AA25582CF1",
                "list": [
                    {
                        "challengeId": "BE35D2014ECAFF022CBE08ADF701B3CB",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "89AD14A848DE42DC2A5CAB94BB25FCF9",
                "list": [
                    {
                        "challengeId": "34150BD24607CE5CDCC6C49278466E3A",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "895471FA4A8A74AB2FEE16BF35FC9D04",
                "list": [
                    {
                        "challengeId": "09047C31486F9AE7F599F2A5D7D839E6",
                        "challengeCompletionValue": 756,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner"
                    }
                ]
            },
            {
                "itemId": "D7D7D07B4FB0FABDBF8C3CBE62EB6E96",
                "list": [
                    {
                        "challengeId": "5FA0EFFF4B7EA3A3DC8C87BED87C1E33",
                        "challengeCompletionValue": 3600,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "667B362746F7049D78BFC08A996D2876",
                "list": [
                    {
                        "challengeId": "0A348B4449A2F6359192FD845D49E0E0",
                        "challengeCompletionValue": 4,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "8BF4B8E24F4CD5AB9DEA78851D73A0CC",
                "list": [
                    {
                        "challengeId": "D95AEB6F400965E19E9BFD942EF4EADF",
                        "challengeCompletionValue": 6750,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "A82051B5470DC62447DCB0800F756A9E",
                "list": [
                    {
                        "challengeId": "FEBBC7804EBC5D094D0E258F06DD86F8",
                        "challengeCompletionValue": 350,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            }
        ],
        "prestigeLevel": 0
    },
    "objectId": "RunnerGroupC",
    "schemaVersion": 1,
    "version": 3
}
RunnerGroupD = {
    "data": {
        "characterId": {
            "tagName": "Runner.Switch"
        },
        "equipment": [
            "F201BA114D675F8B62879199B3E5BEC9",
            "81688A484ADDF511C219C89DF3B2CE4F",
            "5DD486354855AEA9825B79AE6E306C82",
            "C619BC1049C2C0FAC3907A914FD26469"
        ],
        "equippedBonuses": [
            "CE235B2C497B4381DA1742BA22999128",
            "F91593E346415A85CFD0ED9CEBFBBDEA"
        ],
        "equippedPerks": [
            "350B26074604529237BF0CB22B60A9B8",
            "04650B23493C386FA87E48947D26D79F"
        ],
        "equippedPowers": [
            "C8AF3D534973F82FADBB40BDA96F9DCD"
        ],
        "equippedWeapons": [
            "23744B06493AE1220576529C4DB530B1"
        ],
        "pickedChallenges": [
            {
                "itemId": "ED14BB8240B4AE8124EDA69ECD37AB10",
                "list": [
                    {
                        "challengeId": "4F67D7064B9E706B36EEDABDBAB43AFD",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "72FF4B494F0257218238C695F072D794",
                "list": [
                    {
                        "challengeId": "EB68DD384E4BB1B012E8759F41980EF7",
                        "challengeCompletionValue": 2,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner"
                    }
                ]
            },
            {
                "itemId": "5F89822342D5E60F474080A36A7E6A5D",
                "list": [
                    {
                        "challengeId": "0BC1B3CF4FB218A9437CFABD534AD4F8",
                        "challengeCompletionValue": 270,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Heal_Runner.Challenge_Heal_Runner"
                    }
                ]
            },
            {
                "itemId": "807857C9498AEC6575932689C7733231",
                "list": [
                    {
                        "challengeId": "A7D3E8064C64AF0C80DE24B8988F731E",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner"
                    }
                ]
            },
            {
                "itemId": "0BD046FD439CDEC9DB6B138AF66B849D",
                "list": [
                    {
                        "challengeId": "F8B3276A4FF09F6366A6D19E86F21FAD",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "863513AF4D63B2AF0E70E7B670754E44",
                "list": [
                    {
                        "challengeId": "01601C514D2538D5424C83A14423BCEA",
                        "challengeCompletionValue": 14,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "5A8F3E354CBC6F8B5BD015AB89DE031A",
                "list": [
                    {
                        "challengeId": "9054DF734604F0076336789453A9EBBD",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "51CAE9D747988206193B08BAD648FF96",
                "list": [
                    {
                        "challengeId": "39E81FA4478ED4730F0717ABDFBC77C3",
                        "challengeCompletionValue": 2,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_BloodMode_Runner.Challenge_BloodMode_Runner"
                    }
                ]
            },
            {
                "itemId": "287E08D341A4C1D79E16A086E603A926",
                "list": [
                    {
                        "challengeId": "C500AB104B4D06219DB234B869289E5F",
                        "challengeCompletionValue": 45,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner"
                    }
                ]
            },
            {
                "itemId": "E8CE4B54417D9A6712B4B2927BF49376",
                "list": [
                    {
                        "challengeId": "46E60E174613D6E9E21940BEFC1DFB6F",
                        "challengeCompletionValue": 9450,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner"
                    }
                ]
            },
            {
                "itemId": "25CA213F463F21AC064611925BF357B7",
                "list": [
                    {
                        "challengeId": "032735174748799E27706CB28035567C",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "CBC263344E4D94F5AA1D3AAF46685EA8",
                "list": [
                    {
                        "challengeId": "251FEF7844BF2309631F99B1EB6EB4DD",
                        "challengeCompletionValue": 14,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates"
                    }
                ]
            },
            {
                "itemId": "832CDFB74A4C1A77BF4875BABEB31287",
                "list": [
                    {
                        "challengeId": "0DD143DC4E4AA67B60FACC984D45E31D",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "A0138AA648CE0DF4BBDB969A25C32EB2",
                "list": [
                    {
                        "challengeId": "FA68BDFD413B82B0A7B7109A55BB7127",
                        "challengeCompletionValue": 756,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner"
                    }
                ]
            },
            {
                "itemId": "F501B9E34800BEA6B29CFC87C1584669",
                "list": [
                    {
                        "challengeId": "D758EC434105075A146170B757E174B0",
                        "challengeCompletionValue": 360,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Climb_Runner.Challenge_Climb_Runner"
                    }
                ]
            },
            {
                "itemId": "D5674BD74129FD5F4C36958930CF7252",
                "list": [
                    {
                        "challengeId": "E9A1EE3844569C30E201C8847B30DF2B",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "828C25F148899221FEBD11976BD91551",
                "list": [
                    {
                        "challengeId": "DD4CCDF047F831EFCD876D9AC54DEFEA",
                        "challengeCompletionValue": 5,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "19E643BF4612E414EBE75B8EB069A15A",
                "list": [
                    {
                        "challengeId": "E66EE56F450413191BFEADB828A22D94",
                        "challengeCompletionValue": 105,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "FEE8A7004DC0DDFE1A22AC9156675E92",
                "list": [
                    {
                        "challengeId": "5A2C5CBB416C121FD0DE648271808591",
                        "challengeCompletionValue": 1200,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner"
                    }
                ]
            },
            {
                "itemId": "4FDB6DFE4E545F793CEF5780D40B84A6",
                "list": [
                    {
                        "challengeId": "AB711C4C4B383070F50016A4C2D8006F",
                        "challengeCompletionValue": 1890,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "F8E2A13648900939B5B086B2D61A6E43",
                "list": [
                    {
                        "challengeId": "624E6D924EB71A58BF6CFB827EE99D40",
                        "challengeCompletionValue": 11340,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "2729DEB04123FAF12B80D2970F6E5C98",
                "list": [
                    {
                        "challengeId": "55C1A7864DF7AB42F7EF1783E095B53C",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates"
                    }
                ]
            },
            {
                "itemId": "AD6D6B384FA0CB8D11149E8CBD2E65CD",
                "list": [
                    {
                        "challengeId": "6AD721414D3CDD85C4D42DBCAC1B5F83",
                        "challengeCompletionValue": 250,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "6BE58FB140091754841745BD81B1CD52",
                "list": [
                    {
                        "challengeId": "112847484561E72A98C392BFCC07B529",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "2D391C604941F465AA4EE7800AEF401F",
                "list": [
                    {
                        "challengeId": "57657766407BB9AF5EA38084D2A1BF31",
                        "challengeCompletionValue": 1,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner"
                    }
                ]
            },
            {
                "itemId": "B9FD9CD4489CDBCA483E96AB689B1FCE",
                "list": [
                    {
                        "challengeId": "98E66E8E4BF296519389949A1F50FAB8",
                        "challengeCompletionValue": 84,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "F732FE3845585D24E94AE39BA12D5E71",
                "list": [
                    {
                        "challengeId": "22639F234C9E4CCCECB7C6ACDD773A8E",
                        "challengeCompletionValue": 11340,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "A925877C4FA6CB2C470D11B7FF487D34",
                "list": [
                    {
                        "challengeId": "8ADE40CD4B61C349AF36BE94E1433006",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner"
                    }
                ]
            },
            {
                "itemId": "9C2F6A4F49A38054D8A3DBB3FF6DC7D6",
                "list": [
                    {
                        "challengeId": "E0C544B9402DE4896523BD905E16ED64",
                        "challengeCompletionValue": 6750,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "B8E6EB014D43FC4E7C5CEDBD530969ED",
                "list": [
                    {
                        "challengeId": "1B98F29341C2D71819B52ABDC37FCD08",
                        "challengeCompletionValue": 44100,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "AD1759374CC44614DCC46DBA60A9C670",
                "list": [
                    {
                        "challengeId": "171025E74F144CB256D0CDA3852E306F",
                        "challengeCompletionValue": 2000,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "D63DC301472FB3505E0E00BB878404C9",
                "list": [
                    {
                        "challengeId": "1F3C3C5548444F2D1DED4FAF9BCDDCFB",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "8438827D44AA0C807A8C85ABA3A9481B",
                "list": [
                    {
                        "challengeId": "72B688754657E294298BAB99D3366661",
                        "challengeCompletionValue": 27,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo"
                    }
                ]
            },
            {
                "itemId": "DF5AEE0248C6F69C140B67A038EFE2C8",
                "list": [
                    {
                        "challengeId": "179FD2EC47F7FC6E91FFB09FBD33B645",
                        "challengeCompletionValue": 4590,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "53954CDB4EB93E44EAB2EA9EF4D9C19C",
                "list": [
                    {
                        "challengeId": "176A1AEE43912906E0DB09AB27C6C420",
                        "challengeCompletionValue": 15,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "ED943B334280F225A7C2AE88B3DC48B9",
                "list": [
                    {
                        "challengeId": "AC57C1734CD39022B74670A6377B5338",
                        "challengeCompletionValue": 350,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "43916EE24C8F0395C826A2960D23AB6B",
                "list": [
                    {
                        "challengeId": "00B6FF4D4C1264D7007B73AF47605B52",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "36CE4DFC412B8FDF255791A609CCBEF4",
                "list": [
                    {
                        "challengeId": "3934DC7F4283AE4ECCF35D94DC3BD23D",
                        "challengeCompletionValue": 21,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "9B9218FB4DE925E6C729FA8162FDB505",
                "list": [
                    {
                        "challengeId": "98E33AD540CB22BB8DC7B6BEE264A789",
                        "challengeCompletionValue": 90,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "75D6E6DF48575AFB5758CAB46C9D7534",
                "list": [
                    {
                        "challengeId": "00F3159149A18ED735900C85887B51D0",
                        "challengeCompletionValue": 6800,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "2A8C0EAD44A5A393CCEE738C2E7409D9",
                "list": [
                    {
                        "challengeId": "0BB4F9F24D28C3C769E730900D2404E5",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "C133B57849D2179835EBC4AA25582CF1",
                "list": [
                    {
                        "challengeId": "BE35D2014ECAFF022CBE08ADF701B3CB",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "89AD14A848DE42DC2A5CAB94BB25FCF9",
                "list": [
                    {
                        "challengeId": "34150BD24607CE5CDCC6C49278466E3A",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "895471FA4A8A74AB2FEE16BF35FC9D04",
                "list": [
                    {
                        "challengeId": "09047C31486F9AE7F599F2A5D7D839E6",
                        "challengeCompletionValue": 756,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner"
                    }
                ]
            },
            {
                "itemId": "D7D7D07B4FB0FABDBF8C3CBE62EB6E96",
                "list": [
                    {
                        "challengeId": "5FA0EFFF4B7EA3A3DC8C87BED87C1E33",
                        "challengeCompletionValue": 3600,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "667B362746F7049D78BFC08A996D2876",
                "list": [
                    {
                        "challengeId": "0A348B4449A2F6359192FD845D49E0E0",
                        "challengeCompletionValue": 4,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "8BF4B8E24F4CD5AB9DEA78851D73A0CC",
                "list": [
                    {
                        "challengeId": "D95AEB6F400965E19E9BFD942EF4EADF",
                        "challengeCompletionValue": 6750,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "A82051B5470DC62447DCB0800F756A9E",
                "list": [
                    {
                        "challengeId": "FEBBC7804EBC5D094D0E258F06DD86F8",
                        "challengeCompletionValue": 350,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            }
        ],
        "prestigeLevel": 0
    },
    "objectId": "RunnerGroupD",
    "schemaVersion": 1,
    "version": 3
}
RunnerGroupE = {
    "data": {
        "characterId": {
            "tagName": "Runner.Smoke"
        },
        "equipment": [
            "84DBF7B141246372690AFBA436B51C30",
            "642E3BFA4F89698DD59E64AC133E266B",
            "74C21FF949E644AF2231CDB796E9386E",
            "0743E9B44190283D81A76480701EB07E"
        ],
        "equippedBonuses": [
            "1E08AFFA485E92BAFF2C1BB85CEFB81E",
            "1F5CD9004224C56746D81991AA40448A"
        ],
        "equippedPerks": [
            "20FF1865462FD26B0253A08F18EFAA10",
            "E4892E8A495FFB38F90729A1C97F3AC9"
        ],
        "equippedPowers": [
            "C8AF3D534973F82FADBB40BDA96F9DCD"
        ],
        "equippedWeapons": [
            "492232504161420C872A0F82FC16ACDB"
        ],
        "pickedChallenges": [
            {
                "itemId": "ED14BB8240B4AE8124EDA69ECD37AB10",
                "list": [
                    {
                        "challengeId": "4F67D7064B9E706B36EEDABDBAB43AFD",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "72FF4B494F0257218238C695F072D794",
                "list": [
                    {
                        "challengeId": "EB68DD384E4BB1B012E8759F41980EF7",
                        "challengeCompletionValue": 2,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner"
                    }
                ]
            },
            {
                "itemId": "5F89822342D5E60F474080A36A7E6A5D",
                "list": [
                    {
                        "challengeId": "0BC1B3CF4FB218A9437CFABD534AD4F8",
                        "challengeCompletionValue": 270,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Heal_Runner.Challenge_Heal_Runner"
                    }
                ]
            },
            {
                "itemId": "807857C9498AEC6575932689C7733231",
                "list": [
                    {
                        "challengeId": "A7D3E8064C64AF0C80DE24B8988F731E",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner"
                    }
                ]
            },
            {
                "itemId": "0BD046FD439CDEC9DB6B138AF66B849D",
                "list": [
                    {
                        "challengeId": "F8B3276A4FF09F6366A6D19E86F21FAD",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "863513AF4D63B2AF0E70E7B670754E44",
                "list": [
                    {
                        "challengeId": "01601C514D2538D5424C83A14423BCEA",
                        "challengeCompletionValue": 14,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "5A8F3E354CBC6F8B5BD015AB89DE031A",
                "list": [
                    {
                        "challengeId": "9054DF734604F0076336789453A9EBBD",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "51CAE9D747988206193B08BAD648FF96",
                "list": [
                    {
                        "challengeId": "39E81FA4478ED4730F0717ABDFBC77C3",
                        "challengeCompletionValue": 2,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_BloodMode_Runner.Challenge_BloodMode_Runner"
                    }
                ]
            },
            {
                "itemId": "287E08D341A4C1D79E16A086E603A926",
                "list": [
                    {
                        "challengeId": "C500AB104B4D06219DB234B869289E5F",
                        "challengeCompletionValue": 45,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner"
                    }
                ]
            },
            {
                "itemId": "E8CE4B54417D9A6712B4B2927BF49376",
                "list": [
                    {
                        "challengeId": "46E60E174613D6E9E21940BEFC1DFB6F",
                        "challengeCompletionValue": 9450,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner"
                    }
                ]
            },
            {
                "itemId": "25CA213F463F21AC064611925BF357B7",
                "list": [
                    {
                        "challengeId": "032735174748799E27706CB28035567C",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "CBC263344E4D94F5AA1D3AAF46685EA8",
                "list": [
                    {
                        "challengeId": "251FEF7844BF2309631F99B1EB6EB4DD",
                        "challengeCompletionValue": 14,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates"
                    }
                ]
            },
            {
                "itemId": "832CDFB74A4C1A77BF4875BABEB31287",
                "list": [
                    {
                        "challengeId": "0DD143DC4E4AA67B60FACC984D45E31D",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "A0138AA648CE0DF4BBDB969A25C32EB2",
                "list": [
                    {
                        "challengeId": "FA68BDFD413B82B0A7B7109A55BB7127",
                        "challengeCompletionValue": 756,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner"
                    }
                ]
            },
            {
                "itemId": "F501B9E34800BEA6B29CFC87C1584669",
                "list": [
                    {
                        "challengeId": "D758EC434105075A146170B757E174B0",
                        "challengeCompletionValue": 360,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Climb_Runner.Challenge_Climb_Runner"
                    }
                ]
            },
            {
                "itemId": "D5674BD74129FD5F4C36958930CF7252",
                "list": [
                    {
                        "challengeId": "E9A1EE3844569C30E201C8847B30DF2B",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "828C25F148899221FEBD11976BD91551",
                "list": [
                    {
                        "challengeId": "DD4CCDF047F831EFCD876D9AC54DEFEA",
                        "challengeCompletionValue": 5,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "19E643BF4612E414EBE75B8EB069A15A",
                "list": [
                    {
                        "challengeId": "E66EE56F450413191BFEADB828A22D94",
                        "challengeCompletionValue": 105,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "FEE8A7004DC0DDFE1A22AC9156675E92",
                "list": [
                    {
                        "challengeId": "5A2C5CBB416C121FD0DE648271808591",
                        "challengeCompletionValue": 1200,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner"
                    }
                ]
            },
            {
                "itemId": "4FDB6DFE4E545F793CEF5780D40B84A6",
                "list": [
                    {
                        "challengeId": "AB711C4C4B383070F50016A4C2D8006F",
                        "challengeCompletionValue": 1890,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "F8E2A13648900939B5B086B2D61A6E43",
                "list": [
                    {
                        "challengeId": "624E6D924EB71A58BF6CFB827EE99D40",
                        "challengeCompletionValue": 11340,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "2729DEB04123FAF12B80D2970F6E5C98",
                "list": [
                    {
                        "challengeId": "55C1A7864DF7AB42F7EF1783E095B53C",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates"
                    }
                ]
            },
            {
                "itemId": "AD6D6B384FA0CB8D11149E8CBD2E65CD",
                "list": [
                    {
                        "challengeId": "6AD721414D3CDD85C4D42DBCAC1B5F83",
                        "challengeCompletionValue": 250,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "6BE58FB140091754841745BD81B1CD52",
                "list": [
                    {
                        "challengeId": "112847484561E72A98C392BFCC07B529",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "2D391C604941F465AA4EE7800AEF401F",
                "list": [
                    {
                        "challengeId": "57657766407BB9AF5EA38084D2A1BF31",
                        "challengeCompletionValue": 1,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner"
                    }
                ]
            },
            {
                "itemId": "B9FD9CD4489CDBCA483E96AB689B1FCE",
                "list": [
                    {
                        "challengeId": "98E66E8E4BF296519389949A1F50FAB8",
                        "challengeCompletionValue": 84,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "F732FE3845585D24E94AE39BA12D5E71",
                "list": [
                    {
                        "challengeId": "22639F234C9E4CCCECB7C6ACDD773A8E",
                        "challengeCompletionValue": 11340,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "A925877C4FA6CB2C470D11B7FF487D34",
                "list": [
                    {
                        "challengeId": "8ADE40CD4B61C349AF36BE94E1433006",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner"
                    }
                ]
            },
            {
                "itemId": "9C2F6A4F49A38054D8A3DBB3FF6DC7D6",
                "list": [
                    {
                        "challengeId": "E0C544B9402DE4896523BD905E16ED64",
                        "challengeCompletionValue": 6750,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "B8E6EB014D43FC4E7C5CEDBD530969ED",
                "list": [
                    {
                        "challengeId": "1B98F29341C2D71819B52ABDC37FCD08",
                        "challengeCompletionValue": 44100,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "AD1759374CC44614DCC46DBA60A9C670",
                "list": [
                    {
                        "challengeId": "171025E74F144CB256D0CDA3852E306F",
                        "challengeCompletionValue": 2000,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "D63DC301472FB3505E0E00BB878404C9",
                "list": [
                    {
                        "challengeId": "1F3C3C5548444F2D1DED4FAF9BCDDCFB",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "8438827D44AA0C807A8C85ABA3A9481B",
                "list": [
                    {
                        "challengeId": "72B688754657E294298BAB99D3366661",
                        "challengeCompletionValue": 27,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo"
                    }
                ]
            },
            {
                "itemId": "DF5AEE0248C6F69C140B67A038EFE2C8",
                "list": [
                    {
                        "challengeId": "179FD2EC47F7FC6E91FFB09FBD33B645",
                        "challengeCompletionValue": 4590,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "53954CDB4EB93E44EAB2EA9EF4D9C19C",
                "list": [
                    {
                        "challengeId": "176A1AEE43912906E0DB09AB27C6C420",
                        "challengeCompletionValue": 15,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "ED943B334280F225A7C2AE88B3DC48B9",
                "list": [
                    {
                        "challengeId": "AC57C1734CD39022B74670A6377B5338",
                        "challengeCompletionValue": 350,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "43916EE24C8F0395C826A2960D23AB6B",
                "list": [
                    {
                        "challengeId": "00B6FF4D4C1264D7007B73AF47605B52",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "36CE4DFC412B8FDF255791A609CCBEF4",
                "list": [
                    {
                        "challengeId": "3934DC7F4283AE4ECCF35D94DC3BD23D",
                        "challengeCompletionValue": 21,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "9B9218FB4DE925E6C729FA8162FDB505",
                "list": [
                    {
                        "challengeId": "98E33AD540CB22BB8DC7B6BEE264A789",
                        "challengeCompletionValue": 90,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "75D6E6DF48575AFB5758CAB46C9D7534",
                "list": [
                    {
                        "challengeId": "00F3159149A18ED735900C85887B51D0",
                        "challengeCompletionValue": 6800,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "2A8C0EAD44A5A393CCEE738C2E7409D9",
                "list": [
                    {
                        "challengeId": "0BB4F9F24D28C3C769E730900D2404E5",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "C133B57849D2179835EBC4AA25582CF1",
                "list": [
                    {
                        "challengeId": "BE35D2014ECAFF022CBE08ADF701B3CB",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "89AD14A848DE42DC2A5CAB94BB25FCF9",
                "list": [
                    {
                        "challengeId": "34150BD24607CE5CDCC6C49278466E3A",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "895471FA4A8A74AB2FEE16BF35FC9D04",
                "list": [
                    {
                        "challengeId": "09047C31486F9AE7F599F2A5D7D839E6",
                        "challengeCompletionValue": 756,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner"
                    }
                ]
            },
            {
                "itemId": "D7D7D07B4FB0FABDBF8C3CBE62EB6E96",
                "list": [
                    {
                        "challengeId": "5FA0EFFF4B7EA3A3DC8C87BED87C1E33",
                        "challengeCompletionValue": 3600,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "667B362746F7049D78BFC08A996D2876",
                "list": [
                    {
                        "challengeId": "0A348B4449A2F6359192FD845D49E0E0",
                        "challengeCompletionValue": 4,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "8BF4B8E24F4CD5AB9DEA78851D73A0CC",
                "list": [
                    {
                        "challengeId": "D95AEB6F400965E19E9BFD942EF4EADF",
                        "challengeCompletionValue": 6750,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "A82051B5470DC62447DCB0800F756A9E",
                "list": [
                    {
                        "challengeId": "FEBBC7804EBC5D094D0E258F06DD86F8",
                        "challengeCompletionValue": 350,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            }
        ],
        "prestigeLevel": 0
    },
    "objectId": "RunnerGroupE",
    "schemaVersion": 1,
    "version": 3
}
RunnerGroupF = {
    "data": {
        "characterId": {
            "tagName": "Runner.Dash"
        },
        "equipment": [
            "BA470A974C8EEC39D7248F91F3ABFACD",
            "6A45DC544903218CEC18D4B7A27CEE51",
            "1EBB7B3043BED679F382B087C0D6DE56",
            "92CC1AC04868D1F9A99E6EA35BCDAD56"
        ],
        "equippedBonuses": [
            "E13EA0CF46EE94F27F75BFAAD48D29D1",
            "CEE62C37472E49AF36BC2A9809EEF2AD"
        ],
        "equippedPerks": [
            "97501DEF493625107AEDCAAB2ADEDF4B",
            "2BD43A50459BD9094DADC49A0F5F2551"
        ],
        "equippedPowers": [
            "C8AF3D534973F82FADBB40BDA96F9DCD"
        ],
        "equippedWeapons": [
            "272369C042147225E364CFA42947859F"
        ],
        "pickedChallenges": [
            {
                "itemId": "ED14BB8240B4AE8124EDA69ECD37AB10",
                "list": [
                    {
                        "challengeId": "4F67D7064B9E706B36EEDABDBAB43AFD",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "72FF4B494F0257218238C695F072D794",
                "list": [
                    {
                        "challengeId": "EB68DD384E4BB1B012E8759F41980EF7",
                        "challengeCompletionValue": 2,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner"
                    }
                ]
            },
            {
                "itemId": "5F89822342D5E60F474080A36A7E6A5D",
                "list": [
                    {
                        "challengeId": "0BC1B3CF4FB218A9437CFABD534AD4F8",
                        "challengeCompletionValue": 270,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Heal_Runner.Challenge_Heal_Runner"
                    }
                ]
            },
            {
                "itemId": "807857C9498AEC6575932689C7733231",
                "list": [
                    {
                        "challengeId": "A7D3E8064C64AF0C80DE24B8988F731E",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner"
                    }
                ]
            },
            {
                "itemId": "0BD046FD439CDEC9DB6B138AF66B849D",
                "list": [
                    {
                        "challengeId": "F8B3276A4FF09F6366A6D19E86F21FAD",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "863513AF4D63B2AF0E70E7B670754E44",
                "list": [
                    {
                        "challengeId": "01601C514D2538D5424C83A14423BCEA",
                        "challengeCompletionValue": 14,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "5A8F3E354CBC6F8B5BD015AB89DE031A",
                "list": [
                    {
                        "challengeId": "9054DF734604F0076336789453A9EBBD",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "51CAE9D747988206193B08BAD648FF96",
                "list": [
                    {
                        "challengeId": "39E81FA4478ED4730F0717ABDFBC77C3",
                        "challengeCompletionValue": 2,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_BloodMode_Runner.Challenge_BloodMode_Runner"
                    }
                ]
            },
            {
                "itemId": "287E08D341A4C1D79E16A086E603A926",
                "list": [
                    {
                        "challengeId": "C500AB104B4D06219DB234B869289E5F",
                        "challengeCompletionValue": 45,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner"
                    }
                ]
            },
            {
                "itemId": "E8CE4B54417D9A6712B4B2927BF49376",
                "list": [
                    {
                        "challengeId": "46E60E174613D6E9E21940BEFC1DFB6F",
                        "challengeCompletionValue": 9450,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner"
                    }
                ]
            },
            {
                "itemId": "25CA213F463F21AC064611925BF357B7",
                "list": [
                    {
                        "challengeId": "032735174748799E27706CB28035567C",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "CBC263344E4D94F5AA1D3AAF46685EA8",
                "list": [
                    {
                        "challengeId": "251FEF7844BF2309631F99B1EB6EB4DD",
                        "challengeCompletionValue": 14,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates"
                    }
                ]
            },
            {
                "itemId": "832CDFB74A4C1A77BF4875BABEB31287",
                "list": [
                    {
                        "challengeId": "0DD143DC4E4AA67B60FACC984D45E31D",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "A0138AA648CE0DF4BBDB969A25C32EB2",
                "list": [
                    {
                        "challengeId": "FA68BDFD413B82B0A7B7109A55BB7127",
                        "challengeCompletionValue": 756,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner"
                    }
                ]
            },
            {
                "itemId": "F501B9E34800BEA6B29CFC87C1584669",
                "list": [
                    {
                        "challengeId": "D758EC434105075A146170B757E174B0",
                        "challengeCompletionValue": 360,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Climb_Runner.Challenge_Climb_Runner"
                    }
                ]
            },
            {
                "itemId": "D5674BD74129FD5F4C36958930CF7252",
                "list": [
                    {
                        "challengeId": "E9A1EE3844569C30E201C8847B30DF2B",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "828C25F148899221FEBD11976BD91551",
                "list": [
                    {
                        "challengeId": "DD4CCDF047F831EFCD876D9AC54DEFEA",
                        "challengeCompletionValue": 5,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "19E643BF4612E414EBE75B8EB069A15A",
                "list": [
                    {
                        "challengeId": "E66EE56F450413191BFEADB828A22D94",
                        "challengeCompletionValue": 105,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "FEE8A7004DC0DDFE1A22AC9156675E92",
                "list": [
                    {
                        "challengeId": "5A2C5CBB416C121FD0DE648271808591",
                        "challengeCompletionValue": 1200,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner"
                    }
                ]
            },
            {
                "itemId": "4FDB6DFE4E545F793CEF5780D40B84A6",
                "list": [
                    {
                        "challengeId": "AB711C4C4B383070F50016A4C2D8006F",
                        "challengeCompletionValue": 1890,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "F8E2A13648900939B5B086B2D61A6E43",
                "list": [
                    {
                        "challengeId": "624E6D924EB71A58BF6CFB827EE99D40",
                        "challengeCompletionValue": 11340,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "2729DEB04123FAF12B80D2970F6E5C98",
                "list": [
                    {
                        "challengeId": "55C1A7864DF7AB42F7EF1783E095B53C",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates"
                    }
                ]
            },
            {
                "itemId": "AD6D6B384FA0CB8D11149E8CBD2E65CD",
                "list": [
                    {
                        "challengeId": "6AD721414D3CDD85C4D42DBCAC1B5F83",
                        "challengeCompletionValue": 250,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "6BE58FB140091754841745BD81B1CD52",
                "list": [
                    {
                        "challengeId": "112847484561E72A98C392BFCC07B529",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "2D391C604941F465AA4EE7800AEF401F",
                "list": [
                    {
                        "challengeId": "57657766407BB9AF5EA38084D2A1BF31",
                        "challengeCompletionValue": 1,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner"
                    }
                ]
            },
            {
                "itemId": "B9FD9CD4489CDBCA483E96AB689B1FCE",
                "list": [
                    {
                        "challengeId": "98E66E8E4BF296519389949A1F50FAB8",
                        "challengeCompletionValue": 84,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "F732FE3845585D24E94AE39BA12D5E71",
                "list": [
                    {
                        "challengeId": "22639F234C9E4CCCECB7C6ACDD773A8E",
                        "challengeCompletionValue": 11340,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "A925877C4FA6CB2C470D11B7FF487D34",
                "list": [
                    {
                        "challengeId": "8ADE40CD4B61C349AF36BE94E1433006",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner"
                    }
                ]
            },
            {
                "itemId": "9C2F6A4F49A38054D8A3DBB3FF6DC7D6",
                "list": [
                    {
                        "challengeId": "E0C544B9402DE4896523BD905E16ED64",
                        "challengeCompletionValue": 6750,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "B8E6EB014D43FC4E7C5CEDBD530969ED",
                "list": [
                    {
                        "challengeId": "1B98F29341C2D71819B52ABDC37FCD08",
                        "challengeCompletionValue": 44100,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "AD1759374CC44614DCC46DBA60A9C670",
                "list": [
                    {
                        "challengeId": "171025E74F144CB256D0CDA3852E306F",
                        "challengeCompletionValue": 2000,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "D63DC301472FB3505E0E00BB878404C9",
                "list": [
                    {
                        "challengeId": "1F3C3C5548444F2D1DED4FAF9BCDDCFB",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "8438827D44AA0C807A8C85ABA3A9481B",
                "list": [
                    {
                        "challengeId": "72B688754657E294298BAB99D3366661",
                        "challengeCompletionValue": 27,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo"
                    }
                ]
            },
            {
                "itemId": "DF5AEE0248C6F69C140B67A038EFE2C8",
                "list": [
                    {
                        "challengeId": "179FD2EC47F7FC6E91FFB09FBD33B645",
                        "challengeCompletionValue": 4590,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "53954CDB4EB93E44EAB2EA9EF4D9C19C",
                "list": [
                    {
                        "challengeId": "176A1AEE43912906E0DB09AB27C6C420",
                        "challengeCompletionValue": 15,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "ED943B334280F225A7C2AE88B3DC48B9",
                "list": [
                    {
                        "challengeId": "AC57C1734CD39022B74670A6377B5338",
                        "challengeCompletionValue": 350,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "43916EE24C8F0395C826A2960D23AB6B",
                "list": [
                    {
                        "challengeId": "00B6FF4D4C1264D7007B73AF47605B52",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "36CE4DFC412B8FDF255791A609CCBEF4",
                "list": [
                    {
                        "challengeId": "3934DC7F4283AE4ECCF35D94DC3BD23D",
                        "challengeCompletionValue": 21,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "9B9218FB4DE925E6C729FA8162FDB505",
                "list": [
                    {
                        "challengeId": "98E33AD540CB22BB8DC7B6BEE264A789",
                        "challengeCompletionValue": 90,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "75D6E6DF48575AFB5758CAB46C9D7534",
                "list": [
                    {
                        "challengeId": "00F3159149A18ED735900C85887B51D0",
                        "challengeCompletionValue": 6800,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "2A8C0EAD44A5A393CCEE738C2E7409D9",
                "list": [
                    {
                        "challengeId": "0BB4F9F24D28C3C769E730900D2404E5",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "C133B57849D2179835EBC4AA25582CF1",
                "list": [
                    {
                        "challengeId": "BE35D2014ECAFF022CBE08ADF701B3CB",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "89AD14A848DE42DC2A5CAB94BB25FCF9",
                "list": [
                    {
                        "challengeId": "34150BD24607CE5CDCC6C49278466E3A",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "895471FA4A8A74AB2FEE16BF35FC9D04",
                "list": [
                    {
                        "challengeId": "09047C31486F9AE7F599F2A5D7D839E6",
                        "challengeCompletionValue": 756,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner"
                    }
                ]
            },
            {
                "itemId": "D7D7D07B4FB0FABDBF8C3CBE62EB6E96",
                "list": [
                    {
                        "challengeId": "5FA0EFFF4B7EA3A3DC8C87BED87C1E33",
                        "challengeCompletionValue": 3600,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "667B362746F7049D78BFC08A996D2876",
                "list": [
                    {
                        "challengeId": "0A348B4449A2F6359192FD845D49E0E0",
                        "challengeCompletionValue": 4,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "8BF4B8E24F4CD5AB9DEA78851D73A0CC",
                "list": [
                    {
                        "challengeId": "D95AEB6F400965E19E9BFD942EF4EADF",
                        "challengeCompletionValue": 6750,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "A82051B5470DC62447DCB0800F756A9E",
                "list": [
                    {
                        "challengeId": "FEBBC7804EBC5D094D0E258F06DD86F8",
                        "challengeCompletionValue": 350,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            }
        ],
        "prestigeLevel": 0
    },
    "objectId": "RunnerGroupF",
    "schemaVersion": 1,
    "version": 3
}
HunterGroupA = {
    "data": {
        "characterId": {
            "tagName": "Hunter.Stalker"
        },
        "equipment": [
            "5B6E31EA4E175EB002243D8942832223",
            "334A7F0D417F3922E34BBDA4A66A5334",
            "CC59BE294499B62827A639949AB3C2A3",
            "3BB3C4774D87712BF8F6388F14E48FB2",
            "B95774E641C37130DAE2F0A6C5E82C38",
            "667EF1B74448A67A2E1B5EB74B2DBA66"
        ],
        "equippedBonuses": [
            "791F12E047DA9E26E246E3859C3F587E",
            "8A5BF2274640C2F23EF3C996A6F6404D"
        ],
        "equippedPerks": [
            "7CE5AFBF459102E5728DCDAA6F88C0F1",
            "2DBF9B114B82A63940936396CBA68BCD"
        ],
        "equippedPowers": [
            "10A8C667458016646E2EFA9452E3141A",
            "08DC38B6470A7A5B0BA025B96279DAA8",
            "5159591743CBF0B57EC6FEB3341960D6"
        ],
        "equippedWeapons": [
            "364665404243311408F6A0BD4DCE05BD",
            "307A0B13417737DED675309F8B978AB8"
        ],
        "pickedChallenges": [
            {
                "itemId": "ED14BB8240B4AE8124EDA69ECD37AB10",
                "list": [
                    {
                        "challengeId": "4F67D7064B9E706B36EEDABDBAB43AFD",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "72FF4B494F0257218238C695F072D794",
                "list": [
                    {
                        "challengeId": "EB68DD384E4BB1B012E8759F41980EF7",
                        "challengeCompletionValue": 2,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner"
                    }
                ]
            },
            {
                "itemId": "5F89822342D5E60F474080A36A7E6A5D",
                "list": [
                    {
                        "challengeId": "0BC1B3CF4FB218A9437CFABD534AD4F8",
                        "challengeCompletionValue": 270,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Heal_Runner.Challenge_Heal_Runner"
                    }
                ]
            },
            {
                "itemId": "807857C9498AEC6575932689C7733231",
                "list": [
                    {
                        "challengeId": "A7D3E8064C64AF0C80DE24B8988F731E",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner"
                    }
                ]
            },
            {
                "itemId": "0BD046FD439CDEC9DB6B138AF66B849D",
                "list": [
                    {
                        "challengeId": "F8B3276A4FF09F6366A6D19E86F21FAD",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "863513AF4D63B2AF0E70E7B670754E44",
                "list": [
                    {
                        "challengeId": "01601C514D2538D5424C83A14423BCEA",
                        "challengeCompletionValue": 14,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "5A8F3E354CBC6F8B5BD015AB89DE031A",
                "list": [
                    {
                        "challengeId": "9054DF734604F0076336789453A9EBBD",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "51CAE9D747988206193B08BAD648FF96",
                "list": [
                    {
                        "challengeId": "39E81FA4478ED4730F0717ABDFBC77C3",
                        "challengeCompletionValue": 2,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_BloodMode_Runner.Challenge_BloodMode_Runner"
                    }
                ]
            },
            {
                "itemId": "287E08D341A4C1D79E16A086E603A926",
                "list": [
                    {
                        "challengeId": "C500AB104B4D06219DB234B869289E5F",
                        "challengeCompletionValue": 45,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner"
                    }
                ]
            },
            {
                "itemId": "E8CE4B54417D9A6712B4B2927BF49376",
                "list": [
                    {
                        "challengeId": "46E60E174613D6E9E21940BEFC1DFB6F",
                        "challengeCompletionValue": 9450,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner"
                    }
                ]
            },
            {
                "itemId": "25CA213F463F21AC064611925BF357B7",
                "list": [
                    {
                        "challengeId": "032735174748799E27706CB28035567C",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "CBC263344E4D94F5AA1D3AAF46685EA8",
                "list": [
                    {
                        "challengeId": "251FEF7844BF2309631F99B1EB6EB4DD",
                        "challengeCompletionValue": 14,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates"
                    }
                ]
            },
            {
                "itemId": "832CDFB74A4C1A77BF4875BABEB31287",
                "list": [
                    {
                        "challengeId": "0DD143DC4E4AA67B60FACC984D45E31D",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "A0138AA648CE0DF4BBDB969A25C32EB2",
                "list": [
                    {
                        "challengeId": "FA68BDFD413B82B0A7B7109A55BB7127",
                        "challengeCompletionValue": 756,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner"
                    }
                ]
            },
            {
                "itemId": "F501B9E34800BEA6B29CFC87C1584669",
                "list": [
                    {
                        "challengeId": "D758EC434105075A146170B757E174B0",
                        "challengeCompletionValue": 360,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Climb_Runner.Challenge_Climb_Runner"
                    }
                ]
            },
            {
                "itemId": "D5674BD74129FD5F4C36958930CF7252",
                "list": [
                    {
                        "challengeId": "E9A1EE3844569C30E201C8847B30DF2B",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "828C25F148899221FEBD11976BD91551",
                "list": [
                    {
                        "challengeId": "DD4CCDF047F831EFCD876D9AC54DEFEA",
                        "challengeCompletionValue": 5,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "19E643BF4612E414EBE75B8EB069A15A",
                "list": [
                    {
                        "challengeId": "E66EE56F450413191BFEADB828A22D94",
                        "challengeCompletionValue": 105,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "FEE8A7004DC0DDFE1A22AC9156675E92",
                "list": [
                    {
                        "challengeId": "5A2C5CBB416C121FD0DE648271808591",
                        "challengeCompletionValue": 1200,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner"
                    }
                ]
            },
            {
                "itemId": "4FDB6DFE4E545F793CEF5780D40B84A6",
                "list": [
                    {
                        "challengeId": "AB711C4C4B383070F50016A4C2D8006F",
                        "challengeCompletionValue": 1890,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "F8E2A13648900939B5B086B2D61A6E43",
                "list": [
                    {
                        "challengeId": "624E6D924EB71A58BF6CFB827EE99D40",
                        "challengeCompletionValue": 11340,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "2729DEB04123FAF12B80D2970F6E5C98",
                "list": [
                    {
                        "challengeId": "55C1A7864DF7AB42F7EF1783E095B53C",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates"
                    }
                ]
            },
            {
                "itemId": "AD6D6B384FA0CB8D11149E8CBD2E65CD",
                "list": [
                    {
                        "challengeId": "6AD721414D3CDD85C4D42DBCAC1B5F83",
                        "challengeCompletionValue": 250,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "6BE58FB140091754841745BD81B1CD52",
                "list": [
                    {
                        "challengeId": "112847484561E72A98C392BFCC07B529",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "2D391C604941F465AA4EE7800AEF401F",
                "list": [
                    {
                        "challengeId": "57657766407BB9AF5EA38084D2A1BF31",
                        "challengeCompletionValue": 1,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner"
                    }
                ]
            },
            {
                "itemId": "B9FD9CD4489CDBCA483E96AB689B1FCE",
                "list": [
                    {
                        "challengeId": "98E66E8E4BF296519389949A1F50FAB8",
                        "challengeCompletionValue": 84,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "F732FE3845585D24E94AE39BA12D5E71",
                "list": [
                    {
                        "challengeId": "22639F234C9E4CCCECB7C6ACDD773A8E",
                        "challengeCompletionValue": 11340,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "A925877C4FA6CB2C470D11B7FF487D34",
                "list": [
                    {
                        "challengeId": "8ADE40CD4B61C349AF36BE94E1433006",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner"
                    }
                ]
            },
            {
                "itemId": "9C2F6A4F49A38054D8A3DBB3FF6DC7D6",
                "list": [
                    {
                        "challengeId": "E0C544B9402DE4896523BD905E16ED64",
                        "challengeCompletionValue": 6750,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "B8E6EB014D43FC4E7C5CEDBD530969ED",
                "list": [
                    {
                        "challengeId": "1B98F29341C2D71819B52ABDC37FCD08",
                        "challengeCompletionValue": 44100,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "AD1759374CC44614DCC46DBA60A9C670",
                "list": [
                    {
                        "challengeId": "171025E74F144CB256D0CDA3852E306F",
                        "challengeCompletionValue": 2000,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "D63DC301472FB3505E0E00BB878404C9",
                "list": [
                    {
                        "challengeId": "1F3C3C5548444F2D1DED4FAF9BCDDCFB",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "8438827D44AA0C807A8C85ABA3A9481B",
                "list": [
                    {
                        "challengeId": "72B688754657E294298BAB99D3366661",
                        "challengeCompletionValue": 27,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo"
                    }
                ]
            },
            {
                "itemId": "DF5AEE0248C6F69C140B67A038EFE2C8",
                "list": [
                    {
                        "challengeId": "179FD2EC47F7FC6E91FFB09FBD33B645",
                        "challengeCompletionValue": 4590,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "53954CDB4EB93E44EAB2EA9EF4D9C19C",
                "list": [
                    {
                        "challengeId": "176A1AEE43912906E0DB09AB27C6C420",
                        "challengeCompletionValue": 15,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "ED943B334280F225A7C2AE88B3DC48B9",
                "list": [
                    {
                        "challengeId": "AC57C1734CD39022B74670A6377B5338",
                        "challengeCompletionValue": 350,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "43916EE24C8F0395C826A2960D23AB6B",
                "list": [
                    {
                        "challengeId": "00B6FF4D4C1264D7007B73AF47605B52",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "36CE4DFC412B8FDF255791A609CCBEF4",
                "list": [
                    {
                        "challengeId": "3934DC7F4283AE4ECCF35D94DC3BD23D",
                        "challengeCompletionValue": 21,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "9B9218FB4DE925E6C729FA8162FDB505",
                "list": [
                    {
                        "challengeId": "98E33AD540CB22BB8DC7B6BEE264A789",
                        "challengeCompletionValue": 90,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "75D6E6DF48575AFB5758CAB46C9D7534",
                "list": [
                    {
                        "challengeId": "00F3159149A18ED735900C85887B51D0",
                        "challengeCompletionValue": 6800,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "2A8C0EAD44A5A393CCEE738C2E7409D9",
                "list": [
                    {
                        "challengeId": "0BB4F9F24D28C3C769E730900D2404E5",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "C133B57849D2179835EBC4AA25582CF1",
                "list": [
                    {
                        "challengeId": "BE35D2014ECAFF022CBE08ADF701B3CB",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "89AD14A848DE42DC2A5CAB94BB25FCF9",
                "list": [
                    {
                        "challengeId": "34150BD24607CE5CDCC6C49278466E3A",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "895471FA4A8A74AB2FEE16BF35FC9D04",
                "list": [
                    {
                        "challengeId": "09047C31486F9AE7F599F2A5D7D839E6",
                        "challengeCompletionValue": 756,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner"
                    }
                ]
            },
            {
                "itemId": "D7D7D07B4FB0FABDBF8C3CBE62EB6E96",
                "list": [
                    {
                        "challengeId": "5FA0EFFF4B7EA3A3DC8C87BED87C1E33",
                        "challengeCompletionValue": 3600,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "667B362746F7049D78BFC08A996D2876",
                "list": [
                    {
                        "challengeId": "0A348B4449A2F6359192FD845D49E0E0",
                        "challengeCompletionValue": 4,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "8BF4B8E24F4CD5AB9DEA78851D73A0CC",
                "list": [
                    {
                        "challengeId": "D95AEB6F400965E19E9BFD942EF4EADF",
                        "challengeCompletionValue": 6750,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "A82051B5470DC62447DCB0800F756A9E",
                "list": [
                    {
                        "challengeId": "FEBBC7804EBC5D094D0E258F06DD86F8",
                        "challengeCompletionValue": 350,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            }
        ],
        "prestigeLevel": 0
    },
    "objectId": "HunterGroupA",
    "schemaVersion": 1,
    "version": 3
}
HunterGroupB = {
    "data": {
        "characterId": {
            "tagName": "Hunter.Inquisitor"
        },
        "equipment": [
            "6B1B9949479BFD2B75E137AFFF3DBBD4",
            "54526C4A4FF83835E02711B308AA80F5",
            "5C4F9FC84B0CAE9CF00423A6768AEA23",
            "611F4DCB4A5C38EC4E423DB512CD9DC6",
            "3B3BC3704395FAF545A97CBF8F601901",
            "24D5F6164191358D93B8E5BDFFE763F1"
        ],
        "equippedBonuses": [
            "1098BEE241B1515B44013A87EDB16BDC",
            "EDB6D6B742023AE61AD8718CAC073C0E"
        ],
        "equippedPerks": [
            "F055513D48AACBAC280B2AA00A984180",
            "5998C1C548AB7BDA80C87295F2764C5D"
        ],
        "equippedPowers": [
            "7902D836470BBB49DE9B9D97F17C9DB5",
            "08DC38B6470A7A5B0BA025B96279DAA8",
            "5159591743CBF0B57EC6FEB3341960D6"
        ],
        "equippedWeapons": [
            "50D3005B437066E4C4D99F9397CF1B0B",
            "973C9176404A29F926D13BACB76A2425"
        ],
        "pickedChallenges": [
            {
                "itemId": "ED14BB8240B4AE8124EDA69ECD37AB10",
                "list": [
                    {
                        "challengeId": "4F67D7064B9E706B36EEDABDBAB43AFD",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "72FF4B494F0257218238C695F072D794",
                "list": [
                    {
                        "challengeId": "EB68DD384E4BB1B012E8759F41980EF7",
                        "challengeCompletionValue": 2,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner"
                    }
                ]
            },
            {
                "itemId": "5F89822342D5E60F474080A36A7E6A5D",
                "list": [
                    {
                        "challengeId": "0BC1B3CF4FB218A9437CFABD534AD4F8",
                        "challengeCompletionValue": 270,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Heal_Runner.Challenge_Heal_Runner"
                    }
                ]
            },
            {
                "itemId": "807857C9498AEC6575932689C7733231",
                "list": [
                    {
                        "challengeId": "A7D3E8064C64AF0C80DE24B8988F731E",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner"
                    }
                ]
            },
            {
                "itemId": "0BD046FD439CDEC9DB6B138AF66B849D",
                "list": [
                    {
                        "challengeId": "F8B3276A4FF09F6366A6D19E86F21FAD",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "863513AF4D63B2AF0E70E7B670754E44",
                "list": [
                    {
                        "challengeId": "01601C514D2538D5424C83A14423BCEA",
                        "challengeCompletionValue": 14,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "5A8F3E354CBC6F8B5BD015AB89DE031A",
                "list": [
                    {
                        "challengeId": "9054DF734604F0076336789453A9EBBD",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "51CAE9D747988206193B08BAD648FF96",
                "list": [
                    {
                        "challengeId": "39E81FA4478ED4730F0717ABDFBC77C3",
                        "challengeCompletionValue": 2,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_BloodMode_Runner.Challenge_BloodMode_Runner"
                    }
                ]
            },
            {
                "itemId": "287E08D341A4C1D79E16A086E603A926",
                "list": [
                    {
                        "challengeId": "C500AB104B4D06219DB234B869289E5F",
                        "challengeCompletionValue": 45,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner"
                    }
                ]
            },
            {
                "itemId": "E8CE4B54417D9A6712B4B2927BF49376",
                "list": [
                    {
                        "challengeId": "46E60E174613D6E9E21940BEFC1DFB6F",
                        "challengeCompletionValue": 9450,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner"
                    }
                ]
            },
            {
                "itemId": "25CA213F463F21AC064611925BF357B7",
                "list": [
                    {
                        "challengeId": "032735174748799E27706CB28035567C",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "CBC263344E4D94F5AA1D3AAF46685EA8",
                "list": [
                    {
                        "challengeId": "251FEF7844BF2309631F99B1EB6EB4DD",
                        "challengeCompletionValue": 14,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates"
                    }
                ]
            },
            {
                "itemId": "832CDFB74A4C1A77BF4875BABEB31287",
                "list": [
                    {
                        "challengeId": "0DD143DC4E4AA67B60FACC984D45E31D",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "A0138AA648CE0DF4BBDB969A25C32EB2",
                "list": [
                    {
                        "challengeId": "FA68BDFD413B82B0A7B7109A55BB7127",
                        "challengeCompletionValue": 756,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner"
                    }
                ]
            },
            {
                "itemId": "F501B9E34800BEA6B29CFC87C1584669",
                "list": [
                    {
                        "challengeId": "D758EC434105075A146170B757E174B0",
                        "challengeCompletionValue": 360,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Climb_Runner.Challenge_Climb_Runner"
                    }
                ]
            },
            {
                "itemId": "D5674BD74129FD5F4C36958930CF7252",
                "list": [
                    {
                        "challengeId": "E9A1EE3844569C30E201C8847B30DF2B",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "828C25F148899221FEBD11976BD91551",
                "list": [
                    {
                        "challengeId": "DD4CCDF047F831EFCD876D9AC54DEFEA",
                        "challengeCompletionValue": 5,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "19E643BF4612E414EBE75B8EB069A15A",
                "list": [
                    {
                        "challengeId": "E66EE56F450413191BFEADB828A22D94",
                        "challengeCompletionValue": 105,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "FEE8A7004DC0DDFE1A22AC9156675E92",
                "list": [
                    {
                        "challengeId": "5A2C5CBB416C121FD0DE648271808591",
                        "challengeCompletionValue": 1200,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner"
                    }
                ]
            },
            {
                "itemId": "4FDB6DFE4E545F793CEF5780D40B84A6",
                "list": [
                    {
                        "challengeId": "AB711C4C4B383070F50016A4C2D8006F",
                        "challengeCompletionValue": 1890,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "F8E2A13648900939B5B086B2D61A6E43",
                "list": [
                    {
                        "challengeId": "624E6D924EB71A58BF6CFB827EE99D40",
                        "challengeCompletionValue": 11340,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "2729DEB04123FAF12B80D2970F6E5C98",
                "list": [
                    {
                        "challengeId": "55C1A7864DF7AB42F7EF1783E095B53C",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates"
                    }
                ]
            },
            {
                "itemId": "AD6D6B384FA0CB8D11149E8CBD2E65CD",
                "list": [
                    {
                        "challengeId": "6AD721414D3CDD85C4D42DBCAC1B5F83",
                        "challengeCompletionValue": 250,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "6BE58FB140091754841745BD81B1CD52",
                "list": [
                    {
                        "challengeId": "112847484561E72A98C392BFCC07B529",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "2D391C604941F465AA4EE7800AEF401F",
                "list": [
                    {
                        "challengeId": "57657766407BB9AF5EA38084D2A1BF31",
                        "challengeCompletionValue": 1,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner"
                    }
                ]
            },
            {
                "itemId": "B9FD9CD4489CDBCA483E96AB689B1FCE",
                "list": [
                    {
                        "challengeId": "98E66E8E4BF296519389949A1F50FAB8",
                        "challengeCompletionValue": 84,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "F732FE3845585D24E94AE39BA12D5E71",
                "list": [
                    {
                        "challengeId": "22639F234C9E4CCCECB7C6ACDD773A8E",
                        "challengeCompletionValue": 11340,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "A925877C4FA6CB2C470D11B7FF487D34",
                "list": [
                    {
                        "challengeId": "8ADE40CD4B61C349AF36BE94E1433006",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner"
                    }
                ]
            },
            {
                "itemId": "9C2F6A4F49A38054D8A3DBB3FF6DC7D6",
                "list": [
                    {
                        "challengeId": "E0C544B9402DE4896523BD905E16ED64",
                        "challengeCompletionValue": 6750,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "B8E6EB014D43FC4E7C5CEDBD530969ED",
                "list": [
                    {
                        "challengeId": "1B98F29341C2D71819B52ABDC37FCD08",
                        "challengeCompletionValue": 44100,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "AD1759374CC44614DCC46DBA60A9C670",
                "list": [
                    {
                        "challengeId": "171025E74F144CB256D0CDA3852E306F",
                        "challengeCompletionValue": 2000,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "D63DC301472FB3505E0E00BB878404C9",
                "list": [
                    {
                        "challengeId": "1F3C3C5548444F2D1DED4FAF9BCDDCFB",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "8438827D44AA0C807A8C85ABA3A9481B",
                "list": [
                    {
                        "challengeId": "72B688754657E294298BAB99D3366661",
                        "challengeCompletionValue": 27,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo"
                    }
                ]
            },
            {
                "itemId": "DF5AEE0248C6F69C140B67A038EFE2C8",
                "list": [
                    {
                        "challengeId": "179FD2EC47F7FC6E91FFB09FBD33B645",
                        "challengeCompletionValue": 4590,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "53954CDB4EB93E44EAB2EA9EF4D9C19C",
                "list": [
                    {
                        "challengeId": "176A1AEE43912906E0DB09AB27C6C420",
                        "challengeCompletionValue": 15,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "ED943B334280F225A7C2AE88B3DC48B9",
                "list": [
                    {
                        "challengeId": "AC57C1734CD39022B74670A6377B5338",
                        "challengeCompletionValue": 350,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "43916EE24C8F0395C826A2960D23AB6B",
                "list": [
                    {
                        "challengeId": "00B6FF4D4C1264D7007B73AF47605B52",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "36CE4DFC412B8FDF255791A609CCBEF4",
                "list": [
                    {
                        "challengeId": "3934DC7F4283AE4ECCF35D94DC3BD23D",
                        "challengeCompletionValue": 21,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "9B9218FB4DE925E6C729FA8162FDB505",
                "list": [
                    {
                        "challengeId": "98E33AD540CB22BB8DC7B6BEE264A789",
                        "challengeCompletionValue": 90,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "75D6E6DF48575AFB5758CAB46C9D7534",
                "list": [
                    {
                        "challengeId": "00F3159149A18ED735900C85887B51D0",
                        "challengeCompletionValue": 6800,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "2A8C0EAD44A5A393CCEE738C2E7409D9",
                "list": [
                    {
                        "challengeId": "0BB4F9F24D28C3C769E730900D2404E5",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "C133B57849D2179835EBC4AA25582CF1",
                "list": [
                    {
                        "challengeId": "BE35D2014ECAFF022CBE08ADF701B3CB",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "89AD14A848DE42DC2A5CAB94BB25FCF9",
                "list": [
                    {
                        "challengeId": "34150BD24607CE5CDCC6C49278466E3A",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "895471FA4A8A74AB2FEE16BF35FC9D04",
                "list": [
                    {
                        "challengeId": "09047C31486F9AE7F599F2A5D7D839E6",
                        "challengeCompletionValue": 756,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner"
                    }
                ]
            },
            {
                "itemId": "D7D7D07B4FB0FABDBF8C3CBE62EB6E96",
                "list": [
                    {
                        "challengeId": "5FA0EFFF4B7EA3A3DC8C87BED87C1E33",
                        "challengeCompletionValue": 3600,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "667B362746F7049D78BFC08A996D2876",
                "list": [
                    {
                        "challengeId": "0A348B4449A2F6359192FD845D49E0E0",
                        "challengeCompletionValue": 4,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "8BF4B8E24F4CD5AB9DEA78851D73A0CC",
                "list": [
                    {
                        "challengeId": "D95AEB6F400965E19E9BFD942EF4EADF",
                        "challengeCompletionValue": 6750,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "A82051B5470DC62447DCB0800F756A9E",
                "list": [
                    {
                        "challengeId": "FEBBC7804EBC5D094D0E258F06DD86F8",
                        "challengeCompletionValue": 350,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            }
        ],
        "prestigeLevel": 0
    },
    "objectId": "HunterGroupB",
    "schemaVersion": 1,
    "version": 3
}
HunterGroupC = {
    "data": {
        "characterId": {
            "tagName": "Hunter.Poacher"
        },
        "equipment": [
            "0398A38946C5FD3871B10A9E6B4B2BEC",
            "B83713F044EED4FB220F2F9337AD14A2",
            "4F563EB64882529F0CC42397CCCCB4A4",
            "9373067D4895DE2C33EFBA8711F6E1D6",
            "D91835664F2FAD7765BCF78B18CA9082",
            "AA25DA8543EDF88C233713B438B43365"
        ],
        "equippedBonuses": [
            "6BE28177483A89CF00B2FD839726ACE1",
            "4431395744543533907B099952F81510"
        ],
        "equippedPerks": [
            "EB90A75F44EA4D821B385EA00B45E1BE",
            "305F597C424FDD0A0A6B2BB6CF5CC542"
        ],
        "equippedPowers": [
            "D14477DA4ED69E001DC36ABCEA0B42BC",
            "08DC38B6470A7A5B0BA025B96279DAA8",
            "5159591743CBF0B57EC6FEB3341960D6"
        ],
        "equippedWeapons": [
            "89A14A794CD70E50ADFEB497B89E4381",
            "738CFAEB44A48BF6DA5F109C50068BE3"
        ],
        "pickedChallenges": [
            {
                "itemId": "ED14BB8240B4AE8124EDA69ECD37AB10",
                "list": [
                    {
                        "challengeId": "4F67D7064B9E706B36EEDABDBAB43AFD",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "72FF4B494F0257218238C695F072D794",
                "list": [
                    {
                        "challengeId": "EB68DD384E4BB1B012E8759F41980EF7",
                        "challengeCompletionValue": 2,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner"
                    }
                ]
            },
            {
                "itemId": "5F89822342D5E60F474080A36A7E6A5D",
                "list": [
                    {
                        "challengeId": "0BC1B3CF4FB218A9437CFABD534AD4F8",
                        "challengeCompletionValue": 270,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Heal_Runner.Challenge_Heal_Runner"
                    }
                ]
            },
            {
                "itemId": "807857C9498AEC6575932689C7733231",
                "list": [
                    {
                        "challengeId": "A7D3E8064C64AF0C80DE24B8988F731E",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner"
                    }
                ]
            },
            {
                "itemId": "0BD046FD439CDEC9DB6B138AF66B849D",
                "list": [
                    {
                        "challengeId": "F8B3276A4FF09F6366A6D19E86F21FAD",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "863513AF4D63B2AF0E70E7B670754E44",
                "list": [
                    {
                        "challengeId": "01601C514D2538D5424C83A14423BCEA",
                        "challengeCompletionValue": 14,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "5A8F3E354CBC6F8B5BD015AB89DE031A",
                "list": [
                    {
                        "challengeId": "9054DF734604F0076336789453A9EBBD",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "51CAE9D747988206193B08BAD648FF96",
                "list": [
                    {
                        "challengeId": "39E81FA4478ED4730F0717ABDFBC77C3",
                        "challengeCompletionValue": 2,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_BloodMode_Runner.Challenge_BloodMode_Runner"
                    }
                ]
            },
            {
                "itemId": "287E08D341A4C1D79E16A086E603A926",
                "list": [
                    {
                        "challengeId": "C500AB104B4D06219DB234B869289E5F",
                        "challengeCompletionValue": 45,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner"
                    }
                ]
            },
            {
                "itemId": "E8CE4B54417D9A6712B4B2927BF49376",
                "list": [
                    {
                        "challengeId": "46E60E174613D6E9E21940BEFC1DFB6F",
                        "challengeCompletionValue": 9450,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner"
                    }
                ]
            },
            {
                "itemId": "25CA213F463F21AC064611925BF357B7",
                "list": [
                    {
                        "challengeId": "032735174748799E27706CB28035567C",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "CBC263344E4D94F5AA1D3AAF46685EA8",
                "list": [
                    {
                        "challengeId": "251FEF7844BF2309631F99B1EB6EB4DD",
                        "challengeCompletionValue": 14,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates"
                    }
                ]
            },
            {
                "itemId": "832CDFB74A4C1A77BF4875BABEB31287",
                "list": [
                    {
                        "challengeId": "0DD143DC4E4AA67B60FACC984D45E31D",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "A0138AA648CE0DF4BBDB969A25C32EB2",
                "list": [
                    {
                        "challengeId": "FA68BDFD413B82B0A7B7109A55BB7127",
                        "challengeCompletionValue": 756,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner"
                    }
                ]
            },
            {
                "itemId": "F501B9E34800BEA6B29CFC87C1584669",
                "list": [
                    {
                        "challengeId": "D758EC434105075A146170B757E174B0",
                        "challengeCompletionValue": 360,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Climb_Runner.Challenge_Climb_Runner"
                    }
                ]
            },
            {
                "itemId": "D5674BD74129FD5F4C36958930CF7252",
                "list": [
                    {
                        "challengeId": "E9A1EE3844569C30E201C8847B30DF2B",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "828C25F148899221FEBD11976BD91551",
                "list": [
                    {
                        "challengeId": "DD4CCDF047F831EFCD876D9AC54DEFEA",
                        "challengeCompletionValue": 5,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "19E643BF4612E414EBE75B8EB069A15A",
                "list": [
                    {
                        "challengeId": "E66EE56F450413191BFEADB828A22D94",
                        "challengeCompletionValue": 105,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "FEE8A7004DC0DDFE1A22AC9156675E92",
                "list": [
                    {
                        "challengeId": "5A2C5CBB416C121FD0DE648271808591",
                        "challengeCompletionValue": 1200,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner"
                    }
                ]
            },
            {
                "itemId": "4FDB6DFE4E545F793CEF5780D40B84A6",
                "list": [
                    {
                        "challengeId": "AB711C4C4B383070F50016A4C2D8006F",
                        "challengeCompletionValue": 1890,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "F8E2A13648900939B5B086B2D61A6E43",
                "list": [
                    {
                        "challengeId": "624E6D924EB71A58BF6CFB827EE99D40",
                        "challengeCompletionValue": 11340,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "2729DEB04123FAF12B80D2970F6E5C98",
                "list": [
                    {
                        "challengeId": "55C1A7864DF7AB42F7EF1783E095B53C",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates"
                    }
                ]
            },
            {
                "itemId": "AD6D6B384FA0CB8D11149E8CBD2E65CD",
                "list": [
                    {
                        "challengeId": "6AD721414D3CDD85C4D42DBCAC1B5F83",
                        "challengeCompletionValue": 250,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "6BE58FB140091754841745BD81B1CD52",
                "list": [
                    {
                        "challengeId": "112847484561E72A98C392BFCC07B529",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "2D391C604941F465AA4EE7800AEF401F",
                "list": [
                    {
                        "challengeId": "57657766407BB9AF5EA38084D2A1BF31",
                        "challengeCompletionValue": 1,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner"
                    }
                ]
            },
            {
                "itemId": "B9FD9CD4489CDBCA483E96AB689B1FCE",
                "list": [
                    {
                        "challengeId": "98E66E8E4BF296519389949A1F50FAB8",
                        "challengeCompletionValue": 84,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "F732FE3845585D24E94AE39BA12D5E71",
                "list": [
                    {
                        "challengeId": "22639F234C9E4CCCECB7C6ACDD773A8E",
                        "challengeCompletionValue": 11340,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "A925877C4FA6CB2C470D11B7FF487D34",
                "list": [
                    {
                        "challengeId": "8ADE40CD4B61C349AF36BE94E1433006",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner"
                    }
                ]
            },
            {
                "itemId": "9C2F6A4F49A38054D8A3DBB3FF6DC7D6",
                "list": [
                    {
                        "challengeId": "E0C544B9402DE4896523BD905E16ED64",
                        "challengeCompletionValue": 6750,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "B8E6EB014D43FC4E7C5CEDBD530969ED",
                "list": [
                    {
                        "challengeId": "1B98F29341C2D71819B52ABDC37FCD08",
                        "challengeCompletionValue": 44100,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "AD1759374CC44614DCC46DBA60A9C670",
                "list": [
                    {
                        "challengeId": "171025E74F144CB256D0CDA3852E306F",
                        "challengeCompletionValue": 2000,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "D63DC301472FB3505E0E00BB878404C9",
                "list": [
                    {
                        "challengeId": "1F3C3C5548444F2D1DED4FAF9BCDDCFB",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "8438827D44AA0C807A8C85ABA3A9481B",
                "list": [
                    {
                        "challengeId": "72B688754657E294298BAB99D3366661",
                        "challengeCompletionValue": 27,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo"
                    }
                ]
            },
            {
                "itemId": "DF5AEE0248C6F69C140B67A038EFE2C8",
                "list": [
                    {
                        "challengeId": "179FD2EC47F7FC6E91FFB09FBD33B645",
                        "challengeCompletionValue": 4590,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "53954CDB4EB93E44EAB2EA9EF4D9C19C",
                "list": [
                    {
                        "challengeId": "176A1AEE43912906E0DB09AB27C6C420",
                        "challengeCompletionValue": 15,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "ED943B334280F225A7C2AE88B3DC48B9",
                "list": [
                    {
                        "challengeId": "AC57C1734CD39022B74670A6377B5338",
                        "challengeCompletionValue": 350,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "43916EE24C8F0395C826A2960D23AB6B",
                "list": [
                    {
                        "challengeId": "00B6FF4D4C1264D7007B73AF47605B52",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "36CE4DFC412B8FDF255791A609CCBEF4",
                "list": [
                    {
                        "challengeId": "3934DC7F4283AE4ECCF35D94DC3BD23D",
                        "challengeCompletionValue": 21,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "9B9218FB4DE925E6C729FA8162FDB505",
                "list": [
                    {
                        "challengeId": "98E33AD540CB22BB8DC7B6BEE264A789",
                        "challengeCompletionValue": 90,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "75D6E6DF48575AFB5758CAB46C9D7534",
                "list": [
                    {
                        "challengeId": "00F3159149A18ED735900C85887B51D0",

                        "challengeCompletionValue": 6800,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "2A8C0EAD44A5A393CCEE738C2E7409D9",
                "list": [
                    {
                        "challengeId": "0BB4F9F24D28C3C769E730900D2404E5",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "C133B57849D2179835EBC4AA25582CF1",
                "list": [
                    {
                        "challengeId": "BE35D2014ECAFF022CBE08ADF701B3CB",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "89AD14A848DE42DC2A5CAB94BB25FCF9",
                "list": [
                    {
                        "challengeId": "34150BD24607CE5CDCC6C49278466E3A",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "895471FA4A8A74AB2FEE16BF35FC9D04",
                "list": [
                    {
                        "challengeId": "09047C31486F9AE7F599F2A5D7D839E6",
                        "challengeCompletionValue": 756,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner"
                    }
                ]
            },
            {
                "itemId": "D7D7D07B4FB0FABDBF8C3CBE62EB6E96",
                "list": [
                    {
                        "challengeId": "5FA0EFFF4B7EA3A3DC8C87BED87C1E33",
                        "challengeCompletionValue": 3600,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "667B362746F7049D78BFC08A996D2876",
                "list": [
                    {
                        "challengeId": "0A348B4449A2F6359192FD845D49E0E0",
                        "challengeCompletionValue": 4,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "8BF4B8E24F4CD5AB9DEA78851D73A0CC",
                "list": [
                    {
                        "challengeId": "D95AEB6F400965E19E9BFD942EF4EADF",
                        "challengeCompletionValue": 6750,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "A82051B5470DC62447DCB0800F756A9E",
                "list": [
                    {
                        "challengeId": "FEBBC7804EBC5D094D0E258F06DD86F8",
                        "challengeCompletionValue": 350,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            }
        ],
        "prestigeLevel": 0
    },
    "objectId": "HunterGroupC",
    "schemaVersion": 1,
    "version": 3
}
HunterGroupD = {
    "data": {
        "characterId": {
            "tagName": "Hunter.Mass"
        },
        "equipment": [
            "5CBD38644EA136989CB0E3BBF4A8E54B",
            "321B9FA34B4497CA94F1CDB007735A57",
            "525F6BE644576B3832ED77A10193F8A3",
            "F01A992E429392A4F839FD93C25B34DB",
            "9109796A49930831B017B3994A9F22EA",
            "C814E8904A7C9D9A2F2594A3153E77A0"
        ],
        "equippedBonuses": [
            "172080544A05F838E2473790FDF4873A",
            "3D377249421D35F0F750578919A7E210"
        ],
        "equippedPerks": [
            "3C9D2E0A44ED015979667DBA4F080B49",
            "AA00BB584A47234168A63D9F14C4C4E8"
        ],
        "equippedPowers": [
            "7A541DCB4F04DAB2E10FAB84395BB967",
            "08DC38B6470A7A5B0BA025B96279DAA8",
            "0703E3634B0E4409623E2D8C06B14C79"
        ],
        "equippedWeapons": [
            "6562B26B48C9C791C82A3EAE344EBEE1",
            "0606F8464D4C7EB70601CC84C50BCAC6"
        ],
        "pickedChallenges": [
            {
                "itemId": "ED14BB8240B4AE8124EDA69ECD37AB10",
                "list": [
                    {
                        "challengeId": "4F67D7064B9E706B36EEDABDBAB43AFD",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "72FF4B494F0257218238C695F072D794",
                "list": [
                    {
                        "challengeId": "EB68DD384E4BB1B012E8759F41980EF7",
                        "challengeCompletionValue": 2,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner"
                    }
                ]
            },
            {
                "itemId": "5F89822342D5E60F474080A36A7E6A5D",
                "list": [
                    {
                        "challengeId": "0BC1B3CF4FB218A9437CFABD534AD4F8",
                        "challengeCompletionValue": 270,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Heal_Runner.Challenge_Heal_Runner"
                    }
                ]
            },
            {
                "itemId": "807857C9498AEC6575932689C7733231",
                "list": [
                    {
                        "challengeId": "A7D3E8064C64AF0C80DE24B8988F731E",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner"
                    }
                ]
            },
            {
                "itemId": "0BD046FD439CDEC9DB6B138AF66B849D",
                "list": [
                    {
                        "challengeId": "F8B3276A4FF09F6366A6D19E86F21FAD",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "863513AF4D63B2AF0E70E7B670754E44",
                "list": [
                    {
                        "challengeId": "01601C514D2538D5424C83A14423BCEA",
                        "challengeCompletionValue": 14,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "5A8F3E354CBC6F8B5BD015AB89DE031A",
                "list": [
                    {
                        "challengeId": "9054DF734604F0076336789453A9EBBD",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "51CAE9D747988206193B08BAD648FF96",
                "list": [
                    {
                        "challengeId": "39E81FA4478ED4730F0717ABDFBC77C3",
                        "challengeCompletionValue": 2,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_BloodMode_Runner.Challenge_BloodMode_Runner"
                    }
                ]
            },
            {
                "itemId": "287E08D341A4C1D79E16A086E603A926",
                "list": [
                    {
                        "challengeId": "C500AB104B4D06219DB234B869289E5F",
                        "challengeCompletionValue": 45,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner"
                    }
                ]
            },
            {
                "itemId": "E8CE4B54417D9A6712B4B2927BF49376",
                "list": [
                    {
                        "challengeId": "46E60E174613D6E9E21940BEFC1DFB6F",
                        "challengeCompletionValue": 9450,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner"
                    }
                ]
            },
            {
                "itemId": "25CA213F463F21AC064611925BF357B7",
                "list": [
                    {
                        "challengeId": "032735174748799E27706CB28035567C",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "CBC263344E4D94F5AA1D3AAF46685EA8",
                "list": [
                    {
                        "challengeId": "251FEF7844BF2309631F99B1EB6EB4DD",
                        "challengeCompletionValue": 14,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates"
                    }
                ]
            },
            {
                "itemId": "832CDFB74A4C1A77BF4875BABEB31287",
                "list": [
                    {
                        "challengeId": "0DD143DC4E4AA67B60FACC984D45E31D",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "A0138AA648CE0DF4BBDB969A25C32EB2",
                "list": [
                    {
                        "challengeId": "FA68BDFD413B82B0A7B7109A55BB7127",
                        "challengeCompletionValue": 756,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner"
                    }
                ]
            },
            {
                "itemId": "F501B9E34800BEA6B29CFC87C1584669",
                "list": [
                    {
                        "challengeId": "D758EC434105075A146170B757E174B0",
                        "challengeCompletionValue": 360,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Climb_Runner.Challenge_Climb_Runner"
                    }
                ]
            },
            {
                "itemId": "D5674BD74129FD5F4C36958930CF7252",
                "list": [
                    {
                        "challengeId": "E9A1EE3844569C30E201C8847B30DF2B",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "828C25F148899221FEBD11976BD91551",
                "list": [
                    {
                        "challengeId": "DD4CCDF047F831EFCD876D9AC54DEFEA",
                        "challengeCompletionValue": 5,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "19E643BF4612E414EBE75B8EB069A15A",
                "list": [
                    {
                        "challengeId": "E66EE56F450413191BFEADB828A22D94",
                        "challengeCompletionValue": 105,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "FEE8A7004DC0DDFE1A22AC9156675E92",
                "list": [
                    {
                        "challengeId": "5A2C5CBB416C121FD0DE648271808591",
                        "challengeCompletionValue": 1200,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner"
                    }
                ]
            },
            {
                "itemId": "4FDB6DFE4E545F793CEF5780D40B84A6",
                "list": [
                    {
                        "challengeId": "AB711C4C4B383070F50016A4C2D8006F",
                        "challengeCompletionValue": 1890,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "F8E2A13648900939B5B086B2D61A6E43",
                "list": [
                    {
                        "challengeId": "624E6D924EB71A58BF6CFB827EE99D40",
                        "challengeCompletionValue": 11340,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "2729DEB04123FAF12B80D2970F6E5C98",
                "list": [
                    {
                        "challengeId": "55C1A7864DF7AB42F7EF1783E095B53C",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates"
                    }
                ]
            },
            {
                "itemId": "AD6D6B384FA0CB8D11149E8CBD2E65CD",
                "list": [
                    {
                        "challengeId": "6AD721414D3CDD85C4D42DBCAC1B5F83",
                        "challengeCompletionValue": 250,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "6BE58FB140091754841745BD81B1CD52",
                "list": [
                    {
                        "challengeId": "112847484561E72A98C392BFCC07B529",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "2D391C604941F465AA4EE7800AEF401F",
                "list": [
                    {
                        "challengeId": "57657766407BB9AF5EA38084D2A1BF31",
                        "challengeCompletionValue": 1,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner"
                    }
                ]
            },
            {
                "itemId": "B9FD9CD4489CDBCA483E96AB689B1FCE",
                "list": [
                    {
                        "challengeId": "98E66E8E4BF296519389949A1F50FAB8",
                        "challengeCompletionValue": 84,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "F732FE3845585D24E94AE39BA12D5E71",
                "list": [
                    {
                        "challengeId": "22639F234C9E4CCCECB7C6ACDD773A8E",
                        "challengeCompletionValue": 11340,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "A925877C4FA6CB2C470D11B7FF487D34",
                "list": [
                    {
                        "challengeId": "8ADE40CD4B61C349AF36BE94E1433006",
                        "challengeCompletionValue": 51,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner"
                    }
                ]
            },
            {
                "itemId": "9C2F6A4F49A38054D8A3DBB3FF6DC7D6",
                "list": [
                    {
                        "challengeId": "E0C544B9402DE4896523BD905E16ED64",
                        "challengeCompletionValue": 6750,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "B8E6EB014D43FC4E7C5CEDBD530969ED",
                "list": [
                    {
                        "challengeId": "1B98F29341C2D71819B52ABDC37FCD08",
                        "challengeCompletionValue": 44100,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner"
                    }
                ]
            },
            {
                "itemId": "AD1759374CC44614DCC46DBA60A9C670",
                "list": [
                    {
                        "challengeId": "171025E74F144CB256D0CDA3852E306F",
                        "challengeCompletionValue": 2000,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "D63DC301472FB3505E0E00BB878404C9",
                "list": [
                    {
                        "challengeId": "1F3C3C5548444F2D1DED4FAF9BCDDCFB",
                        "challengeCompletionValue": 3,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "8438827D44AA0C807A8C85ABA3A9481B",
                "list": [
                    {
                        "challengeId": "72B688754657E294298BAB99D3366661",
                        "challengeCompletionValue": 27,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo"
                    }
                ]
            },
            {
                "itemId": "DF5AEE0248C6F69C140B67A038EFE2C8",
                "list": [
                    {
                        "challengeId": "179FD2EC47F7FC6E91FFB09FBD33B645",
                        "challengeCompletionValue": 4590,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "53954CDB4EB93E44EAB2EA9EF4D9C19C",
                "list": [
                    {
                        "challengeId": "176A1AEE43912906E0DB09AB27C6C420",
                        "challengeCompletionValue": 15,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner"
                    }
                ]
            },
            {
                "itemId": "ED943B334280F225A7C2AE88B3DC48B9",
                "list": [
                    {
                        "challengeId": "AC57C1734CD39022B74670A6377B5338",
                        "challengeCompletionValue": 350,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "43916EE24C8F0395C826A2960D23AB6B",
                "list": [
                    {
                        "challengeId": "00B6FF4D4C1264D7007B73AF47605B52",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "36CE4DFC412B8FDF255791A609CCBEF4",
                "list": [
                    {
                        "challengeId": "3934DC7F4283AE4ECCF35D94DC3BD23D",
                        "challengeCompletionValue": 21,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner"
                    }
                ]
            },
            {
                "itemId": "9B9218FB4DE925E6C729FA8162FDB505",
                "list": [
                    {
                        "challengeId": "98E33AD540CB22BB8DC7B6BEE264A789",
                        "challengeCompletionValue": 90,
                        "challengeAsset": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner"
                    }
                ]
            },
            {
                "itemId": "75D6E6DF48575AFB5758CAB46C9D7534",
                "list": [
                    {
                        "challengeId": "00F3159149A18ED735900C85887B51D0",
                        "challengeCompletionValue": 6800,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "2A8C0EAD44A5A393CCEE738C2E7409D9",
                "list": [
                    {
                        "challengeId": "0BB4F9F24D28C3C769E730900D2404E5",
                        "challengeCompletionValue": 300,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner"
                    }
                ]
            },
            {
                "itemId": "C133B57849D2179835EBC4AA25582CF1",
                "list": [
                    {
                        "challengeId": "BE35D2014ECAFF022CBE08ADF701B3CB",
                        "challengeCompletionValue": 7,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "89AD14A848DE42DC2A5CAB94BB25FCF9",
                "list": [
                    {
                        "challengeId": "34150BD24607CE5CDCC6C49278466E3A",
                        "challengeCompletionValue": 50,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            },
            {
                "itemId": "895471FA4A8A74AB2FEE16BF35FC9D04",
                "list": [
                    {
                        "challengeId": "09047C31486F9AE7F599F2A5D7D839E6",
                        "challengeCompletionValue": 756,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner"
                    }
                ]
            },
            {
                "itemId": "D7D7D07B4FB0FABDBF8C3CBE62EB6E96",
                "list": [
                    {
                        "challengeId": "5FA0EFFF4B7EA3A3DC8C87BED87C1E33",
                        "challengeCompletionValue": 3600,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner"
                    }
                ]
            },
            {
                "itemId": "667B362746F7049D78BFC08A996D2876",
                "list": [
                    {
                        "challengeId": "0A348B4449A2F6359192FD845D49E0E0",
                        "challengeCompletionValue": 4,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner"
                    }
                ]
            },
            {
                "itemId": "8BF4B8E24F4CD5AB9DEA78851D73A0CC",
                "list": [
                    {
                        "challengeId": "D95AEB6F400965E19E9BFD942EF4EADF",
                        "challengeCompletionValue": 6750,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner"
                    }
                ]
            },
            {
                "itemId": "A82051B5470DC62447DCB0800F756A9E",
                "list": [
                    {
                        "challengeId": "FEBBC7804EBC5D094D0E258F06DD86F8",
                        "challengeCompletionValue": 350,
                        "challengeAsset": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner"
                    }
                ]
            }
        ],
        "prestigeLevel": 0
    },
    "objectId": "HunterGroupD",
    "schemaVersion": 1,
    "version": 3
}

RunnerGroups = [RunnerGroupA, RunnerGroupB, RunnerGroupC, RunnerGroupD, RunnerGroupE, RunnerGroupF]
HunterGroups = [HunterGroupA, HunterGroupB, HunterGroupC, HunterGroupD]
progression = []
weekly_challenges = [
"Challenge_ARB_Damage_HunterWeekly",
"Challenge_AssaultRifleWins_HunterWeekly",
"Challenge_BleedOut_HunterWeekly",
"Challenge_BleedOut_RunnerWeekly",
"Challenge_Damage_HunterWeekly",
"Challenge_Double_HunterWeekly",
"Challenge_DroneActivation_HunterWeekly",
"Challenge_Efficient_HunterWeekly",
"Challenge_Emotional_HunterWeekly",
"Challenge_Emotional_RunnerWeekly",
"Challenge_Greed_HunterWeekly",
"Challenge_Greed_RunnerWeekly",
"Challenge_Headshot_HunterWeekly",
"Challenge_HuntingShotgunWins_HunterWeekly",
"Challenge_InDenial_HunterWeekly",
"Challenge_LMGWins_HunterWeekly",
"Challenge_Mines_HunterWeekly",
"Challenge_Mines_RunnerWeekly",
"Challenge_Reveals_hunterWeekly",
"Challenge_RingOut_hunterWeekly",
"Challenge_Shields_RunnerWeekly",
"Challenge_ShotgunDowns_HunterWeekly",
"Challenge_Speed_HunterWeekly",
"Challenge_SpeedCapture_RunnerWeekly",
"Challenge_Stuns_RunnerWeekly",
"Challenge_Turrets_HunterWeekly",
"Challenge_Turrets_RunnerWeekly",
"Challenge_UPs_RunnerWeekly",
"Challenge_Wasteful_HunterWeekly",
"Challenge_Wasteful_RunnerWeekly",
"Challenge_WUP_HunterWeekly",
"Challenge_WUP_RunnerWeekly"
]
daily_challenges = [
"Daily_Domination_Hunter",
"Daily_Domination_Runner",
]


def generate_challenge(challenge_id):
    challengeCompletionValue = random.randint(1, 100)
    progression.append({"challengeId": challenge_id, "value": 0, "completed": False,
                        "challengeCompletionValue": challengeCompletionValue,
                        "lifetime": {"creationTime": "2019-11-25T02:17:22.484Z","expirationTime": "2020-11-25T02:17:22.484Z"}})


def populate(challengeId):
    progression.append({"challengeId": challengeId, "value": 0, "completed": False})


def login_update_time(userId):
    current_date = "2023-11-25T02:17:22.484Z"
    current_expire = "2024-11-25T02:17:22.484Z"
    for challenge_int in daily_challenges:
        for challenge in progression:
            if challenge['challengeId'] == challenge_int:
                if challenge['lifetime']['expirationTime'] < current_date:
                    challenge['lifetime']['expirationTime'] = current_expire
                    challenge['lifetime']['creationTime'] = current_date
                    print(f"Set date for challenge {challenge['challengeId']} to {current_date} and {current_expire}")


def update_progression(challengeId, value):
    for challenge_int in progression:
        if challenge_int['challengeId'] == challengeId:
            challenge_int['value'] = value


def complete_challenge(challengeId):
    for challenge_int in progression:
        if challenge_int['challengeId'] == challengeId:
            challenge_int['completed'] = True


def get_challenge(challengeId):
    for challenge_int in progression:
        if challenge_int['challengeId'] == challengeId:
            return challenge_int
    return None


def generate_execute_response(userid, challengeId, value):
    update_progression(challengeId, value)
    challenge_int = get_challenge(challengeId)
    #if value >= challenge_int['challengeCompletionValue']:
    #    complete_challenge(challengeId)
    #    return {"userId": userid, "challengeId": challengeId, "value": value, "completed": True}
    return {"userId": userid, "challengeId": challengeId, "value": value, "completed": False}


for runner_group in RunnerGroups:
    for runner_challenge in runner_group['data']['pickedChallenges']:
        populate(runner_challenge['list'][0]['challengeId'])

for hunter_group in HunterGroups:
    for hunter_challenge in hunter_group['data']['pickedChallenges']:
        populate(hunter_challenge['list'][0]['challengeId'])

print(progression)
update_progression('4F67D7064B9E706B36EEDABDBAB43AXD', 50)
print(get_challenge('4F67D7064B9E706B36EEDABDBAB43AXD'))
for challenge in weekly_challenges:
    generate_challenge(challenge)
all_weeklys = []
for challenge in weekly_challenges:
    all_weeklys.append(get_challenge(challenge))
print(all_weeklys)

for challenge in daily_challenges:
    generate_challenge(challenge)
all_dailys = []
for challenge in daily_challenges:
    all_dailys.append(get_challenge(challenge))
print(all_dailys)

print(generate_execute_response("test", "4F67D7064B9E706B36EEDABDBAB43AFD", 50))
login_update_time("asdasdads")