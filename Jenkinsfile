pipeline {
  agent any
  stages {
    stage('Load Groovy file') {
      steps {
        script {
          def filename = 'jenkins.' + env.BRANCH_NAME + '.groovy'
          groovyfile = load filename
        }

      }
    }

    stage('Build app') {
      steps {
        script {
          groovyfile.build_app()
        }

      }
    }

    stage('Stress Testing') {
      steps {
        script {
          groovyfile.stress_test_app()
        }

      }
    }

    stage('Docker images down') {
      steps {
        script {
          groovyfile.down_app()
        }

      }
    }

    stage('creating release branch') {
      steps {
        script {
          groovyfile.release_app()
        }

      }
    }

  }
}