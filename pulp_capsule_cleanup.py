""" App to cleanup Satellite Capsule when removing the lifecycle """

import re
import requests
import urllib3
from const import SAT_SERVER, CAPSULE_NAME, USERNAME, PASSWORD, CONF_FILE


global lfc_sat_server

lfc_sat_server = []
lfc_sat_server_full = []
lfc_diff = []
repos_sat_capsule = []
repos_to_delete = []

"""
Capsule Cleanup

    0. Reading pulp conf file to retrieve the user and password
        - read_conf()

    1. Will retrieve the information related to the Capsule
        - retrieve_capsule_info()

    2. Will retrieve the lifecycle from Capsule
        - lifecycle_capsule(ch_id)

    3. Will retrieve all life cycles from Satellite Server
        - retrieve_all_lifecycles()

    4. Will retrieve the complete repo list from Capsule
        - retrieve_repo_list()

    5. Will compare lists and define what will be removed *repo*
        - compare_lists()

    6. Will delete the repos
        - delete_repos()

    7. Will delete all orphan objects
        - delete_orphan_objects()

"""


def read_conf():
    global CAP_USERNAME
    global CAP_PASSWORD

    f = open(CONF_FILE, "r")

    for line_file in f:
        if re.findall("^default_login", line_file):
            fields_line = re.split(":", line_file)
            CAP_USERNAME = fields_line[1].strip()
            print("Pulp Username: " + CAP_USERNAME)

        if re.findall("^default_password", line_file):
            fields_line = re.split(":", line_file)
            CAP_PASSWORD = fields_line[1].strip()
            print("Pulp Password: " + CAP_PASSWORD)


def retrieve_capsule_info():
    """ Responsible for retrieve the capsule info """

    print("Sat Server: " + SAT_SERVER)
    print("Ext Capsule: " + CAPSULE_NAME)
    urllib3.disable_warnings()
    capsule_content = requests.get(SAT_SERVER+"/katello/api/capsules", \
        auth=(USERNAME, PASSWORD), verify=False)

    data_capsule_content = capsule_content.json()

    for capsule in data_capsule_content.get('results'):
        # print (capsule.get('name'))
        if CAPSULE_NAME in capsule.get('name'):
            print("capsule hostname: " + capsule.get('name'))
            print("capsule id: " + str(capsule.get('id')))
            lifecycle_capsule(str(capsule.get('id')))

    print("LFC on capsule " + CAPSULE_NAME + " from Satellite perspective: " + str(lfc_sat_server))

def lifecycle_capsule(ch_id):
    """ Just to check the ID passed """
    # print("ID Passed: " + ch_id)
    content_sat_view = requests.get(SAT_SERVER+"/katello/api/capsules/" + ch_id + "/content/lifecycle_environments", \
        auth=(USERNAME, PASSWORD), verify=False)
    data_content_sat_view = content_sat_view.json()

    for lfc in data_content_sat_view.get('results'):
        """ print the lifecycle name on the capsule from Satellite perspective """
        # print(lfc.get('name'))
        lfc_sat_server.append(lfc.get('name'))


def retrieve_all_lifecycles():
    """ Responsible for retrieve all life cycles """
    aux = []
    full_environments = requests.get(SAT_SERVER+"/katello/api/environments/", \
        auth=(USERNAME, PASSWORD), verify=False)
    data_full_environments = full_environments.json()
    # print(data_ext_capsule_content)
    for env in data_full_environments.get('results'):
        # print(env.get('name'))
        aux.append(env.get('name'))
        # repos_sat_capsule.append(repo.get('id'))

    global lfc_sat_server_full
    lfc_sat_server_full = set(aux)


def retrieve_repo_list():
    """ Responsible for retrieve the repo list """
    print("Retrieving repo list via pulp api")
    # curl -X GET -su admin:aZCehD5szBULC4z2EZhHFZGg5BJav9je -k https://sat631caps.local.domain/pulp/api/v2/repositories/
    global repos_sat_capsule

    ext_capsule_content = requests.get("https://"+CAPSULE_NAME+"/pulp/api/v2/repositories/", \
        auth=(CAP_USERNAME, CAP_PASSWORD), verify=False)
    data_ext_capsule_content = ext_capsule_content.json()
    # print(data_ext_capsule_content)
    for repo in data_ext_capsule_content:
        # print(repo.get('id'))
        repos_sat_capsule.append(repo.get('id'))


def compare_lists():
    """ Comparing values to figure out what will be removed """
    # print("Let's compare the list")
    stage_list = []

    global lfc_diff
    lfc_diff = set(lfc_sat_server_full).difference(lfc_sat_server)


    for i in lfc_diff:
        for j in repos_sat_capsule:
            if i in j:
                # print("FOI: " + i + "--" + j)
                stage_list.append(i)

    global repos_to_delete
    repos_to_delete = set(stage_list)
    print("To be removed on the Capsule: " + str(repos_to_delete))


def delete_repos():
    # print("deleting .....")
    """ This will delete all repos on the list repos_to_delete """
    for lfc in repos_to_delete:
            for repo in repos_sat_capsule:
                if lfc in repo:
                    print("Deleting repo " + repo + " of lifecycle " + lfc)
                    delete_repo_req = requests.delete("https://"+CAPSULE_NAME+"/pulp/api/v2/repositories/"+repo, \
                        auth=(CAP_USERNAME, CAP_PASSWORD), verify=False)
                    data_delete_repo_req = delete_repo_req.json()
                    print("Delete return info: " + str(data_delete_repo_req))


def delete_orphan_objects():
    """ removing orphan objects """
    if not repos_to_delete:
        print("Orphans ... Nothing to do")
    else:
        delete_orphan = requests.delete("https://"+CAPSULE_NAME+"/pulp/api/v2/content/orphans/", \
            auth=(CAP_USERNAME, CAP_PASSWORD), verify=False)
        data_delete_orphan = delete_orphan.json
        print("Delete orphan info: " + str(data_delete_orphan))


def main():
    """ main function """

    read_conf()
    retrieve_capsule_info()
    retrieve_all_lifecycles()
    retrieve_repo_list()
    compare_lists()
    delete_repos()

    delete_orphan_objects()

    print("All lfc: " + str(lfc_sat_server_full))
    print("Sat repo: " + str(lfc_sat_server))
    print("Ext Caps: " + str(repos_sat_capsule))


if __name__ == "__main__":
    main()
