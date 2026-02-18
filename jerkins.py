##Checkout + Show Files

pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/HARINISRI2907/calculate-program.git'
            }
        }

        stage('Show Files') {
            steps {
                bat 'dir'
            }
        }
    }
}

##Checkout + Print Directory

pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/HARINISRI2907/calculate-program.git'
            }
        }

        stage('Print Directory') {
            steps {
                bat 'cd'
            }
        }
    }
}

##Checkout + Print Message

pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/HARINISRI2907/calculate-program.git'
            }
        }

        stage('Print Message') {
            steps {
                echo 'Hello! Jenkins Pipeline executed successfully'
            }
        }
    }
}

##Checkout + Create File

pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/HARINISRI2907/calculate-program.git'
            }
        }

        stage('Create File') {
            steps {
                bat 'echo This file is created by Jenkins > demo.txt'
            }
        }
    }
}

##Checkout + Read File

pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/HARINISRI2907/calculate-program.git'
            }
        }

        stage('Read File') {
            steps {
                bat 'type README.md'
            }
        }
    }
}

##all 5

pipeline {
    agent any

    stages {

        stage('1. Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/HARINISRI2907/calculate-program.git'
            }
        }

        stage('2. Show Files') {
            steps {
                bat 'dir'
            }
        }

        stage('3. Print Directory') {
            steps {
                bat 'cd'
            }
        }

        stage('4. Print Message') {
            steps {
                echo 'Hello! Jenkins Pipeline executed successfully'
            }
        }

        stage('5. Create File') {
            steps {
                bat 'echo This file is created by Jenkins > demo.txt'
            }
        }

        stage('6. Read File') {
            steps {
                bat 'type demo.txt'
            }
        }
    }  
}

##git checkout -b feature/add
##git add app.py
##git commit -m "version 2"
##git merge feature/add
##git push origin main