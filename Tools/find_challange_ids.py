import json

challenge_data = [
    {
        "challenge_id": "AAA17F074165BF5D36D1029C127A0D4E",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 540,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "6D7104C44F1D143B6C7A96B214155193",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 21,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "ED1B3E1B4AC3E5D56C670A9F62F07C92",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 4,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D23CCD2440F235D959F516A6787B7A71",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 51,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "9D2C755D41ACB426C2042EA6487E1945",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner",
        "faction": "Hunter",
        "ChallengeCompletionValue": 6000,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "85D90BCC4147CD43F2044C821D6EB49D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 3780,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "23757B8E40899EF1A0E4F7A4686E9D0C",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "F7A6294144F05769C416A3BBFBE57C22",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 5,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "A4E40AF148E7B58E6E58C48291C6297B",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 27,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "FAF0784740A1FB67281B5092951102F4",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner",
        "faction": "Hunter",
        "ChallengeCompletionValue": 9450,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "9E0448E34302A5AB2792159B3055E0F6",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_TakeDamage_Runner.Challenge_TakeDamage_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "8C12E22F4325BC90558D7BA934B93E8B",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 14000,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "42723BB44FF9DC6167710EBD3BB1974E",
        "challengeBlueprint": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 50,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "F0151A004C947006E58CE396309648DE",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 84,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "B2058F55486621D39C9E0886337D460E",
        "challengeBlueprint": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 90,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "8B99C4B84F34B0F2AF386BBE4BCD789D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 4,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "E69B0FAA4F4FAC91B5787F9DB3767BF0",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 10,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "C72716CA47D500773FC92DBCB5255106",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates",
        "faction": "General",
        "ChallengeCompletionValue": 14,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "706225D341BDAF02FD2DE489FDAE40FA",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 1350,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "1270093F4EBCC061941CC9A24487F4BA",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 35,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "3AE829D3417269BA58C78C9B6CE68FC5",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 972,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "32842C1A49A9FA69F3B59BA9719D9CF0",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 4,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "9EC0B6BB467C2BDDEAA4FEB0A82A5539",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Heal_Runner.Challenge_Heal_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 750,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "46A33A56458CDBF6C9700296A13AA6C3",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "A01881EA449E3C4D41DBAD934AB22597",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 6300,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "3FA81C43432C4DEA41B6758D0FE8A67A",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "42C825664E99C96FEABA959B232936F8",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Climb_Runner.Challenge_Climb_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 360,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "750289504426ADB8B60708AF69B86D0D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 51,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "FA0E56EE4F397A01C00EC08098DF5385",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 125,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "164951C94A19DB316632A3A046D9BD65",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner",
        "faction": "Hunter",
        "ChallengeCompletionValue": 8400,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "8B5F3CD6462B8F079E9A86ACB18A7E8C",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 15,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "8FB6FB66450F5309051BAD833482623D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 3,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "603C159E423B886BFBDB8DB8B531CEFC",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates",
        "faction": "General",
        "ChallengeCompletionValue": 4,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "C5A3051242EF5CC2075AEDA6737F6A78",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 85,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "0065304F4C997DBC41E1D4B97CB8C862",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 5,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "7CF554E54AFF988E8547EF9D9045CE09",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "5893E0D94DB8A214A95264998BB64F87",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner",
        "faction": "Hunter",
        "ChallengeCompletionValue": 1200,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "F163ED574599F99909E48F9335B3A1EE",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner",
        "faction": "Hunter",
        "ChallengeCompletionValue": 1680,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D3AB5C05423354AF7CB31091084A7E5A",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Climb_Runner.Challenge_Climb_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 360,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D073F5084433EA1F7C18DAB318653311",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 204,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "AAD9E4254D00764939666B9DC156C759",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2700,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "591522B94F53059CCA6C8D9470B857CF",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 350,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "1EFAB0FB46A2A7A21C13B79582DA3266",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 15,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "ADFE598B4A7C43682E8957BB6DE649E6",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 21,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "7EE014F04125C50B6B6255800EEFAAE3",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2430,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "CBFE70634B82AC7C22CF4F8DAB454492",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 51,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "6AC6D5594F4307C7253B918EABDFF3E0",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 5,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "C7206BC84327B808DF4A76B1A8C324B8",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 7,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "F7078C8D406048F06C9D3E8CE12DD56B",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 540,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "66EC672C444D73BD9B47E78D8C904ED6",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_BloodMode_Runner.Challenge_BloodMode_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "DA7110DE4FF009FCE54AFF82592B5C8D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 11340,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "F1C883B04A1391995B772183648BBD57",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 85,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "CDE496DC4D0DA4B0496677A341F1AF51",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 5,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D5DCCA6E431ACFD7D424828F82A7B61A",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "0AC000E2483D9DDAF111CB8C694133F0",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_BloodMode_Runner.Challenge_BloodMode_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 1,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "4A7FB78F4F530C0B3CCAC59F777777B8",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 84,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "6FB16D124A5F585A7BCB148AAEBF596A",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 27,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "45C10C124535F0340C0336B85B316A7E",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 51,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "9DE5C1044206ECBF86F8149D9FFE8EC0",
        "challengeBlueprint": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 250,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "A683FE3949DA091923CD0E831266BB82",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates",
        "faction": "General",
        "ChallengeCompletionValue": 14,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "E468EFA0429FAF9457710BA79A3AE558",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_BloodMode_Runner.Challenge_BloodMode_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 1,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "0EB94497403DE9F5D2668DB924C8D101",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2800,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "98F9681D4003C0FB51B9EF930DFB2B3C",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 972,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "163D4DA246FF4443E97826A31C4A3AC1",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner",
        "faction": "Hunter",
        "ChallengeCompletionValue": 9450,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "E1A9D7B64F8EF23D889B5C80D1A7B806",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 75,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "04F9E7C14939F94BCDA87EB649202CD2",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 7,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "E4DEF0C64FEA1AC7A6BA5F9717A20266",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 15,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "059227104A00630F8A08DBB8CFB6273D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 21,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "09B0305041CA51C2248975930B1324EC",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 45,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "69CA910845AB81A4CFC4C3B940EEA1A9",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_BloodMode_Runner.Challenge_BloodMode_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 4,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "7009CA6E4FF410F3254A678401BA7842",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 250,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "BFADEA9745CCDF83DAE0FC928072D33E",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 7,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "92C3E6EF4FAC78B1C39E7288EE9E1795",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2000,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "9AC18CBF4FF9575E229AECA3B5417A13",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_TakeDamage_Runner.Challenge_TakeDamage_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 140,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "F0052A4947B609EC8AB1E1ADD1A77DC3",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "6D34DAEE43E5D78968FA199F200D733C",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 6750,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "C4D8FAD94D32B38C2FEF01AEEB8B7E01",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 5,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "A183C0D3408DE57E1000F28CA3613929",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 7,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "05161C8749F31F177A0BCBAEBCD7AC9B",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 6300,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "59C019E84AAE0006C937DCB91707FC87",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 756,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "9949A5D34C3C06041D180EBB040D87A7",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 3600,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "1E85903B4CC9099002E3F79AFF06A2DF",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates",
        "faction": "General",
        "ChallengeCompletionValue": 7,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "15EA8D7E4BF9757FB8B1FDA103FC2BC0",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner",
        "faction": "Hunter",
        "ChallengeCompletionValue": 6000,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "98F402784EB4DBE2B4735FAFA172E275",
        "challengeBlueprint": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 350,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D922EF45416CD5BCB5C4719593D720D3",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 15,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "A22145A740EBBECB2B523388EE869A30",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 756,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "EEA2A912460118B9CAA06EA9920E76C4",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 90,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "8AFC192646EB8D57C0A4518F0F13EFC8",
        "challengeBlueprint": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 170,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "1B71DA4E403D35E8B5452F8D3E8A769A",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Heal_Runner.Challenge_Heal_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 750,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "B5DA00184414589945D4EBBE694F7560",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 9450,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "174C50B54DDC26925C21DF80D6270F0C",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 25,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "F46A7D004C759979D5E792A31DB57D78",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_BloodMode_Runner.Challenge_BloodMode_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "5D9306164D90E8943FDC22B62381F1B0",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 27,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "B2E82C2C494AC504CFD276988ED4B8B7",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates",
        "faction": "General",
        "ChallengeCompletionValue": 7,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "5B803D4E4B03704131C014BAD8C0AFCA",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_TakeDamage_Runner.Challenge_TakeDamage_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "2AE248D44BF86C4AFF937096385B29A5",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 14,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "7896DADB42E5A3F7F7B0D3A3EA7BE835",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner",
        "faction": "Hunter",
        "ChallengeCompletionValue": 1200,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "461AB9F64F22C5BA2C0132A703991391",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 21,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "BCBFD25F44922B3D1B8224BB26FF5C3E",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 11340,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "C88D6602411137B4BE090191F882E370",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 4590,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "C92343134AC1B78E360372B5FD1A1D12",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 125,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "DA239E56489929FAF7005394B6DD2AE0",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Heal_Runner.Challenge_Heal_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 1050,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "EF6954524C56AFDF9E56CCB96EE9577B",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2000,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "28C59774451700EBB70E958FC6171D31",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 5,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "F762F80847C407137CA3A5B21F591B40",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_TakeDamage_Runner.Challenge_TakeDamage_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 180,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "ABAA68CA4089D15F7EEB08964EB3AAE5",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 1836,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "2755281243A26C43273AA19C057D5F0B",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 10,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "3955701343985CAC238B55B4CD7B5CE7",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "1546DDAA4853CAA51906F79A5FAD865A",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 540,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "FF58FDB64DAD1547B9A7358753B3DF12",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 5,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "036F25EC4DD408316D952DB676EFF044",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 45,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "F7AA22B44C90014CB065B5911C578C4C",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates",
        "faction": "General",
        "ChallengeCompletionValue": 7,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "997258A24843F1E80DD676BB41B9107B",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 5,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "B4CF103C4717A51624FAC9A7CE22D3F2",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 7,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "169A25E84BF7BE4853B3058303507AAF",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 15,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D3D8315247133A0B0D40A69A5E1E6719",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 84,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "A696FEF048FA3384D78B859B2DE741EB",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates",
        "faction": "General",
        "ChallengeCompletionValue": 4,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "9BBA3FF4492F32575EC7DEA6A06F7164",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_TakeDamage_Runner.Challenge_TakeDamage_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 340,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "38016B1E4F18E86CE5145C8136B5C1FF",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_TakeDamage_Runner.Challenge_TakeDamage_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "E9EC69E145769F48D2DE78AD5297DC3D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 21,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "4E0F23E3412D0A0F24F6F28B4276AE09",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 15,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "4E601129495EC548005489B7F060E30A",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_BloodMode_Runner.Challenge_BloodMode_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "7BF92257432294693A2FD28893AB9976",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner",
        "faction": "Hunter",
        "ChallengeCompletionValue": 2160,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "962EE31A423129BF016982B386942B06",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 85,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "1F41D86145B2220958430087F8E4F777",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 15,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "B2CF1E1F499B71CACEE56881CD6860E4",
        "challengeBlueprint": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 350,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "E229A5204C58A10236ABBD819855EEAC",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 60,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "56B3864846DF674AB111E5A98825CFE9",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 21,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "18B9683744C9F21BAAE84393382E9A72",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 4,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "AABDE5134D9D217100D68885A267539C",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 4,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "6D145AFA4F3DB055AC39168AEDDA94EA",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner",
        "faction": "Hunter",
        "ChallengeCompletionValue": 6000,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "065CB5D34EDA174A7BDB0299FBDCA79F",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 3780,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "19DA7D4B49FB74C397BC72AEC7C0355F",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 540,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "36EF7149447BD17D1EA6EB9D6CDD78C7",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 21,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "5ED0A6F6444EBCE486CAF78D8B448317",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 27,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "A1EB501E46B1C338F4A3A395781476AF",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 170,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "C4EE835D4931FCC86E1A20BFF15130D0",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 10,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "67238BEC4BE231ACF535F38C23A7266F",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 420,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "E12A636A4634823E381923BD1C1FC8A9",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 25,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "75BF02A64A5C3B68BDAD9E8DBAA56B37",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2800,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "DBCA16B240902F1B6ECD4E8F0CC94D4A",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 972,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "872B0B1D4041CCA913357A9F20862E22",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 4,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "DC365A434E6B15782137379511889DC5",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 300,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "55318B5A432DF1D7CDEABF99A7D5395D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates",
        "faction": "General",
        "ChallengeCompletionValue": 14,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "05B53085458EF8914EDFCD9384CEAE03",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_TakeDamage_Runner.Challenge_TakeDamage_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 100,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "1CD80000427F00763959A0A6B89976C4",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2800,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "BA6D4C0544CAC07C2A3DC5809E1BF1D3",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Climb_Runner.Challenge_Climb_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 360,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "34CAB3C441A6B009913CD896B2C360E0",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_BloodMode_Runner.Challenge_BloodMode_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 4,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "CD62C97F41A854DE857405B4D60650B5",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 31500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "1AE367C443582706BB158990CE887DAC",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 44100,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "0B6C5E534DB5A4558470498026D141E7",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HunterClose_Runner.Challenge_HunterClose_Runner",
        "faction": "Hunter",
        "ChallengeCompletionValue": 1200,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "3FE930264D67A74322052F9D8F681D3B",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "F2B9423C42605CAD77E39C80EB763499",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 108,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "DA207F1E42C1A9C646E3829DA5844F43",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 7,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D5D062F84C15E86C5460BAA05FACCBB1",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 5,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "F93FAAAD499A95DA71FAA2B6E7A9A40D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 44100,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "6DDB9CD04AC3650334DAC1B4E2441203",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 6300,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "8E8832024C6495502620C19553E22C92",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 35,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "2BF407594A478736B9B781BFA63F7D4D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_TakeDamage_Runner.Challenge_TakeDamage_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 180,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "45F1D9A449A00416B1CCA3A3168EE378",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 6750,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "F2435C384654B7B302EA589B5A991FC0",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 75,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "4FB5DACD409DEBDA6B98D58CDC7BFADB",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 175,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "2BFEF31440B7397EE8A966BD4665FA54",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 25,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "13F9C0754105DB7C89677CB148CF6B32",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 84,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "CC286C9640A50510B51C4DA5BE3FB302",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 4,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "608C4A1D4118B3AB02FC2A9D36D7B924",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 7,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "196A8EA1481213547C42D687B89E55C3",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 5,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "BCAEBA8144F4E2EA5F423C879F3DC2B5",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_TeamActions_Runner.Challenge_TeamActions_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 9450,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "97FB5BBC4ACEC49D2CF9429C9D91867C",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 15,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "48151EA64045F7038803C0A9BC0CBD2A",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 21,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "482681A246632681F2422BB5D83C76B4",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Heal_Runner.Challenge_Heal_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 270,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "844F97884EEF96B95A3CB79B592FFE5A",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 4,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "FFC2BF94472CD33CEF3F04A797599B0C",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 5,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "8C472D41428C21037BED70BAC405DF83",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_BloodMode_Runner.Challenge_BloodMode_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 7,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "DE506D7146741C14D3E570915C93BAAF",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 60,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "43BDD08946497B9092A965969E04F0EF",
        "challengeBlueprint": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 70,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "163D880C4F2458C9B0F578ABA4F48829",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 27,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "4352D1CE44E94FE9E83EE9B022765D13",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 85,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "55840FDB4183457E8E9338B42E58FF16",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 5,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "FEF1EB04436543EC78076FA5B4D683D9",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 420,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "66440FF14462830A1430F48E6D208700",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 540,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "0E2EC800441DAC59B95BA99EB12BE93C",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 21,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "F3B9AD584485D2922367BA8F27DE5B38",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 6,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "5BCD08534B40721E037FED9B84A067A5",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 51,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "96854C5744248E69DA6BDCBF1649E50D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_BloodMode_Runner.Challenge_BloodMode_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 5,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "532ABF474B5204C9AE8181AC6229DA4A",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "3936E915400264F07EFA10B8C86F82EC",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "E8D73E764734C06F07B26F8CB9216948",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2800,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "8D208A2C48CD0ECB21770F8C4749FEF7",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "6CE2326B4185086029627FB62A521472",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 204,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "4C0003C84B2281BE374C5A9C9CB12138",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Heal_Runner.Challenge_Heal_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 750,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "31A25AC44573CA7EB6753DAB6282F085",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_TakeDamage_Runner.Challenge_TakeDamage_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 700,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "FE057AA34C42FA716CDDC6877FE1B794",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 540,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "A75663B64E9C7BD673A35F9773BC8A3E",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 5,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "A61972474D92FECCCE0E2FA63472A16D",
        "challengeBlueprint": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 90,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "779163ED40920922476AE6B089D7DCDE",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 85,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "9452224E4A2EEBF58F7C159BF4597D92",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2700,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "654DF5994AEF4407310BFCA2765BCD6A",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 7,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "37E04B7F43CCEA7269C8EF9690DDF59B",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 25,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "037E9EA045EFB79EF804B880B9541F03",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 756,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "AC8A90934C381CC44E46E18D8E27B94E",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 108,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "0632304440CF07FDABAF89A07024890F",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 11,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "8385C1F8491ECC0B44A2EDB55AC81125",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 75,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "93C161134CEEAF1AA74228B8182AE6A5",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 350,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "600A434C4E3771514A09EEB5ACC557F1",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 1,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "79FCC284493740AE837D37A2336AED4D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 70,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "FD0513C841AFD9088926ABBB475D1258",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 3600,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "4CC4E8C24351DA95908B7A90061F9DBB",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 4,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "9BE2C2F94A9D727AB2AC3685AB1F7330",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 75,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "6DB4EB1E41636E83312DEE89FB2CF44E",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 21,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "E0696E684104FF90CC56A5BB45B83307",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Climb_Runner.Challenge_Climb_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 200,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "6DC50A604D67748F1E02B8A70E110A03",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 756,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "5E9B862549B2552585A2F5AD25FCEA40",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 108,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "4BBB62A34BB22D602520158BCBCD2CCF",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 1836,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "17D51EAC4D124D764233798151969128",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 125,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "0E14CAE941FDE3DE234EACA60EA8EACC",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "45FA8D83455CD3861CD46181FABE5A52",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_BloodMode_Runner.Challenge_BloodMode_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 1,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "9B82F45946C61F6529F9DE9D9CDA95C7",
        "challengeBlueprint": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 70,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "A186C08A4373196CCFE03885412E6231",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 90,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "6B21EED64756586CFE550986146D6BA8",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 85,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "018DCE9D474FDC62EDFB76851A80B4FC",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 5,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "7877F66546938C9F36B1C5AA35BB2665",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 3780,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "7ABF3C314F7B2F0394F7FE99D74FB0B5",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "4E5D3FA14E5FC13EF4D153B36DEB2F44",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 3,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "64EF2715495A57ED33EC0F9746E8C340",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 6,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "6C79957240AB9A6194AAC09909BD463E",
        "challengeBlueprint": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 170,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "8C25E8284FF576AE31B37BB5CA44C968",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 75,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "6850CB1D45C2E8FED39C9D888420EF29",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 7,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "6712657D4D850CA80C75868B4316F2D2",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_BloodMode_Runner.Challenge_BloodMode_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 1,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "AA7AC9BD47C52C590778199B3B62F8F8",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 84,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "DEA988464ADB1ABC692BB8A9D882B0E0",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 90,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "E488E10444690F84DC417CAD56249018",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 1836,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "BB0BC1A047EE6D25A1B32490785D6B9B",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Heal_Runner.Challenge_Heal_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 750,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "56B3B1024D63C067DC59439F277413BF",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 175,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "EAEBE1294401AF40714DE792A97A70D1",
        "challengeBlueprint": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 50,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "8275929343583667137F81B4A4D795C6",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Climb_Runner.Challenge_Climb_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 280,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "126C948848F1E740565FEAA9A8893B0E",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_TakeDamage_Runner.Challenge_TakeDamage_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 180,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "0FF59116401E217A44A27FBE02796DCC",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 51,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "3C87B22B42626E1E3A5CB88799351D08",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2700,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "4E693EF14DC18A4B91DB959546DE983B",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 420,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "FBFAB7964EF765CD355EA982118C10B1",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 1,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "8EBB2B90481482237E1095BE49E6B8FB",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 5,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D77235244F6877FF7165F3A8D12C60C8",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 11340,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "4539060D4C54FA6B5246419D5C47645D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_TakeDamage_Runner.Challenge_TakeDamage_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 340,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "FCBB6FFF4CC2B6BCAD96F79BD42875BB",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 75,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "95A4EC1C4DADBAC0CBDBCEBB23945A82",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 350,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "78A3F70740D1BFE21A5187BBB4C16C21",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_TakeDamage_Runner.Challenge_TakeDamage_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 100,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "DEE3F0534C4959950B4C9E863BEE20FA",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Climb_Runner.Challenge_Climb_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 280,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "BA517A924215D22F9D848A809533BF9F",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "ECF222BA4AF4135BDD057CBE874905F7",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 4,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "3E87EE0040170F507B236BB749EA5E04",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_TakeDamage_Runner.Challenge_TakeDamage_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "B43B27124C8262C43CDBD68A4F487333",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 7,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "417F869543A501F0C5F6958D910A1BC7",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2000,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "03D2B11A476DA71E762F1F996B5CF9AA",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 756,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "B97C6AB24306EB77966A308E052C80E9",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Mark_Runner.Challenge_Mark_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 90,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "B3D273EA468C2DF124DC268105223A38",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 7,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "6E3643024C2BF7992605B88840448509",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 75,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "F97623484222025061C10AAA9548E938",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectWeaponUpgrades_Runner.Challenge_CollectWeaponUpgrades_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "316E9D0A4E348A899F817AB8BC241E3D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 15,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "884E5E144DD86D127A9797843A2E68CA",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 756,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "2C6E39CF473498C302D52B85F70EBAC2",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_DisableDrones_Runner.Challenge_DisableDrones_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 27,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D6E984B643404F1C4A1CA2984781A0FC",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_TakeDamage_Runner.Challenge_TakeDamage_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 340,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "DEA0380D492D525CB81599A50177194D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 10,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "07641C70428A2A5FF41FB3B76462B50B",
        "challengeBlueprint": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 350,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "B673DBAC4CF237CA7D8829A036CC4033",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 6300,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "3B9D178F44BC35FB6653D9BB506ADCE6",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 35,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "8B3805374EF3064CC22DCDA64C8DE521",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_TakeDamage_Runner.Challenge_TakeDamage_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 180,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "C7D626DC4A901421DBD141BD4E0B09D7",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_TakeDamage_Runner.Challenge_TakeDamage_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 340,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "AB874CEB4D2D591A08DF5EA669B1454F",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 10,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "325A9E5F41061F3BC834DCA2DCEA3A9D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 21,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "FFD721B046320248FE855B81A7DF887A",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_DangerClose_Runner.Challenge_DangerClose_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 3,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "96F279AE44DF7A95A613AD895AFE37E1",
        "challengeBlueprint": "/Game/Challenges/Challenge_Deliver_Runner.Challenge_Deliver_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 70,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "6E1578164A5F12779AE1929F152C3CB1",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_AssistAChase_Runner.Challenge_AssistAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "3659C7134DC957B2D8AF208032E9998D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 6750,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "879DCA4241B115AD2FA4C7800EC1F860",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 300,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "5BFB317F48E7D4307FF26C9351A25CCF",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SurviveAChase_Runner.Challenge_SurviveAChase_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 14,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "912F3EA64C0BBD18054E4DB964439DB9",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_BloodMode_Runner.Challenge_BloodMode_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 1,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "554E1F1043510A52E2EBDEB0C8E73FBB",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 756,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "101B66194A4A111DBFCC82AE6ADBD75E",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Exit_Runner.Challenge_Exit_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "3D4E59A14FC9E887D46E779BE2C25D43",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 1836,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "60B1BFC741B502E8E2F88791738C54E4",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Evade_Runner.Challenge_Evade_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 300,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "271D018B46A39EA1CB3E409645913280",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Runner.Challenge_Travel_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 14000,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "1BFB28584EB0F872D278F28971BE0AA0",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 540,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "88F917094F77F0F610050998E5DD4157",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_TakeDamage_Runner.Challenge_TakeDamage_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 140,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "82DEF8AE4575062516E595A9358DB330",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 11340,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "44D5F8254E63B6BE535B899418DB18C3",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_SpendNPI_Runner.Challenge_SpendNPI_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 85,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "3CF6BB164AA978CC477B43A3BAC27931",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_ConstructDefeats_Runner.Challenge_ConstructDefeats_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 2700,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D1A234104ECDBECAC65F189B23DE6628",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Ressources_Runner.Challenge_Ressources_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 44100,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "DCB92FCC42BE9D370AE3319C884492C9",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Hunter.Challenge_Travel_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 3000,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "DFA32F29462005F463753DB1AFF45363",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HackCrates_Hunter.Challenge_HackCrates_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 35,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "B8D4D5F04BB6B46F717E5BA9BCAB19DD",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_RingOut_Hunter.Challenge_RingOut_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 216,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "416AFD98439DB116F6814C8803CC9D5B",
        "challengeBlueprint": "/Game/Challenges/Challenge_DroneCharger_Hunter.Challenge_DroneCharger_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 51,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "90DF801D4F63346716A817890113A4A0",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Downing_Hunter.Challenge_Downing_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 42000,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "614BA77749DCB088EF3864BC9D39E060",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Execution_Hunter.Challenge_Execution_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 52500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "8DE146FD4E7B54928DC03E8FA520E839",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Execution_Hunter.Challenge_Execution_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 7500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "4CEAC318465B9DCE0F5299978BE5BB19",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Reveal_Hunter.Challenge_Reveal_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 35,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "9B87F77F4D4102244FA088AD12641BD0",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_LastMAnStanding_Hunter.Challenge_LastManStanding_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 2,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "95ED5B054FA37DD50DBB769A3D7BEF11",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Hacking_Hunter.Challenge_Hacking_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 5100,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "047123084261A40C69363798C33B11D4",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Hunter.Challenge_Travel_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 15000,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "60E619B54B23CCD46C103F9DB2C1C429",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "6E7FE9EC4D10F936A6AEB1A614DE31F9",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_RingOut_Hunter.Challenge_RingOut_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 120,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "B8A3998A4E1561254EB97DA431228316",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Drones_Hunter.Challenge_Drones_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 2100,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "820E1F864C7374462FA94DB4F41C6F79",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Execution_Hunter.Challenge_Execution_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 13500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "55CE30D243A0A202B654BAB29F9964E0",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Execution_Hunter.Challenge_Execution_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 25500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "5776CC20434CD8C6508E178FEDED520D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Hacking_Hunter.Challenge_Hacking_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 7500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "F036A4E44BA16494AF6888AB659B75D7",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D484B4534A0F7502BB7A56BB3339C10B",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Aim_Hunter.Challenge_Aim_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 5,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "0E56E8834E4492D6F60CB89D0D253DE2",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 1680,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "30A47EA040A97112034A4A8323B946F8",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Supercharge_Hunter.Challenge_Supercharge_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 216,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "2A71B42A461617A5AEBD30874A9F9C07",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Hacking_Hunter.Challenge_Hacking_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 5100,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "71598BEC466C1C3E0C0DF7B6EDCD5843",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Downing_Hunter.Challenge_Downing_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 42000,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "AF8E633540C03ECBEE17A5AF815EC0B9",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Execution_Hunter.Challenge_Execution_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 52500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "AB6D78814C4140A9FC12CDBD5E337906",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Aim_Hunter.Challenge_Aim_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 5,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "B35772FB48CBB381E9FC55BF303E68C3",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Execution_Hunter.Challenge_Execution_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 10500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "B0F4E6874472ACB92722D2B08DA59FB0",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Reveal_Hunter.Challenge_Reveal_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 45,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "5A7B97CA46EEA18FF3A4BBAD8DC239C3",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Hacking_Hunter.Challenge_Hacking_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 5100,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "9FAF17A449CBAC432BC2098994E11E18",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Drones_Hunter.Challenge_Drones_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 7500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "5217BAB947FB58408AB3E4AB2EAD78AC",
        "challengeBlueprint": "/Game/Challenges/Challenge_DroneCharger_Hunter.Challenge_DroneCharger_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "61CB73574BAC0C69429A6F86B30133F1",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_RingOut_Hunter.Challenge_RingOut_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 120,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "CF0119DD4AE1F82068AB18A1FB115D02",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Reveal_Hunter.Challenge_Reveal_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 35,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "3368F739404426559F6A3A873CEE5DF0",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Stomp_Hunter.Challenge_Stomp_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 18,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "BFA738BE496B18463927A2ACF0D26703",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Stomp_Hunter.Challenge_Stomp_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 34,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "BD7BDDE448067BF3591405B1C374EA10",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Aim_Hunter.Challenge_Aim_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 25,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "ED4D6914411F2EA9BDA50FA8D8A90A73",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Reveal_Hunter.Challenge_Reveal_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 175,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "361E338845BD912078DBAC8564662A37",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Execution_Hunter.Challenge_Execution_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 7500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "8FEA3CC74C199D8847AF4F8BDF36066E",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 1680,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D4FD0A5F4EF1C68E2D0E90A3DFE7F25E",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 27,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D48C17EE4CDC2BE8736663B030771D01",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Execution_Hunter.Challenge_Execution_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 25500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D15A648945D87D6910551D95377FB676",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_RingOut_Hunter.Challenge_RingOut_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 600,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "82F9285940925F3CF4E9B89C636948C6",
        "challengeBlueprint": "/Game/Challenges/Challenge_DroneCharger_Hunter.Challenge_DroneCharger_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "AF49E8854AF90258FB0CB5925F1280C5",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Supercharge_Hunter.Challenge_Supercharge_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 120,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "6B2465894CC277B984F3609CB9F1B173",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Execution_Hunter.Challenge_Execution_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 10500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "B3C2A4C3488C5F8DAC236DB50C006776",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Drones_Hunter.Challenge_Drones_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 2700,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "CA3C76284F80887C3F6B0D8181D6C6DE",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Execution_Hunter.Challenge_Execution_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 25500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "4F68D0A7426CE06A7B9FFC840F9270D7",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates",
        "faction": "General",
        "ChallengeCompletionValue": 75,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "1F3F32ED4BDEFAA0F63690AE73CC762F",
        "challengeBlueprint": "/Game/Challenges/Challenge_DroneCharger_Hunter.Challenge_DroneCharger_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "261E4A0747E2258D4092A396EB3920B6",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HackCrates_Hunter.Challenge_HackCrates_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 25,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "B9B28EFE4720ED2B85535AABBE01E9F1",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Execution_Hunter.Challenge_Execution_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 10500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "8675C8554E7921F9BD0B318BD3AFC1D5",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Aim_Hunter.Challenge_Aim_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 9,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "129D557E45C35D65A445E98638975713",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Supercharge_Hunter.Challenge_Supercharge_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 408,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "DA2804E64DDD361AAA095DAE73A4FE25",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 6000,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "38618C9E4079EF8897AF5786D6A5BBE5",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Drones_Hunter.Challenge_Drones_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 10500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "8BBB61AE4E06E378D5185BABBCE65CB8",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Drones_Hunter.Challenge_Drones_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 1500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "2A69969E448A6C46A551C1981D44CC3B",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Execution_Hunter.Challenge_Execution_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 10500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "31CBC6644EC11C787107B1980C26D62F",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Aim_Hunter.Challenge_Aim_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 9,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "B10B10924C71861914FA16BDFFF349D8",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_RingOut_Hunter.Challenge_RingOut_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 408,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "39763AE84036C7853B4AAAA91841E434",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Aim_Hunter.Challenge_Aim_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 25,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "7D49C57A4C5960EC4763DB85EE245A3A",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates",
        "faction": "General",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "F792E9BE4393B5D5409A66B1BBE6BE13",
        "challengeBlueprint": "/Game/Challenges/Challenge_DroneCharger_Hunter.Challenge_DroneCharger_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 15,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "C1AA03EC4189571DB33EB0A314F99A06",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Hacking_Hunter.Challenge_Hacking_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 2100,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "459D254C4321A84AF894D39057AD8878",
        "challengeBlueprint": "/Game/Challenges/Challenge_DroneCharger_Hunter.Challenge_DroneCharger_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 27,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "9C854EA94D3184FB6C3E97A3C8E5127D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Drones_Hunter.Challenge_Drones_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 5100,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "6DB47CD642558C1E93525680F3272846",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HackCrates_Hunter.Challenge_HackCrates_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 125,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D224172244C5901F8E500E93237B79D0",
        "challengeBlueprint": "/Game/Challenges/Challenge_DroneCharger_Hunter.Challenge_DroneCharger_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "315F687547B0B48506ECC6B3B0B1D28A",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Reveal_Hunter.Challenge_Reveal_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 25,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "627D610949C861DD115DC98DDD0A4603",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Execution_Hunter.Challenge_Execution_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 10500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D2233C3B45C9A8CEB2FAD7AE4A5CBA75",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Hunter.Challenge_Travel_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 5400,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "669586A0465325C449B9CDBBCB1D702D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Stomp_Hunter.Challenge_Stomp_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 34,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D61A1DC54BF6D8DEF76746BC857FBC79",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 75,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "AB4EC4084221002C6C8B028457B8D33F",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Downing_Hunter.Challenge_Downing_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 58800,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "501940744554461643B8B0935351E8A5",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 15,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "270350C642B42C6B49D055A83078CD50",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Execution_Hunter.Challenge_Execution_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 10500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "E59D76A14078E64102F1FB92124FAC72",
        "challengeBlueprint": "/Game/Challenges/Challenge_DroneCharger_Hunter.Challenge_DroneCharger_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 27,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "C397753D47F60B92F550FDA294454E14",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 4080,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "F39777774D91859F8F3B1AB3BCE02E11",
        "challengeBlueprint": "/Game/Challenges/Challenge_DroneCharger_Hunter.Challenge_DroneCharger_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 75,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "5CACFEA64B6E5498E8E283B1A9C4AB70",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 8400,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "ECB444994501D360A04AEB961490BF7F",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Aim_Hunter.Challenge_Aim_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 5,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "0965D81E46519BE334B88B9363CF0FEC",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Supercharge_Hunter.Challenge_Supercharge_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 168,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "7C886A4B4A973DC40C6819AF8E5821EF",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 2160,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "A8E417F941F75B0DF086F6BF33556F7B",
        "challengeBlueprint": "/Game/Challenges/Challenge_DroneCharger_Hunter.Challenge_DroneCharger_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 51,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "994B515643DB544EEF5621985F99114F",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Reveal_Hunter.Challenge_Reveal_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 125,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "AE24C9F546BC4D9F5A6DBF9798021031",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_LastMAnStanding_Hunter.Challenge_LastManStanding_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 7,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "28814D7D49263DB24BF6D8A3F062ADFB",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Hacking_Hunter.Challenge_Hacking_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 1500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "655EF1824CE7E794F325DAABADB206CB",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Execution_Hunter.Challenge_Execution_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 10500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "FC5E6F8249F763CDAC6EBE94F1E3066C",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HackCrates_Hunter.Challenge_HackCrates_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 45,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "595213CE4C0FDFF637D41CB310976211",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Aim_Hunter.Challenge_Aim_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 17,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "140342BC4D92E3ED74BFEBB2F6753D63",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Supercharge_Hunter.Challenge_Supercharge_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 600,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "7DDE2030442DDB6828CEA88F35D7FAE6",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Hunter.Challenge_Travel_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 21000,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "546B950F4AFF9B44008A2A841FA48C84",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Drones_Hunter.Challenge_Drones_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 1500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "604FBB8D464FECD9E9E9E4B40F4B14E9",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Drones_Hunter.Challenge_Drones_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 2100,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "6F5EF1AF41605B95A1030FA7A1883B10",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 27,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "0878CA434DFA158425B66982ABD06074",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates",
        "faction": "General",
        "ChallengeCompletionValue": 51,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "9570DA3845398BF46CC656AEC28D12BD",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 75,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "58FB6A2C42DBD6D13C03259B643C8DDE",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_LastMAnStanding_Hunter.Challenge_LastManStanding_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 7,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "50AC8712417A4B5CA01C4DB175AF78A8",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HackCrates_Hunter.Challenge_HackCrates_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 25,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "DCDD95A24B2BFCCA151614AD11C79355",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Reveal_Hunter.Challenge_Reveal_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 35,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "C641D23F4A60B235146541B9A9AB464E",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Hacking_Hunter.Challenge_Hacking_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 2700,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "C63D0E2640DA950F06BDB8AF9D5ABA88",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Downing_Hunter.Challenge_Downing_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 28560,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "9D12783B4E0FBC46B85953A83667FC3C",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Stomp_Hunter.Challenge_Stomp_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 50,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "0A38F9864A96B05F2BD80C82ABD71707",
        "challengeBlueprint": "/Game/Challenges/Challenge_DroneCharger_Hunter.Challenge_DroneCharger_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "64CCC6B7458FBF580FFF01B645D39E81",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HackCrates_Hunter.Challenge_HackCrates_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 25,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "7DA727D049CB91CF922C0095DA4FCE5D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_RingOut_Hunter.Challenge_RingOut_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 168,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "43D8C7434DEA0FC6361C07BB9FFF7372",
        "challengeBlueprint": "/Game/Challenges/Challenge_DroneCharger_Hunter.Challenge_DroneCharger_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 27,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "7307E47F433CD5AF6F577EA5603E7D28",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_LastMAnStanding_Hunter.Challenge_LastManStanding_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 4,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "5D9FD6F9463E3C6D9B2709BDFC7560FB",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_LastMAnStanding_Hunter.Challenge_LastManStanding_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 5,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "AB13DF0C41E11C362E1057A0876D470A",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_RingOut_Hunter.Challenge_RingOut_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 840,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "E2A1BC424525BC43EBF5DCAAD62E0E33",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Stomp_Hunter.Challenge_Stomp_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 10,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "04F7C8124F1B0BF5B266939552F005FF",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Drones_Hunter.Challenge_Drones_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 2100,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "CD03381F4F6426F09ED86B8D2FB2A716",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HackCrates_Hunter.Challenge_HackCrates_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 45,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "CCA293C34B7D525FF295809180FD3E72",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Hunter.Challenge_Travel_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 10200,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "C7619B8A40755DC90325F7AB4A68AFB0",
        "challengeBlueprint": "/Game/Challenges/Challenge_DroneCharger_Hunter.Challenge_DroneCharger_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 75,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "29574EC049CEC135B7F555936A0FC85F",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Reveal_Hunter.Challenge_Reveal_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 175,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "DF1847264871DC8C231B4D86FC5A3D26",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates",
        "faction": "General",
        "ChallengeCompletionValue": 15,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "969879514E89EFDF66C7AE864B1B3F95",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Hunter.Challenge_Travel_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 4200,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "BE255A7E4A77CABF5237E7ADE319DAC4",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 2160,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "BB64C9D64F978E2A8CC5E5ABE777CE43",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 51,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "502C37614F78819D0679D9B492FACD05",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Hacking_Hunter.Challenge_Hacking_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 7500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "25233E9C498B046CE3834CA39CC40F68",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Hacking_Hunter.Challenge_Hacking_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 10500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "258CF54E4B083D00CDB22F8436E8DACA",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_LastMAnStanding_Hunter.Challenge_LastManStanding_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 1,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "E25E5A8A4C58C3C184104480207DC761",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HackCrates_Hunter.Challenge_HackCrates_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 35,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "B79C42B1464BC0D9E263608E0C5931F0",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_RingOut_Hunter.Challenge_RingOut_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 216,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "359DE01D40A363D83FC7CE84029958D1",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Stomp_Hunter.Challenge_Stomp_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 34,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "8E82394549CE12A39CB119BBA3548A3A",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Reveal_Hunter.Challenge_Reveal_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 125,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "BE290D2245088B230DEB0AB49D24ABD1",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates",
        "faction": "General",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D2B103364D0138EA4D8FCEBE9290734D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HackCrates_Hunter.Challenge_HackCrates_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 25,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "582C65B8429B0E12F8ADBBA732FB242B",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates",
        "faction": "General",
        "ChallengeCompletionValue": 21,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "99FCD5D141D233B0AA10B09499B5B726",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_LastMAnStanding_Hunter.Challenge_LastManStanding_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 2,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "3E17BB214E97BDD16C26B2ABAB472F4B",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_LastMAnStanding_Hunter.Challenge_LastManStanding_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 4,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "7144FA8F4DC8586E27E4AFB100B526CB",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Drones_Hunter.Challenge_Drones_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 7500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D03DA2884E91DB6FB5298D8B1AD5A831",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Hunter.Challenge_Travel_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 21000,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "CE1D8624459B18BB427360A65B336B5F",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_RingOut_Hunter.Challenge_RingOut_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 120,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "ED11BF044F9AA2F46AA339863D0F1FCA",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 21,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "9C5D248F47ABC797C34B859D0D848350",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Drones_Hunter.Challenge_Drones_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 2700,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "9BB10EEC48A4E344BCB8A1902C4211FE",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates",
        "faction": "General",
        "ChallengeCompletionValue": 51,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "C3A86FC14225D5195536F1901A622FC4",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 75,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "323ABD8E49F88B732D8188B2E3338203",
        "challengeBlueprint": "/Game/Challenges/Challenge_DroneCharger_Hunter.Challenge_DroneCharger_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "928704A143ED2A240C30009631469493",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HackCrates_Hunter.Challenge_HackCrates_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 25,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "62E041F845C382EE592B378372EFBDA6",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Reveal_Hunter.Challenge_Reveal_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 35,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "73090F59403D011E60D07CAF6A5D3B38",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 2160,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "1774AD6B4C4BA913168C0AB98AD3720E",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Hunter.Challenge_Travel_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 10200,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "77F6C3CD405B8984C18C0E82E7F8494F",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HackCrates_Hunter.Challenge_HackCrates_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 125,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "69CC6D4841E3E865AE14D9BF9651262F",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Hunter.Challenge_Travel_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 21000,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "C9CA82B34CDA32C160B191BAF80EECC8",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_LastMAnStanding_Hunter.Challenge_LastManStanding_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 1,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "FF384041406E46D36B3D4D8774B87E26",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Drones_Hunter.Challenge_Drones_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 2100,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "883292D0456E314E41C9939C44EE9ECA",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Downing_Hunter.Challenge_Downing_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 15120,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "B5462A3D4FB854FF46050BA4C5FF1119",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_LastMAnStanding_Hunter.Challenge_LastManStanding_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 4,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "B610A93A4E5724CD4673C28542313CD1",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Downing_Hunter.Challenge_Downing_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 42000,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "C7CAB62544C9C8AF72AF45AB9D7D92E1",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_LastMAnStanding_Hunter.Challenge_LastManStanding_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 7,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "772734FF40F812A1EA66119037FBD8B1",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Hacking_Hunter.Challenge_Hacking_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 1500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "A12FA6C041D02002022496877A0148F0",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Supercharge_Hunter.Challenge_Supercharge_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 168,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "77EFA0114751FB5555D037BA34C54D97",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 27,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "E7CA31CC405280433D2C44BA65277CA5",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Supercharge_Hunter.Challenge_Supercharge_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 408,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "C499B1EC45D8174D4EDB0CBE735F0F80",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Reveal_Hunter.Challenge_Reveal_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 125,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "1B49E9ED4D9C7AADED6B66BEC9688F5C",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates",
        "faction": "General",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "E5220391492AFD2B354815AE2A1B517C",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HackCrates_Hunter.Challenge_HackCrates_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 25,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "A71A05964273C756A2FEF382566C7878",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Downing_Hunter.Challenge_Downing_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 11760,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "DE0F5DA34BF1532B2FF4B39279BB1FA7",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_RingOut_Hunter.Challenge_RingOut_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 216,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "6C99A51C4EB589A8A37DB3A32FC76A3D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Execution_Hunter.Challenge_Execution_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 25500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "CDC366604DCA8B506538EABC506A915D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Execution_Hunter.Challenge_Execution_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 37500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "2550058642E1B9453138C2AE42E974F7",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "8CC7F2D847E54850AF7D6DBC26704D1F",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Drones_Hunter.Challenge_Drones_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 1500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "3F54925A4297A06A834353ACE22E2D62",
        "challengeBlueprint": "/Game/Challenges/Challenge_DroneCharger_Hunter.Challenge_DroneCharger_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 21,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "1F96617648BE2D3A7AFCAEB0E8F2F3A3",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Hunter.Challenge_Travel_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 5400,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "5B495EB24E9A52F92AB11E8F402443F2",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Hunter.Challenge_Travel_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 10200,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "83AD10264C70F950AACF5592269F1378",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Aim_Hunter.Challenge_Aim_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 25,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "A8A6DE22402055670F921A9597805615",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Supercharge_Hunter.Challenge_Supercharge_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 840,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "62EC375C42A55B0002909AA7D930E5D9",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Drones_Hunter.Challenge_Drones_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 1500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "434B35DB4A4D2BB2F7386199E7A0D015",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates",
        "faction": "General",
        "ChallengeCompletionValue": 21,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "DED9AB8249C47DD58202F4BE6B4798A8",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Reveal_Hunter.Challenge_Reveal_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 45,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "8AD3C9C74E94440706B3619EE91910AA",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Hunter.Challenge_Travel_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 10200,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D5BE1E024A3DE77193295B9EA20D6450",
        "challengeBlueprint": "/Game/Challenges/Challenge_DroneCharger_Hunter.Challenge_DroneCharger_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 75,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "96FF5A4344D5C642E9E5F697F35614E7",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Drones_Hunter.Challenge_Drones_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 10500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D736300846860319BD4165ABBB35E0F0",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_RingOut_Hunter.Challenge_RingOut_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 120,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "2040B158499CF4E5BDF741838F099C89",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_RingOut_Hunter.Challenge_RingOut_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 168,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "914189F446CA895E7A573ABE78E11AC5",
        "challengeBlueprint": "/Game/Challenges/Challenge_DroneCharger_Hunter.Challenge_DroneCharger_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 27,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "E1028BB24DC0CD5B274A2B83610355B4",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Execution_Hunter.Challenge_Execution_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 25500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "A385E5C340620E2D675BC09A664B3247",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates",
        "faction": "General",
        "ChallengeCompletionValue": 75,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "B0818B5B4C91EF0FEF7F64AFA1DB63BE",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "A7E716234CA8E96F061BB680B60A6E06",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HackCrates_Hunter.Challenge_HackCrates_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 25,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "DCE6B1964F09A62636AA6A8A1F20C107",
        "challengeBlueprint": "/Game/Challenges/Challenge_DroneCharger_Hunter.Challenge_DroneCharger_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 21,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "770A825A4A0AF2B30F9008ABE398996A",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HackCrates_Hunter.Challenge_HackCrates_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 45,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "B3A0F9234DABA3A63BD4AAA3EC439849",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates",
        "faction": "General",
        "ChallengeCompletionValue": 51,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "FF5F17DE41610116334B59BC45FE3E76",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 75,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "CEBB3A6B40D76CF894B4E4ACCEBF0285",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "4E051CD848C32CE45A397F890D4908F5",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_LastMAnStanding_Hunter.Challenge_LastManStanding_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 1,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "1A725A8B411BA4BB005C63BE240523AC",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Drones_Hunter.Challenge_Drones_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 2100,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "AC06AD744F279F2AA412E7817A2CBB6B",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 27,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "0F1DC6A34F9695425924CE8FB66BD430",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Aim_Hunter.Challenge_Aim_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 17,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D19B92E442D0372CC14AE7A0125FA8B8",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_RingOut_Hunter.Challenge_RingOut_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 600,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "7656C3584F8994BF46F4BD8B3D724B69",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates",
        "faction": "General",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "610073E94C98886783DBBBA65B50DC1D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Hunter.Challenge_Travel_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 3000,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "7F936C8A4B2705EF67ED9794A0758BC7",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates",
        "faction": "General",
        "ChallengeCompletionValue": 21,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D369B7744CDB442D8D8D9B9579189B0D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Stomp_Hunter.Challenge_Stomp_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 18,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D7E161954B0954964DFC41A879AFF7D6",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_LastMAnStanding_Hunter.Challenge_LastManStanding_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 4,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "001844EF46B0EF6E2AF3108BB447088C",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_LastMAnStanding_Hunter.Challenge_LastManStanding_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 5,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "50D46D4D4F58CD06A872198C8B18F88E",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Drones_Hunter.Challenge_Drones_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 10500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "AC2C60A54BD71F1F32A154BA132F10D6",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HackCrates_Hunter.Challenge_HackCrates_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 25,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "BD2B49D94146B776376B99A45A94FB1D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Hunter.Challenge_Travel_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 4200,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "3D327CBE4A80BBB0310712857EBFCE17",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Hunter.Challenge_Travel_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 5400,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "714366294138F4F41A09F99A74A22271",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Reveal_Hunter.Challenge_Reveal_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 85,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "048EE1BF48FA9959F8C52DBF0CEFB581",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 6000,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "E9BF5BA248A2F153522A66B1C0FEF086",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates",
        "faction": "General",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "0DA8CED0485630A82C86DDBE67FD77F4",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Downing_Hunter.Challenge_Downing_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 8400,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "65ECFFBE4E5AAB374008A484A4D692E4",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HackCrates_Hunter.Challenge_HackCrates_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 35,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "C46A63354887C01D6F9237A45EC6E078",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 27,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "E4E30D514747443042FF88BE2780E672",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Execution_Hunter.Challenge_Execution_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 25500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "A389FBD64B864CADB7D30D92B6814A68",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Supercharge_Hunter.Challenge_Supercharge_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 600,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "8DA38F1B4FB47300699E8381871CB36D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_LastMAnStanding_Hunter.Challenge_LastManStanding_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 7,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D838C1B64F5351869803A28F3B041C32",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Drones_Hunter.Challenge_Drones_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 1500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "AD32D3CB40997A00DE699EA32CBBF0FF",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Drones_Hunter.Challenge_Drones_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 2100,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "5A37EACA4EEADA1BA6767EB43F542FC3",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_LastMAnStanding_Hunter.Challenge_LastManStanding_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 2,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "DCF4B7814E942E1573D7EF99EA14DD0F",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Reveal_Hunter.Challenge_Reveal_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 85,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "0E568A0E478FCC9153B8A3ADB8D54D06",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Execution_Hunter.Challenge_Execution_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 37500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "7A27F5B145D118D792B2D8B59969481A",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "70CF13894A5D4CFA690DB182559EE85A",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 15,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "FA5164ED4EABE0ACE47DDDAC3E854BDF",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Execution_Hunter.Challenge_Execution_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 10500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "981C0DF54780E21FA5557C880FC43271",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Reveal_Hunter.Challenge_Reveal_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 45,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "B324E19D4EF7846D00E41892A45C598D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_RingOut_Hunter.Challenge_RingOut_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 408,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "48048D3640D2363CF6608DA2F3C074B7",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Hacking_Hunter.Challenge_Hacking_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 7500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "F10BBB724B55528313AD2681B3D3B71C",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Hacking_Hunter.Challenge_Hacking_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 10500,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "1718C86645AFAAE2AB4282A460A4AC84",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Hunter.Challenge_Travel_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 3000,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "BF13CF544A13A8B93B662CA89BB0745E",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_LastMAnStanding_Hunter.Challenge_LastManStanding_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 2,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "45D8760C4C4CA3E70B7E4BAE2A82D100",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Drones_Hunter.Challenge_Drones_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 2700,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "B9CACA964B9FFBC928AAC18D3C12793D",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 4080,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "3718D43F44037C86B3D20FB2DA13BADF",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Stomp_Hunter.Challenge_Stomp_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 50,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "13F9A19A4463E27403DA819BA6061993",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "756FEA904FD555DF7094D4B19A75E23F",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Aim_Hunter.Challenge_Aim_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 5,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "76111C73423154EA1A21C9BED344C90E",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates",
        "faction": "General",
        "ChallengeCompletionValue": 21,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "B18FF3DF4A199C8F4909B38C332F8A69",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HackCrates_Hunter.Challenge_HackCrates_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 45,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "50D1FAC647B70C1641E9F5BA7DF2F8A0",
        "challengeBlueprint": "/Game/Challenges/Challenge_DroneCharger_Hunter.Challenge_DroneCharger_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 51,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "CA3312CE4ADAA5153567269E4B31CDA9",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectHealthCrates.Challenge_CollectHealthCrates",
        "faction": "General",
        "ChallengeCompletionValue": 75,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "755EDB00419874E9F9400884C8345A3B",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_CollectAmmo.Challenge_CollectAmmo",
        "faction": "General",
        "ChallengeCompletionValue": 105,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "52D4F4D64D20D1969C720E98152F9069",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Damage_Hunter.Challenge_Damage_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 1200,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "D3F497FE47D42165A2ABF2A910C0A3A6",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_HackCrates_Hunter.Challenge_HackCrates_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 35,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "65EB708940DDCE3FA7B8DAA8C3A22801",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Supercharge_Hunter.Challenge_Supercharge_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 216,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "F73A9EB14513566DB5334A8A35D5001C",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Supercharge_Hunter.Challenge_Supercharge_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 408,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "913147E74F09B0816CD1E7860A0C809A",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Travel_Hunter.Challenge_Travel_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 15000,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "DFF9C1BF47B317D864B924B776C793C4",
        "challengeBlueprint": "/Game/Challenges/Progression/General/Challenge_Downing_Hunter.Challenge_Downing_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 58800,
        "type": "currency",
        "challengeType": "ChallengeProgressionCounter"
    },
    {
        "challenge_id": "Challenge_Domination_Hunter",
        "challengeBlueprint": "/Game/Challenges/Daily/Challenge_Domination_Hunter.Challenge_Domination_Hunter",
        "faction": "Hunter",
        "ChallengeCompletionValue": 1,
        "type": "currency",
        "challengeType": "Daily"
    },
    {
        "challenge_id": "Challenge_Deliver_Runner",
        "challengeBlueprint": "/Game/Challenges/Daily/Challenge_Deliver_Runner.Challenge_Deliver_Runner",
        "faction": "Runner",
        "ChallengeCompletionValue": 50,
        "type": "currency",
        "challengeType": "Daily"
    }
]


unknown_challenges = [
         "BA2D4A5445CB70276A8F5D9E1AFCE080",
         "AAD05B9D46471DC811BBE0BA91916AB7",
         "E51981B946BEE3D45C5C41B2FCFF310B",
         "2CAEBB354D506D7C43B941BC1DA775A0",
         "EFAB89E6465D1163D62A07B11048F2B6",
         "B78308DF48036BCF914060944AAF4A19",
         "4B140F6E4B53D6C249FE3F8FC42E4DA5",
         "EB1241634D002F8BC4D1AEA75BEDB285",
         "23941697434305C8E373C7A88D4EBBEC",
         "8AD5A0194A0528BDC957EFABCFF03CA4",
         "0B0F4B304275B9933051E7966D6A5E00",
         "BB546B5140211D2D316AAFA8A83CE8BF",
         "D19B97D4407780490BBAFBB5446C24C3",
         "4D6510D3474A414BE76C95A42D09024C",
         "5B9CCC03408C7B49717192831A9E4288",
         "9537D1064AF1BFE099FDB7A6751D9AB6",
         "35ACE3734A321824B6FE909ACC96C8C4",
         "D8E343EB49F4DBA11DA6A19E409A4661",
         "6D79A03B4F3E4EDA33FAD69FF55289BA",
         "FEBF64E8455F901A5DC7D0BD14BB1400",
         "439B378440E88E8F1F514FB4877951D6",
         "B409ED514217FB125D510496C256AE2D",
         "24CE65364362CB2A90C0E08876176937",
         "22B70F5B49B3973D84DD9E9E621987BC",
         "5649ABFE45E32AAAE6993E9DEBFB06FD",
         "E231B784476D659DDFAB5B8F6C05D01A",
         "6A3080A643C13A17FEF94C96368FC752",
         "9A0964D947748E6C0338AA9684DF1055",
         "FE25D08C41CAED4853FA41823E3661C8",
         "2E36387D422C70F5F5538D8E62063E14",
         "BF755068484D5C88B1D2F2B625942D20",
         "B0B11BDC4AF524274D6171A8BF605CF8",
         "885A5CBE4C36F665FA3296ABDD81D610",
         "BB00FFB542608BF6A46A668DDDD2FEC4",
         "DC82CE9C471895975D5767B5D560D7E5",
         "61F8376740A0EF3457B397AB9F50C3B7",
         "AF8CBA94413BCED1445D269F99D3F747",
         "4C89321E49A5E4F0FD8F2C96B0FB612E",
         "0E9820174B86BE2CAD3FD0A7958D2936",
         "F53EA76F418A09E564BDC8B1A46C09AD",
         "F2D57F3443BF0F1A162ED8AF80A509D7",
         "37B650F145BF27B3B670CB9D84D58111",
         "8419C3F7425A874050B1FCA9D0A611F1",
         "812917BD4AE4A5C7B80C78944F940262",
         "9ECC51DF4F4385EC87E35E9C18EECA0B",
         "2ABDC29A4D174CDC114AEBACB898927E",
         "CB47A1954EC9E8628ECA06A49D75B312",
         "856D77794A0B22750E907F955EC3CFBA",
         "195A67754C681147F9CE59AEB7E7BEC7",
         "4F99C43949B5CAC87BCEB4877B7FAB64",
         "688EC1704C4EA4BCB18181ADE23E2C3D",
         "E575BCFA4267C3414C79C2AD8083290C",
         "71DB143B4CF6A8699FA9318B96423747",
         "3459AEC7438F69ED834D5687D9AACACB",
         "0A728AD54AF5EAB6CB4356A074F01C1B",
         "00AD3B9242B7410E078240B39E64C3E6",
         "B055D23146B974285C57B7A20F373E56",
         "3B3A64794CD311B80C0025A511FA6011",
         "FD314A694D049989202D01BC36269F44",
         "950524C144BE794AABFFED8142C119B4",
         "E6FD8271485E71993830409FA5C88F48",
         "1A314E87440477C6FFB56083E0E3755C",
         "103B1ED848C7EE0BF31EB49C07375EB1",
         "15C925544AA67E20214C8AB09F5B33E9",
         "5B4DC5E840CE26A7D014CF8EBB05AF77",
         "D5F76E7C4BDC3B94534089AEB9A764A3",
         "436D7A0343761BC74BD353B2CE4E80BC",
         "B4B156CC47C8D987B9BDBEB910B12C9E",
         "B54522334820602C6E998D9FD7E785BA",
         "328F1E204B3675B4DF8B1CBAFB226224",
         "9B1FD9DF461803D0FA039BBD2B0093C4",
         "A34BD07D4BE1D72F0E10EEBB626795F0",
         "6CAD2AAC4C56C1224448C599A0E16119",
         "F1F4BDCF4672C243DCDF9895F511E445",
         "35FC22764C5A44D0968058AF6BFC3770",
         "57F0FFB346492B6A8A458893A17ECBB7",
         "ECCBA78D4055676F9C17D79B9D5FA2D4"
      ]
# import json catalog
path = "../src/json/catalog/te-18f25613-36778-ue4-374f864b/catalog.json"
with open(path, 'r') as f:
    catalog_data = json.load(f)


for unknown in unknown_challenges:
    found = False
    for item in challenge_data:
        if item["challenge_id"] == unknown:
            print(f"Challenge found: {unknown}")
            found = True
            break
    if not found:
        for item in catalog_data["result"]:
            try:
                for challenge in item["requiredChallengesToComplete"]:
                    if challenge == unknown:
                        print(f"Challenge found in catalog: {unknown}")
                        found = True
                        break
            except KeyError:
                pass

    list_passed = [
    "B4B156CC47C8D987B9BDBEB910B12C9E",
    "15C925544AA67E20214C8AB09F5B33E9",
    "950524C144BE794AABFFED8142C119B4",
    "F2D57F3443BF0F1A162ED8AF80A509D7",
    "AF8CBA94413BCED1445D269F99D3F747",
    "885A5CBE4C36F665FA3296ABDD81D610",
    "FD314A694D049989202D01BC36269F44",
    "0A728AD54AF5EAB6CB4356A074F01C1B",
    "688EC1704C4EA4BCB18181ADE23E2C3D",
    "4F99C43949B5CAC87BCEB4877B7FAB64",
    "2ABDC29A4D174CDC114AEBACB898927E",
    "37B650F145BF27B3B670CB9D84D58111",
    "B0B11BDC4AF524274D6171A8BF605CF8",
    "9A0964D947748E6C0338AA9684DF1055",
    "22B70F5B49B3973D84DD9E9E621987BC",
    "ECCBA78D4055676F9C17D79B9D5FA2D4",
    "6CAD2AAC4C56C1224448C599A0E16119",
    "B54522334820602C6E998D9FD7E785BA",
    "4D6510D3474A414BE76C95A42D09024C",
    "8AD5A0194A0528BDC957EFABCFF03CA4",
    "B78308DF48036BCF914060944AAF4A19",
    "24CE65364362CB2A90C0E08876176937",
    "6D79A03B4F3E4EDA33FAD69FF55289BA",
    "5B9CCC03408C7B49717192831A9E4288"
    ]
    if unknown not in list_passed:
        print(f"Challenge not found: {unknown}")



