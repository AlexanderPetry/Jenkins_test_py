pipeline {
  agent any
  stages {
    stage('Print') {
      steps {
        echo 'this works'
      }
    }
    stage('hello') {
      steps {
        bat 'python hello.py'
      }
    }
      stage('send_to_twin') {
      steps {
        bat 'python send.py'
      }
    }
    
  }
}
