pipeline {
  agent any
  stages {
    stage('Building, Running, Testing Flask app') {
      parallel {
        stage('Build and Running Flask app') {
          steps {
            bat 'sudo docker-compose up'
          }
        }

        stage('Testing') {
          steps {
            sleep 100
            script {
              if(env.BRANCH_NAME != 'master' && env.BRANCH_NAME != 'release' && env.BRANCH_NAME != 'develop'){
                echo "In feature branch. Unit tests incoming !"
                bat 'python test_app.py'
                echo "Pushing into develop branch !"
              }else if(env.BRANCH_NAME == 'develop'){
                echo "In develop branch. Stress tests incoming !"
                bat 'python stress_test_app.py'
                echo "Push into release branch !"
              }else if(env.BRANCH_NAME == 'release'){
                echo "In release branch."
              }
            }

          }
        }

        stage('Docker images down') {
          steps {
            sleep 100
            script {
              if(env.BRANCH_NAME != 'master'){
                bat 'sudo docker-compose down'
              }
            }

          }
        }

      }
    }
  }
}
