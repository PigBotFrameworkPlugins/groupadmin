import requests, sys, time
sys.path.append('../..')
import go, tools

def delete_friend(uid, gid, message):
    dataa = requests.get(url=meta_data.get('botSettings').get('httpurl')+'/delete_friend?friend_id={0}'.format(message))

def delete_msg(uuid, mid):
    datajson = go.CallApi('delete_msg', {'message_id':mid}, uuid=uuid)
    if datajson['status'] == 'ok':
        return 200
    else:
        return 500

def sendnotice(meta_data):
    uid = meta_data.get('se').get('user_id')
    gid = meta_data.get('se').get('group_id')
    message = meta_data.get('message')
    
    dataa = requests.get(url=meta_data.get('botSettings').get('httpurl')+'/_send_group_notice?group_id={0}&content={1}'.format(gid, message))
    datajson = dataa.json()
    if datajson['status'] == 'ok':
        go.send(meta_data, '[CQ:face,id=161] 成功！')
    else:
        go.send(meta_data, '[CQ:face,id=151] 发送公告失败了，qwq')
        
def muteall(meta_data, iff=1):
    uid = meta_data.get('se').get('user_id')
    gid = meta_data.get('se').get('group_id')
    mode = meta_data.get('message')
    
    dataa = requests.get(url=meta_data.get('botSettings').get('httpurl')+'/set_group_whole_ban?group_id={0}&enable={1}'.format(gid, mode))
    datajson = dataa.json()
    if datajson['status'] == 'ok':
        message = '[CQ:face,id=161] 执行成功！'
    else:
        message = '[CQ:face,id=151] 执行失败！'
    if iff:
        go.send(meta_data, message)

def mute(meta_data):
    uid = meta_data.get('se').get('user_id')
    gid = meta_data.get('se').get('group_id')
    message = meta_data.get('message')
    
    message1 = message.split(' ')
    duration = message1[1]
    userid = go.getCQValue('qq', message1[0])
    dataa = requests.get(url=meta_data.get('botSettings').get('httpurl')+'/set_group_ban?group_id={0}&user_id={1}&duration={2}'.format(gid, userid, duration))
    datajson = dataa.json()
    if datajson['status'] == 'ok':
        go.send(meta_data, '[CQ:face,id=161] 执行成功！')
    else:
        go.send(meta_data, '[CQ:face,id=151] 执行失败！')

def kick(meta_data):
    uid = meta_data.get('se').get('user_id')
    gid = meta_data.get('se').get('group_id')
    message = meta_data.get('message')
    
    message1 = go.getCQValue('qq', message)
    dataa = requests.get(url=meta_data.get('botSettings').get('httpurl')+'/set_group_kick?group_id={0}&user_id={1}'.format(gid, message1))
    datajson = dataa.json()
    if datajson['status'] == 'ok':
        go.send(meta_data, '[CQ:face,id=161] 执行成功！')
    else:
        go.send(meta_data, '[CQ:face,id=151] 执行失败！')

def setSettings(meta_data):
    uid = meta_data.get('se').get('user_id')
    gid = meta_data.get('se').get('group_id')
    message = meta_data.get('message')
    
    message1 = message.split('===')
    key = message1[0]
    value = message1[1]
    if key == 'id' or key == 'qn':
        send(meta_data, '[CQ:face,id=189] 关键标识不可修改！')
    else:
        if isinstance(value,int):
            sql = 'UPDATE `botSettings` SET `'+str(key)+'`='+str(value)+' WHERE `qn`='+str(gid)
        else:
            sql = 'UPDATE `botSettings` SET `'+str(key)+'`="'+str(value)+'" WHERE `qn`='+str(gid)
        go.commonx(sql)
        tools.loadConfig(meta_data)
        go.send(meta_data, '[CQ:face,id=161] 设置成功！')
