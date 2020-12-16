pipeline {
  agent any
  stages {
    stage('Flask App: Build, Run, Test') {
      parallel {
        stage('Build and Run Flask app') {
          steps {
            sh 'sudo docker-compose up --build'
          }
        }

        stage('Testing') {
          steps {
            sleep 100
            script {
              if(env.BRANCH_NAME != 'master' && env.BRANCH_NAME != 'release' && env.BRANCH_NAME != 'develop'){
                echo "In feature branch. Unit tests incoming !"
                sh 'python test_app.py'
                echo "Pushing into develop branch !"
              }
              else if(env.BRANCH_NAME == 'develop'){
                echo "In develop branch. Stress tests incoming !"
                sh 'python stress_test_app.py'
                echo "Push into release branch !"
              }
              else if(env.BRANCH_NAME == 'release'){
                echo "In release branch."
              }
            }

          }
        }

        stage('Down Docker images') {
          steps {
            sleep 100
            script {
              if(env.BRANCH_NAME != 'master'){
                sh 'sudo docker-compose down'
              }
            }

          }
        }

      }
    }
  }
}
