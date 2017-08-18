pipeline {
  agent {
    docker {
      image 'java:oracle-java8'
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