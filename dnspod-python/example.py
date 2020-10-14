#!/usr/bin/env python
# -*- coding:utf-8 -*-


from dnspod import apicn


def main():
    # please refer to:
    # https://support.dnspod.cn/Kb/showarticle/tsid/227/
    login_token = ""

    domain = "iqg.pub"

    # print "DomainCreate", domain
    # api = apicn.DomainCreate(domain, login_token=login_token)
    # print(api)

    # domain_id = api().get("domain", {}).get("id")
    # print(domain_id)
#     print "%s's id is %s" % (domain, domain_id)
#
#     print "DomainList"
    api = apicn.DomainList(login_token=login_token)
    res = api().get("domains")

    for item in res:
        if item.get("name") == domain:
            domain_id = item.get("id")
#
#     print "RecordType"
#     api = apicn.RecordType("D_Ultra", login_token=login_token)
#     print(api().get("types"))
#
    # print "RecordLine"
    # api = apicn.RecordLine("D_Free", login_token=login_token)
    # print(api().get("lines"))
#
    # print "RecordCreate"
    # api = apicn.RecordCreate("test", "A", u'默认'.encode("utf8"), '1.1.1.1', 600, domain_id=domain_id, login_token=login_token)
    # record = api().get("record", {})
    # record_id = record.get("id")
    # print("Record id", record_id)
#
#     print "RecordList"
    api = apicn.RecordList(domain_id, login_token=login_token)
    res = api().get("records")
    print(res)
    for item in res:
        if item.get("name") == "test":
            record_modify_dict = dict(record_id = item.get("id"),record_line = item.get('line'),record_type = item.get('type'))

    name = "test"
    value = "2.2.2.2"
    record_modify_dict.update(dict(sub_domain=name,value=value,login_token=login_token,domain_id=domain_id))
    print(record_modify_dict)
    api = apicn.RecordModify(**record_modify_dict)
    api()

    # api = apicn.RecordModify(record_id,"test", "A", u'默认'.encode("utf8"), '2.2.2.2', 600, domain_id=domain_id, login_token=login_token)
    # record = api().get("record", {})
    # record_id = record.get("id")
    # print("Record id", record_id)


#     print "DomainRemove"
#     api = apicn.DomainRemove(domain_id, login_token=login_token)
#     print api()
#
#
if __name__ == '__main__':
    main()
