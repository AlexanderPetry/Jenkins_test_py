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
        bat 'C:\\Users\\RobbertjanVerschuren\\AppData\\Local\\Programs\\Python\\Python312\\python.exe hello.py'
      }
    }
      stage('send_to_twin') {
      steps {
        bat 'C:\\Users\\RobbertjanVerschuren\\AppData\\Local\\Programs\\Python\\Python313\\python.exe send.py'
      }
    }
    
  }
}
