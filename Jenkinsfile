def groovyfile
pipeline{
  agent any
  
  stages {
    
/*   stage('Docker images down first time'){
      steps{
        catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
          sh 'docker rm -f redis'
          sh 'docker rm -f myflaskapp_c'
          sh 'docker rmi -f myflaskapp'
          sh 'docker rm -f redis'
          sh 'docker rm -f myflaskapp_c'
          sh 'docker rmi -f myflaskapp'
        }
      }
    }*/
	  
	  stage ('Build Scripe'){
	  	steps{
			script{
				 def filename = 'jenkins.' + env.BRANCH_NAME + '.groovy'
				 groovyfile = load filename
			}
		}
	  }
    
    stage('Build Flask app'){
      steps{
        script{
          groovyfile.build_app()
        }
      }
    }
   /* stage('Run docker images'){
      parallel{
        stage('Run Redis'){
          steps{
            script{
              if(env.BRANCH_NAME == 'develop' || env.BRANCH_NAME == 'release'){
                sh 'docker run -d -p 6379:6379 --name redis redis:alpine'
              }
            }
          }
        }
        stage('Run Flask App'){
          steps{
            script{
              if(env.BRANCH_NAME == 'develop' || env.BRANCH_NAME == 'release'){
                sh 'docker run -d -p 5000:5000 --name myflaskapp_c myflaskapp'
              }
            }
          }
        }
      }
    }*/
    stage('Testing'){
      steps{
        script{
          groovyfile.test_app()
        }
      }
    }
    stage('Docker images down'){
      steps{
        script{
          groovyfile.down_app()
        }
      }
	}
      stage('creating release branch'){
        steps{
		script{
          groovyfile.release_app()
		}
        }
      }
    }
}