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
        bat 'C:\Users\RobbertjanVerschuren\AppData\Local\Programs\Python\Python313\python.exe hello.py'
      }
    }
  }
}
