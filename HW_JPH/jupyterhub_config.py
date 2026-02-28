import os

c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000

c.Spawner.default_url = '/lab'

c.Authenticator.admin_users = {os.environ.get('JUPYTERHUB_ADMIN', 'admin')}
