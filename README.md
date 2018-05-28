# pulp_capsule_cleanup

Welcome, the idea of this project is just to reclaim space on file system from Satellite Capsules after remove one/a lot lifecycles from the Capsule. Actually the product doesn't provide any tool or feature to do it, then this app will help on this process.

Below instuctions about how to use.

- Do one backup of your machine :-), this script is not supported by the Company, actually is just to improve the funcionality and fix some issues related to space/storage.
- Copy this file to the Satellite Capsule
- Will be necessary edit the file pulp_cleanup.py */etc/pulp_cleanup.conf -- symlink* to update the username / password to authenticate on the Satellite. Yet on the same file, will be necessary update the pulp password

All information below
~~~
SAT_SERVER="http://sat631.local.domain"
USERNAME="admin"
PASSWORD="redhat"
~~~
There is another flag named COMMIT, by default is False and means, no file/repo will be touched on your Capsule file system. If you change it to 
~~~
COMMIT=False
~~~


- Now it's time to execute the script, the same will verify all lifecycles / repos and will remove what should not be anymore on your environment.

Note. All information will be logged on the default output *terminal*, soon I'll implement the log feature.

Now, live :-)


Nothing change on my env and actually I can see some lifecycles *[u'lfc_zabbix', u'lfc1', u'lfc2', u'lfc3', u'dev-lfc3']*
~~~
Sat Server: http://sat631.local.domainExt Capsule: sat631caps.local.domaincapsule hostname: sat631caps.local.domaincapsule id: 2
LFC on capsule sat631caps.local.domain from Satellite perspective: [u'lfc_zabbix', u'lfc1', u'lfc2', u'lfc3', u'dev-lfc3']
CAPsTo be removed on the Capsule: set([])
Orphans ... Nothing to do
All lfc: set([u'dev-lfc3', u'Library', u'lfc_zabbix', u'lfc3', u'lfc2', u'lfc1'])
Sat repo: [u'lfc_zabbix', u'lfc1', u'lfc2', u'lfc3', u'dev-lfc3']
Ext Caps: [u'1-cv_all_zabbix-lfc_zabbix-6c8bfc83-08b0-4ace-9f2f-f18dbeed6f70', u'1-cv_all_zabbix-lfc_zabbix-5e0087e1-7e72-42b4-82f9-13efb5f51bbe', u'1-cv_all_zabbix-lfc_zabbi
x-4b5dce23-cb23-445f-8598-d2e4ec5480c2', u'1-cv_all_zabbix-lfc_zabbix-b241de8e-2848-40d7-afd8-eb2815ce2b46', u'1-cv_all_zabbix-lfc_zabbix-863326ff-74c8-439f-a6f9-0a24580f5421
', u'1-cv_all_zabbix-lfc_zabbix-e78e53aa-02d0-46e3-96a6-e4953a93f9a7', u'1-test-lfc2-6c8bfc83-08b0-4ace-9f2f-f18dbeed6f70', u'1-test-test-test-lfc3-b7c68510-69c6-4cb1-b98f-a6
4c622f19d6', u'1-test-lfc2-4b5dce23-cb23-445f-8598-d2e4ec5480c2', u'1-cv_rhel_test2-lfc1-3d430f89-2482-4693-a653-1ac62a8101be', u'1-cv_rhel_test1-lfc1-5328890d-f633-4404-af68
-a5ac979c166c', u'1-cv_all_zabbix-lfc_zabbix-3a268ef7-4cec-4228-aea2-5baf08542f63', u'1-cv_all_zabbix-lfc_zabbix-905aba62-5fa3-4255-8297-8258d12c13e7', u'1-cv_all_zabbix-lfc_
zabbix-6df74399-90a6-4922-a5cf-1b6c9e45196e', u'1-cv_all_zabbix-lfc_zabbix-b7c68510-69c6-4cb1-b98f-a64c622f19d6']
~~~


Ok, let's remove the lifecycle *lfc_zabbix and lfc1* via Satellite webUI and then rerun the script
~~~
Sat Server: http://sat631.local.domainExt Capsule: sat631caps.local.domaincapsule hostname: sat631caps.local.domaincapsule id: 2
LFC on capsule sat631caps.local.domain from Satellite perspective: [u'lfc2', u'lfc3', u'dev-lfc3']
CAPs
To be removed on the Capsule: set([u'lfc1', u'lfc_zabbix'])

Deleting repo 1-cv_rhel_test2-lfc1-3d430f89-2482-4693-a653-1ac62a8101be of lifecycle lfc1
Delete return info: {u'spawned_tasks': [{u'_href': u'/pulp/api/v2/tasks/87c9f185-c97d-468c-ac17-210d6a89ac34/', u'task_id': u'87c9f185-c97d-468c-ac17-210d6a89ac34'}], u'result': None, u'error': None}

Deleting repo 1-cv_rhel_test1-lfc1-5328890d-f633-4404-af68-a5ac979c166c of lifecycle lfc1
Delete return info: {u'spawned_tasks': [{u'_href': u'/pulp/api/v2/tasks/cb03472f-a516-4f23-915c-cb12c3669cf1/', u'task_id': u'cb03472f-a516-4f23-915c-cb12c3669cf1'}], u'result': None, u'error': None}

Deleting repo 1-cv_all_zabbix-lfc_zabbix-6c8bfc83-08b0-4ace-9f2f-f18dbeed6f70 of lifecycle lfc_zabbix
Delete return info: {u'spawned_tasks': [{u'_href': u'/pulp/api/v2/tasks/52699632-2333-49c3-bccc-59ca190889a9/', u'task_id': u'52699632-2333-49c3-bccc-59ca190889a9'}], u'result': None, u'error': None}

Deleting repo 1-cv_all_zabbix-lfc_zabbix-5e0087e1-7e72-42b4-82f9-13efb5f51bbe of lifecycle lfc_zabbix
Delete return info: {u'spawned_tasks': [{u'_href': u'/pulp/api/v2/tasks/b511ed4f-8be5-4f6e-a72b-797706e0794b/', u'task_id': u'b511ed4f-8be5-4f6e-a72b-797706e0794b'}], u'result': None, u'error': None}

Deleting repo 1-cv_all_zabbix-lfc_zabbix-4b5dce23-cb23-445f-8598-d2e4ec5480c2 of lifecycle lfc_zabbix
Delete return info: {u'spawned_tasks': [{u'_href': u'/pulp/api/v2/tasks/7bcd4e1f-2d57-4b9f-b2a7-9f0c76cb75a2/', u'task_id': u'7bcd4e1f-2d57-4b9f-b2a7-9f0c76cb75a2'}], u'result': None, u'error': None}

Deleting repo 1-cv_all_zabbix-lfc_zabbix-b241de8e-2848-40d7-afd8-eb2815ce2b46 of lifecycle lfc_zabbix
Delete return info: {u'spawned_tasks': [{u'_href': u'/pulp/api/v2/tasks/3957ec6d-fb44-49f1-958d-754135f8e168/', u'task_id': u'3957ec6d-fb44-49f1-958d-754135f8e168'}], u'result': None, u'error': None}

Deleting repo 1-cv_all_zabbix-lfc_zabbix-863326ff-74c8-439f-a6f9-0a24580f5421 of lifecycle lfc_zabbix
Delete return info: {u'spawned_tasks': [{u'_href': u'/pulp/api/v2/tasks/5697f72b-7ba5-489f-b73f-0c6e6252d7cb/', u'task_id': u'5697f72b-7ba5-489f-b73f-0c6e6252d7cb'}], u'result': None, u'error': None}

Deleting repo 1-cv_all_zabbix-lfc_zabbix-e78e53aa-02d0-46e3-96a6-e4953a93f9a7 of lifecycle lfc_zabbix
Delete return info: {u'spawned_tasks': [{u'_href': u'/pulp/api/v2/tasks/a25f4b4c-e28f-483a-8457-bc09de276b07/', u'task_id': u'a25f4b4c-e28f-483a-8457-bc09de276b07'}], u'result': None, u'error': None}

Deleting repo 1-cv_all_zabbix-lfc_zabbix-3a268ef7-4cec-4228-aea2-5baf08542f63 of lifecycle lfc_zabbix
Delete return info: {u'spawned_tasks': [{u'_href': u'/pulp/api/v2/tasks/6ae73b97-062c-46cb-a2ff-2f68737f9c5b/', u'task_id': u'6ae73b97-062c-46cb-a2ff-2f68737f9c5b'}], u'result': None, u'error': None}

Deleting repo 1-cv_all_zabbix-lfc_zabbix-905aba62-5fa3-4255-8297-8258d12c13e7 of lifecycle lfc_zabbix
Delete return info: {u'spawned_tasks': [{u'_href': u'/pulp/api/v2/tasks/34036e60-5113-4f00-8cda-1000ae6422eb/', u'task_id': u'34036e60-5113-4f00-8cda-1000ae6422eb'}], u'result': None, u'error': None}

Deleting repo 1-cv_all_zabbix-lfc_zabbix-6df74399-90a6-4922-a5cf-1b6c9e45196e of lifecycle lfc_zabbix
Delete return info: {u'spawned_tasks': [{u'_href': u'/pulp/api/v2/tasks/2c64cbb8-1462-423d-8bc4-4f20c630cb8a/', u'task_id': u'2c64cbb8-1462-423d-8bc4-4f20c630cb8a'}], u'result': None, u'error': None}

Deleting repo 1-cv_all_zabbix-lfc_zabbix-b7c68510-69c6-4cb1-b98f-a64c622f19d6 of lifecycle lfc_zabbix
Delete return info: {u'spawned_tasks': [{u'_href': u'/pulp/api/v2/tasks/3eccd651-8d12-4fef-8475-92624115c5a0/', u'task_id': u'3eccd651-8d12-4fef-8475-92624115c5a0'}], u'result': None, u'error': None}

Delete orphan info: <bound method Response.json of <Response [202]>>

All lfc: set([u'dev-lfc3', u'Library', u'lfc_zabbix', u'lfc3', u'lfc2', u'lfc1'])

Sat repo: [u'lfc2', u'lfc3', u'dev-lfc3']

Ext Caps: [u'1-cv_all_zabbix-lfc_zabbix-6c8bfc83-08b0-4ace-9f2f-f18dbeed6f70', u'1-cv_all_zabbix-lfc_zabbix-5e0087e1-7e72-42b4-82f9-13efb5f51bbe', u'1-cv_all_zabbix-lfc_zabbix-4b5dce23-cb23-445f-8598-d2e4ec5480c2', u'1-cv_all_zabbix-lfc_zabbix-b241de8e-2848-40d7-afd8-eb2815ce2b46', u'1-cv_all_zabbix-lfc_zabbix-863326ff-74c8-439f-a6f9-0a24580f5421', u'1-cv_all_zabbix-lfc_zabbix-e78e53aa-02d0-46e3-96a6-e4953a93f9a7', u'1-test-lfc2-6c8bfc83-08b0-4ace-9f2f-f18dbeed6f70', u'1-test-test-test-lfc3-b7c68510-69c6-4cb1-b98f-a64c622f19d6', u'1-test-lfc2-4b5dce23-cb23-445f-8598-d2e4ec5480c2', u'1-cv_rhel_test2-lfc1-3d430f89-2482-4693-a653-1ac62a8101be', u'1-cv_rhel_test1-lfc1-5328890d-f633-4404-af68-a5ac979c166c', u'1-cv_all_zabbix-lfc_zabbix-3a268ef7-4cec-4228-aea2-5baf08542f63', u'1-cv_all_zabbix-lfc_zabbix-905aba62-5fa3-4255-8297-8258d12c13e7', u'1-cv_all_zabbix-lfc_zabbix-6df74399-90a6-4922-a5cf-1b6c9e45196e', u'1-cv_all_zabbix-lfc_zabbix-b7c68510-69c6-4cb1-b98f-a64c622f19d6']
~~~

and if rerun ...

~~~
Sat Server: http://sat631.local.domain
Ext Capsule: sat631caps.local.domain
capsule hostname: sat631caps.local.domain
capsule id: 2LFC on capsule sat631caps.local.domain from Satellite perspective: [u'lfc2', u'lfc3', u'dev-lfc3']
CAPs
To be removed on the Capsule: set([])
Orphans ... Nothing to do
All lfc: set([u'dev-lfc3', u'Library', u'lfc_zabbix', u'lfc3', u'lfc2', u'lfc1'])
Sat repo: [u'lfc2', u'lfc3', u'dev-lfc3']
Ext Caps: [u'1-test-lfc2-6c8bfc83-08b0-4ace-9f2f-f18dbeed6f70', u'1-test-test-test-lfc3-b7c68510-69c6-4cb1-b98f-a64c622f19d6', u'1-test-lfc2-4b5dce23-cb23-445f-8598-d2e4ec5480c2']
~~~


From Capsule / File System perspective, the best way to follow can be executing the command below
~~~
# watch "du -hs /var/lib/pulp/content"
~~~

One important part of this script is the log generated, then feel free to check in /var/log/pulp_cleanup.log*, the output will be similar to below

- Checking without lifecycle / repos to be removed
~~~
INFO 2018-05-28 17:47:38,515 Starting the cleanup process
INFO 2018-05-28 17:47:38,515 COMMIT Status: True
INFO 2018-05-28 17:47:38,516 Pulp Username: admin
INFO 2018-05-28 17:47:38,516 Pulp Password: aZCehD5szBULC4z2EZhHFZGg5BJav9je
INFO 2018-05-28 17:47:38,517 Sat Server: http://sat631.local.domain
INFO 2018-05-28 17:47:38,517 Ext Capsule: sat631caps.local.domain
INFO 2018-05-28 17:47:38,524 Starting new HTTP connection (1): sat631.local.domain
INFO 2018-05-28 17:47:38,539 Starting new HTTPS connection (1): sat631.local.domain
INFO 2018-05-28 17:47:38,599 capsule hostname: sat631caps.local.domain
INFO 2018-05-28 17:47:38,599 capsule id: 2
INFO 2018-05-28 17:47:38,600 Starting new HTTP connection (1): sat631.local.domain
INFO 2018-05-28 17:47:38,612 Starting new HTTPS connection (1): sat631.local.domain
INFO 2018-05-28 17:47:38,656 LFC on capsule sat631caps.local.domain from Satellite perspective: []
INFO 2018-05-28 17:47:38,657 Starting new HTTP connection (1): sat631.local.domain
INFO 2018-05-28 17:47:38,668 Starting new HTTPS connection (1): sat631.local.domain
INFO 2018-05-28 17:47:38,889 All LFC: set([u'dev-lfc3', u'Library', u'lfc_zabbix', u'lfc3', u'lfc2', u'lfc1'])
INFO 2018-05-28 17:47:38,889 Retrieving repo list via pulp api from capsule sat631caps.local.domain
INFO 2018-05-28 17:47:38,890 Starting new HTTPS connection (1): sat631caps.local.domain
INFO 2018-05-28 17:47:38,952 Ext Caps / Repos *all*: [u'e53f14c8-c4db-4364-94bc-b99ec02b0cdd', u'5328890d-f633-4404-af68-a5ac979c166c', u'86dc4ad5-6cb1-4444-a236-1d5f70364a9c', u'980e8031-aaa0-4339-a9ea-f8dd22545ff3', u'52ca6edc-0a6c-4443-b7d0-4a83e6c0e7e9', u'3d430f89-2482-4693-a653-1ac62a8101be', u'bd6ed606-80d4-4519-8707-3a3afbb7b7ab', u'4b55b942-9be5-41b4-ae2d-ddbda4d1f3c2', u'b241de8e-2848-40d7-afd8-eb2815ce2b46', u'905aba62-5fa3-4255-8297-8258d12c13e7', u'b7c68510-69c6-4cb1-b98f-a64c622f19d6', u'3a268ef7-4cec-4228-aea2-5baf08542f63', u'4b5dce23-cb23-445f-8598-d2e4ec5480c2', u'e78e53aa-02d0-46e3-96a6-e4953a93f9a7', u'863326ff-74c8-439f-a6f9-0a24580f5421', u'6df74399-90a6-4922-a5cf-1b6c9e45196e', u'6c8bfc83-08b0-4ace-9f2f-f18dbeed6f70', u'5e0087e1-7e72-42b4-82f9-13efb5f51bbe']
INFO 2018-05-28 17:47:38,952 To be removed on the Capsule: set([])
INFO 2018-05-28 17:47:38,952 Orphans ... Nothing to do
INFO 2018-05-28 17:47:38,952 Finishing the cleanup process
~~~

- Checking removing lifecycle / repos "lfc1"
~~~
INFO 2018-05-28 17:50:43,838 Starting the cleanup process
INFO 2018-05-28 17:50:43,838 COMMIT Status: True
INFO 2018-05-28 17:50:43,860 Pulp Username: admin
INFO 2018-05-28 17:50:43,861 Pulp Password: aZCehD5szBULC4z2EZhHFZGg5BJav9je
INFO 2018-05-28 17:50:43,862 Sat Server: http://sat631.local.domain
INFO 2018-05-28 17:50:43,862 Ext Capsule: sat631caps.local.domain
INFO 2018-05-28 17:50:43,893 Starting new HTTP connection (1): sat631.local.domain
INFO 2018-05-28 17:50:47,407 Starting new HTTPS connection (1): sat631.local.domain
INFO 2018-05-28 17:50:47,484 capsule hostname: sat631caps.local.domain
INFO 2018-05-28 17:50:47,485 capsule id: 2
INFO 2018-05-28 17:50:47,485 Starting new HTTP connection (1): sat631.local.domain
INFO 2018-05-28 17:50:47,524 Starting new HTTPS connection (1): sat631.local.domain
INFO 2018-05-28 17:50:47,719 LFC on capsule sat631caps.local.domain from Satellite perspective: [u'lfc_zabbix', u'lfc2', u'lfc3', u'dev-lfc3']
INFO 2018-05-28 17:50:47,720 Starting new HTTP connection (1): sat631.local.domain
INFO 2018-05-28 17:50:47,753 Starting new HTTPS connection (1): sat631.local.domain
INFO 2018-05-28 17:50:48,031 All LFC: set([u'dev-lfc3', u'Library', u'lfc_zabbix', u'lfc3', u'lfc2', u'lfc1'])
INFO 2018-05-28 17:50:48,031 Retrieving repo list via pulp api from capsule sat631caps.local.domain
INFO 2018-05-28 17:50:48,032 Starting new HTTPS connection (1): sat631caps.local.domain
INFO 2018-05-28 17:50:48,086 Ext Caps / Repos *all*: [u'1-cv_all_zabbix-lfc_zabbix-6df74399-90a6-4922-a5cf-1b6c9e45196e', u'1-cv_all_zabbix-lfc_zabbix-3a268ef7-4cec-4228-aea2-5baf08542f63', u'1-test-lfc2-4b5dce23-cb23-445f-8598-d2e4ec5480c2', u'1-test-lfc2-6c8bfc83-08b0-4ace-9f2f-f18dbeed6f70', u'1-cv_rhel_test2-lfc1-3d430f89-2482-4693-a653-1ac62a8101be', u'1-cv_rhel_test1-lfc1-5328890d-f633-4404-af68-a5ac979c166c', u'1-cv_all_zabbix-lfc_zabbix-863326ff-74c8-439f-a6f9-0a24580f5421', u'1-cv_all_zabbix-lfc_zabbix-b7c68510-69c6-4cb1-b98f-a64c622f19d6', u'1-cv_all_zabbix-lfc_zabbix-e78e53aa-02d0-46e3-96a6-e4953a93f9a7', u'1-cv_all_zabbix-lfc_zabbix-b241de8e-2848-40d7-afd8-eb2815ce2b46', u'1-cv_all_zabbix-lfc_zabbix-905aba62-5fa3-4255-8297-8258d12c13e7', u'1-cv_all_zabbix-lfc_zabbix-4b5dce23-cb23-445f-8598-d2e4ec5480c2', u'1-cv_all_zabbix-lfc_zabbix-5e0087e1-7e72-42b4-82f9-13efb5f51bbe', u'1-cv_all_zabbix-lfc_zabbix-6c8bfc83-08b0-4ace-9f2f-f18dbeed6f70', u'1-test-test-test-lfc3-b7c68510-69c6-4cb1-b98f-a64c622f19d6']
INFO 2018-05-28 17:50:48,086 To be removed on the Capsule: set([u'lfc1'])
INFO 2018-05-28 17:50:48,087 Deleting repo 1-cv_rhel_test2-lfc1-3d430f89-2482-4693-a653-1ac62a8101be of lifecycle lfc1
INFO 2018-05-28 17:50:48,088 Starting new HTTPS connection (1): sat631caps.local.domain
INFO 2018-05-28 17:50:48,139 Delete return info: {u'spawned_tasks': [{u'_href': u'/pulp/api/v2/tasks/bf30930d-f426-4ced-9094-45719175a4da/', u'task_id': u'bf30930d-f426-4ced-9094-45719175a4da'}], u'result': None, u'error': None}
INFO 2018-05-28 17:50:48,139 Deleting repo 1-cv_rhel_test1-lfc1-5328890d-f633-4404-af68-a5ac979c166c of lifecycle lfc1
INFO 2018-05-28 17:50:48,140 Starting new HTTPS connection (1): sat631caps.local.domain
INFO 2018-05-28 17:50:48,209 Delete return info: {u'spawned_tasks': [{u'_href': u'/pulp/api/v2/tasks/f3f815b1-7aab-4f85-bf9d-9d7a6c0f9795/', u'task_id': u'f3f815b1-7aab-4f85-bf9d-9d7a6c0f9795'}], u'result': None, u'error': None}
INFO 2018-05-28 17:50:48,210 Removing Orphan objects
INFO 2018-05-28 17:50:53,217 Starting new HTTPS connection (1): sat631caps.local.domain
INFO 2018-05-28 17:50:53,306 Delete orphan info: <bound method Response.json of <Response [202]>>
INFO 2018-05-28 17:50:53,306 Finishing the cleanup process
~~~

- Checking removing "just warning" lifecycle / repos "lfc2"
~~~
INFO 2018-05-28 17:53:23,138 Starting the cleanup process
INFO 2018-05-28 17:53:23,138 COMMIT Status: False
INFO 2018-05-28 17:53:23,139 Pulp Username: admin
INFO 2018-05-28 17:53:23,139 Pulp Password: aZCehD5szBULC4z2EZhHFZGg5BJav9je
INFO 2018-05-28 17:53:23,140 Sat Server: http://sat631.local.domain
INFO 2018-05-28 17:53:23,140 Ext Capsule: sat631caps.local.domain
INFO 2018-05-28 17:53:23,153 Starting new HTTP connection (1): sat631.local.domain
INFO 2018-05-28 17:53:23,171 Starting new HTTPS connection (1): sat631.local.domain
INFO 2018-05-28 17:53:23,250 capsule hostname: sat631caps.local.domain
INFO 2018-05-28 17:53:23,250 capsule id: 2
INFO 2018-05-28 17:53:23,251 Starting new HTTP connection (1): sat631.local.domain
INFO 2018-05-28 17:53:23,264 Starting new HTTPS connection (1): sat631.local.domain
INFO 2018-05-28 17:53:23,442 LFC on capsule sat631caps.local.domain from Satellite perspective: [u'lfc_zabbix', u'lfc3', u'dev-lfc3']
INFO 2018-05-28 17:53:23,444 Starting new HTTP connection (1): sat631.local.domain
INFO 2018-05-28 17:53:23,454 Starting new HTTPS connection (1): sat631.local.domain
INFO 2018-05-28 17:53:23,735 All LFC: set([u'dev-lfc3', u'Library', u'lfc_zabbix', u'lfc3', u'lfc2', u'lfc1'])
INFO 2018-05-28 17:53:23,735 Retrieving repo list via pulp api from capsule sat631caps.local.domain
INFO 2018-05-28 17:53:23,736 Starting new HTTPS connection (1): sat631caps.local.domain
INFO 2018-05-28 17:53:23,804 Ext Caps / Repos *all*: [u'1-cv_all_zabbix-lfc_zabbix-6df74399-90a6-4922-a5cf-1b6c9e45196e', u'1-cv_all_zabbix-lfc_zabbix-3a268ef7-4cec-4228-aea2-5baf08542f63', u'1-test-lfc2-4b5dce23-cb23-445f-8598-d2e4ec5480c2', u'1-test-lfc2-6c8bfc83-08b0-4ace-9f2f-f18dbeed6f70', u'1-cv_all_zabbix-lfc_zabbix-863326ff-74c8-439f-a6f9-0a24580f5421', u'1-cv_all_zabbix-lfc_zabbix-b7c68510-69c6-4cb1-b98f-a64c622f19d6', u'1-cv_all_zabbix-lfc_zabbix-e78e53aa-02d0-46e3-96a6-e4953a93f9a7', u'1-cv_all_zabbix-lfc_zabbix-b241de8e-2848-40d7-afd8-eb2815ce2b46', u'1-cv_all_zabbix-lfc_zabbix-905aba62-5fa3-4255-8297-8258d12c13e7', u'1-cv_all_zabbix-lfc_zabbix-4b5dce23-cb23-445f-8598-d2e4ec5480c2', u'1-cv_all_zabbix-lfc_zabbix-5e0087e1-7e72-42b4-82f9-13efb5f51bbe', u'1-cv_all_zabbix-lfc_zabbix-6c8bfc83-08b0-4ace-9f2f-f18dbeed6f70', u'1-test-test-test-lfc3-b7c68510-69c6-4cb1-b98f-a64c622f19d6']
INFO 2018-05-28 17:53:23,804 To be removed on the Capsule: set([u'lfc2'])
INFO 2018-05-28 17:53:23,804 Deleting repo 1-test-lfc2-4b5dce23-cb23-445f-8598-d2e4ec5480c2 of lifecycle lfc2
INFO 2018-05-28 17:53:23,804 ## Just to report, repo will not be removed at this moment.
INFO 2018-05-28 17:53:23,804 Deleting repo 1-test-lfc2-6c8bfc83-08b0-4ace-9f2f-f18dbeed6f70 of lifecycle lfc2
INFO 2018-05-28 17:53:23,804 ## Just to report, repo will not be removed at this moment.
INFO 2018-05-28 17:53:23,804 Finishing the cleanup process
~~~


How to install on the Capsule

I'll prepare one package in a few but if you would like to test it ASAP you can

- Create the file /usr/bin/pulp_cleanup with content below
~~~
#!/usr/bin/env python

from pulp_capsule_cleanup import main
main.main()
~~~

- Update the permission
~~~
# chmod +x /usr/bin/pulp_cleanup
~~~


- Create the conf file link
~~~
# ln -s /usr/lib/python2.7/site-packages/pulp_capsule_cleanup/pulp_cleanup.py /etc/pulp_cleanup.conf
~~~

- Copy the content of url below to your local capsule, then just proceed with steps
~~~
# cd /tmp/
# git clone https://github.com/waldirio/pulp_capsule_cleanup.git
# mv pulp_capsule_cleanup/pulp_capsule_cleanup/ /usr/lib/python2.7/site-packages/
~~~

After steps above, just type
~~~
# pulp_cleanup
~~~


That's it. Enjoy it.

See you all!

Waldirio


---

Changelog
~~~
    - Collect all lifecycle available on the Sat server
    - Collect the lifecycle list available on the capsule
    - Collect all repos available on the Satellite Capsule
    - Processing the information and saying at the end what should be removed
    - Removing the repo from pulp on Satellite Capsule
    - Removing orphan objects on Satellite Capsule

    May/28/2017
    - Reading config file to retrieve pulp username and password