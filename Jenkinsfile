pipeline {
  agent {
    docker {
      image 'java:8'
    }
    
  }
  stages {
    stage('Init Pipeline') {
      steps {
        sh '''echo Hello World
java -version'''
      }
    }
  }
}