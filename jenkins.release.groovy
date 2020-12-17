def build_app(){
  sh 'sudo docker-compose up -d'
}

def e2e_test(){
  echo 'release-specific testing here'
}
def user_acceptance(){
  input "proceed with deployment to live?"
}

def test_app(){
  e2e_test()
  user_acceptance()
}

def down_app(){
  sh 'sudo docker-compose down'
}

def release_app(){
}

def live_app(){
  echo 'merge with main'
}

return this
