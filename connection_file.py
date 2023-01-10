import paramiko


def loginCheck(credentials):
    conn = paramiko.SSHClient()
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        conn.connect(hostname=credentials['ip'], port=22, username=credentials['username'], password=credentials['password'])
        return True
                
    except Exception as e:
        return False


def get_conn(credentials):
    conn = paramiko.SSHClient()
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        conn.connect(hostname=credentials['ip'], port=22, username=credentials['username'], password=credentials['password'])
        return conn
                
    except Exception as e:
        return "ERROR"