def build_app(){
  echo 'start docker image'
  bat 'docker-compose up -d'
}

def stress_test_app(){
  echo 'stress test'
  bat 'C:/Users/Daija/AppData/Local/Programs/Python/Python39/python.exe stress_test_app.py'
}

def down_app(){
  echo 'down image'
  bat 'docker-compose down'
}

def release_app(){
  echo 'branch into release'
}

def live_app(){
}

return this
