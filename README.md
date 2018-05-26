# pulp_capsule_cleanup

Welcome, the idea of this project is just to reclaim space on file system from Satellite Capsules after remove one/a lot lifecycles from the Capsule. Actually the product doesn't provide any tool or feature to do it, then this app will help on this process.

Below instuctions about how to use.

- Do one backup of your machine :-), this script is not supported by the Company, actually is just to improve the funcionality and fix some issues related to space/storage.
- Copy this file to the Satellite Capsule
- Will be necessary edit the file const.py to update the username / password to authenticate on the Satellite. Yet on the same file, will be necessary update the pulp password

All information below
~~~
SAT_SERVER="http://sat631.local.domain"
USERNAME="admin"
PASSWORD="redhat"
~~~

The Pulp password
~~~
CAP_PASSWORD="aZCehD5szBULC4z2EZhHFZGg5BJav9je"
~~~
to collect this one from your environment, execute the command below
~~~
# grep ^default_password password /etc/pulp/server.conf|cut -d: -f3 | sed -e 's/ //'
TYHXmXF7Nm2VKogWCpE9Pk82JoVr6geq
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



That's it.

See you all!
Waldirio
