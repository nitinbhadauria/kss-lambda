pipeline {
  agent {
    docker {
      image 'hello-world'
    }
    
  }
  stages {
    stage('Init Pipeline') {
      steps {
        sh 'echo Hello World'
      }
    }
  }
}