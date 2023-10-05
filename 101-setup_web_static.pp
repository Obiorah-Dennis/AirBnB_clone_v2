# set_up the servers

exec {'install-Nginx':
  command  => 'sudo apt update ; sudo apt -y install nginx',
  provider => shell,
  before   => Exec['create folders'],
}

exec {'create folders':
  command  => 'sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/',
  provider => shell,
  before   => Exec['create file'],
}

exec {'create file':
  command  => 'echo "Fake content" | sudo tee /data/web_static/releases/test/index.html',
  provider => shell,
  before   => Exec['symbolic'],
}

exec {'symbolic':
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  provider => shell,
  before   => Exec['owner'],
}

exec {'owner':
  command => '/bin/chown -R ubuntu:ubuntu /data/',
  before  => Exec['content'],
}

exec {'content':
  command  => 'sudo sed -i \'43i\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t autoindex on;\n\t}\n\' /etc/nginx/sites-available/default',
  provider => shell,
  before   => Exec['config'],
}

exec {'config':
  command  => 'sudo service nginx restart',
  provider => shell,
}
