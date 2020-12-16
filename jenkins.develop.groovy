def build_app(){
  sh 'sudo docker-compose up -d'
}

def test_app(){
  sh 'python test_app.py'
}

def down_app(){
  sh 'sudo docker-compose down'
}

def release_app(){
  echo 'branch into release'
}

def live_app(){
}

return this
