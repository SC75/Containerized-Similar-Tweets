pipeline {
  agent { sudo docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python test_app.py'
      }   
    }
    stage('test Stress') {
      steps {
        sh 'python stress_test_app.py'
      }   
    }
  }
}
