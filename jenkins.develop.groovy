def build_app(){
  echo 'start docker image'
  sh 'docker-compose up -d'
}

def stress_test_app(){
  echo 'stress test'
  sh 'python stress_test_app.py'

def down_app(){
  echo 'down image'
  sh 'docker-compose down'
}

def release_app(){
  echo 'branch into release'
}

def live_app(){
}

return this
