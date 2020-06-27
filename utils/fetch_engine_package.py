import json


def pkg_details(ds_type):
    with open("./settings.json", "r") as sj:
        setting_list = json.load(sj)
    return setting_list["db_engines"][ds_type] if setting_list else False


if __name__ == "__main__":
    det = pkg_details('destination')
    print(det)
