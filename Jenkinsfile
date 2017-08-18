pipeline {
    agent any

    parameters {
        string(defaultValue: "TEST", description: 'What environment?', name: 'userFlag')
        // choices are newline separated
        choice(choices: 'US-EAST-1\nUS-WEST-2', description: 'What AWS region?', name: 'region')
    }

    stages {
        stage("foo") {
            steps {
		sh "echo ${params.region}"
            }
        }
    }
}
